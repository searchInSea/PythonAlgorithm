import numpy as np
import random
import matplotlib.pyplot as plt

#生成输入数据

#plt.show()
def generateOriginData(samNum):
    X1 = np.random.random((samNum, 1)) * 10
    Y = np.zeros((samNum, 1))
    Y[(samNum // 2):] = 1
    # print(Y)
    # print(X1)
    X2 = 3 * X1 + 10
    # print(X2)
    plt.plot(X1, X2)
    offset = np.random.uniform(1, 100, size=(samNum, 1))
    X2[0:samNum // 2] -= offset[0:samNum // 2]
    X2[samNum // 2:] += offset[samNum // 2:]
    plt.scatter(X1[:samNum // 2], X2[:samNum // 2], marker='*', color='g')
    plt.scatter(X1[samNum // 2:], X2[samNum // 2:], marker='+', color='r')
    X12 = np.append(X1, X2, axis=1)
    plt.show()
    print('X12=', X12.T, '\nY=', Y.T)
    return (X12,Y)

#画线函数
def plotLine(X1, X2, W, B):
    X1 = np.array(X1).reshape(len(X1), 1)
    X2 = np.array(X2).reshape(len(X2), 1)
    plt.plot(X1, -(W[0] / W[1] * X1) - B)
    plt.scatter(X1[:samNum // 2], X2[:samNum // 2], marker='*', color='g')
    plt.scatter(X1[samNum // 2:], X2[samNum // 2:], marker='+', color='r')
    plt.show()

def procForward(W, X12, B):
    Z = np.dot(W.T, X12) + B
    Z = Z.T
    # print('z=',Z.T)
    A = 1 / (1 + np.exp(-Z))
    return A

samNum = 100
X12,Y = generateOriginData(samNum)
#学习参数
W = np.zeros((2, 1))  # 只有2个特征
B = np.zeros((1, 1))

X12 = X12.T  # 变成两行,每一列都是一个样点
#X12 = np.array([[3.41827387,2.84210487,   5.46492579,   1.37031555],[-28.43534583, -21.74959217,  31.71029071,  45.06466409]])
effect = np.array([[0.005],])
Jprev = 1;
Jcuren = 0xFFFFFFFF
cnt = 0;
while (Jcuren - Jprev < -10e-8 or cnt < 15) and cnt < 19000:  #避免前几次迭代不稳定，导致J下降不明显
    cnt+=1
    Z = np.dot(W.T, X12) + B
    Z = Z.T
    # print('z=',Z.T)
    A = 1 / (1 + np.exp(-Z))

    L = [Y * np.log(A) + (1 - Y) * np.log(1 - A)] * np.array([-1])
    #     # print('L*-1=',L*(np.array([-1])))
    #print('L=',L.T)
    Jprev = Jcuren;
    Jcuren = np.sum(L) / samNum
    #print('J=', Jcuren, 'Jprev=', Jprev, 'J-Jprev=',Jcuren-Jprev,  'cunt=',cnt)

    dA = -Y / A + (1 - Y) / (1 - A)
    dZ = dA * (A * (1 - A))
    dW = dZ * (X12.T)
    dB = dZ

    dWAve = np.sum(dW, axis=0) / samNum
    dBAve = np.sum(dB, axis=0) / samNum
    dWAve = np.array(dWAve).reshape(len(dWAve), 1)
    dBAve = np.array(dBAve).reshape(len(dBAve), 1)
    # print('dWAve=',dWAve)
    # print('dBAve=',dBAve)
    W = W - effect * dWAve
    B = B - effect * dBAve

print('A=',A.T)
print('W=', W, ' B=', B, '-W0/W1=', -W[0] / W[1])
print('J=', Jcuren, 'Jprev=', Jprev, 'J-Jprev=',Jcuren-Jprev,  'cunt=',cnt)
#print('X12=',X12, '\nX12.shape=',X12.shape,'\nX12[0].shape=',X12[0].shape,'\nX12[1].shape',X12[1].shape )
plotLine(X12[0], X12[1], W, B)