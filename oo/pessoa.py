class Pessoa:
    def __init__(self, nome=None, idade=22):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Pedro')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.nome)
    p.nome = 'Henrique'
    print(p.nome)
    print(p.idade)
