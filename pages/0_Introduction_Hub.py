import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Introduction & Platform Overview",
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
    st.markdown("### Platform Navigation")
    st.caption("Active Module: Introduction & Core Research Objectives")

# الترجمات الخاصة بصفحة المقدمة
if lang_choice == "English":
    title_text = "ChemResearch AI: Introduction & Core Objectives"
    desc_text = "Foundational framework for Q1 analytical chemistry research, advanced green synthesis, and systematic parameter optimization."
    sec_title = "1. Research Scope & Methodological Overview"
    body_text = """
    This platform serves as an advanced computational bridge for doctoral-level research in analytical chemistry. 
    Focusing on high-impact Q1 journal standards, the system integrates:
    - **Green Analytical Chemistry:** Conversion of plant waste and biomass into tailored bio-adsorbents.
    - **Advanced Separation & Preconcentration:** Solid-phase extraction (SPE/MSPE), heavy metal remediation, and chemical speciation.
    - **Rigorous Thermodynamic & Kinetic Modeling:** Automated evaluation of isotherm models, activation energies, and surface interactions.
    """
elif lang_choice == "Türkçe":
    title_text = "ChemResearch AI: Giriş ve Temel Hedefler"
    desc_text = "Q1 analitik kimya araştırmaları, gelişmiş yeşil sentez ve sistematik parametre optimizasyonu için temel altyapı."
    sec_title = "1. Araştırma Kapsamı ve Metodolojik Genel Bakış"
    body_text = """
    Bu platform, analitik kimyada doktora düzeyindeki araştırmalar için gelişmiş bir hesaplama köprüsü görevi görür.
    Yüksek etki faktörlü Q1 dergi standartlarına odaklanan sistem şunları entegre eder:
    - **Yeşil Analitik Kimya:** Bitki atıklarının ve biyokütlenin özel biyo-adsorbanlara dönüştürülmesi.
    - **Gelişmiş Ayırma ve Zenginleştirme:** Katı faz ekstraksiyonu (SPE/MSPE), ağır metal giderimi ve kimyasal türlendirme.
    - **Titiz Termodinamik ve Kinetik Modelleme:** İzoterm modellerinin, aktivasyon enerjilerinin ve yüzey etkileşimlerinin otomatik değerlendirilmesi.
    """
else:  # العربية
    title_text = "المنصة الأكاديمية: المقدمة والأهداف الأساسية"
    desc_text = "الإطار التأسيسي لأبحاث الكيمياء التحليلية المصنفة في الـ Q1، الكيمياء الخضراء المتقدمة، وتحسين المعلمات بشكل منهجي."
    sec_title = "1. نطاق البحث ونظرة عامة على المنهجية"
    body_text = """
    تعتبر هذه المنصة جسراً حسابياً متقدماً لأبحاث الدكتوراه في الكيمياء التحليلية. 
    مع التركيز على معايير مجلات الـ Q1 عالية التأثير، تدمج المنصة العناصر التالية:
    - **الكيمياء التحليلية الخضراء:** تحويل المخلفات النباتية والكتلة الحيوية إلى مواد ممتصة حيوية مصممة خصيصاً.
    - **الفصل والتركيز المتقدم:** الاستخلاص الصلب (SPE/MSPE)، معالجة الثقيلة، وتحديد الأنواع الكيميائية.
    - **النمذجة الثيرموديناميكية والحركية الصارمة:** التقييم التلقائي لنماذج الإيزوثيرم، طاقات التنشيط، والتفاعلات السطحية.
    """

# --- عرض المحتوى ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{title_text}</h1>
        <p>{desc_text}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"### {sec_title}")
st.markdown(body_text)

st.markdown("---")
st.info("Tip: Use the sidebar to navigate between the Introduction Hub, Literature Hub, Optimization Parameters, and Characterization modules.")
