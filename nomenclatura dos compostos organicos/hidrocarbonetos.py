from quimica_organica import Organico, limpa_tela

class Hidrocarboneto(Organico):
    def monta_composto(self):
        ligacao, nome_tratado, radical_tratado, radicais_existem = super().define_cadeia_basica()

        if radicais_existem:
            composto = str(f'O nome do seu composto é: {radical_tratado}-{nome_tratado}{ligacao}{self.get_sufixo()}')
        else:  
            composto = str(f'O nome do seu composto é: {nome_tratado.title()}{ligacao}{self.get_sufixo()}')

        return composto

    def get_sufixo(self):
        return 'o'