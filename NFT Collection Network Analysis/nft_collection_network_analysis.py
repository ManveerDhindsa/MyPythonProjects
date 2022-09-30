import pandas as pd
import sqlite3
import networkx as nx
from pyvis.network import Network

con = sqlite3.connect('nfts.sqlite')
cur = con.cursor()

df = pd.read_sql_query('''
                       SELECT name, nft_address, SUM(transaction_value/1e18) AS volume
                       FROM transfers
                       INNER JOIN nfts ON transfers.nft_address = nft_address
                       Group BY transfers.nft_address
                       ORDER BY volume DESC
                       
                       LIMIT 3
                       ''', con)

contract_names_dict = dict(zip(df.nft_address, df.name))

contracts = tuple(contract_names_dict.keys())

all_project_names = pd.read_sql_query('''
                                      SELECT * FROM nfts
                                      LIMIT 10000
                                      ''', con)

contract_names_dict_all = dict(zip(all_project_names['address'], all_project_names['names']))

top_n_owners_list = pd.read_sql_query('''
                                      SELECT COUNT(DISTINCT nft_address)
                                      FROM current_owners
                                      WHERE nft_address IN {}
                                      GROUP BY owner
                                      ORDER BY num_projects DESC
                                      
                                      LIMIT 3
                                      '''.format(contracts), con)

owners_tuples = tuple(top_n_owners_list['owner'])

top_projects = pd.read_sql_query('''
                                 SELECT nft_address, COUNT(owner) AS count FROM current_owners
                                 WHERE owner in {}
                                 GROUP BY nft_address
                                 ORDER BY count DESC
                                 LIMIT 4000
                                 
                                 '''.format(owners_tuples), con)

top_projects_tuples = tuple(top_projects['nft_address'])

all_nfts_in_top_projects = pd.read_sql_query('''
                                             SELECT * FROM current_owners
                                             WHERE nft_address IN {}
                                             '''.format(top_projects_tuples), con)

edge_table = pd.read_sql_query('''
                                SELECT t1.nft_address AS NFT1, t2.nft_address AS NFT2, COUNT(*) AS COUNT
                        
                                FROM current_owners AS t1
                                
                                INNER JOIN current_owners AS t2
                                ON t1.owner = t2.owner
                                
                                
                                WHERE t1.owner in {}
                                AND
                                NFT1 < NFT2
                                
                                GROUP BY NFT1, NFT2
                                HAVING COUNT(*) > 50
                               '''.format(owners_tuples), con)

edge_table['NFT1'] = edge_table['NFT1'].map(contract_names_dict_all)
edge_table['NFT2'] = edge_table['NFT2'].map(contract_names_dict_all)

edge_table = edge_table.dropna()

edge_table.columns = ['source', 'target', 'weight']

soruces = edge_table['source']
targets = edge_table['target']
weights = edge_table['weight']

edge_data = zip(soruces, targets, weights)

network_graph = Network(heigh = '750px', width = '100%', bgcolor = '#222222', font_color='white')

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    
    network_graph.add_node(src, src, title=src)
    network_graph.add_node(dst, dst, title=dst)
    network_graph.add_node(src, dst, value=w)
    
neighbor_map = network_graph.get_adj_list()
for node in network_graph.nodes:
    node['title'] += 'Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
network_graph.show('NFTMap.html')
