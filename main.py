from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/resultado')
def resultado():
    # Esta é a IA comparando os dados técnicos que colocamos no HTML
    analise_ia = """
    • Sistema Operacional: Android 13 vs iOS 17. 
    • Vida útil da bateria: O S23 Ultra apresenta maior duração em uso intenso devido à capacidade de 5000mAh. 
    • Câmeras: O S23 Ultra oferece maior resolução (200MP) e zoom, enquanto o iPhone 15 Pro foca em processamento de imagem profissional e vídeo ProRes.
    """
    return render_template('resultado.html', analise=analise_ia)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
