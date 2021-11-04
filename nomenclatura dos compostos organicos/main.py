from hidrocarbonetos import Hidrocarboneto, limpa_tela
from alcool import Alcool

def run():
    limpa_tela()
    print('Boas vindas ao programa de Química Orgânica!\n'
    'Primeiramente, escolha com qual tipo de composto você deseja trabalhar:\n'
    '(1) Hidrocarboneto\n'
    '(2) Álcool / Fenol\n'
    )

    escolha = int(input('Digite aqui: '))

    if escolha == 1:   
        hidrocarboneto = Hidrocarboneto()
        composto = hidrocarboneto.monta_composto()
        print(composto)
    elif escolha == 2:
        alcool = Alcool()
        composto = alcool.monta_composto()
        print(composto)

    print('Programa encerrado.')

if __name__ == '__main__':
    run()