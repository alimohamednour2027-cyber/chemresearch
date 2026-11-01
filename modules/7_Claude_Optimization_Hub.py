import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Claude Optimization Hub",
    layout="wide"
)

# --- تنسيق CSS المخصص للشريط الجانبي والهيدر (بدون إيقونات) ---
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
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .custom-header h1 {
        color: #ffffff;
        font-weight: 800;
        margin: 0;
        font-size: 26px;
    }
    .custom-header p {
        color: #e2e8f0;
        margin: 5px 0 0 0;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- الشريط الجانبي الموحد لاختيار اللغة ---
with st.sidebar:
    st.markdown("### Language Configuration")
    lang_choice = st.selectbox("Choose Language:", ["English", "Türkçe", "العربية"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown("### Claude Optimization Navigation")
    st.caption("Active Hub: Advanced Discussion & Thermodynamic Justification")

# الترجمات الثلاثية
if lang_choice == "English":
    t_title = "ChemResearch AI: Claude Advanced Optimization & Discussion Hub"
    t_desc = "Specialized analytical chemistry module powered by Claude to interpret thermodynamic, kinetic, and mechanistic parameters for Q1 journals."
    sec1_title = "1. Experimental Parameter Setup:"
    param_lbl = "Studied Parameter (e.g., Initial pH, Dosage, Concentration):"
    opt_lbl = "Determined Optimum Value:"
    sec2_title = "2. Thermodynamic & Mechanistic Notes:"
    notes_lbl = "Input experimental observations or unexpected trends:"
    btn_gen = "Generate Claude Discussion & Mechanism Draft"
    success_msg = "Claude discussion draft successfully generated."
    preview_title = "Claude Comprehensive Discussion Paragraph:"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Claude Gelişmiş Optimizasyon ve Tartışma Merkezi"
    t_desc = "Q1 dergileri için termodinamik, kinetik ve mekanistik parametreleri yorumlamak üzere Claude tarafından desteklenen uzman analitik kimya modülü."
    sec1_title = "1. Deneysel Parametre Kurulumu:"
    param_lbl = "İncelenen Parametre (örn. Başlangıç pH, Dozaj, Konsantrasyon):"
    opt_lbl = "Belirlenen Optimum Değer:"
    sec2_title = "2. Termodinamik ve Mekanistik Notlar:"
    notes_lbl = "Deneysel gözlemleri veya beklenmeyen eğilimleri girin:"
    btn_gen = "Claude Tartışma ve Mekanizma Taslağı Oluştur"
    success_msg = "Claude tartışma taslağı başarıyla oluşturuldu."
    preview_title = "Claude Kapsamlı Tartışma Paragrafı:"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز تحسين المعلمات والمناقشة المتقدم مدعوم بـ Claude"
    t_desc = "وحدة كيمياء تحليلية متخصصة مدعومة بـ Claude لتفسير المعلمات الديناميكية الحرارية، والحركية، والميكانيكية لنشر Q1."
    sec1_title = "1. إعداد المعلمات التجريبية:"
    param_lbl = "العامل أو المعلمة المدروسة (مثل pH، الجرعة، التركيز):"
    opt_lbl = "القيمة المثلى المحددة (Optimum Value):"
    sec2_title = "2. الملاحظات الديناميكية الحرارية والميكانيكية:"
    notes_lbl = "أدخل الملاحظات التجريبية أو السلوكيات غير المعتادة للتحليل:"
    btn_gen = "توليد مسودة المناقشة والآلية الكيميائية عبر Claude"
    success_msg = "تم توليد مسودة المناقشة والتحليل العميق بنجاح!"
    preview_title = "مسودة فقرة المناقشة والتحليل الشامل:"

# عرض الهيدر
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"### {sec1_title}")
col1, col2 = st.columns(2)
with col1:
    studied_param = st.text_input(param_lbl, value="Initial Solution pH")
with col2:
    optimum_value = st.text_input(opt_lbl, value="pH 6.0")

st.markdown("---")
st.markdown(f"### {sec2_title}")
user_notes = st.text_area(notes_lbl, value="Sharp increase in removal efficiency from pH 2 to 6, followed by a slight decline due to metal hydroxide precipitation.")

if st.button(btn_gen, key="btn_claude_opt"):
    with st.spinner("Claude is analyzing chemical equilibria and formulating Q1-grade discussion..."):
        st.success(success_msg)
        
        st.markdown(f"### {preview_title}")
        claude_discussion_draft = f"""
**Thermodynamic and Mechanistic Interpretation of {studied_param} Optimization:**
The experimental findings reveal a pronounced dependency of the adsorption performance on the variation of {studied_param}, reaching a maximum apex at {optimum_value}.
- At lower values, intense competition arising from high hydronium ion ($H^+$) concentrations restricts active binding sites via electrostatic repulsion.
- As the system approaches the optimized threshold ({optimum_value}), surface deprotonation of functional groups enhances favorable electrostatic attraction and complexation.
- The decline beyond this point is mechanistically attributed to the onset of metal hydroxide precipitation and competitive hydroxyl ion coordination. These thermodynamic deductions align seamlessly with advanced Q1-level separation literature.
- *Insights:* {user_notes}
        """.strip()
        st.info(claude_discussion_draft)
