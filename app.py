import streamlit as st
from datetime import datetime
import os

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Portal Hub",
    layout="wide"
)

# --- تنسيق CSS المخصص للهيدر، الشريط الجانبي، وأزرار النظام بوضوح تام ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #2b4c7e;
        color: #ffffff;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    .custom-header {
        background-color: #1a365d;
        color: #ffffff;
        padding: 25px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .custom-header h1 {
        color: #ffffff;
        font-weight: 800;
        margin: 0;
        font-size: 28px;
    }
    .custom-header p {
        color: #e2e8f0;
        margin: 8px 0 0 0;
        font-size: 14px;
    }
    .card-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .card-box h3 {
        color: #1a365d;
        margin-top: 0;
    }
    div.stButton > button {
        background-color: #1a365d !important;
        color: white !important;
        font-weight: 600;
        border: 1px solid #2b4c7e;
    }
    div.stButton > button:hover {
        background-color: #2b4c7e !important;
        color: white !important;
        border-color: #1a365d;
    }
    </style>
""", unsafe_allow_html=True)

LOG_FILE = "access_logs.txt"

def log_access(username):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"User: {username} | Access Time: {current_time}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def get_recent_logs():
    if not os.path.exists(LOG_FILE):
        return ["No access logs recorded yet."]
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines[-5:]]

# --- الشريط الجانبي الثابت والجاهز ---
with st.sidebar:
    st.success("Status: Workspace Active (Admin)")
    st.markdown("---")
    st.caption("ChemResearch AI - Q1 Analytical Engine")

# --- دالة الـ Dashboard واللوحة التعريفية ---
def show_dashboard():
    st.markdown(f"""
        <div class="custom-header">
            <h1>ChemResearch AI: Welcome to Main Workspace</h1>
            <p>Advanced computational support for Q1 journal publications in analytical chemistry, separation science, and material engineering.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("Security Audit Trail: Recent Workspace Activity"):
        logs = get_recent_logs()
        for l in logs:
            st.text(l)

    st.markdown("### Platform Overview & Modules Directory:")
    
    col_a, col_b = st.columns(2)
    
    col_a.markdown("""
        <div class="card-box">
            <h3>1. Literature & Introduction Hub</h3>
            <p>Leverages massive context windows to synthesize rigorous Q1 introductions, extract research gaps, and process multi-document review literature.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_a.markdown("""
        <div class="card-box">
            <h3>2. Advanced Optimization Parameters Hub</h3>
            <p>Specialized analytical module covering Adsorption, SPE/MSPE, and Environmental Removal with isolated parameter analysis and targeted reference indexing.</p>
        </div>
    """, unsafe_allow_html=True)

    col_b.markdown("""
        <div class="card-box">
            <h3>3. Characterisation Analysis</h3>
            <p>Interprets structural, morphological, and spectroscopic data (FTIR, XRD, SEM, XPS) for novel synthesized sorbents and magnetic nanocomposites.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_b.markdown("""
        <div class="card-box">
            <h3>4. Graphical Abstract & Similarity Screening</h3>
            <p>Transforms raw experimental protocols into publication-ready visual workflows, non-linear isotherm fitting, and integrated plagiarism screening.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("Use the sidebar menu above to switch between the specialized analytical modules.")

# --- نظام التنقل الشامل والمستقر لجميع الوحدات بدون انقطاع ---
pages = {
    "Main Hub": [
        st.Page(show_dashboard, title="Dashboard Hub", default=True),
    ],
    "Analytical Modules": [
        st.Page("modules/0_Introduction_Hub.py", title="Introduction Hub"),
        st.Page("modules/1_literature_hub.py", title="Literature Hub"),
        st.Page("modules/2_optimization_parameters.py", title="Optimization Parameters"),
        st.Page("modules/3_characterization_analysis.py", title="Characterization Analysis"),
        st.Page("modules/4_adsorption_kinetics.py", title="Adsorption Kinetics"),
        st.Page("modules/5_graphical_abstract.py", title="Graphical Abstract"),
        st.Page("modules/6_Claude_Literature_Hub.py", title="Claude Literature Hub"),
        st.Page("modules/7_Claude_Optimization_Hub.py", title="Claude Optimization Hub"),
        st.Page("modules/8_similarity_checker.py", title="Similarity Checker"),
    ]
}

pg = st.navigation(pages)
pg.run()
