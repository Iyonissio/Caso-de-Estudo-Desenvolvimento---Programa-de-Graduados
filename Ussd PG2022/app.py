from weakref import ref
from flask import Flask, request, json, Response, render_template
import lottusapp
import lottus
from pythonsmpplib.sendsms import sendsms
# from utils.clientactions.generic_response import GenericResponse
import xmltodict
import dicttoxml


app = Flask(__name__)

lottus_app = lottusapp.get_lottus_app()


@app.route('/')
def index(name=None):
    return render_template('build/index.html', name=name)


@app.route('/ussd/ussdapp/xml/', methods=['POST', 'GET'])
def ussd_xml_api():
    if request.method == 'POST':
        js = json.dumps(xmltodict.parse(request.data))
        #print(request.data)
        
        req_dict = json.loads(js)
        #print('Puro: ----->',req_dict)
        #print(req_dict['ussd'])
        #req_dict = req_dict['transactionid']  
        req_dict = req_dict['ussd']       
        req_dict['phone'] = req_dict['msisdn']
        req_dict['session_id'] = req_dict['sessionid']
        req_dict['command'] = req_dict['msg']
        print(req_dict['phone'])
        msisdn = req_dict['phone']
        #SendControlAllRequestsInicio
        if (req_dict['command']=='*744#'):
            type = "Requisição - Entrou no Sistema"
            GenericRequests.control_all_requests(msisdn, type)
       
        #SendControlAllRequestsFim
        
        resp = lottus_app.process_request(req_dict)
        resp = lottus.window_response(resp)
        #resp['options'] = filter(lambda n: not(n['option'] == "-1"), resp['options'])
        #resp['options'] = [r for r in resp['options'] if not(r['option'] == "-1")]

        resp['options'] = [str(r['option'])+'. '+str(r['value']) for r in resp['options'] if not(r['option'] == "-1")]
        #response = Response(json.dumps(resp), status=200, mimetype='application/json')
        # resp = GenericResponse.create_personalized_answer(resp,req_dict)
        msg = resp['message']+'\n'
        for x in resp['options']:
            msg = msg + '\n'+x
        
        resp['msg'] = msg
        
        resp['msisdn'] = req_dict['phone']
        resp['sessionid'] = req_dict['session_id']
        resp['type'] = 2 if resp['type'] =="FORM" else 3
        del resp['options']
        del resp['title']
        del resp['message']

        #print(dicttoxml.dicttoxml(resp,custom_root='ussd',attr_type=False).replace(b'<?xml version="1.0" encoding="UTF-8" ?>', b''))
        #response = Response(dicttoxml.dicttoxml(resp,custom_root='ussd',attr_type=False), status=200, mimetype='application/xml')
        response = Response(dicttoxml.dicttoxml(resp,custom_root='ussd',attr_type=False).replace(b'<?xml version="1.0" encoding="UTF-8" ?>', b''), status=200, mimetype='application/xml')
        #response.header['Access-Control-Allow-Origin'] = '*'
    else:
        resp = {}
        resp['msg'] = 'Its working'
        resp['msisdn'] = request.values.get('msisdn')
        resp['sessionid'] = request.values.get('sessionid')
        resp['type'] = 2
        response = Response(dicttoxml.dicttoxml(resp,custom_root='ussd',attr_type=False).replace(b'<?xml version="1.0" encoding="UTF-8" ?>', b''), status=200, mimetype='application/xml')

    return response

@app.route('/ussd/ussdapp/json/', methods=['POST', 'GET'])
def ussd_json_api():
    if request.method == 'POST':
        js = json.dumps(request.json)
        req_dict = json.loads(js)
        
        resp = lottus_app.process_request(req_dict)
        resp = lottus.window_response(resp)
        #resp['options'] = filter(lambda n: not(n['option'] == "-1"), resp['options'])
        resp['options'] = [r for r in resp['options'] if not(r['option'] == "-1")]
                # if (resp['title'] == 'STM, TRANSPARENCIA E SEGURANÇA'):
                #     print('Titulo Encontrado')
                #     print("nUMERO DE CELULAR", req_dict['phone'])
                #     resp['title'] = 'MUDEI O TITULO'
        response = Response(json.dumps(resp), status=200, mimetype='application/json')
        #response.header['Access-Control-Allow-Origin'] = '*'

    else:
        resp = {}
        resp['msg'] = 'Its working'
        resp['msisdn'] = request.values.get('msisdn')
        resp['sessionid'] = request.values.get('sessionid')
        resp['type'] = 3
        response = Response(dicttoxml.dicttoxml(resp,custom_root='ussd',attr_type=False), status=200, mimetype='application/xml')

    return response

if __name__ == "__main__":
    app.run(debug=True)
