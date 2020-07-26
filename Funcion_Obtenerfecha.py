# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:10:40 2020

@author: Andres Agudelo
"""
import json
from datetime import datetime, timedelta
 


def Encontrar_ultimo_Dia(cadena):                                                       #Metodo Principal
    cadena_json = json.loads(cadena) 
    formato_fecha =  "%Y-%m-%d"
    cadena_datetime = datetime.strptime(cadena_json["date"], formato_fecha)
    datetimepost= cadena_datetime + timedelta(days=22)                                              
    if datetimepost.month == 12: 
        return datetimepost.replace(day=31) 
    return datetimepost.replace(month=datetimepost.month+1, day=1) - timedelta(days=1)
    


json_fecha='{"date":"2020-03-30"}'
datetime_ultimo_dia= Encontrar_ultimo_Dia(json_fecha)                                     #Implementacion del metodo
print(datetime_ultimo_dia)
