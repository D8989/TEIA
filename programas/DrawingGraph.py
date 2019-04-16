import matplotlib.pyplot as plt

class DrawingGraph:
    
    @staticmethod
    def drawPoint(x, y):
        plt.scatter(x, y, s=10, c='r' )
    
    @staticmethod
    def draw(x, f, title): # valores x e função f
        plt.plot(x, [f(a) for a in x])
        plt.title(title)
        plt.show()
    
    @staticmethod
    def drawPoint2(x, y):
        plt.scatter(x, y, s=10, c='b' )
        plt.show()