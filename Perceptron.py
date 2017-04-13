import numpy as np
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp =x1*w1 +x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta :
        return 1


def ANDb(x1,x2):
    x =np.array([x1,x2])
    w =np.array([0.5,0.5])
    b =-0.7
    tmp =np.sum(w*x) +b
    if tmp <= 0:
        return 0
    else:
        return 1

def NANDb(x1,x2):
    x = np.array([x1, x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
def ORb(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XORb(x1,x2):
    s1 =NANDb(x1,x2)
    s2 =ORb(x1,x2)
    y =ANDb(s1,s2)
    return y

def step_function(x):
    #配列であれば x>0であれば True,それ以外は Falseの配列にする
    y =x >0
    #boolean配列をnumpy.intの配列に変換 True->1,False->0
    return y.astype(np.int)