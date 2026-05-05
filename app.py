import streamlit as st
 
st.title ("Calculadora ")
st.subheader("Feito com streamlit")

altura = st.number_input("Digite a sua altura", min_value=0.0)
peso = st.number_input("Digite o seu peso", min_value=0.0)

if st.button("calcular"):
    # imc = peso / altura ** 2
    # st.sucess (f"Seu IMC é {imc:.2f}")
    imc = peso / altura ** 2 
    st.success(f"Seu Imc é {imc:.2f}")
    if imc < 18.5:
        st.error("Abaixo do peso")
    elif imc < 24.9:
        st.success("Peso anormal")    
    elif imc < 29.9:
        st.error("sobrepeso")
    elif imc < 34.4:
        st.error("Obesidade Grau 1")
    elif imc < 39.9:
        st.error("Obesidade Grau 2")
    else:
        st.error("Obesidade Grau 3")
