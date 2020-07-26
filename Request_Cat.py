# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 13:58:34 2020

@author: Andres Agudelo
"""
import requests
url='https://cat-fact.herokuapp.com/facts/random'
def request_Fact_Cat(url_api):
    response = requests.get(url_api)
    return(response.json()['text'])
    
frase_gato=request_Fact_Cat(url)
print(frase_gato)

