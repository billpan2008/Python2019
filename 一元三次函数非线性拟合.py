import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy.linalg import solve

def Coefficient(n, Xi=[], Yi=[]):
    Coe_a = 1; Coe_b = 0; Coe_c = 0; Coe_d = 0; Coe_y = 0
    for i in range(0, n):
        Coe_b += Xi[i]
        Coe_c += (Xi[i]) ** 2
        Coe_d += (Xi[i]) ** 3
        Coe_y += Yi[i]
    Coe_b = Coe_b / n
    Coe_c = Coe_c / n
    Coe_d = Coe_d / n
    Coe_y = Coe_y / n
    return(Coe_a, Coe_b, Coe_c, Coe_d, Coe_y)

def fit(n, Xi, Yi):
    num = (Xi - Yi)**n
    return num

# y = 16.9 + 3.6*x - 8.2*x**2 + 1.69*x**3
Xi_1 = [-3, -2, -1, -0.5, 0.5, 1, 2, 3, 4, 6]
Yi_1 = [-113.8, -36.1, 3.45, 12.3, 16.5, 14.5, 4.84, -0.47, 8.03, 111.7]

m = 4    #几个系数，一元三次方程 m=3+1
Row = []
for i in range(0, m):
    k = len(Xi_1) - i
    Row.append(list(Coefficient(k, Xi_1, Yi_1)))
#print(Row)

#解方程组
Fa = np.array([Row[0][0:m], Row[1][0:m], Row[2][0:m], Row[3][0:m]])
Fb = np.array([Row[0][m:m+1], Row[1][m:m+1], Row[2][m:m+1], Row[3][m:m+1]])
xx = solve(Fa, Fb)

###绘图，看拟合效果###
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')      #装载中文字库
plt.figure(figsize = (5, 5))    #创建图形，设置图形整体大小，单位为英寸
plt.scatter(Xi_1, Yi_1, color = "red", label = "样本点", linewidth = 2)    #画样本点
x = np.linspace(Xi_1[0] - 0.3, Xi_1[len(Xi_1) - 1] + 0.3, 1000)    #确定X轴需显示数据的范围，并设置曲线点数

#绘制y = a + b*x + c*x^2 + d*x^3函数 及计算拟合优度 R-square
a = round(xx[0][0], 6)
b = round(xx[1][0], 6)
c = round(xx[2][0], 6)
d = round(xx[3][0], 6)
print('a＝{0}，b＝{1}，c＝{2}，d＝{3}。'.format(a, b, c, d))
y = a + b*x + c*x**2 + d*x**3
Xp = np.mean(Xi_1)    #求列表Xi_1的平均值
Yp = np.mean(Yi_1)    #求列表Yi_1的平均值
YL2 = 0; YP2 = 0; XP2 = 0; XP3 = 0; YP3 = 0
for i in range(len(Xi_1)):
    YL2 += fit(2, Yi_1[i], a + b*Xi_1[i] + c*Xi_1[i]**2 + d*Xi_1[i]**3)
    YP2 += fit(2, Yi_1[i], Yp)
    #XP2 += fit(2, Xi_1[i], Xp)
    #XP3 += fit(1, Xi_1[i], Xp)
    #YP3 += fit(1, Yi_1[i], Yp)
square = 1 - YL2 / YP2    #拟合优度 R-squar
print('拟合优度 R-square=', square)
#r = XP3 * YP3 / (XP2 * YP2)**0.5
#print('相关系数 r=', square)
plt.plot(x, y, color = "orange", label = "拟合数据", linewidth=2)    #画拟合曲线
plt.title("拟合曲线为 y ＝ {0}+{1}x+{2}x^2+{3}x^3".format(a, b, c, d), FontProperties='STKAITI', fontsize=14)    #需在坐标图顶部标注的字

plt.legend(prop=myfont)     # 设置图例，显示中文字体。
plt.show()


'''
def transform(x):
    xx1 = 16.9 + 3.6*x - 8.2*x**2 + 1.69*x**3
    return xx1
Xi_1 = [-3, -2, -1, -0.5, 0.5, 1, 2, 3, 4, 6]
num = list(map(transform, Xi_1))
print(num)
'''

