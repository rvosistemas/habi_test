import http.server
import urllib.parse

from app.routes.endpoints import MyRequestHandler


def main():
    host = "localhost"
    port = 8000
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    print(f"Starting server on {host}:{port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
