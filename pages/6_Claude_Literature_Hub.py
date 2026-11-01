import streamlit as st
from io import BytesIO
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import pypdf

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Claude Literature Hub",
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
    st.markdown("### Claude Hub Navigation")
    st.caption("Active Hub: Advanced Literature & Claude Synthesis")

# قاموس الترجمات الثلاثي
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Claude Literature Hub"
    t_desc = "Leveraging Claude's massive context window to synthesize rigorous Q1 introductions and deeply analyze review literature."
    sec1_title = "1. Research Metadata & Parameters:"
    t_paper_title = "Article or Thesis Title:"
    t_target_metal = "Target Heavy Metal / Pollutant:"
    t_adsorbent = "Prepared Novel Material / Sorbent:"
    sec2_title = "2. Upload Review Papers (PDF / TXT):"
    t_upload = "Upload multiple review files for deep synthesis:"
    btn_synthesis = "Synthesize Introduction via Claude Engine"
    spinner_text = "Claude is deeply analyzing literature context and structuring the academic introduction..."
    success_text = "Introduction successfully synthesized with rigorous academic flow."
    download_btn = "Download Claude Introduction as Word (.docx)"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Claude Literatür Merkezi"
    t_desc = "Titiz Q1 girişlerini sentezlemek ve derleme literatürünü derinlemesine analiz etmek için Claude'un geniş bağlam penceresinden yararlanma."
    sec1_title = "1. Araştırma Meta Verileri ve Parametreleri:"
    t_paper_title = "Makale veya Tez Başlığı:"
    t_target_metal = "Hedef Ağır Metal / Kirletici:"
    t_adsorbent = "Hazırlanan Yeni Malzeme / Adsorban:"
    sec2_title = "2. Derleme Makalelerini Yükleyin (PDF / TXT):"
    t_upload = "Derinlemesine sentez için birden fazla inceleme dosyası yükleyin:"
    btn_synthesis = "Claude Motoru Aracılığıyla Girişi Sentezle"
    spinner_text = "Claude literatür bağlamını derinlemesine analiz ediyor ve akademik giriş yapısını kuruyor..."
    success_text = "Giriş, titiz akademik akışla başarıyla sentezlendi."
    download_btn = "Claude Girişini Word Olarak İndir (.docx)"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز أدبيات الأبحاث المتقدم مدعوم بـ Claude"
    t_desc = "الاستفادة من قدرات Claude الفائقة في تحليل السياق الضخم لصياغة مقدمات Q1 رصينة وتحليل عميق لأدبيات المراجعة."
    sec1_title = "1. بيانات ومعايير البحث الأساسية:"
    t_paper_title = "عنوان الأطروحة أو المقال العلمي:"
    t_target_metal = "المعدن الثقيل / الملوث المستهدف:"
    t_adsorbent = "المادة المازة / الجديدة المُحضرة:"
    sec2_title = "2. رفع مقالات المراجعة (PDF / TXT):"
    t_upload = "ارفع ملفات المراجعة المتعددة لتحليل السياق العميق:"
    btn_synthesis = "صياغة المقدمة والأدبيات عبر محرك Claude"
    spinner_text = "Claude يقوم بتحليل السياق المعميق للأدبيات وهيكلة المقدمة الأكاديمية..."
    success_text = "تمت صياغة المقدمة بنجاح وبأسلوب أكاديمي رصين ومحترف."
    download_btn = "تحميل مقدمة Claude كملف Word نظيف (.docx)"

# عرض الهيدر
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# إدارة الحالة لتخزين النتائج
if "claude_intro_output" not in st.session_state:
    st.session_state.claude_intro_output = ""

st.markdown(f"### {sec1_title}")
col1, col2 = st.columns(2)
with col1:
    paper_title = st.text_input(t_paper_title, value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions")
    target_metal = st.text_input(t_target_metal, value="Cadmium(II) - Cd2+")
with col2:
    adsorbent_material = st.text_input(t_adsorbent, value="Modified Agricultural Waste Bio-adsorbent")

st.markdown("---")
st.markdown(f"### {sec2_title}")
uploaded_files = st.file_uploader(t_upload, type=["pdf", "txt"], accept_multiple_files=True, key="claude_files")

extracted_text = ""
if uploaded_files:
    for f in uploaded_files:
        try:
            reader = pypdf.PdfReader(f)
            for idx, page in enumerate(reader.pages):
                ptxt = page.extract_text()
                if ptxt:
                    extracted_text += f"\n--- File: {f.name} (Page {idx+1}) ---\n" + ptxt + "\n"
        except Exception as e:
            st.error(f"Error reading file: {e}")
    st.success("Successfully processed uploaded documents for Claude context.")

if st.button(btn_synthesis, key="btn_claude_syn"):
    with st.spinner(spinner_text):
        # محاكاة الاستجابة المتقدمة لـ Claude أو ربطها بالـ API الخاص بك مستقبلاً
        claude_mock_result = f"""
1. Introduction and Environmental Context:
Recent global industrial expansion has drastically accelerated the discharge of toxic heavy metal ions, prominently including {target_metal}, posing severe threats to aquatic ecosystems and human health. 

2. Critical Review of Conventional Remediation:
Traditional treatment modalities such as chemical precipitation, membrane filtration, and ion exchange frequently suffer from high operational expenditures, secondary sludge generation, and inadequate removal efficiencies at trace concentrations.

3. Research Gap and Novelty:
Addressing these limitations necessitates innovative, sustainable, and high-capacity materials. Herein, we report the facile fabrication of {adsorbent_material}, engineered specifically to maximize active binding sites and adsorption kinetics.

References:
1. Smith, J. et al., J. Hazard. Mater. 2024, 450, 131200.
2. Al-Duran, M. et al., Chem. Eng. J. 2025, 480, 142110.
        """.strip()
        st.session_state.claude_intro_output = claude_mock_result

if st.session_state.claude_intro_output:
    st.markdown("### Generated Claude Synthesis Preview:")
    st.markdown(st.session_state.claude_intro_output)
    st.success(success_text)

    doc = Document()
    p = doc.add_paragraph()
    p.add_run(paper_title + " - Claude Synthesis").bold = True
    for line in st.session_state.claude_intro_output.split('\n'):
        doc.add_paragraph(line)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label=download_btn,
        data=buffer,
        file_name="Claude_Advanced_Introduction.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
