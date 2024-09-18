import socket
import ssl
import json

from urllib.parse import urlparse

class requests:
    def __init__(self):
        self.response = None
        self.headers  = None

    def get(self, url, headers=None):
        if headers is None:
            headers = {}
        parsed = urlparse(url)
        scheme = parsed.scheme
        host   = parsed.hostname
        path   = parsed.path if parsed.path else '/'
        port   = 443 if scheme == 'https' else 80

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if scheme == 'https':
                ctx = ssl.create_default_context()
                with ctx.wrap_socket(s, server_hostname=host) as ssl_sock:
                    ssl_sock.connect((host, port))
                    self.response = self.request(ssl_sock, host, path, headers)
            else:
                s.connect((host, port))
                self.response = self.request(s, host, path, headers)
        
        return self
    
    def request(self, sock, host, path, headers, body=None):
        method = 'POST' if body is not None else 'GET'
        request = f"{method} {path} HTTP/1.1\r\n"
        headers['Host'] = host
        header = ''.join(f"{key}: {value}\r\n" for key, value in headers.items())
        request = request + header + "\r\n"
        if body:
            request += body

        sock.sendall(request.encode('utf-8'))

        response = b''
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk

        return response.decode('utf-8')
    
    @property
    def text(self):
        if self.response:
            return self.response
        return ''

    def json(self):
        if self.response:
            response = self.response
            bracket1 = response.find('{')
            bracket2 = response.rfind('}') + 1
            if bracket1 != -1 and bracket2 != -1:
                json_str = response[bracket1:bracket2]
                try:
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    return {}
        return {}