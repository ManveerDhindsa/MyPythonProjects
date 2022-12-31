# the goal of this file is to recommend the user an amazon product that is within the budget they input for the product they wish to buy. 
# this is done by comparing the ratio of the rating to the price of the first page products with a rating above 4 stars and with atleast 100 reviews which is also within the budget for the product
# returns the best product based on rating to price ratio in the budget
# made with the help of this youtube video which I modified for my application and purpose: https://www.youtube.com/watch?v=_AeudsbKYG8&ab_channel=IzzyAnalytics

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge import service

edgeOption = webdriver.EdgeOptions()
edgeOption.use_chromium = True
edgeOption.add_argument("start-maximized")
edgeOption.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
s=service.Service(r'C:\Users\manve\OneDrive\Documents\Python VSCode learning programs\msedgedriver.exe')
driver = webdriver.Edge(service=s, options=edgeOption)

def get_url(search_term):
    # generate a url from search term
    template = 'https://www.amazon.ca/s?k={}'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)


def extract_record(item):
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.ca' + atag.get('href')

    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        price = 'no price'

    try:
        rating = item.i.text
    except AttributeError:
        rating = 'no rating'
    
    try:
        num_of_reviews = item.find('span', {'class':'a-size-base s-underline-text'}).text
    except AttributeError:
        num_of_reviews = 'no reviews'
    
    try:
        ratio = float(price[1:]) / float(rating[0:3])
    except:
        ratio = 'no ratio'
    
    results = (description, price, rating, num_of_reviews, url, ratio)
    return results


def main():
    answer = input('Enter Item: ')
    while True:
        try:
            budget = int(input('Enter Budget with only integers and no $ sign: '))
            break
        except ValueError:
            continue
    url = get_url(answer)
    driver.get(url)
    driver.implicitly_wait(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    records = []
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    for item in results:
        record = extract_record(item)
        if record:
            records.append(record)
    
    for row in records:
        if [','] in row[3]:
            row[3].replace(',', '')

    highest = ['No product for user input',0,0,0,None,0]
    
    for row in records:
        if int(row[3]) > 100:
            if float(row[5]) > 4.0:
                if float(row[1:]) < budget:
                    if row[5] > highest[5]:
                        highest.clear()
                        highest.append(row)
    
    print()
    print('Best Product: ', highest[0])
    print('URL to Product: ', highest[4])
    
    
if __name__ == '__main__':
    main()