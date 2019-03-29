# codigo feito no VS code

class LMSTrainer:
    def __init__(self, x, y, taxa, limite):
        self.__delta0 = 0       # hipotese constante
        self.__delta1 = 0       # hipotese coeficiente angular
        self.__x = x            # vetor dados
        self.__y = y            # vetor gabarito
        self.__m = len(y)       # quantidade de testes
        self.__taxa = taxa      # taxa de aprendizado
        self.__limite = limite  # limite do erro do criterio de parada
        self.__it = 0           # iteracoes
        self.__limitIt = 9999999# limite para as iteracoes
    
    def __hipotese(self, x):
        return self.__delta0 + self.__delta1*x

    def __custo(self):
        error = .0
        for i, x in enumerate(self.__x):
            error += (self.__hipotese(x) - self.__y[i])**2
        return error / (2.0*self.__m)

    def __convergiu(self):
        self.__it += 1
        return self.__it == self.__limitIt or self.__custo() <= self.__limite
    
    def __errorSumDelta0(self):
        sum = .0
        for i, x in enumerate(self.__x):
            sum += self.__hipotese(x) - self.__y[i]
        return sum
    
    def __errorSumDelta1(self):
        sum = .0
        for i, x in enumerate(self.__x):
            sum += (self.__hipotese(x) - self.__y[i]) * x
        return sum
    
    def grad(self, delta0, delta1):
        self.__delta0 = delta0
        self.__delta1 = delta1

        while not self.__convergiu():
            temp0 = self.__delta0 - self.__taxa * (1.0/self.__m) * self.__errorSumDelta0()
            temp1 = self.__delta1 - self.__taxa * (1.0/self.__m) * self.__errorSumDelta1()
            self.__delta0 = temp0
            self.__delta1 = temp1
            # print(self.__delta0, self.__delta1)
        
        if self.__it == self.__limitIt:
            print("ESTOUROU O LIMITE DE ITERACOES")
    
    def getParams(self):
        return self.__delta0, self.__delta1
    
