from Regrecao_logistica import LMSTrainer
from DrawingGraph import DrawingGraph
import numpy as np


x_train = np.array([[1,2],[1,3],[1,4]])
y_train = np.array([0,0,1])

teste = np.array([x[1] for x in x_train])
trainer = LMSTrainer([1,1], 0.1, 1)

#DrawingGraph.draw_point(teste, y_train)
#DrawingGraph.draw(teste, trainer.funcAfim, 'hipotese')
print("deltas: ", trainer.getDelta())

pred = trainer.fit(x_train, y_train)

#DrawingGraph.draw_point(teste, y_train)
#DrawingGraph.draw(teste, trainer.funcAfim, "resltado")
print("deltas: ", trainer.getDelta())

print(pred.predict(5))