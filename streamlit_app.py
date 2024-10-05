import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 시각화 라이브러리


st.title('Streamlit for sin and cos function visualizaion')

x_start = st.slider('x 시작 값', 0.0, 10.0, 0.0)
x_end = st.slider('x 끝 값', 10.0, 20.0, 10.0)

x = np.linspace(x_start, x_end)

y_sin = np.sin(x)
y_cos = np.cos(x)

fig , ax = plt.subplots()

ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin', 'cos'])
ax.set_xlabel('X-axis')
ax.set_ylabel('X-axis')

ax.set_title('sin and cos function')

st.pyplot(fig)


@st.cache
def expensive_computataion(x):
    return np.sin(x) + np.cos(x)

result = expensive_computataion(x)


import plotly.express as px
fig = px.imshow([[1,23,49],[123,5,4],[45,6,3]])
fig.show()



data_canada = px.data.gapminder().query("country == 'Canada'")
data_canada

fig1 = px.line(data_canada, x = 'year', y = 'lifeExp' ,
              title = 'Life expectacy in Canada')
st.plotly_chart(fig1)


fig = px.bar(data_canada, x='year' , y='pop')
st.plotly_chart(fig)
