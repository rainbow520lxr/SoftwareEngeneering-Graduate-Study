# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#导入模块
import numpy as np
import matplotlib.pyplot as plt

#产生数据集
X=np.array([[1,2],[-1,2],[0,-1]])
#产生目标数据集
Y=np.array([1,0,0])

#产生参数集
#w=np.random.RandomState(seed).rand(1,2)
w=np.array([[1,-0.8]])
print(w)

x=np.linspace(-2,2)
y=-(w[0,0]/w[0,1]*x)
plt.scatter(X[:,0],X[:,1]) 
plt.plot(x,y)           
plt.show()

#前向传播计算函数
def cacul(x,w):
    y=np.dot(x.T,w)
    if y>0:
        res=1
    else:
        res=0
    return res

#训练反向传播
STEPS=10
for i in range(STEPS):
    print('训练了',i,'次')
    if cacul(X[0],w[0])!=1:
        print('加变换')
        w[0]=w[0]+X[0]
        print(w[0])
        
        x=np.linspace(-2,2)
        y=-(w[0,0]/w[0,1]*x)
        plt.scatter(X[:,0],X[:,1]) 
        plt.plot(x,y)           
        plt.show()
        
    if cacul(X[1],w[0])!=0:
        print('减变换1')
        w[0]=w[0]-X[1]
        print(w[0])
        
        x=np.linspace(-2,2)
        y=-(w[0,0]/w[0,1]*x)
        plt.scatter(X[:,0],X[:,1]) 
        plt.plot(x,y)           
        plt.show()
        
    if cacul(X[2],w[0])!=0:
        print('减变换2')
        w[0]=w[0]-X[2]
        print(w[0])
        
        x=np.linspace(-2,2)
        y=-(w[0,0]/w[0,1]*x)
        plt.scatter(X[:,0],X[:,1]) 
        plt.plot(x,y)           
        plt.show()
        
print('结果为：',w[0])

x=np.linspace(-2,2)
y=-(w[0,0]/w[0,1]*x)
plt.scatter(X[:,0],X[:,1]) 
plt.plot(x,y)           
plt.show()
















          

