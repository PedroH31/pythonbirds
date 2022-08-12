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


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    silvio = Homem(renzo, nome='Silvio')
    print(Pessoa.cumprimentar(renzo))
    print(id(renzo))
    print(silvio.nome)
    print(renzo.idade)
    for filho in silvio.filhos:
        print(filho.nome)
        silvio.sobrenome = 'de Freitas'
        print(silvio.olhos)
        print(Pessoa.olhos)
        print(renzo.olhos)
        print(silvio.__dict__)
        print(renzo.__dict__)
    print(Pessoa.metodo_estatico(), silvio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), silvio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)


    