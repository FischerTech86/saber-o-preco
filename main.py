def buscar_na_api_ml(produto):
    # Mudamos o 'site' para buscar em todo o Brasil (MLB)
    # E adicionamos um 'sort' para garantir que venha algo
    url = f"https://api.mercadolivre.com/sites/MLB/search?q={produto}&limit=5"
    try:
        response = requests.get(url)
        # Vamos imprimir o status para debug caso precise
        if response.status_code == 200:
            data = response.json()
            resultados = []
            for item in data.get('results', []):
                resultados.append({
                    'titulo': item.get('title'),
                    'preco': item.get('price'),
                    'link': item.get('permalink')
                })
            return resultados
        return []
    except:
        return []
