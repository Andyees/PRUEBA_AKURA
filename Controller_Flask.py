# -*- coding: utf-8 -*- 
from flask import Flask, request
import json
app=Flask(__name__)
@app.route("/procesingEndpoint", methods=['GET'])
def hello():

    monto = int(request.args.get('monto'))
    id_transaccion=int(request.args.get('id'))
    if(monto==None or id_transaccion==None):
        return "No se pudieron leer los parametros Get /n por favor revisar la peticion"
    total=(monto*id_transaccion)/4

    response={"success":"ok",'total':total}
    
    return json.dumps(response)