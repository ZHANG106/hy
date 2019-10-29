import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

b_val = 10
c_val = 20
mpl.rcParams['font.sans-serif'] = ['SimHei']
burning = pd.read_excel(r'.\燃烧热.xlsx', header=None, sheet_name='工作表1')

plt.xlim(0, 30)
plt.ylim(0, 1.45)

X, y = burning[0], burning[1]
X_ab, y_ab = burning[burning[0] <= b_val][0], burning[burning[0] <= b_val][1]
X_bc, y_bc = burning[(burning[0] > b_val) & (burning[0] < c_val)][0], \
             burning[(burning[0] > b_val) & (burning[0] < c_val)][1]
X_cd, y_cd = burning[burning[0] >= c_val][0], burning[burning[0] >= c_val][1]

polyfit_ab = np.polyfit(X_ab, y_ab, 1)
p_ab = np.poly1d(polyfit_ab)
yvals_ab = p_ab(X_ab)

polyfit_cd = np.polyfit(X_cd, y_cd, 1)
p_cd = np.poly1d(polyfit_cd)
yvals_cd = p_cd(X_cd)

X_bc_ = np.array([list(X_ab)[-1]] + list(X_bc) + [list(X_cd)[0]])
y_bc_ = np.array([list(y_ab)[-1]] + list(y_bc) + [list(y_cd)[0]])
polyfit_bc = np.polyfit(X_bc_, y_bc_, 4)
p_bc = np.poly1d(polyfit_bc)
yvals_bc = p_bc(X_bc_)

# 这一块用sklearn的回归方法试了下，结果一样

# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
#
# linear_model = LinearRegression()
# poly_reg = PolynomialFeatures(degree=4)
# X_bc_ = X_bc_.reshape(-1, 1)
# y_bc_ = y_bc_.reshape(-1, 1)
# X_ploy = poly_reg.fit_transform(X_bc_)
# lin_reg_2 = LinearRegression()
# lin_reg_2.fit(X_ploy, y_bc_)
#
# plt.plot(X_bc_, lin_reg_2.predict(poly_reg.fit_transform(X_bc_)), 'g-')


plt.plot(X_ab, yvals_ab, 'r', linewidth=2.5)
plt.plot(X_cd, yvals_cd, 'r', linewidth=2.5)
plt.plot(X_bc_, yvals_bc, 'g-', linewidth=2.5)
plt.scatter(burning[0], burning[1], s=18)


def get_x_0(y_o):
    '''
    二分法求解x_o的坐标
    :param y_o:
    :return:
    '''

    for i in list(X_bc):
        a = i
        if p_bc(a) > y_o:
            break
        b = i
    x_o = (a + b) / 2
    while abs(p_bc(x_o) - y_o) >= 0.0001:
        x_o = (a + b) / 2
        if p_bc(x_o) < y_o:
            b = (a + b) / 2
        elif p_bc(x_o) > y_o:
            a = (a + b) / 2
        else:
            return x_o
    return x_o


y_bcss = burning[(burning[0] >= b_val) & (burning[0] <= c_val)][1]

y_o = (y_bcss.min() + y_bcss.max()) / 2
x_o = get_x_0(y_o)

X_bcs, y_bcs = burning[(burning[0] >= b_val) & (burning[0] <= c_val)][0], \
               burning[(burning[0] >= b_val) & (burning[0] <= c_val)][1]
E_x = X_bcs[y_bcs == y_bcs.min()]
F_x = X_bcs[y_bcs == y_bcs.max()]

plt.plot([X_bc_[0], x_o], p_ab([X_bc_[0], x_o]), '--', linewidth=2.5)
plt.plot(x_o, p_ab(x_o), '.', markersize=4)
plt.text(x_o + 0.08, p_ab(x_o) - 0.05, 'E\nE\'', fontsize=14)
plt.plot([x_o, X_bc_[-1]], p_cd([x_o, X_bc_[-1]]), '--', linewidth=2.5)
plt.plot(x_o, p_cd(x_o), '.', markersize=4)
plt.text(x_o + 0.08, p_cd(x_o) - 0.05, 'F\nF\'', fontsize=14)
A = (x_o, -0.1)
B = (x_o, y_cd.max() + 0.1)

plt.plot([A[0], B[0]], [A[1], B[1]], '-', color='black', linewidth=2.5)
plt.plot([0, x_o], [y_o, y_o], '--', color='black', linewidth=2.5)
plt.plot([0, x_o], [y_bcs.min(), y_bcs.min()], '--', color='black', linewidth=2.5)
plt.plot([0, F_x], [y_bcs.max(), y_bcs.max()], '--', color='black', linewidth=2.5)
plt.text(0.04, y_o + 0.02, 'T', horizontalalignment='left', fontsize=12)
plt.text(0.04, y_bcs.min() + 0.02, 'T1', horizontalalignment='left', fontsize=12)
plt.text(0.04, y_bcs.max() + 0.02, 'T2', horizontalalignment='left', fontsize=12)
plt.plot(x_o, y_o, 'ro')
plt.text(x_o, y_o, ' O', fontsize=14)
print('△T=%-6f' % float(p_cd(x_o) - p_ab(x_o)))
plt.xlabel('时间/min')
plt.ylabel('温度/℃')
plt.title('苯甲酸燃烧曲线的雷诺校正图', fontsize=20)
plt.show()