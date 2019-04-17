import matplotlib.pyplot as plt


class DrawingGraph:
    Id = 1

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
    def draw_classification(x, y, title):
        plt.figure(DrawingGraph.Id)
        plt.title(title)
        DrawingGraph.Id += 1
        temp0y = []
        temp0x = []
        temp1y = []
        temp1x = []
        for i, yi in enumerate(y):
            if yi <= 0.5:
                temp0y += [yi]
                temp0x += [x[i]]
            else:
                temp1y += [yi]
                temp1x += [x[i]]
        plt.axis((x[0][0]-1, x[-1][0]+1, -0.5, 1.5))
        plt.scatter(temp0x, temp0y, s=60, c='r')
        plt.scatter(temp1x, temp1y, s=60, c='b')
        #plt.show()

    @staticmethod
    def show():
        plt.show()

