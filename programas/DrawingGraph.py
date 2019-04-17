import matplotlib.pyplot as plt


class DrawingGraph:

    @staticmethod
    def draw_point(x, y):
        plt.scatter(x, y, s=10, c='r' )

    @staticmethod
    def draw(x, f, title): # valores x e função f
        plt.plot(x, [f(a) for a in x])
        plt.title(title)
        plt.show()
    
    @staticmethod
    def draw_point2(x, y):
        plt.scatter(x, y, s=10, c='b')
        plt.show()

    @staticmethod
    def draw_classification(x, y):
        temp0y = []
        temp0x = []
        temp1y = []
        temp1x = []
        for i, yi in enumerate(y):
            if yi == 0:
                temp0y += [yi]
                temp0x += [x[i]]
            else:
                temp1y += [yi]
                temp1x += [x[i]]
        plt.scatter(temp0x, temp0y, s=10, c='r')
        plt.scatter(temp1x, temp1y, s=10, c='b')

