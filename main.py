from turtle import width
import streamlit as st
import random

# Функция для отображения главной страницы
def show_main_page():
    st.title('Лабораторная работа №2')
    st.subheader('Исследование выпрямительных устройств')

    # Добавляем изображение перед остальным кодом
    st.image("однополупериодный выпрямитель.jpg", caption="Рисунок 1. Схема однополупериодного выпрямителя", use_column_width=True)

    Uinput = st.number_input('Введите напряжение вторичной обмотки трансформатора (U2)', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 трансформатора = ', Uinput, ' В')
    Udiod = 0.45 * Uinput

    RLoad = st.slider("Введите сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки (Rн)", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    st.write("---")

# Функция для отображения страницы с однофазной мостовой
def show_single_phase_bridge_page():
    st.title('Однофазная мостовая схема выпрямления')

    # Добавляем изображение перед остальным кодом
    st.image("мостовой выпрямитель.jpg", caption="Рисунок 2. Схема мостового выпрямителя", use_column_width=True)

    Uinput = st.number_input('Введите напряжение вторичной обмотки трансформатора (U2)', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 трансформатора = ', Uinput, ' В')
    Udiod = 0.9 * Uinput

    RLoad = st.slider("Введите сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки (Rн)", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    st.write("---")

# Функция для отображения страницы с трехфазной 1-полупериодной
def show_three_phase_single_half_wave_page():
    st.title('Трехфазная однополупериодная схема выпрямления')

    st.image("3-фазная одно.jpg", caption="Рисунок 3. Схема однополупериодного трехфазного выпрямителя", use_column_width=True)
    Uinput = st.number_input('Введите напряжение вторичной обмотки трансформатора (U2)', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 трансформатора = ', Uinput, ' В')
    Udiod = 1.17 * Uinput

    RLoad = st.slider("Введите сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки (Rн)", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    st.write("---")


# Функция для отображения страницы с трехфазной мостовой
def show_three_phase_bridge_page():
    st.title('Трехфазная мостовая схема выпрямления')

    st.image("3-фазная мост.jpg", caption="Рисунок 4. Схема мостового трехфазного выпрямителя", use_column_width=True)
    Uinput = st.number_input('Введите напряжение вторичной обмотки трансформатора (U2)', min_value=10, max_value=20, value="min", step=1)
    st.write('U2 трансформатора = ', Uinput, ' В')
    Udiod = 2.34 * Uinput

    RLoad = st.slider("Введите сопротивление нагрузки", 1.0, 5.0, 1.5)
    st.write("Сопротивление нагрузки (Rн)", RLoad, 'Ом')
    Rvn = 0.2
    ILoad = Udiod / (RLoad + Rvn)
    st.write("Ток нагрузки", ILoad, 'А')
    st.write("Напряжение на нагрузке", RLoad * ILoad, 'В')
    st.write("---")

# Основная часть программы
st.sidebar.title("Лабораторная работа №2")
st.sidebar.subheader("Исследование выпрямительных устройств")
page = st.sidebar.selectbox("Выберите тип выпрямителя", ["Однофазная 1-полупериодная", "Однофазная мостовая", "Трехфазная 1-полупериодная", "Трехфазная мостовая"])

if page == "Однофазная 1-полупериодная":
    show_main_page()
elif page == "Однофазная мостовая":
    show_single_phase_bridge_page()
elif page == "Трехфазная 1-полупериодная":
    show_three_phase_single_half_wave_page()
elif page == "Трехфазная мостовая":
    show_three_phase_bridge_page()
