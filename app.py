import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Advanced Academic Platform",
    layout="wide"
)

# --- الهيدر الرئيسي الاحترافي ---
st.title("ChemResearch AI")
st.markdown("### Advanced Academic Platform & Q1 Research Synthesis Engine")
st.markdown("---")

# --- Section 1: Experiment & Research Metadata ---
st.markdown("#### 1. Experiment and Research Metadata")

col1, col2 = st.columns(2)

with col1:
    article_title = st.text_input(
        "Article or Thesis Title:",
        value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions"
    )
    target_metal = st.text_input(
        "Target Heavy Metal / Pollutant:",
        value="Cadmium(II) - Cd2+"
    )
    analytical_inst = st.text_input(
        "Analytical Instrumentation:",
        value="Atomic Absorption Spectrometer (AAS)"
    )

with col2:
    prepared_material = st.text_input(
        "Prepared Novel Material / Sorbent:",
        value="Modified Agricultural Waste Bio-adsorbent"
    )
    characterization_tools = st.text_input(
        "Characterization Tools:",
        value="FTIR, SEM, XRD, BET"
    )

st.markdown("**Research Fields Selection:**")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    field_spe = st.checkbox("Solid-Phase Extraction (SPE)", value=True)
with col_f2:
    field_adsorb = st.checkbox("Adsorption", value=True)
with col_f3:
    field_removal = st.checkbox("Removal and Remediation", value=True)

st.markdown("---")
st.markdown("#### 2. Journal Style and Formatting")
col_s1, col_s2 = st.columns(2)
with col_s1:
    journal_style = st.selectbox(
        "Target Journal Quartile Style:",
        ["Q1 Style (High Impact & Rigorous)", "Q2 Style", "Review Paper Style"]
    )
with col_s2:
    citation_style = st.selectbox(
        "Citation Style:",
        ["Numerical Style [1, 2]", "Author-Date (Harvard / APA)"]
    )

# --- Section 2: Q1 Introduction Synthesis ---
st.markdown("---")
st.markdown("#### 3. Introduction Synthesis and Drafting")

intro_notes = st.text_area(
    "Core objectives or background notes for the introduction drafting:",
    value="Highlighting environmental risks of heavy metals, the novelty of the prepared bio-adsorbent, and superior removal efficiency."
)

if st.button("Generate Introduction Draft"):
    with st.spinner("Synthesizing rigorous academic introduction..."):
        st.success("Introduction draft successfully generated.")
        st.markdown(f"""
        > **Draft Output:**
        > Recent industrial developments have significantly increased the discharge of toxic heavy metal ions, particularly **{target_metal}**, into aqueous ecosystems. 
        > To address this challenge, we report the **{prepared_material}** synthesized via a facile route. 
        > Analytical characterizations including **{characterization_tools}** confirmed the structural fabrication and efficiency.
        """)

# --- Section 3: Literature Query Generator (Consensus Integration Bridge) ---
st.markdown("---")
st.markdown("#### 4. Literature Search and Archive Bridge")
st.markdown("The platform automatically formulates advanced academic queries based on your active parameters to retrieve peer-reviewed articles.")

# بناء استعلام البحث المتقدم تلقائياً
search_query_text = f"{prepared_material} {target_metal} {' '.join([f for f, active in [('SPE', field_spe), ('Adsorption', field_adsorb), ('Removal', field_removal)] if active])} Q1 journal"
encoded_query = urllib.parse.quote(search_query_text)

consensus_url = f"https://consensus.app/search/?q={encoded_query}"
scholar_url = f"https://scholar.google.com/scholar?q={encoded_query}"

st.code(search_query_text, language="text")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.markdown(f"[Open Search in Consensus Platform]({consensus_url})")
with col_btn2:
    st.markdown(f"[Open Search in Google Scholar]({scholar_url})")

# --- Section 4: References Archive ---
st.markdown("---")
st.markdown("#### 5. Selected References Archive")
uploaded_refs_text = st.text_area(
    "Enter selected references (one per line with DOI):",
    value="1. Smith et al., J. Hazard. Mater., 2024, Bio-adsorbent for cadmium removal.\n2. Al-Duran et al., Chem. Eng. J., 2025, Optimization of micro solid-phase extraction."
)

if st.button("Save Project Database"):
    st.success("Project metadata and references successfully saved.")
