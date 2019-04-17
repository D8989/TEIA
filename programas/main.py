from Regrecao_logistica import LMSTrainer
from DrawingGraph import DrawingGraph
import numpy as np


# x_train = np.array([[1,2],[1,3],[1,4]])
x_train = [[1], [1.5], [2], [3.5], [4], [4.5]]
#y_train = np.array([0,0,1])
y_train = [0,0,0,1,1,1]

x_teste =[[1],[5],[3.5],[4.5],[3.9],[4.1],[4]]
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

DrawingGraph.show()
