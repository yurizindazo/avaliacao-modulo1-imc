import streamlit as st
import random

st.title("✊✋✌️ Pedra, Papel ou Tesoura")

opcoes = ["Pedra", "Papel", "Tesoura"]

# placar
if "player" not in st.session_state:
    st.session_state.player = 0
if "cpu" not in st.session_state:
    st.session_state.cpu = 0

escolha = st.radio("Escolha uma opção:", opcoes)

if st.button("Jogar"):
    computador = random.choice(opcoes)

    st.write(f"🤖 Computador escolheu: **{computador}**")

    if escolha == computador:
        st.info("Empate!")
    elif (
        (escolha == "Pedra" and computador == "Tesoura") or
        (escolha == "Papel" and computador == "Pedra") or
        (escolha == "Tesoura" and computador == "Papel")
    ):
        st.success("Você ganhou! 🎉")
        st.session_state.player += 1
    else:
        st.error("Você perdeu! 😢")
        st.session_state.cpu += 1

st.write("### 🏆 Placar")
st.write(f"Você: {st.session_state.player} | CPU: {st.session_state.cpu}")

if st.button("Resetar placar"):
    st.session_state.player = 0
    st.session_state.cpu = 0
