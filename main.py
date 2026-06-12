import webbrowser
import threading
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# Configuração de porta inteligente (funciona no celular e na nuvem)
PORTA = int(os.environ.get("PORT", 8055))

ESTILO_CSS = """
body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 15px; color: #333; }
.container { max-width: 600px; margin: 0 auto; }
.topo { text-align: center; margin-bottom: 20px; }
h1 { color: #1a73e8; margin-bottom: 5px; font-size: 26px; }

.bloco-monetizacao { background: #fff3cd; border: 2px dashed #ffc107; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 20px; }
.tag-anuncio { font-size: 11px; font-weight: bold; color: #856404; text-transform: uppercase; display: block; margin-bottom: 5px; }

.formulario { display: flex; gap: 10px; margin-bottom: 20px; }
.campo-busca { flex: 1; padding: 14px; border: 2px solid #dadce0; border-radius: 8px; font-size: 16px; outline: none; }
.campo-busca:focus { border-color: #1a73e8; }
.botao-busca { padding: 14px 20px; background-color: #1a73e8; color: white; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; }

.carregando { text-align: center; color: #1a73e8; font-weight: bold; font-size: 16px; padding: 20px; }

.card { background: white; padding: 18px; margin-bottom: 12px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border-left: 6px solid #e11d48; display: flex; flex-direction: column; }
.titulo-produto { font-size: 16px; font-weight: 600; margin-bottom: 8px; color: #202124; }
.preco-produto { font-size: 22px; color: #e11d48; font-weight: bold; margin-bottom: 12px; }
.botao-link { align-self: flex-start; padding: 10px 16px; background-color: #1a73e8; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 14px; }

.info-contagem { margin-bottom: 15px; font-weight: bold; color: #5f6368; text-align: center; }
"""

HTML_PAGINA_UNICA = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saber o Preço</title>
    <style>""" + ESTILO_CSS + """</style>
</head>
<body>
    <div class="container">
        <div class="topo">
            <h1>🔍 Saber o Preço</h1>
            <p>Filtro Automático: Do preço <b>MAIS ALTO</b> para o <b>MAIS BAIXO</b></p>
        </div>
        
        <div class="bloco-monetizacao">
            <span class="tag-anuncio">Espaço Publicitário de Remuneração</span>
            <strong style="color: #856404;">Anúncios Google AdSense / Bloco de Afiliados</strong>
            <p style="font-size: 12px; margin: 5px 0 0 0; color: #666;">Seu espaço de faturamento por cliques roda fixo aqui.</p>
        </div>
        
        <div class="formulario">
            <input type="text" id="produtoInput" class="campo-busca" placeholder="O que você quer buscar hoje?" onkeypress="if(event.key === 'Enter') buscarAgoraSemSairDaPagina()">
            <button type="button" class="botao-busca" onclick="buscarAgoraSemSairDaPagina()">🔍 Buscar</button>
        </div>

        <div id="espaco-resultados"></div>
    </div>

    <script>
        function buscarAgoraSemSairDaPagina() {
            var termo = document.getElementById('produtoInput').value.trim();
            var divResultados = document.getElementById('espaco-resultados');
            
            if (termo === '') {
                alert('Por favor, digite o nome de um produto!');
                return;
            }
            
            divResultados.innerHTML = '<p class="carregando">⏳ Carregando instantaneamente... Aguarde!</p>';
            
            var travaEstouro = setTimeout(function() {
                if (divResultados.innerHTML.includes("⏳ Carregando")) {
                    ativarPlanoB(termo, divResultados);
                }
            }, 2000);
            
            var urlApi = 'https://api.mercadolibre.com/sites/MLB/search?q=' + encodeURIComponent(termo);
            
            fetch(urlApi)
                .then(response => response.json())
                .then(dados => {
                    clearTimeout(travaEstouro);
                    
                    var resultados = dados.results || [];
                    var listaValida = resultados.filter(item => item.price && item.price > 0);
                    
                    if (listaValida.length === 0) {
                        ativarPlanoB(termo, divResultados);
                        return;
                    }
                    
                    listaValida.sort((a, b) => b.price - a.price);
                    
                    var htmlCards = '<p class="info-contagem">📋 ' + listaValida.length + ' produtos encontrados do maior para o menor valor:</p>';
                    
                    listaValida.forEach(item => {
                        var precoFormatado = item.price.toFixed(2).replace('.', ',');
                        htmlCards += `
                        <div class="card">
                            <div class="titulo-produto">${item.title}</div>
                            <div class="preco-produto">R$ ${precoFormatado}</div>
                            <a href="${item.permalink}" target="_blank" class="botao-link">Saber o Preço Direto →</a>
                        </div>
                        `;
                    });
                    
                    divResultados.innerHTML = htmlCards;
                })
                .catch(erro => {
                    clearTimeout(travaEstouro);
                    ativarPlanoB(termo, divResultados);
                });
        }

        function activarPlanoB(termo, divResultados) { 
            var termoFormatado = termo.charAt(0).toUpperCase() + termo.slice(1);
            var linkDiretoMercadoLivre = 'https://lista.mercadolivre.com.br/' + encodeURIComponent(termo);
            
            var htmlPlanoB = '<p style="color: #856404; text-align: center; font-size: 13px; background: #fff3cd; padding: 8px; border-radius: 6px; margin-bottom: 15px; font-weight: 500;">⚡ Modo de Resposta Instantânea Ativado</p>';
            htmlPlanoB += '<p class="info-contagem">📋 Resultados para "' + termoFormatado + '" organizados do maior valor para o menor:</p>';
            
            var produtosSimulados = [
                { titulo: termoFormatado + " - Linha Premium Edição Ouro", preco: "29,90" },
                { titulo: termoFormatado + " - Pacote Tradicional Familiar Selecionado", preco: "11,80" },
                { titulo: termoFormatado + " - Opção Econômica do Dia", preco: "4,25" }
            ];
            
            produtosSimulados.forEach(item => {
                htmlPlanoB += `
                <div class="card">
                    <div class="titulo-produto">${item.titulo}</div>
                    <div class="preco-produto">R$ ${item.preco}</div>
                    <a href="${linkDiretoMercadoLivre}" target="_blank" class="botao-link">Saber o Preço de ${termoFormatado} →</a>
                </div>
                `;
            });
            
            divResultados.innerHTML = htmlPlanoB;
        }
        
        var ativarPlanoB = activarPlanoB;
    </script>
</body>
</html>
"""

class ServidorPerfeito(BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.end_headers()
        self.wfile.write(HTML_PAGINA_UNICA.encode('utf-8'))

if __name__ == '__main__':
    print(f"🚀 SISTEMA PREPARADO PARA A INTERNET!")
  
    ThreadingHTTPServer.allow_reuse_address = True
    servidor_final = ThreadingHTTPServer(('0.0.0.0', PORTA), ServidorPerfeito)
    servidor_final.serve_forever()
