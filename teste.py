import streamlit as st
import pandas as pd

# Título do aplicativo
st.title('Aplicativo de Cadastro Simples')

# Campos do formulário
with st.form(key='cadastro_form'):
    nome = st.text_input('Nome')
    email = st.text_input('E-mail')
    mensagem = st.text_area('Mensagem')
    submit_button = st.form_submit_button(label='Enviar')

# Lista para armazenar os dados cadastrados
if 'cadastros' not in st.session_state:
    st.session_state.cadastros = []

# Quando o botão de envio for pressionado
if submit_button:
    novo_cadastro = {'Nome': nome, 'E-mail': email, 'Mensagem': mensagem}
    st.session_state.cadastros.append(novo_cadastro)
    st.success('Cadastro enviado com sucesso!')

# Mostrar os dados cadastrados
if st.session_state.cadastros:
    df = pd.DataFrame(st.session_state.cadastros)
    st.write('Cadastros:')
    st.dataframe(df)

