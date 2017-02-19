import matplotlib.pyplot as plt

def eisenhowerMatrix(x,y,display=True):
    i=0
    decisions = {}
    for a,b in zip(x,y):
        i+=1
        if a>=-50 and a<=-1 and b >= -50 and b<=-1:
            decisions[i]={'Do it Later':(a,b)}
        elif a>=-50 and a<=-1 and b >= 0 and b<=50:
            decisions[i]={'Decide When':(a,b)}
        elif a>=0 and a <= 50 and b>=-50 and b<=-1:
            decisions[i]={'Delegate to Someone Else':(a,b)}
        elif a>=0 and a<=50 and b>=0 and b<=50:
            decisions[i]={'Do it Now':(a,b)}
    i=0
    if display==True:
        plt.xlim([-50,50])
        plt.ylim([-50,50])
        plt.plot([-50,50], linewidth=1, color='black' )
        plt.plot([-50,50], [0,0], linewidth=1, color='black' )
        plt.xlabel('Urgency')
        plt.ylabel('Importance')
        plt.annotate('Do it Later', xy=(-25, 25), xytext=(-33, -25))
        plt.annotate('Delegate to Someone Else', xy=(25, -25), xytext=(5, -25))
        plt.annotate('Decide When', xy=(-25, 25), xytext=(-33, 25))
        plt.annotate('Do it Now', xy=(25, 25), xytext=(15, 25))
        plt.title('Eisenhower Decision Matrix')
        plt.plot(x,y,'x', color='red')
        for a,b in zip(x,y):
            i+=1
            plt.annotate(i, xy=(a,b), textcoords='data')
        plt.show()
        plt.close()
    return decisions