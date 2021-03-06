import numpy as np
import math
# from sklearn.base import BaseEstimator


# class LMSTrainer(BaseEstimator):
class LMSTrainer():
    def __init__(self, delta, alpha, tolerancia, analitic=False):
        self.analitic = analitic
        self._trained = False
        self.analitic = analitic
        self._trained = False
        self._delta = delta  # vetor de parametros
        self._alpha = alpha  # taxa de convergencias
        self._tolerancia = tolerancia  # erro maximo
        self._custoAnt = 0.0  # quarda o custo da iteracao anterior
        self._max = 999999  # quantidade maxima de iteracoes
        self._it = 0  # iteracao atual
        self._epslon = 0.000001

    def fit(self, X, y=None):
        if self.analitic:
            # TODO: FAZER POR MATRIZES
            pass
        else:
            Xi = np.insert(X, 0, values=1, axis=1)
            self.grad(Xi, y)
        self._trained = True

        return self

    def predict(self, X, y=None):
        if not self._trained:
            raise RuntimeError("You must train classifer before predicting data!")
        else:
            # Xi = np.insert(X, 0, values=1, axis=1)
            Xi = [1] + X
            return self.h(Xi)

    def h(self, x):
        #if type(x) is int:
        #   x = [1, x]
        return 1. / (1. + math.e ** -(np.dot(self._delta, x)))
        # if type(x) is int:
        #    return self.funcAfim(x)
        # else:
        #    return np.dot(x, self._delta)

    def custo(self, X, y, n):
        error = 0.0
        for i, x in enumerate(X):
            error += (-y[i] * math.log(self.h(x)+self._epslon)) - ((1 - y[i]) * math.log(1 - self.h(x)+self._epslon))  # (self.h(x) - y[i])**2
        return error / n

    def convergiu(self, X, y, n):
        self._it += 1
        custo_atual = self.custo(X, y, n)
        flag1 = self._it >= self._max
        flag2 = np.abs(custo_atual - self._custoAnt) <= self._tolerancia
        self._custoAnt = custo_atual

        return flag1 or flag2

    def grad(self, X, y):
        m = len(y)
        while not self.convergiu(X, y, m):
            tmp = []
            qtd = len(self._delta)
            for i in range(qtd):
                tmp.append(self._delta[i] - self._alpha * self.sumDiff(X, y, m, i))
            self._delta = np.copy(tmp)
        if self._it >= self._max:
            print("número máximo de iterações alcançado.")

    def sumDiff(self, X, y, n, j):
        sum = 0.0
        for i, x in enumerate(X):
            sum += ((self.h(x) - y[i]) * x[j])
        return sum / n

    def funcAfim(self, x):
        return self._delta[0] + self._delta[1] * x

    def getDelta(self):
        return self._delta
