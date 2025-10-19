import streamlit as st
from datetime import date, timedelta

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Calculadora de Fechas", page_icon="⏳", layout="centered")

# --- ESTILO CSS (Opcional) ---
st.markdown("""
<style>
    h1 {
        text-align: center;
        color: #6a0dad; /* Morado */
    }
    .stButton > button {
        background-color: #6a0dad;
        color: white;
        border-radius: 5px;
    }
    .stDateInput > label {
        font-weight: bold;
    }
    .result-box {
        background-color: #f0f2f6;
        border: 1px solid #dcdcdc;
        border-radius: 5px;
        padding: 1em;
        text-align: center;
        margin-top: 1em;
    }
    .result-box strong {
        font-size: 1.5em;
        color: #6a0dad;
    }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("⏳ Calculadora de Diferencia entre Fechas")

# --- ENTRADA DE FECHAS ---
st.subheader("Selecciona las fechas:")
col1, col2 = st.columns(2)
with col1:
    fecha_inicio = st.date_input("Fecha de Inicio", value=date.today() - timedelta(days=30))
with col2:
    fecha_fin = st.date_input("Fecha de Fin", value=date.today())

# --- CÁLCULO Y RESULTADO ---
if fecha_inicio and fecha_fin:
    if fecha_fin >= fecha_inicio:
        diferencia = fecha_fin - fecha_inicio
        dias_totales = diferencia.days
        
        # Opcional: Calcular años, meses, días (aproximado)
        anios = dias_totales // 365
        meses = (dias_totales % 365) // 30
        dias_restantes = (dias_totales % 365) % 30
        
        st.markdown("---")
        st.subheader("Resultado:")
        
        st.markdown(f"""
        <div class="result-box">
            La diferencia total es de:<br>
            <strong>{dias_totales} días</strong><br><br>
            (Aproximadamente: {anios} años, {meses} meses y {dias_restantes} días)
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("Error: La fecha de fin debe ser igual o posterior a la fecha de inicio.")

else:
    st.info("Por favor, selecciona ambas fechas.")

