import streamlit as st
from datetime import datetime, timedelta, time


FORM_URL = "https://docs.google.com/forms/d/1ebAOKr3CoGdjd0AmDBDAO5SoK4BiDyrnwEw4SjOY1Vs/edit?ts=67d80e2c"


HORA_ABERTURA = time(5, 0)     
HORA_FECHAMENTO = time(21, 0)  


st.set_page_config(
    page_title="Formulário Disponibilidade",
    page_icon="https://imagensempng.com.br/wp-content/uploads/2022/02/Logo-Shopee-Png.png",
    layout="centered"
)

st.image("https://i.pinimg.com/736x/05/7b/27/057b274c134bcf92ac151758478949b3.jpg", width=150)
st.title("Formulário de Disponibilidade")

st.info("🔔 O formulário é sempre para o carregamento do dia seguinte. Menos quando preencher sábado e domingo, que é válido para a segunda-feira.")
st.info("📅 Exemplo: Se você preencher na segunda, é para o trabalho de terça-feira.")


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
