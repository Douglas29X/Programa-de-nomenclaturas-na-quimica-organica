from quimica_organica import Organico, limpa_tela

class Alcool(Organico):

    def __init__(self):
        self.posicoes = []

    def get_sufixo(self):

        sufixo_tratado = ''
        posicao = 1

        while posicao <= len(self.posicoes):

            if posicao == 1 and len(self.posicoes) != 1:
                sufixo_tratado += str(f'-{self.posicoes[posicao-1]},')
            elif len(self.posicoes) == 1:
                if self.posicoes[0] != 1:
                    sufixo_tratado += str(f'-{self.posicoes[0]}-ol')
                else:
                    sufixo_tratado += str(f'ol')
            elif posicao < len(self.posicoes):
                sufixo_tratado += str(f'{self.posicoes[posicao-1]},')
            else:
                sufixo_tratado += str(f'{self.posicoes[posicao-1]}-{super().quantidade[len(self.posicoes) - 2]}ol')

            posicao+= 1

        return sufixo_tratado
    
    def monta_composto(self):
        ligacao, nome_tratado, radical_tratado, radicais_existem = super().define_cadeia_basica(self)

        n_OH = int(input('Quantos radicais orgânicos do tipo OH o seu composto possui (máximo 4)? Digite aqui: '))

        for n in range(0, n_OH):
            posicao = int(input(f'Digite a posição do seu radical orgânico número {n + 1}: '))
            self.posicoes.append(posicao)

        if radicais_existem:
            composto = str(f'O nome do seu composto é: {radical_tratado}-{nome_tratado}{ligacao}{self.get_sufixo()}')
        else:  
            composto = str(f'O nome do seu composto é: {nome_tratado.title()}{ligacao}{self.get_sufixo()}')

        return composto