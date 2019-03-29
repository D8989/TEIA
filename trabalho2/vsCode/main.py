import LMSTrainer as lms

teste = lms.LMSTrainer([1,2,3], [2,4,6], 1, 0.9)

print(teste.getParams())

teste.grad(1.0,5.0)

print(teste.getParams())