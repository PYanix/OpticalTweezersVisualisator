import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import math
import requests

st.title('Расчет динамики частицы в оптическом пинцете')
#
st.header('Выбор параметров системы')
#Размер перетяжки 1, 0.5, 0.25 длины волны
waist = st.radio(
    "Размер перетяжки в "+r'$\lambda$',
    [1, 0.5, 0.25],
    index=None, 
    horizontal=True,
)

st.write("You selected:", waist)
#Размер частицы 0.05, 0.1, 0.2, 0.5 длины волны
radius = st.radio(
    "Размер частицы",
    [0.05, 0.1, 0.2, 0.5],
    index=None,
    horizontal=True,
)

st.write("You selected:", radius)
#Контраст n частицы/n окружения 1.2, 2.1, 3, 3.9
contrast = st.radio(
    "Контраст n частицы/n окружения",
    [1.2, 2.1, 3, 3.9],
    index=None,
    horizontal=True,
)

st.write("You selected:", contrast)
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'System №',
     df['first column'])

'You selected: ', option
#response
res = requests.get(f'http://127.0.0.1:8000/{str(option)}')
st.write(res.text)

res = requests.get(f'http://127.0.0.1:8000/waist{waist}/radius{radius}/contrast{contrast}')
st.write(res.text)

#
st.header('Выбор начальных координат')
x0 = st.slider('x',  min_value=-1.0, max_value=1.0, value = 1.0, step=0.1)  # 👈 this is a widget
z0 = st.slider('z',  min_value=-300, max_value=300, value = 100, step=1)  # 👈 this is a widget
st.write('x0 =', x0,'z0 = ', z0)

#or 

number_x = st.number_input('enter the x coordinate', min_value=-100, max_value=100, value = 50)
number_z = st.number_input('enter the z coordinate', min_value=-100, max_value=100, value = 50)
st.write('x = ', number_x, 'z = ', number_z)

#start
if st.button('Start'):
    st.write('begin to do smth')
    st.write(f'x={x0}')
    st.write(f'Sistem № {option}')

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

    # Generate curve data
    k_x = 4
    k_y = 9
    m = 1
    omega_x = (k_x/m)**0.5
    omega_y = (k_y/m)**0.5
    omega = math.sqrt(k_x / m)


    # задание силы F от координаты
    def F_x(x):
        return -k_x * x

    def F_y(y):
        return -k_y * y


    # начальные условия
    #x0 = 1 #math.cos(0)
    v0_x = 1 #-omega_x*math.sin(0)
    y0 = 0.5 #math.cos(math.pi/1)
    v0_y = -omega_y*math.sin(math.pi/1)
    Tmax = 2 * math.pi / omega
    A = x0
    B = v0_x / omega

    # velocity-Verle method

    x = x0
    y = y0
    v_x = v0_x
    v2_x = 0
    v_y = v0_y
    v2_y = 0
    dt = Tmax / 1000
    t = dt
    arr_x = [x0]
    arr_v_x = [v0_x]
    arr_y = [y0]
    arr_v_y = [v0_y]
    arr_t = [0]

    while t < 100 * Tmax:
        for _ in range(5):  # частота запоминания x, v с периодичностью...
            v2_x = v_x + dt / 2 * F_x(x) / m
            x = x + dt * v2_x
            v_x = v2_x + dt / 2 * F_x(x) / m

            v2_y = v_y + dt / 2 * F_y(y) / m
            y = y + dt * v2_y
            v_y = v2_y + dt / 2 * F_y(y) / m

            t += dt
        arr_x.append(x)
        arr_v_x.append(v_x)
        arr_y.append(y)
        arr_v_y.append(v_y)
        arr_t.append(t)


    t = arr_t
    x = arr_x
    y = arr_y
    xm = np.min(x) - 1.5
    xM = np.max(x) + 1.5
    ym = np.min(y) - 1.5
    yM = np.max(y) + 1.5
    N = 50
    s = np.linspace(-1, 1, N)
    xx = s + s ** 2
    yy = s - s ** 2


    # Create figure
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
                y=[arr_y[k]],
                mode="markers",
                marker=dict(color="red", size=10))])

            for k in range(0, N, 4)]
    )

    #fig.show()
    st.write(fig)

