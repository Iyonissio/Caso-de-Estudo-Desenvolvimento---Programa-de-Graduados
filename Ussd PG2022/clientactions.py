from tokenize import Double, String
from unicodedata import name
import mysql.connector
import requests
from pythonsmpplib import sendsms
from datetime import date
import time
from datetime import datetime
import string
import random
from xml.dom.minidom import Notation

today = date.today()
print(datetime.today().strftime('%Y-%m-%d'))

def mysql_conn():
    return mysql.connector.connect(host="34.102.65.72", user="administrator", password="Messis#01", database="dbstm")

def codFilaGenarator(size=6, chars=string.ascii_uppercase + string.digits):
    den = ''.join(random.choice(chars) for _ in range(size))
    return 'DEN'+den

def SendFilaCod(msisdn, msg):
    mydb = mysql_conn()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nome_servico FROM tb_servicos WHERE tb_contribuente.tel1_prop = '"+msisdn+"'")
    myresult = mycursor.fetchall()
    options = []

    rmsg = ""
    if(len(myresult) > 0):
        nr = 0
        for x in myresult:
            nr += 1
            rmsg = rmsg+'Os servicos disponiveis na plataforma sao:.',myresult[0][0]
            Response = {'valid': True, 'window': "PAG_VAL1",
                        'message': 'IPRA', 'type': 'FORM',
                        'options': options, 'name': 'GetDados', 'title': 'Dados do CLiente', "auto_process": True, "active": True}
    else:
        rmsg = 'Caro cliente, sem dados disponiveis referente aos servicos.'

    sendsms.sendsms(msisdn, rmsg)
    return {'valid': True, 'window': 'PAGAMENTOS',
            'message': 'O seu contacto é '+msisdn, 'type': 'MESSAGE',
            'options': [], 'title': 'Informação pessoal'}

def SendFilaCod(msisdn, msg):
    rmsg = "O seu codigo na Fila é.",codFilaGenarator()
    sendsms.sendsms(msisdn, rmsg)
    return {'valid': True, 'window': 'PAGAMENTOS',
            'message': 'O seu contacto é '+msisdn, 'type': 'MESSAGE',
            'options': [], 'title': 'Informação pessoal'}


