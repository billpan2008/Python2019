import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy.linalg import solve


def Coefficient(n, Xi=[], Yi=[]):
    Coe_a = 1; Coe_b = 0; Coe_c = 0; Coe_y = 0
    for i in range(0, n):
        Coe_b += Xi[i]
        Coe_c += (Xi[i]) ** 2
        Coe_y += Yi[i]
    Coe_b = Coe_b / n
    Coe_c = Coe_c / n
    Coe_y = Coe_y / n
    return(Coe_a, Coe_b, Coe_c, Coe_y)

# y = 6.9 - 5.6*x + 1.2*x*x
Xi_1 = [-7, -6, -5, -2.5, 1, 2.5, 5, 7, 9, 12]
Yi_1 = [104.6, 83.1, 65.8, 27.5, 2.5, 0.386, 9.36, 26.9, 52.8, 112.6]

m = 3    #几个系数，一元二次函数 m=2+1
Row = []
for i in range(0, m):
    k = len(Xi_1) - i
    Row.append(list(Coefficient(k, Xi_1, Yi_1)))
#print(Row)

#解方程组
Fa = np.array([Row[0][0:m], Row[1][0:m], Row[2][0:m]])
Fb = np.array([Row[0][m:m+1], Row[1][m:m+1], Row[2][m:m+1]])
#Fb = np.array([[Row[0][m]], [Row[1][m]], [Row[2][m]]])    #本行代码与上一行代码等效
xx = solve(Fa, Fb)

###绘图，看拟合效果###
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')      #装载中文字库
plt.figure(figsize = (5, 5))    #创建图形，设置图形整体大小，单位为英寸
plt.scatter(Xi_1, Yi_1, color = "red", label = "样本点", linewidth = 2)    #画样本点
x = np.linspace(Xi_1[0] - 0.3, Xi_1[len(Xi_1) - 1] + 0.3, 1000)    #确定X轴需显示数据的范围，并设置曲线点数

#绘制y = a + b*x + c*x^2函数
a = round(xx[0][0], 6)
b = round(xx[1][0], 6)
c = round(xx[2][0], 6)
print('a＝{0}，b＝{1}，c＝{2}。'.format(a, b, c))
y = a + b*x + c*x**2
plt.plot(x, y, color = "orange", label = "拟合数据", linewidth=2)    #画拟合曲线
plt.title("拟合曲线为 y ＝ {0}+{1}x+{2}x^2".format(a, b, c), FontProperties='STKAITI', fontsize=14)    #需在坐标图顶部标注的字

plt.legend(prop=myfont)     # 设置图例，显示中文字体。
plt.show()


'''
old：
def Lsqcurvefit_02(Xi=[], Yi=[]):
    S_xx_111 = 0
    S_yy_01 = (np.sum(Yi)) / len(Yi)
    S_xx_01 = (np.sum(Xi)) / len(Xi)
    for i in range(0, len(Xi)):
        S_xx_111 += Xi[i] * Xi[i]
    S_xx_01_2 = S_xx_111 / len(Xi)
    S_yy_02 = (S_yy_01 * len(Yi) - Yi[len(Yi)-1] ) /(len(Yi) - 1)
    S_xx_02 = (S_xx_01 * len(Xi) - Xi[len(Xi)-1]) /(len(Xi) - 1)
    S_xx_02_2 = (S_xx_01_2 * len(Xi) - Xi[len(Xi)-1] * Xi[len(Xi)-1]) /(len(Xi) - 1)
    S_yy_03 = (S_yy_02 * (len(Yi)-1) - Yi[len(Yi)-2]) /(len(Yi) - 2)
    S_xx_03 = (S_xx_02 * (len(Xi)-1) - Xi[len(Xi)-2]) /(len(Xi) - 2)
    S_xx_03_2 = (S_xx_01_2 * (len(Xi) - 1) - Xi[len(Xi)-2] * Xi[len(Xi)-2]) /(len(Xi) - 2)
    from scipy.linalg import solve
    m = np.array([[1, S_xx_01, S_xx_01_2], [1, S_xx_02, S_xx_02_2], [1, S_xx_03, S_xx_03_2]])
    n = np.array([S_yy_01, S_yy_02, S_yy_03])
    x = solve(m, n)
    return(x)

下面这个根本不能赋值：
def Coefficient(m, Xi=[], Yi=[]):
    n = len(Xi)
    for i in range(0, m):
        Coe_a[i] = 1    #a的系数
        for j in range(0, m):
            Coe_b[i, j] = 0; Coe_c[i, j] = 0; Coe_y[i, j] = 0
            for k in range(0, n):
                Coe_b[i, j] += (Xi[k]) ** (m - 2)    #计算b的系数
                Coe_c[i, j] += (Xi[k]) ** (m - 1)    #计算c的系数
                Coe_y[i, j] += (Yi[k]) ** (m - 2)
            Coe_b[i, j] = Coe_b[i, j] / (n - j)
            Coe_c[i, j] = Coe_c[i, j] / (n - j)
            Coe_y[i, j] = Coe_y[i, j] / (n - j)
            print(Coe_b[1, 1])

'''
