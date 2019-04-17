from Regrecao_logistica import LMSTrainer
from DrawingGraph import DrawingGraph
import numpy as np
import math


# x_train = np.array([[1,2],[1,3],[1,4]])
x_train = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
#y_train = np.array([0,0,1])
y_train = [0,0,0,0,0,0,1,1,1,1,1,1]

x_teste =[[-1],[1.5],[8.4],[4.5], [5.5],[4.7],[6.5],[5.2]]
# teste = np.array([x[1] for x in x_train])
trainer = LMSTrainer([1,1], 0.1, 0.000001)

#DrawingGraph.draw_point(teste, y_train)
#DrawingGraph.draw(teste, trainer.funcAfim, 'hipotese')

print("deltas: ", trainer.getDelta())

pred = trainer.fit(x_train, y_train)

# DrawingGraph.draw_point(teste, y_train)
#DrawingGraph.draw(teste, trainer.funcAfim, "resltado")
DrawingGraph.draw_classification(x_train, y_train, "gabarito")
print("deltas: ", trainer.getDelta())

resposta = [pred.predict(x) for x in x_teste]
print("resposta = ", resposta)
DrawingGraph.draw_classification(x_teste, resposta, "predicao")

#DrawingGraph.show()


# x_teste = Xi = np.insert(x_teste, 0, values=1, axis=1)
#DrawingGraph.draw(x_teste, pred.h, "hipotese")
# DrawingGraph.draw(x_teste, lambda x : 1/1+math.e**(-x), "Teste")
DrawingGraph.show()
