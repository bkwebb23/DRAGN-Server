import json
import socket
from datetime import datetime
from chatbots.Echo import Echo
from chatbots.Trevor import Trevor
from chatbots.geoff2 import geoff2
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer


chatbots = ["ECHO", "TREVOR", "GEOFF2"]
echo = Echo()
trevor = Trevor()
geoff2 = geoff2()

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def send_json(self, chatbot, json_input):
        chatbot.recv_message(json_input)
        data = chatbot.send_message() 
        data_json = json.dumps(data)
        self._set_headers()
        self.wfile.write(bytes(data_json, "utf-8"))
    def send_json_message(self, json_input):
        data_json = json.dumps(json_input)
        self._set_headers()
        self.wfile.write(bytes(data_json, "utf-8"))
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
    def do_POST(self):
        if self.path == "/":
            self._set_headers()
            root_text = "Currently no implementation at the base level.. \n Please try: /chatbot/<chatbotID or chatbotNAME>"
            data = {"text":root_text}
            self.send_json_message(data)
        elif self.path == "/chatbot" or self.path == "/chatbot/":
            data = {"text":"current list of chatbots", "chatbots":chatbots}
            self.send_json_message(data)
        elif self.path == "/chatbot/echo":
            print("Echo sent a message @: ", str(datetime.now()))
            req_json = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            self.send_json(echo, req_json)
        elif self.path == "/chatbot/trevor":
            print("Trevor sent a message @: ", str(datetime.now()))
            req_json = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            self.send_json(trevor, req_json) 
        elif self.path == "/chatbot/geoff2":
            print("Geoff2 sent a message @: ", str(datetime.now()))
            req_json = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            self.send_json(geoff2, req_json)     
        
# WYRMLING DEFAULT: 127.0.1.1:8088

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ("127.0.0.1", port)   # (socket.gethostbyname(socket.gethostname()), port)
    httpd = server_class(server_address, handler_class)
    # print('Server running at {}:{}...'.format(socket.gethostbyname(socket.gethostname()), port))
    print('Server running at {}:{}...'.format("127.0.0.1", port))
    httpd.serve_forever()

run()
