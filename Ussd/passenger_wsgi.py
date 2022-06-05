import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


#os.execl("/usr/bin/python3.6", "python3.6", *sys.argv)

#wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
#application = wsgi.application

#def application(environ, start_response):
#    start_response('200 OK', [('Content-type', 'text/html')])
#    return 'Hello world'

INTERP = '/home/mzodqjvb/virtualenv/ussd/bin/python'
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)


#print(sys.version)
#print(sys.prefix)

#from app import MyApp as application

from app import app as application


