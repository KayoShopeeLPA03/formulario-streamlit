import streamlit as st
from datetime import datetime, timedelta, time
from pathlib import Path

# Link do formulário
FORM_URL = "https://docs.google.com/forms/d/1ebAOKr3CoGdjd0AmDBDAO5SoK4BiDyrnwEw4SjOY1Vs/edit?ts=67d80e2c"

# Horários de abertura e fechamento
HORA_ABERTURA = time(5, 0)
HORA_FECHAMENTO = time(21, 0)

# Caminho da imagem (altere conforme necessário)


# Configuração da página (sem ícone personalizado)
st.set_page_config(
    page_title="Formulário Disponibilidade",
    page_icon="📝",
    layout="centered"
)

# Mostra imagem
st.image(str(CAMINHO_IMAGEM), width=150)
st.title("Formulário de Disponibilidade")

# Avisos
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

# Verifica se está no horário de abertura
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
