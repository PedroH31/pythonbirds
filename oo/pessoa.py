class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=50, sobrenome=''):
        self.idade = idade
        self.nome = nome
        self.sobrenome = sobrenome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro')
    silvio = Pessoa(pedro, nome='Silvio')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(silvio.nome)
    print(pedro.idade)
    for filho in silvio.filhos:
        print(filho.nome)
        silvio.sobrenome = 'de Freitas'
        print(silvio.olhos)
        print(Pessoa.olhos)
        print(pedro.olhos)
        print(silvio.__dict__)
        print(pedro.__dict__)
    print(Pessoa.metodo_estatico(), silvio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), silvio.olhos())
    