import streamlit as st
from datetime import datetime, timedelta, time

# URL do formulário
FORM_URL = "https://docs.google.com/forms/d/1ebAOKr3CoGdjd0AmDBDAO5SoK4BiDyrnwEw4SjOY1Vs/edit?ts=67d80e2c"

# Horário de abertura e fechamento do formulário
HORA_ABERTURA = time(5, 0)     # 5h da manhã
HORA_FECHAMENTO = time(21, 0)  # 21h da noite

# Configuração da página
st.set_page_config(
    page_title="Formulário Disponibilidade",
    page_icon="📝",
    layout="centered"
)

# Exibe imagem no topo
st.image("https://i.pinimg.com/474x/67/6c/01/676c0101557e1e6b64708ef724669905.jpg", width=200)

# Título e instruções
st.title("📝 Formulário de Disponibilidade")

st.info("🔔 O formulário é sempre para o carregamento do dia seguinte. Menos quando preencher sábado e domingo, que é válido para a segunda-feira.")
st.info("📅 Exemplo: Se você preencher na segunda, é para o trabalho de terça-feira.")

# Hora atual
agora = datetime.now()
hora_atual = agora.time()

# Função para calcular tempo restante
def tempo_restante(alvo):
    delta = datetime.combine(datetime.today(), alvo) - agora
    if delta.total_seconds() < 0:
        delta += timedelta(days=1)
    return str(delta).split(".")[0]

# Verifica se o formulário está aberto ou fechado
if HORA_ABERTURA <= hora_atual < HORA_FECHAMENTO:
    st.success("✅ O formulário está ABERTO agora.")
    st.markdown(f"📎 [Clique aqui para acessar o formulário]({FORM_URL})", unsafe_allow_html=True)

    tempo = tempo_restante(HORA_FECHAMENTO)
    st.info(f"🕒 Tempo restante até o fechamento: `{tempo}`")
else:
    st.warning("🚫 O formulário está FECHADO no momento.")
    tempo = tempo_restante(HORA_ABERTURA)
    st.info(f"⏳ Ele será reaberto em: `{tempo}`")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Kayo Soares")
