import streamlit as st

def hello_word():
    return "TESTANDO O DEPLOY PARA APP APRENDIZADO EM DOCKER"

def main():
    st.write(hello_word())

if __name__ == "__main__":
    main()
    