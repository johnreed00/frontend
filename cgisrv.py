#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("0.0.0.0", 8000)
#handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
