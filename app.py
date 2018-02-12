import http.server,os
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

if __name__ == "__main__":
    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = os.environ['OPENSHIFT_PYTHON_PORT']
    host_name = os.environ['OPENSHIFT_GEAR_DNS']
    server_address = (ip, port)

    httpd = server(server_address, handler)
    httpd.serve_forever()
