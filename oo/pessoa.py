class Pessoa:
    def __init__(self, *filhos, nome=None, idade=50, sobrenome=''):
        self.idade = idade
        self.nome = nome
        self.sobrenome = sobrenome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


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
        print(silvio.__dict__)
        print(pedro.__dict__)
