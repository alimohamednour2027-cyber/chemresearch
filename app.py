import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Portal Hub",
    layout="wide"
)

# --- تنسيق CSS المخصص للهيدر والشريط الجانبي (بدون إيقونات) ---
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
    </style>
""", unsafe_allow_html=True)

# --- إدارة حالة المصادقة (Session State) ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- الشريط الجانبي ---
with st.sidebar:
    st.markdown("### Platform Navigation")
    if st.session_state.authenticated:
        st.success("Status: Authenticated (Admin)")
        st.markdown("---")
        if st.button("Terminate Session (Logout)", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
    else:
        st.warning("Status: Locked / Secure")
    st.markdown("---")
    st.caption("ChemResearch AI - Q1 Analytical Engine")

# --- واجهة تسجيل الدخول (إذا لم يتم الاعتماد بعد) ---
if not st.session_state.authenticated:
    st.markdown("""
        <div class="custom-header" style="text-align: center;">
            <h1>ChemResearch AI: Secure Access Portal</h1>
            <p>Authorized Research Personnel Only - Advanced Q1 Analytical Platform</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Please authenticate to enter workspace:")
        username_input = st.text_input("Username / Researcher ID:")
        password_input = st.text_input("Password:", type="password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Authenticate & Access Platform", use_container_width=True):
            # بيانات الدخول الافتراضية للأدمن (يمكنك تعديلها هنا)
            if username_input == "admin" and password_input == "chem2026":
                st.session_state.authenticated = True
                st.success("Authentication successful. Initializing dashboard...")
                st.rerun()
            else:
                st.error("Invalid credentials. Please verify your researcher ID and password.")

# --- لوحة الترحيب التعريفية (بعد تسجيل الدخول بنجاح) ---
else:
    st.markdown("""
        <div class="custom-header">
            <h1>ChemResearch AI: Welcome to Main Workspace</h1>
            <p>Advanced computational support for Q1 journal publications in analytical chemistry, separation science, and material engineering.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Platform Overview & Modules Directory:")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
            <div class="card-box">
                <h3>1. Literature & Introduction Hub</h3>
                <p>Leverages massive context windows to synthesize rigorous Q1 introductions, extract research gaps, and process multi-document review literature.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="card-box">
                <h3>2. Advanced Optimization Parameters Hub</h3>
                <p>Specialized analytical module covering Adsorption, SPE/MSPE, and Environmental Removal with isolated parameter analysis and targeted reference indexing.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
            <div class="card-box">
                <h3>3. Characterisation Analysis</h3>
                <p>Interprets structural, morphological, and spectroscopic data (FTIR, XRD, SEM, XPS) for novel synthesized sorbents and magnetic nanocomposites.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="card-box">
                <h3>4. Graphical Abstract & Adsorption Kinetics</h3>
                <p>Transforms raw experimental protocols into publication-ready visual workflows, non-linear isotherm fitting, and kinetic modeling calculations.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("Use the sidebar menu or page navigator in Streamlit to switch between the specialized analytical modules above.")
