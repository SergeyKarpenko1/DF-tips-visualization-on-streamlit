import streamlit as st  # импортируем библиотеку для создания интерактивных приложений
import matplotlib.pyplot as plt  # импортируем библиотеку для построения графиков
import seaborn as sns  # импортируем библиотеку для построения статистических графиков
import pandas as pd  # импортируем библиотеку для работы с таблицами

# загружаем датасет tips.csv в переменную tips
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

# выводим сообщение для пользователя
st.write("Для выбора нужного графика нажмите на значок '>' в левом верхнем углу!")
# выводим заголовок приложения
st.title("Исследование по чаевым (датасет tips.csv)")
# создаем выпадающий список для выбора графика
option = st.sidebar.selectbox(
    '**Выберите какой график хотите увидеть**:',  # текст для отображения на странице
    ('Непосредственно датафрейм',  # опции для выбора графика
     'Гистограмма взаимоотношения счета и размера чаевых',
     'Scatterplot показывающий связь между счетом и чаевыми',
     'График связывающий размер счета с размером чаевых',
     'Связь между размером счета и чаевыми',
     'Scatterplot Зависимость дня недели, счета и пола',
     'Гистограмма чаевых на обед и ланч'))

# проверяем выбор пользователя и выводим нужный график
if option == 'Непосредственно датафрейм':
    st.write(tips)  # отображаем таблицу
elif option == 'Гистограмма взаимоотношения счета и размера чаевых':
    st.write('Взаимоотношения счета и размера чаевых')
    hist_data = tips['total_bill']  # берем данные о счете из датасета
    fig, ax = plt.subplots()
    sns.histplot(hist_data, bins=20)  # строим гистограмму
    st.pyplot(fig)  # выводим график на страницу
elif option == 'Scatterplot показывающий связь между счетом и чаевыми':
    st.write('Связь между счетом и чаевыми')
    fig, ax = plt.subplots()
    sns.scatterplot(x='total_bill', y='tip', data=tips)  # строим scatterplot
    st.pyplot(fig)  # выводим график на страницу
elif option == 'График связывающий размер счета с размером чаевых':
    st.write('Связь между счетом и чаевыми с учетом размера счета')
    fig, ax = plt.subplots()
    # строим scatterplot с учетом размера счета
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size')
    st.pyplot(fig)  # выводим график на страницу
elif option == 'Связь между размером счета и чаевыми':
    st.write('''График показывающий связь размера счета и чаевыми для мужчин и женщин,
              с дополнительной разбивкой по курящим/некурящим''')
    s = sns.FacetGrid(tips, col='sex', hue='smoker').map(
        sns.scatterplot, 'total_bill', 'tip').add_legend()  # строим scatterplot с разбивкой по полу и привычке курения
    st.pyplot(s)  # выводим график на страницу
elif option == 'Scatterplot Зависимость дня недели, счета и пола':
    st.write('**Зависимость дня недели, счета и пола**')
    fig, ax = plt.subplots()
    # строим scatterplot с зависимостью дня недели, счета и пола
    sns.scatterplot(x='total_bill', y='day', hue='sex', data=tips)
    st.pyplot(fig)  # выводим график на страницу
elif option == 'Гистограмма чаевых на обед и ланч':
    st.write('Чаевые на обед и ужин')
    # строим гистограмму для чаевых на обед и ужин
    s = sns.FacetGrid(tips, col='time').map(sns.histplot, 'tip')
    st.pyplot(s)  # выводим график на страницу
