import http.server
import socketserver
import ssl

PORT = 4443
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(('0.0.0.0', PORT), Handler)

# Wrap the server socket with SSL
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/certs/server.pem', server_side=True)

print(f"Serving on https://0.0.0.0:{PORT}")
httpd.serve_forever()
