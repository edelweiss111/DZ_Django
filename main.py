from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os

FILE_PATH = os.path.join('src', 'index.html')
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    @staticmethod
    def __get_index(filepath):
        with open(filepath, encoding='utf-8') as f:
            html_file = f.read()
        return html_file

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_index(FILE_PATH)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
