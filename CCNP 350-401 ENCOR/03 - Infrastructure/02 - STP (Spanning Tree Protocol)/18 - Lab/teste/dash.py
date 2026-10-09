import streamlit as st
import pandas as pd
import plotly.express as px

# Configura página para ocupar a tela inteira
st.set_page_config(page_title="Dashboard Spanning Tree & Rede", layout="wide")

st.title("🌐 Observabilidade de Rede & Spanning Tree (STP)")

# 1. Carrega o CSV que você gerou
df = pd.read_csv("tabela_consolidada.csv")

# 2. Cards Topo (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Interfaces Mapeadas", len(df))
col2.metric("Switches Ativos", df['Switch'].nunique())
col3.metric("VLANs Distintas", df['VLAN'].nunique())
col4.metric("Portas Bloqueadas (BLK)", len(df[df['State'] == 'BLK']))

st.divider()

# 3. Filtro Interativo por Switch
switch_selecionado = st.sidebar.selectbox("Selecione um Switch para detalhar:", ["Todos"] + list(df['Switch'].unique()))

if switch_selecionado != "Todos":
    df_filtrado = df[df['Switch'] == switch_selecionado]
else:
    df_filtrado = df

# 4. Gráficos com Plotly embarcados no Streamlit
c1, c2 = st.columns(2)

with c1:
    st.subheader("Distribuição de Funções de Porta (Roles)")
    fig_roles = px.pie(df_filtrado, names='Role', title=f"Funções de Porta ({switch_selecionado})", hole=0.4)
    st.plotly_chart(fig_roles, use_container_width=True)

with c2:
    st.subheader("Uso de CPU por Switch")
    fig_cpu = px.bar(df.groupby('Switch')['CPU'].max().reset_index(), x='Switch', y='CPU', color='CPU', title="Pico de CPU (%)")
    st.plotly_chart(fig_cpu, use_container_width=True)

# 5. Tabela de Dados Formatada
st.subheader("📋 Tabela Consolidada de Interfaces e STP")
st.dataframe(df_filtrado, use_container_width=True)