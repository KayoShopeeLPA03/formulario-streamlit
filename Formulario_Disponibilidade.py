import streamlit as st
from datetime import datetime, timedelta, time


FORM_URL = "https://docs.google.com/forms/d/1ebAOKr3CoGdjd0AmDBDAO5SoK4BiDyrnwEw4SjOY1Vs/edit?ts=67d80e2c"  
HORA_ABERTURA = time(2, 0)   
HORA_FECHAMENTO = time(21, 0)

st.set_page_config(page_title="Formulario Disponibilidade", page_icon="📝", layout="centered")

st.title("📝 Formulário Disponibilidade ")

agora = datetime.now()
hora_atual = agora.time()

def tempo_restante(alvo):
    delta = datetime.combine(datetime.today(), alvo) - agora
    if delta.total_seconds() < 0:
        delta += timedelta(days=1)
    return str(delta).split(".")[0] 


if HORA_ABERTURA <= hora_atual < HORA_FECHAMENTO:
    st.success("✅ O formulário está ABERTO agora.")
    st.markdown(f"📎 [Clique aqui para acessar o formulário]({FORM_URL})", unsafe_allow_html=True)

    
    tempo = tempo_restante(HORA_FECHAMENTO)
    st.info(f"🕒 Tempo restante até o fechamento: `{tempo}`")
else:
    st.warning("🚫 O formulário está FECHADO no momento.")
    
    
    tempo = tempo_restante(HORA_ABERTURA)
    st.info(f"⏳ Ele será reaberto em: `{tempo}`")

st.markdown("---")
st.caption("Desenvolvido por Kayo Soares")
