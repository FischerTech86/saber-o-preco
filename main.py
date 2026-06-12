import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# Código HTML básico do seu buscador
HTML_PAGINA_UNICA = """
<html>
    <head><title>Buscador de Preços</title></head>
    <body>
        <h1>Meu Buscador de Preços</h1>
        <p>O sistema está online e funcionando!</p>
    </body>
</html>
"""

class ServidorPerfeito(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_PAGINA_UNICA.encode('utf-8'))

    def log_message(self, format, *args):
        return  # Esconde logs desnecessários

if __name__ == "__main__":
    # O Render define a porta automaticamente através da variável de ambiente 'PORT'
    port = int(os.environ.get("PORT", 8055))
    servidor_final = ThreadingHTTPServer(('0.0.0.0', port), ServidorPerfeito)
    print(f"🚀 SISTEMA PREPARADO NA PORTA {port}!")
    servidor_final.serve_forever()
