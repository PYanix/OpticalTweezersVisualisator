import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import requests
from scipy.interpolate import RegularGridInterpolator
from PIL import Image

img = Image.open("pictures/инструкция зеленый.jpg")

st.title('Расчет динамики частицы в оптическом пинцете')
col1, col2 = st.columns(2)
with col1:
    st.header('Выбор параметров системы')
    # Размер перетяжки 1, 0.5, 0.25 длины волны
    waist = st.radio(
        "Размер перетяжки в длинах волн",
        [1, 0.75, 0.49, 0.4],
        index=0,
        horizontal=True,
    )
    # Размер частицы 0.05, 0.1, 0.2, 0.5 длины волны
    radius = st.radio(
        "Размер частицы в длинах волн",
        [0.05, 0.1, 0.2, 0.5],
        index=0,
        horizontal=True,
    )
    # Контраст n частицы/n окружения 1.2, 2.1, 3, 3.9
    contrast = st.radio(
        "Контраст " + r'$\frac{n_{2}}{n_{1}}$',
        [1.2, 2.1, 3, 3.9],
        index=0,
        horizontal=True,
    )
with col2:
    st.image(img)

# response
waist_dict = {1: 'waist5.32e-07',
              0.75: 'waist4.0303e-07',
              0.49: 'waist2.5961e-07',
              0.4: 'waist2.1635e-07'}
res = requests.get(f'http://127.0.0.1:8000/{waist_dict[waist]}/contrast{contrast}/radius{radius}')
data = res.json()
table_x = data[0]
table_z = data[1]

# Интерполяция

force = np.random.rand(4, 4)
proj = ''
raz_z = 3000
raz_x = 1500
period = 10
first_koor = 0
c_light = 299792458     # скорость света
p = 1   # мощность
k_ci = p/c_light    # коэфф размерности для силы


def massive(x, z, proj):
    x1 = int(x * 1000000000 // period + raz_x // period) - 1
    z1 = int(z * 1000000000 // period + raz_z // period) - 1
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
    return interp((x, z)) * k_ci

# Fz(Z)
arr_z = []
arr_Fz = []
s0 = 10 ** (-9)
for i in range(-2900, 2900, 10):
    arr_Fz.append(F(s0 * 0.001, s0 * i, 'z'))
    arr_z.append(s0 * i)
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=arr_z, y=arr_Fz, mode='lines', line=dict(width=2, color="black")))
fig.add_trace((go.Scatter(x=np.linspace(arr_z[0],arr_z[-1]), y = np.linspace(0,0), line=dict(width=2, color="red"))))

fig.update_xaxes(title_text="z, м")
fig.update_yaxes(title_text="Fz, Н")
fig.update_layout(title="Зависимость силы Fz от координаты z вдоль оси пучка",
                  showlegend=False,
                  autosize=False,
                  width=600,
                  height=600
    )

st.write(fig)

#
st.header('Выбор начальных параметров')
col1, col2 = st.columns(2)
with col1:
    x0 = st.slider('Начальная координата по x, нм', min_value=-1500, max_value=1500, value=300, step=1)
    z0 = st.slider('Начальная координата по z, нм', min_value=-3000, max_value=3000, value=-1100, step=1)
    dyn_viscosity = st.slider('Динамическая вязкость', min_value=0.05, max_value=0.5, value=0.0, step=0.01)*10**-6 ##динамическая вязкость
with col2:
    iterations = st.slider('Количество итераций', min_value=500, max_value=10000, value=500, step=500)
    dt = st.slider('Шаг по времени, 10^-8 с', min_value=1, max_value=100, value=1, step=1)*10**-8
    p = st.slider('Мощность, Вт', min_value=0.05, max_value=1.0, value=1.0, step=0.05)

