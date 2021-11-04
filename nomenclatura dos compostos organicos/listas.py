def csv_para_python(caminho):
    nomes = []
    with open(caminho, encoding='latin_1') as arquivo:
        for nome in arquivo:
            nome = nome.replace('\n','')
            nomes.append(nome)
        
    return nomes