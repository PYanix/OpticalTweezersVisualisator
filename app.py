import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import math
import requests
from scipy.interpolate import RegularGridInterpolator
from PIL import Image

st.title('Расчет динамики частицы в оптическом пинцете')
#
st.header('Выбор параметров системы')
#Размер перетяжки 1, 0.5, 0.25 длины волны
waist = st.radio(
    "Размер перетяжки в "+r'$\lambda$',
    [1, 0.5, 0.25],
    index=0, 
    horizontal=True,
)
#Размер частицы 0.05, 0.1, 0.2, 0.5 длины волны
radius = st.radio(
    "Размер частицы (радиус)",
    [0.05, 0.1, 0.2, 0.5],
    index=0,
    horizontal=True,
)

#Контраст n частицы/n окружения 1.2, 2.1, 3, 3.9
contrast = st.radio(
    "Контраст "+r'$\frac{n_{particle}}{n_{medium}}$',
    [1.2, 2.1, 3, 3.9],
    index=0,
    horizontal=True,
)

#response

res = requests.get(f'http://127.0.0.1:8000/waist{waist}/radius{radius}/contrast{contrast}')
#st.write(res.text)
data = res.json()
table_x = data[0]
table_z = data[1]

# Интерполяция
R = radius * 532 *10**(-9)      # радиус частицы
density = 1.96 * 1000           # плотность
m = 4*R**3/3*density*math.pi    # масса частицы
k_ci = 1.33*3.3966*10**-26      # коэфф размерности для силы

force = np.random.rand(4, 4)
proj = ''
raz_z = 3000
raz_x = 1500
period = 10
first_koor = 0

def massive(x, z, proj):
    x1 = int(x*1000000000 // period + raz_x // period) - 1
    z1 = int(z*1000000000 // period + raz_z // period) - 1
    if proj == 'x':
        for i in range(4):
            for j in range(4):
                force[i][j] = table_x[i + x1][j + z1]
    elif proj == 'z':
        for i in range(4):
            for j in range(4):
                force[i][j] = table_z[i + x1][j + z1]

def F(x, z, projection):
    x_arr = [(x * 1000000000 // period * period + first_koor) * 0.000000001 - period * 0.000000001,
            (x * 1000000000 // period * period + first_koor) * 0.000000001,
            (x * 1000000000 // period * period + first_koor) * 0.000000001 + period * 0.000000001,
            (x * 1000000000 // period * period + first_koor) * 0.000000001 + 2 * period * 0.000000001]
    z_arr = [z * 1000000000 // period * period * 0.000000001 - period * 0.000000001,
            z * 1000000000 // period * period * 0.000000001,
            z * 1000000000 // period * period * 0.000000001 + period * 0.000000001,
            z * 1000000000 // period * period * 0.000000001 + 2 * period * 0.000000001]

    massive(x, z, projection)
    interp = RegularGridInterpolator((x_arr, z_arr), force, method='cubic')
    return interp((x, z))*k_ci
arr_z = []
arr_Fz = []
s0=10**(-9)
for i in range(-2900, 2900, 10):
    arr_Fz.append(F(s0*0.001, s0*i, 'z'))
    arr_z.append(s0*i)
    print(i)
print(F(s0*300, -s0*1100, 'z'))
fig, ax = plt.subplots()
ax.plot(arr_z, arr_Fz, 'black')
ax.plot([-3000*s0, 3000*s0], [0, 0])
ax.set_ylabel('Fz, Н')
ax.set_xlabel('z, м')
st.pyplot(fig)
#
st.header('Выбор начальных координат') # слайдеры выбора начальных координат
x0 = st.slider('x',  min_value=-1500, max_value=1500, value = 300, step=1) 
z0 = st.slider('z',  min_value=-3000, max_value=3000, value = -1100, step=1)  

#or 

#number_x = st.number_input('enter the x coordinate', min_value=-100, max_value=100, value = 50)
#number_z = st.number_input('enter the z coordinate', min_value=-100, max_value=100, value = 50)
#st.write('x = ', number_x, 'z = ', number_z)

#start
if st.button('Start'):
    
    # расчет массива координат траектории
    
    R = radius * 532 *10**(-9)         # радиус частицы
    density = 1.96 * 1000           # плотность
    m = 4*R**3/3*density*math.pi    # масса частицы
    k_ci = 1.33*3.3966*10**-26      # коэфф размерности для силы

    # начальные условия
    x0 = x0 * 10**-9
    v0_x = 0

    z0 = 10**-9 * z0
    v0_z = 0

    Tmax = 10000
    dt = 1 / 1

    # velocity-Verle method

    x = x0
    v_x = v0_x
    v2_x = 0
    arr_x = [x0]
    arr_v_x = [v0_x]

    z = z0
    v_z = v0_z
    v2_z = 0
    arr_z = [z0]
    arr_v_z = [v0_z]

    t = dt
    arr_t = [0]
    
    while t < 5000 * dt:
        try:
            for _ in range(1):  # частота запоминания x, v с периодичностью...


                v2_x = v_x + dt / 2 * F(x, z, 'x') / m
                v2_z = v_z + dt / 2 * F(x, z, 'z') / m
                print(v2_x)

                x = x + dt * v2_x
                z = z + dt * v2_z

                v_x = v2_x + dt / 2 * F(x, z, 'x') / m
                v_z = v2_z + dt / 2 * F(x, z, 'z') / m

                t += dt

            arr_x.append(x)
            arr_v_x.append(v_x)
            arr_z.append(z)
            arr_v_z.append(v_z)
            arr_t.append(t)
            
        except:
            break
    # отрисовка графиков
    col1, col2 = st.columns([1, 1])
    col1.subheader("trajectory")
    col2.subheader("animated trajectory")    
    # картинка с фоном

    fig, ax = plt.subplots()
    img = Image.open('C:/Users/yana5/PycharmProjects/pythonProject/pictures/пучок_1.jfif')

    ax.plot(arr_x, arr_z, 'green')           #кривая траектории
    ax.scatter(x0, z0, color = 'green', label = 'точка старта')     #точка старта
    ax.scatter(0, 0, color = 'black')#, label = 'начало координат')       # начало координат
    ax.scatter(x, z, color = 'red')#, label = 'конечная точка')   #конечная точка

    plt.imshow(img, cmap='gray', aspect=0.5, alpha=0.7,extent=[-1.5*10**-6, 1.5*10**-6, -4*10**-6, 4*10**-6])
    plt.xlabel("x")
    plt.ylabel("z")
    plt.legend(loc=1)

    col1.pyplot(fig)

    # данные для построения анимированного графика
    x = arr_x
    y = arr_z
    # минимальные и максимальные значения на осях
    xm = -1.5*10**(-6)
    xM = 1.5*10**(-6)
    ym = -4*10**(-6) 
    yM = 4*10**(-6) 

    # отрисовка анимированного графика
    fig = go.Figure(
        data=[go.Scatter(x=x, y=y,
                        mode="lines",
                        line=dict(width=2, color="blue")),
            go.Scatter(x=x, y=y,
                        mode="lines",
                        line=dict(width=2, color="blue"))],
        layout=go.Layout(
            xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
            updatemenus=[dict(type="buttons",
                            buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None])])]),
        frames=[go.Frame(
            data=[go.Scatter(
                x=[arr_x[k]],
                y=[arr_z[k]],
                mode="markers",
                marker=dict(color="red", size=10))])

            for k in range(0, len(arr_x), 50)]
    )
    col2.write(fig)
    