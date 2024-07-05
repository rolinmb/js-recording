import http.server
import socketserver

PORT = 8080
DIRECTORY = "."

class HttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    handler = HttpHandler
    handler.extensions_map.update({
        '.html': 'text/html',
    })
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving src/index.html on http://localhost:{PORT}")
        httpd.serve_forever()
