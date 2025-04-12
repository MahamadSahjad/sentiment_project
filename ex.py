import streamlit as st
st.title("My First Streamlit Example")
st.header("Hello This is streamlit app")
st.subheader("This is a subheader")
st.text("Welcome to the world of streamlit")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write("Hello, " + name + "!")
if st.checkbox("Show Secret Message"):
    st.write("You delivered  a secret message")
option = st.selectbox("Choose your favourite language:",
                      ["Python","Java","C++","JavaScript"])
st.write("You chose:", option)
age = st.slider("Select your age:",1,100,25)
st.write("Your age is ",age)
