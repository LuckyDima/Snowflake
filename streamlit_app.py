import streamlit as s
import pandas as p

#streamlit.title('My Parents Healthy Diner')
#streamlit.header('Breakfast Menu')
#streamlit.text('Omega 3 & Blueberry Oatmeal')
#streamlit.text('Kale, Spinach & Rocket Smothie')
#streamlit.text('Hard-Bolled Free-Range Egg')
#
#streamlit.title('My Mom\'s Healthy Diner')
s.header('Breakfast Favorites')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range Egg')
s.text('🥑🍞 Avocado Toast')


s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

s.multiselect("Pick some fruits:", list(my_fruit_list.index), [Avocado,Strawberries])
s.dataframe(my_fruit_list)
