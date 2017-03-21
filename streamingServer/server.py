'''
Created on 21 mar. 2017

@author: Juanmi
'''
from http.server import  BaseHTTPRequestHandler, HTTPServer

class Server():
    '''
    Clase relativa a la parte servidora de peticiones http
    '''


    def __init__(self):
        '''
        Constructor
        '''
        server = HTTPServer(('', 5050), Handler)
        server.serve_forever()
        
class Handler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Hacer lo que queramos con la petición
        return
    