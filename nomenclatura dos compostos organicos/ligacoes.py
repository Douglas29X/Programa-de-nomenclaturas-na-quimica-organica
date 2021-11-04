def retorna_ligacao(escolha, posicao):
    
    tipo = escolha - 1
    ligacoes = ['an', 'en', 'in']
    if tipo == 0:
        return str(ligacoes[tipo])
    elif tipo == 1:
        return f'-{posicao}-{str(ligacoes[tipo])}'
    elif tipo == 2:
        return f'-{posicao}-{str(ligacoes[tipo])}'