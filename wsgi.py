import BaseHTTPServer
import CGIHTTPServer
import webbrowser

PORT = 8000
#TODO: check that port is available,
# and look for a different one if it isn't.

script_path = "cgi-bin/hit-counter.py"

server_class = BaseHTTPServer.HTTPServer
handler_class = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

url = 'http://localhost:{0}/{1}'.format(PORT, script_path)

webbrowser.open_new_tab(url)

print ("serving at", url)

httpd.serve_forever()
