import http.server
import os
import sys

port = int(os.environ.get('PORT', 8091))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', port), handler)
print(f"Serving on port {port}")
httpd.serve_forever()
