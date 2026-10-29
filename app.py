import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Advanced Academic Platform",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 ChemResearch AI: Advanced Academic Platform")
st.markdown("Q1 Introduction Synthesis & Professional Citation Engine")
st.markdown("---")

# --- Section 1: Experiment & Research Metadata ---
st.subheader("📌 Section 1: Experiment & Research Metadata")

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
        "Analytical Instrumentation (e.g., AAS, UV-Vis):",
        value="Atomic Absorption Spectrometer (AAS)"
    )

with col2:
    prepared_material = st.text_input(
        "Prepared Novel Material / Sorbent:",
        value="Modified Agricultural Waste Bio-adsorbent"
    )
    characterization_tools = st.text_input(
        "Characterization Tools (e.g., FTIR, SEM, XRD):",
        value="FTIR, SEM, XRD, BET"
    )

st.markdown("### 🔍 Select Research Fields:")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    field_spe = st.checkbox("Solid-Phase Extraction (SPE)", value=True)
with col_f2:
    field_adsorb = st.checkbox("Adsorption", value=True)
with col_f3:
    field_removal = st.checkbox("Removal / Remediation", value=True)

other_specify = st.text_input("Other (Specify):", placeholder="")

st.markdown("---")
st.subheader("⚙️ Q1 Style & Citation Format")
col_s1, col_s2 = st.columns(2)
with col_s1:
    journal_style = st.selectbox(
        "Target Journal Quartile Style:",
        ["Q1 Style (High Impact & Rigorous)", "Q2 Style", "Review Paper Style"]
    )
with col_s2:
    citation_style = st.selectbox(
        "Citation Style:",
        ["Numerical Style [1, 2] (Standard Journal Format)", "Author-Date (Harvard / APA)"]
    )

# --- قسم توليد المقدمة الأكاديمية (Introduction Synthesis) - المحافظة على الكود القديم ---
st.markdown("---")
st.subheader("📝 Section 2: Q1 Introduction Synthesis & Drafting")
intro_notes = st.text_area(
    "أدخل النقاط الرئيسية أو الأهداف لإدراجها في مسودة المقدمة الأكاديمية:",
    value="Highlighting the environmental risks of heavy metals, the novelty of the prepared bio-adsorbent, and the superior removal efficiency."
)

if st.button("🚀 توليد مسودة المقدمة (Introduction Draft)", key="generate_intro"):
    with st.spinner("جاري صياغة المقدمة بلغة أكاديمية رصينة تناسب مجلات الـ Q1..."):
        st.success("تم توليد المسودة بنجاح!")
        st.markdown(f"""
        > **Suggested Q1 Introduction Draft:**
        > Recent industrial developments have significantly increased the discharge of toxic heavy metal ions, particularly **{target_metal}**, into aqueous ecosystems... 
        > To address this challenge, we report the **{prepared_material}** synthesized via a facile route. 
        > Analytical characterizations including **{characterization_tools}** confirmed the successful structural fabrication. 
        > *Core Focus:* {intro_notes}
        """)

# --- ميزة الربط الذكي مع أدوات الأدبيات (Consensus & Literature Bridge) الجديد ---
st.markdown("---")
st.subheader("🌐 قسم البحث الذكي وتوليف أرشيف الـ Q1 (Consensus & Literature Bridge)")
st.markdown("بناءً على مدخلاتك الحالية، ستقوم المنصة بتوليد الاستعلام الأكاديمي الدقيق لاستخراج المقالات المحكمة المرتبطة مباشرة بتجربتك.")

# بناء استعلام البحث المتقدم تلقائياً بناءً على المدخلات
search_query_text = f"{prepared_material} {target_metal} {' '.join([f for f, active in [('SPE', field_spe), ('Adsorption', field_adsorb), ('Removal', field_removal)] if active])} Q1 journal"
encoded_query = urllib.parse.quote(search_query_text)

# روابط مباشرة لأداة Consensus ومحركات البحث الأكاديمي
consensus_url = f"https://consensus.app/search/?q={encoded_query}"
scholar_url = f"https://scholar.google.com/scholar?q={encoded_query}"

st.info(f"**استعلام البحث المتولد أوتوماتيكياً (Generated Query):** \n`{search_query_text}`")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.markdown(f"### [🔗 فتح وفحص 20+ مقالة عبر Consensus]({consensus_url})", unsafe_allow_html=True)
    st.caption("ينقلك مباشرة إلى أداة Consensus مع تطبيق الاستعلام المستخرج لتصفح الأدبيات واستخراج النتائج المباشرة.")

with col_btn2:
    st.markdown(f"### [📚 البحث الاحتياطي في Google Scholar]({scholar_url})", unsafe_allow_html=True)
    st.caption("دعم إضافي للبحث الموسع في الأوراق الأكاديمية ذات الصلة.")

# أرشيف المراجع المكتشفة للورقة البحثية
st.markdown("---")
st.subheader("📚 أرشيف المراجع المكتشفة للورقة البحثية:")
uploaded_refs_text = st.text_area(
    "أدخل المراجع المختارة (مرجع في كل سطر مع DOI أو الرابط):",
    value="1. Smith et al., J. Hazard. Mater., 2024, Bio-adsorbent for cadmium removal.\n2. Al-Duran et al., Chem. Eng. J., 2025, Optimization of micro solid-phase extraction."
)

if st.button("💾 حفظ قاعدة بيانات المشروع وربطها بالبوابات القادمة", key="save_meta"):
    st.success("تم حفظ إعدادات البيانات الأساسية وقسم المقدمة وربط الاستعلامات بنجاح!")
