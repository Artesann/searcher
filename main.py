import json
import requests
from searcher import boolSearch
from vector_module_search import vectorSearch

def search_input():
   
    search = input()
    search_set=set(search.strip().split(" "))
    tesaurus_search_set=set()

    for word in search_set:
        tesaurus_search_set.add(word.lower())

    for word in search_set: 
        tesaurus_text=requests.get('http://www.serelex.org/find/ru-patternsim-ruwac-wiki/'+ word).text
        if tesaurus_text.find('relations')!=-1:
            json_buffer=json.loads(tesaurus_text)
            value_buff=0.0
            value=0.0
            for json_word in json_buffer['relations']:
                value_buff+=json_word['value']
            value=value_buff/len(json_buffer['relations'])
            for json_word in json_buffer['relations']:
                if value<=json_word['value']:
                    tesaurus_search_set.add(json_word['word'].lower())
    return list(tesaurus_search_set)

str = search_input()
print("VECTOR SEARCH:")
vectorSearch(str)
print("\nBOOLEAN SEARCH:")
boolSearch(str)
