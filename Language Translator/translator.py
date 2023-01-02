from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

APIKEY = 'n5mEbdGsd7DCLQqLMKfWOo7ZAubGe629oNmC614YCaQk'
URL = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/84231ccd-b722-4b8d-9684-777f5b4a93ce'

authenticator = IAMAuthenticator(APIKEY)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(URL)

def english_to_french(word):
    '''
    translate english to French
    '''
    translation = lt.translate(text=word, model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def english_to_german(word):
    '''
    translate english to German
    '''
    translation = lt.translate(text=word, model_id='en-de').get_result()
    return translation['translations'][0]['translation']
