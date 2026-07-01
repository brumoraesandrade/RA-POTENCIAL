import streamlit as st
import pandas as pd
import random

# --- Configuração da Página ---
st.set_page_config(page_title="Radar de Oportunidades - Concorrentes", layout="wide")
st.title("🎯 Radar de Conversão: Bancos e Adquirentes")
st.write("Mapeamento de fragilidades de concorrentes via Reclame Aqui para geração de leads.")

# --- Simulação de Coleta de Dados (Scraping) ---
def coletar_reclamacoes(concorrente):
    reclamacoes_mock = [
        {"Titulo": "Taxa abusiva na antecipação", "Reclamacao": "Prometeram 1% e estão cobrando 3%. Absurdo!", "Data": "01/07/2026"},
        {"Titulo": "Maquininha não conecta", "Reclamacao": "Estou perdendo vendas no balcão porque o sistema caiu.", "Data": "30/06/2026"},
        {"Titulo": "Dinheiro bloqueado", "Reclamacao": "Fiz vendas e o dinheiro não caiu na conta.", "Data": "29/06/2026"},
        {"Titulo": "Atendimento péssimo", "Reclamacao": "Fico horas no telefone e ninguém resolve meu estorno.", "Data": "28/06/2026"}
    ]
    return random.sample(reclamacoes_mock, 3)

# --- Simulação de Processamento (NLP) ---
def analisar_oportunidade(texto):
    texto = texto.lower()
    if "taxa" in texto or "cobrança" in texto:
        return "Redução de Custos", "Oferecer taxa flat ou isenção de mensalidade."
    elif "maquininha" in texto or "caiu" in texto:
        return "Estabilidade de Hardware", "Destacar conexão Wi-Fi/4G redundante do nosso terminal."
    elif "dinheiro" in texto or "bloqueado" in texto:
        return "Fluxo de Caixa", "Vender antecipação automática em D+0."
    else:
        return "Relacionamento", "Focar em atendimento humanizado 24/7."

# --- Interface do Usuário ---
concorrente = st.text_input("🔍 Digite o nome do banco ou adquirente concorrente (Ex: Stone, Cielo, PagSeguro):")

if st.button("Mapear Oportunidades"):
    if concorrente:
        with st.spinner(f'Buscando dados de {concorrente} no Reclame Aqui...'):
            # 1. Coleta os dados
            dados_brutos = coletar_reclamacoes(concorrente)
            
            # 2. Processa as oportunidades
            resultados = []
            for item in dados_brutos:
                dor, argumento = analisar_oportunidade(item["Reclamacao"])
                resultados.append({
                    "Data": item["Data"],
                    "Reclamação Original": item["Titulo"],
                    "Dor Identificada (Gatilho)": dor,
                    "Argumento de Venda (Ação)": argumento
                })
            
            # 3. Exibe o resultado
            df = pd.DataFrame(resultados)
            
            st.success("Análise concluída!")
            st.dataframe(df, use_container_width=True)
    else:
        st.warning("Por favor, digite o nome de um concorrente.")
