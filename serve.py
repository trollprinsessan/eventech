import http.server, socketserver, os
os.chdir(os.path.join(os.path.dirname(__file__), "site"))
socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler).serve_forever()
