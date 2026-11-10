import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(f"  [+] متجر ميديكير للمستلزمات الطبية يعمل الآن بنجاح!")
        print(f"  [+] الرابط المحلي: {url}")
        print("  [+] اضغط Ctrl+C لإيقاف السيرفر")
        print("=" * 60)
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nتم إيقاف السيرفر بنجاح.")
            httpd.server_close()

if __name__ == "__main__":
    start_server()
