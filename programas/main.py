from Regrecao_logistica import LMSTrainer
import numpy as np
import DrawingGraph as dg


x_train = np.array([[1,2],[1,3],[1,4]])
y_train = np.array([0,0,1])

teste = np.array([x[1] for x in x_train])
trainer = LMSTrainer([1,1], 0.1, 1)

#dg.drawPoint(teste, y_train)
#dg.draw(teste, trainer.funcAfim, "hipotese")
print("deltas: ", trainer.getDelta())

pred = trainer.fit(x_train, y_train)

#dg.drawPoint(teste, y_train)
#dg.draw(teste, trainer.funcAfim, "resltado")
print("deltas: ", trainer.getDelta())

print(pred.predict(5))