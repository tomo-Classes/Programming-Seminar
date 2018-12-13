from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json
import sys

class Handler(BaseHTTPRequestHandler):
	def __init__(self):
		super(self)

	def do_GET(self):
		print("get")

def run(server = HTTPServer, handler = Handler):
	address = ("", 8080)
	httpd = server(address, handler)
	json.dump(handler, sys.stdout)
	print("")
	print("http://localhost:" + str(address[1]))
	httpd.serve_forever()

run()
