from abc import ABCMeta, abstractmethod
from listas import csv_para_python
import os


class Organico(metaclass= ABCMeta):

    quantidade = ['di','tri','tetra']

    @abstractmethod
    def get_sufixo(self):
        pass

    @abstractmethod
    def monta_composto(self):
        pass

    def imprime_radicais(self):
        linha = 1
        for hc in self.get_radicais():
            print(f'{linha} - {hc}')
            linha+=1

    def get_radicais(self):
        radicais = csv_para_python('nomenclaturas/radicais.csv')
        return radicais

    def get_prefixos(self):
        prefixos = csv_para_python('nomenclaturas/prefixos.csv')
        return prefixos

    def retorna_ligacao(self, escolha, posicao):
        tipo = escolha - 1
        ligacoes = ['an', 'en', 'in']
        if tipo == 0:
            return str(ligacoes[tipo])
        elif tipo == 1:
            return f'-{posicao}-{str(ligacoes[tipo])}'
        elif tipo == 2:
            return f'-{posicao}-{str(ligacoes[tipo])}'
            

    def define_cadeia_basica(self):

        radicais = self.get_radicais()
        prefixos = self.get_prefixos()

        limpa_tela()
        numero_C = int(input('Digite o número de carbonos da sua cadeia principal (CP com limite de 20C): ')) - 1

        limpa_tela()
        if numero_C != 0:
            ligacoes_escolhidas = int(input('''Digite o número referente aos tipos de ligações de sua CP:
(1) Apenas ligações simples - (2) Dupla(s) - (3) Tripla(s) - (4) Dupla(s) e Tripla(s): 
'''))
        else:
            ligacoes_escolhidas = 1

        limpa_tela()

        if ligacoes_escolhidas > 1:
            posicao = input('Digite a posição da sua ligação: ')
        else:
            posicao = 0

        escolha_radicais = int(input('O seu composto possui radicais? Digite (1) para SIM e (2) para NÃO: '))

        if escolha_radicais == 1:
            radicais_existem = True
            print('De acordo com a tabela a seguir')
            self.imprime_radicais()
            radical_escolhido = int(input('Escolha e digite o número do seu radical: ')) - 1
            posicao_radical = int(input('Digite o número da posição do radical na sua cadeia: '))
            if posicao_radical == 1:
                radical_tratado = str(radicais[radical_escolhido]).capitalize()
            else:
                radical_tratado = str(f'{posicao_radical}-{radicais[radical_escolhido]}')
        else:
            radical_tratado = None
            radicais_existem = False

        limpa_tela()
        ligacao = self.retorna_ligacao(ligacoes_escolhidas, posicao)
        nome_tratado = str(prefixos[numero_C]).lower()

        return ligacao, nome_tratado, radical_tratado, radicais_existem


def limpa_tela():
            os.system('cls')