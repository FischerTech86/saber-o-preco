import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# HTML com uma caixa de busca simples
HTML_PAGINA = """
<html>
    <head><title>Meu Buscador</title></head>
    <body>
        <h1>Buscador de Preços</h1>
        <form action="/buscar" method="GET">
            <input type="text" name="produto" placeholder="Digite o produto...">
            <button type="submit">Buscar</button>
        </form>
    </body>
</html>
"""

class ServidorPerfeito(BaseHTTPRequestHandler):
    def do_GET(self):
        # Se o usuário acessar a página inicial
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_PAGINA.encode('utf-8'))
        # Se o usuário clicar em "Buscar"
        elif self.path.startswith('/buscar'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("<h1>Buscando...</h1><p>Em breve mostrarei o preço aqui!</p>".encode('utf-8'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8055))
    servidor_final = ThreadingHTTPServer(('0.0.0.0', port), ServidorPerfeito)
    print(f"🚀 SISTEMA ATUALIZADO NA PORTA {port}!")
    servidor_final.serve_forever()