# start
if st.button('Старт'):
    progress_text = "Идет расчет траектории. Пожалуйста подождите."
    my_bar = st.progress(0, text=progress_text)

    # расчет массива координат траектории
    wave_len = 532 *10**(-9)
    R = radius * wave_len  # радиус частицы
    density = 1.96 * 1000  # плотность
    m = 4 * R ** 3 / 3 * density * math.pi  # масса частицы
    k_ci = k_ci*p  # коэфф размерности для силы
    k_liq = 6 * math.pi * R * dyn_viscosity  # F=k*v - сила сопротивления

    # начальные условия
    x0 = x0 * 10 ** -9
    v0_x = 0

    z0 = z0 * 10 ** -9
    v0_z = 0

    # velocity-Verle method
    x = x0
    v_x = v0_x
    v2_x = 0
    arr_x = [x0]

    z = z0
    v_z = v0_z
    v2_z = 0
    arr_z = [z0]

    t = dt
    t_end = iterations * dt

    while t < t_end:
        try:
            v2_x = v_x + dt / 2 * (F(x, z, 'x') - v_x * k_liq) / m
            v2_z = v_z + dt / 2 * (F(x, z, 'z') - v_z * k_liq) / m

            x = x + dt * v2_x
            z = z + dt * v2_z

            v_x = v2_x + dt / 2 * (F(x, z, 'x') - v2_x * k_liq) / m
            v_z = v2_z + dt / 2 * (F(x, z, 'z') - v2_z * k_liq) / m

            t += dt

            arr_x.append(x)
            arr_z.append(z)
            my_bar.progress(t/t_end, text=progress_text)

        except:
            break

    # минимальные и максимальные значения на осях
    xm = -1.5 * 10 ** (-6)
    xM = 1.5 * 10 ** (-6)
    ym = -4 * 10 ** (-6)
    yM = 4 * 10 ** (-6)

    # отрисовка анимированного графика

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    img2 = Image.open("pictures/green.png")
    fig.add_layout_image(
        dict(
            source=img2,
            xref="x",
            yref="y",
            x=-1.5*10**-6,
            y=4*10**-6,
            sizex=3*10**-6,
            sizey=8*10**-6,
            visible=True,
            sizing="stretch",
            opacity=1,
            layer="below")
    )

    fig.update_xaxes(title_text="x, м")
    fig.update_yaxes(title_text="z, м", showgrid=False)
    fig.update_layout(legend_title_text="легенда",
                      title="Траектория частицы",
                      showlegend=False,
                      autosize=False,
                      xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
                      yaxis=dict(range=[ym, yM], autorange=False, zeroline=False)
    )

    #intensity = [i.split() for i in open(f'Force site/field.txt').readlines()] # 801 361
    # трактория частицы
    fig.add_trace(go.Scatter(x=arr_x, y=arr_z,
                             mode="lines",
                             line=dict(width=3, color="white")))
    # конечное положение частицы
    fig.add_trace(go.Scatter(x=[arr_x[-1]],
                             y=[arr_z[-1]],
                             mode="markers",
                             marker=dict(
                                 color='white',
                                 size=12,
                                 line=dict(
                                     color='black',
                                     width=2
                                 )
                             )))
    my_bar.empty()  #удаление ползунка загрузки
    number_frames = 100  #число кадров в гифке
    frames = [dict(
        name=k,
        data=[go.Scatter(x=arr_x[:(k*len(arr_x)//number_frames)],
                         y=arr_z[:(k*len(arr_z)//number_frames)],
                         mode="lines",
                         line=dict(width=3, color="white")),
              go.Scatter(x=[arr_x[k * len(arr_x) // number_frames-1]],
                         y=[arr_z[k * len(arr_z) // number_frames-1]],
                         mode="markers",
                         marker=dict(
                             color='white',
                             size=12,
                             line=dict(
                                 color='black',
                                 width=2
                             )
                         )
                         )
              ],
        traces=[0, 1]
    ) for k in range(number_frames)]
    fig.update_layout(width=600, height=700)

    # Play button
    updatemenus = [dict(type='buttons',
                        buttons=[dict(label='Play',
                                      method='animate',
                                      args=[[f'{i}' for i in range(number_frames)],
                                            dict(frame=dict(duration=500, redraw=True),
                                                 transition=dict(duration=0),
                                                 easing='linear',
                                                 fromcurrent=True,
                                                 mode='immediate'
                                                 )]),
                                 dict(label='Pause',
                                      method='animate',
                                      args=[[None],
                                            dict(frame=dict(duration=0, redraw=False),
                                                 transition=dict(duration=0),
                                                 mode='immediate'
                                                 )])
                                 ],
                        direction='left',
                        pad=dict(r=10, t=85),
                        showactive=True, x=0.1, y=0, xanchor='right', yanchor='top')
                   ]

    # Slider
    sliders = [{'yanchor': 'top',
                'xanchor': 'left',
                'currentvalue': {'font': {'size': 16}, 'prefix': 'Frame: ', 'visible': True, 'xanchor': 'right'},
                'transition': {'duration': 0, 'easing': 'linear'},
                'pad': {'b': 10, 't': 50},
                'len': 0.9, 'x': 0.1, 'y': 0,
                'steps': [{'args': [[k], {'frame': {'duration': 0, 'easing': 'linear', 'redraw': False},
                                          'transition': {'duration': 0, 'easing': 'linear'}}],
                           'label': k, 'method': 'animate'} for k in range(number_frames)
                          ]}]

    fig.update(frames=frames),
    fig.update_layout(updatemenus=updatemenus, sliders=sliders, width=600, height=750)
    st.write(fig)