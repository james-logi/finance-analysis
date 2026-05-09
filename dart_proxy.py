"""
Open DART 재무제표 분석기용 로컬 프록시 서버
사용법: python dart_proxy.py
종료: Ctrl+C
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import urllib.request


class Proxy(BaseHTTPRequestHandler):
    def do_GET(self):
        # /proxy?url=<URL> 형태로 요청을 받아서 그 URL을 대신 호출
        if self.path.startswith('/proxy?url='):
            target = unquote(self.path[len('/proxy?url='):])
            try:
                req = urllib.request.Request(
                    target,
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                with urllib.request.urlopen(req, timeout=30) as r:
                    body = r.read()
                    ctype = r.headers.get('Content-Type', 'application/octet-stream')
                self.send_response(200)
                self.send_header('Content-Type', ctype)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(body)
            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(str(e).encode())

        # /ping → "pong" (브라우저에서 연결 테스트용)
        elif self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'pong')
        else:
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def log_message(self, format, *args):
        # 로그 간소화
        print(f"[{self.address_string()}] {format % args}")


if __name__ == '__main__':
    PORT = 8765
    print(f'=' * 60)
    print(f'Open DART 프록시 서버 시작')
    print(f'주소: http://localhost:{PORT}')
    print(f'테스트: http://localhost:{PORT}/ping (브라우저에서 열어보세요)')
    print(f'종료: Ctrl+C')
    print(f'=' * 60)
    try:
        HTTPServer(('localhost', PORT), Proxy).serve_forever()
    except KeyboardInterrupt:
        print('\n프록시 서버를 종료합니다.')
