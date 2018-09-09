class Animal:
    __nome = ""
    __idade = 0
    _estaVivo = True

    def __init__(self, nome, idade=9):
        self.__nome = nome
        self.__idade = idade

    def __del__(self):
        print('O animal ', self.__nome, 'será apagado da memória!!!')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if len(nome) < 3:
            self.__nome = 'Bandit'
        else:
            self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            self.__idade = 0
        else:
         self.__idade = idade

    @property
    def estaVivo(self):
        return self._estaVivo

    def andar(self):
        print('O animal', self.__nome, 'está andando.')
        print(self.__metodo_privado())

    def __metodo_privado(self):
        print('Este é o método privado!!!')

class Dog(Animal):
    __possuiRabo = True

    def __init__(self, nome, idade=3, possuiRabo=True):
        self.__possuiRabo = possuiRabo
        super().__init__(nome, idade)

    @property
    def possuiRabo(self):
        return self.__possuiRabo

    @possuiRabo.setter
    def possuiRabo(self, possuiRabo):
        self.__possuiRabo = possuiRabo

    def andar(self):
        print('Agora o animal', self.nome, 'é quem está andando!!!')

    def cavar(self):
        if self.estaVivo:
            print('O cachorro', self.nome, 'está cavando!')
            self._estaVivo = False
        else:
            print('O animal', self.nome, 'já morreu :(')


    def morreu(self):
        print('O animal', self.nome, 'já morreu :( ')

#dog1 = Animal(nome='Lennon')
#dog1.nome = 'Re'
#dog1.idade = -9
rex = Dog(nome='Rex', idade=2, possuiRabo=True)
#print(dog1.nome, dog1.idade)
rex.idade = 5
print('O cachorro', rex.nome, 'tem a idade de',rex.idade, 'anos')
rex.cavar()
print(rex.possuiRabo)
rex.morreu()
rex.andar()




