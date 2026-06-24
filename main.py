# ... (código anterior igual)

for linha in linhas:
    if ';' in linha:
        partes = linha.split(';')
        if len(partes) >= 3:
            nome = partes[0].strip()
            preco = partes[1].strip()
            dif = partes[2].strip()
            
            # CRIAÇÃO DO LINK: Garante que o link seja gerado baseado no nome
            # Usamos replace para trocar espaços por '+' para a URL funcionar
            link_busca = f"https://www.google.com/search?q={nome.replace(' ', '+')}&tbm=shop"
            
            lista_final.append({'nome': nome, 'preco': preco, 'dif': dif, 'link': link_busca})

# ... (código posterior igual)
