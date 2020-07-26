# -*- coding: utf-8 -*-
#By Andres Agudelo 22/07/2020

#Usando expresiones regulares y la libreria re hice mi programa que verifica si la cadena ingresada es valida con respecto a las reglas del
#Ejericio heHco para Prueba Akura SAS
"""
Created on Sat Jul 23 00:10:40 2020

@author: Andres Agudelo
"""

import re
print("Ingrese por favor una cadena que cumpla las reglas definidas:\n ")
cadena = input()
flag=False 
RE1="[*]{1}"                                                                  #Expresion regular valida asterisco
RE2="^([A-Z&]){1,}"                                                           #Expresion regular inicio de la cadena"
RE3="[^a-z\-\_]"                                                              # Expresion regular que limita caracteres
Pos_ast=cadena.find("*")
indice= Pos_ast+1 if (len(cadena)>3) else 0
contador_Cadena=Pos_ast   
if(len(cadena)>4 and Pos_ast>1):                                                  
    if(re.search(RE1,cadena) and re.search(RE2,cadena) and not re.search(RE3,cadena[1:Pos_ast]) and re.search(RE2,cadena[indice])):
        for indice in range(len(cadena)):
            caracter = cadena[indice]
            if(caracter=="*" and indice-contador_Cadena>2):
                if(not re.search(RE3,cadena[contador_Cadena+2:indice-1])):
                    next_caracter=indice+1 if(indice+1<len(cadena)) else indice
                    if(re.search(RE2,cadena[next_caracter])):
                        contador_Cadena=indice
                    else:
                        flag=False 
                        break
                else:
                    flag=False 
                    break
                 
            if(indice==len(cadena)-1 and indice-contador_Cadena>1):
                    if(not re.search(RE3,cadena[contador_Cadena+2:indice+1])):
                        flag=True
                        print("\nLa cadena es COMPATIBLE!! cumple la expresion regular!")
                            
                    else:
                         flag=False 
                         break
        
    else:
        
        print("\nError!! no es valido, no cumple las reglas de expresion por favor revisar la sintaxis de la cadena")   
        flag=True
    if(not flag):
        print("\nError!! no es valido, no cumple las reglas de expresion por favor revisar la sintaxis de la cadena")
        
else:    
     print("\nError!! no es valido, no cumple las reglas de expresion por favor revisar la sintaxis de la cadena")
        