import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def Coefficient_2(nn, mm, XY=[]):
    cc = 0
    for i in range(0, nn):
        cc += (XY[i])**mm
    cc = cc / nn
    return cc

def Coefficient(Xi=[], Yi=[]):    #n为数组元素个数，m为一元m次函数, m2为中间变量。
    global n, m, m2, mk, cx, cy
    for i in range(0, m+1):
        cx[m2].append(Coefficient_2(n, i, Xi))
    for i in range(0, 1):
        cy[m2].append(Coefficient_2(n, 1, Yi))
    while mk - 1 >= 0:
        n -= 1; mk -= 1; m2 += 1
        Coefficient(Xi, Yi)
    return cx, cy

#y = -4 + 8*x - 2*x**2 - 5*x**3 + 1.3*x**4 + x**5
Xi_1 = [-2.6, -2.3, -2, -1.5, -1, -0.3, 0.2, 0.5, 1, 1.35, 1.5, 1.9]
Yi_1 = [-9.85, -0.129, 0.8, -4.64, -8.71, -6.44, -2.52, -1.01, -0.7, -0.345, 0.8, 11.4]

# y = 6.9 - 5.6*x + 1.2*x*x
#Xi_1 = [-7, -6, -5, -2.5, 1, 2.5, 5, 7, 9, 12]
#Yi_1 = [104.6, 83.1, 65.8, 27.5, 2.5, 0.386, 9.36, 26.9, 52.8, 112.6]

m = 5    #m为一元m次函数，需手工修改。
n = len(Xi_1); m2 = 0; mk = m; cx = []; cy = []
for i in range(0, m+1):
    cx.insert(m, [])
    cy.insert(m, [])
CX, CY = Coefficient(Xi_1, Yi_1)
#print('CX=', CX, '    CY=', CY)

#解方程组：
xx = solve(np.array(CX), np.array(CY))

###绘图，看拟合效果###
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')      #装载中文字库
plt.figure(figsize = (5, 5))    #创建图形，设置图形整体大小，单位为英寸
plt.scatter(Xi_1, Yi_1, color = "red", label = "样本点", linewidth = 2)    #画样本点
x = np.linspace(Xi_1[0] - 0.02, Xi_1[len(Xi_1) - 1] + 0.02, 1000)    #确定X轴需显示数据的范围，并设置曲线点数

#绘制y = a + b*x + c*x^2 + ……函数
y = 0
for i in range(0, m+1):
    y += xx[i]*x**i
xxx = [num for elem in xx for num in elem]
plt.plot(x, y, color = "orange", label = "拟合数据", linewidth=2)    #画拟合曲线
a = round(xx[0][0], 8)
b = round(xx[1][0], 8)
c = round(xx[2][0], 8)
plt.title("拟合曲线为 y ＝ {0}+{1}x+{2}x^2+…… \n其系数对应为：{3}".format(a, b, c, xxx), FontProperties='STKAITI', fontsize=14)    #需在坐标图顶部标注的字

plt.legend(prop=myfont)     # 设置图例，显示中文字体。
plt.show()
