from turtle import width
import streamlit as st
import random

# Функция для отображения главной страницы
def show_main_page():
    st.title('Лабораторная работа №2')
    st.subheader('Исследование выпрямительных устройств')

    # Добавляем изображение перед остальным кодом
    st.image("однополупериодный выпрямитель.jpg", 
             caption="Рисунок 1. Схема однополупериодного выпрямителя", use_column_width=True)

    Uinput = st.number_input('Введите U2 тр-ра', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 тр-ра = ', Uinput, ' В')
    Udiod = 0.45 * Uinput

    RLoad = st.slider("Сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    idx = random.randint(1, 100)
    st.write("Рандомное число", idx)

    st.write("---")

    col1, col2 = st.columns(2)
    RLoad1 = col1.slider("Сопротивление нагрузки", 0.01, 5.0, 1.0)
    col1.write("Сопротивление нагрузки")

# Функция для отображения страницы с однофазной мостовой
def show_single_phase_bridge_page():
    st.title('Однофазная мостовая схема выпрямления')

    Uinput = st.number_input('Введите U2 тр-ра', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 тр-ра = ', Uinput, ' В')
    Udiod = 0.9 * Uinput

    RLoad = st.slider("Сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    idx = random.randint(1, 100)
    st.write("Рандомное число", idx)

    st.write("---")

    col1, col2 = st.columns(2)
    RLoad1 = col1.slider("Сопротивление нагрузки", 0.01, 5.0, 1.0)
    col1.write("Сопротивление нагрузки")
    col2.write('Рисунок 2. Схема однофазного мостового выпрямителя')
    col2.image("мостовой выпрямитель.jpg")

# Функция для отображения страницы с трехфазной 1-полупериодной
def show_three_phase_single_half_wave_page():
    st.title('Трехфазная однополупериодная схема выпрямления')

    Uinput = st.number_input('Введите U2 тр-ра', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 тр-ра = ', Uinput, ' В')
    Udiod = 0.45 * Uinput

    RLoad = st.slider("Сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    idx = random.randint(1, 100)
    st.write("Рандомное число", idx)

    st.write("---")

    col1, col2 = st.columns(2)
    RLoad1 = col1.slider("Сопротивление нагрузки", 0.01, 5.0, 1.0)
    col1.write("Сопротивление нагрузки")
    col2.write('Рисунок 3. Трехфазная однополупериодная схема выпрямления')
    # col2.image("Рисунок3.jpg")

# Функция для отображения страницы с трехфазной мостовой
def show_three_phase_bridge_page():
    st.title('Трехфазная мостовая схема выпрямления')

    Uinput = st.number_input('Введите U2 тр-ра', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 тр-ра = ', Uinput, ' В')
    Udiod = 0.45 * Uinput

    RLoad = st.slider("Сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    idx = random.randint(1, 100)
    st.write("Рандомное число", idx)

    st.write("---")

    col1, col2 = st.columns(2)
    RLoad1 = col1.slider("Сопротивление нагрузки", 0.01, 5.0, 1.0)
    col1.write("Сопротивление нагрузки")
    col2.write('Рисунок 4. Трехфазная мостовая схема выпрямления')
    # col2.image("Рисунок4.jpg")

# Основная часть программы
page = st.sidebar.selectbox("Выберите страницу", ["Однофазная 1-полупериодная", "Однофазная мостовая", "Трехфазная 1-полупериодная", "Трехфазная мостовая"])

if page == "Однофазная 1-полупериодная":
    show_main_page()
elif page == "Однофазная мостовая":
    show_single_phase_bridge_page()
elif page == "Трехфазная 1-полупериодная":
    show_three_phase_single_half_wave_page()
elif page == "Трехфазная мостовая":
    show_three_phase_bridge_page()
