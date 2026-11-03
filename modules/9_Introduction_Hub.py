import streamlit as st
from io import BytesIO
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import pypdf
from google import genai
import re

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="ChemResearch AI Platform",
    page_icon="🧪",
    layout="wide"
)

# ==================== الحفاظ على البيانات عند تغيير الخيارات (Session State) ====================
if "intro_output" not in st.session_state:
    st.session_state.intro_output = ""

# ==================== الشريط الجانبي وإعدادات الـ API ====================
st.sidebar.title("🌐 Language / Dil / اللغة")
lang_choice = st.sidebar.selectbox("Choose Language:", ["English", "Türkçe", "العربية"])

st.sidebar.markdown("---")
st.sidebar.subheader("🔑 Gemini API Configuration")
api_key_input = st.sidebar.text_input("Enter your Gemini API Key:", type="password", value="")

st.sidebar.markdown("---")
st.sidebar.subheader("📚 Literature Hub")
t_upload_sec2 = "Upload Review Papers (PDFs)"

# قاموس الترجمات الشامل
if lang_choice == "English":
    t_title = "🧪 ChemResearch AI: Advanced Academic Platform"
    t_subtitle = "Q1 Introduction Synthesis & Clean Auto-Citation Engine"
    sec1_title = "📌 Section 1: Experiment & Research Metadata"
    sec2_title = "✍️ Section 2: AI-Synthesized Introduction & Auto-Citations"
    t_paper_title = "Article or Thesis Title:"
    t_target_metal = "Target Heavy Metal / Pollutant:"
    t_adsorbent = "Prepared Novel Material / Sorbent:"
    t_tools = "Characterization Tools (e.g., FTIR, SEM):"
    t_analytical_inst = "Analytical Instrumentation (e.g., AAS, UV-Vis):"
    t_fields_label = "🎯 Select Research Fields:"
    t_field_1 = "Solid-Phase Extraction (SPE)"
    t_field_2 = "Adsorption"
    t_field_3 = "Removal / Remediation"
    t_field_other = "Other (Specify):"
    t_q_style = "📊 Target Journal Quartile Style:"
    t_citation_style = "📖 Citation Style:"
    t_btn_sec2 = "🚀 Synthesize Clean Introduction & Citations"
    t_spinner = "AI is analyzing your PDFs and generating a clean academic synthesis..."
    t_success_gen = "Clean introduction successfully synthesized with organized citations!"
    t_download_btn = "📥 Download Clean Introduction & References as Word (.docx)"

elif lang_choice == "Türkçe":
    t_title = "🧪 ChemResearch AI: Gelişmiş Akademik Platform"
    t_subtitle = "Q1 Giriş Sentezi ve Temiz Otomatik Atıf Motoru"
    sec1_title = "📌 Bölüm 1: Deney ve Araştırma Verileri"
    sec2_title = "✍️ Bölüm 2: Yapay Zeka Destekli Giriş ve Otomatik Atıf Merkezi"
    t_paper_title = "Makale veya Tez Başlığı:"
    t_target_metal = "Hedef Ağır Metal / Kirletici:"
    t_adsorbent = "Hazırlanan Yeni Malzeme / Adsorban:"
    t_tools = "Karakterizasyon Cihazları (örn. FTIR, SEM):"
    t_analytical_inst = "Analitik Ölçüm Cihazı (örn. AAS, UV-Vis):"
    t_fields_label = "🎯 Araştırma Alanlarını Seçin:"
    t_field_1 = "Katı Faz Ekstraksiyonu (SPE)"
    t_field_2 = "Adsorpsiyon (Adsorption)"
    t_field_3 = "Giderim / Arıtma (Removal)"
    t_field_other = "Diğer (Belirtiniz):"
    t_q_style = "📊 Hedef Dergi Düzeyi (Quartile):"
    t_citation_style = "📖 Atıf Stili:"
    t_btn_sec2 = "🚀 Temiz Giriş ve Atıfları Sentezle"
    t_spinner = "Yapay zeka PDF'lerinizi analiz ediyor ve temiz bir sentez oluşturuyor..."
    t_success_gen = "Temiz giriş ve düzenli atıflar başarıyla sentezlendi!"
    t_download_btn = "📥 Temiz Giriş ve Referansları Word Olarak İndir (.docx)"

else:  # العربية
    t_title = "🧪 المنصة الأكاديمية المتقدمة ChemResearch AI"
    t_subtitle = "محرك صياغة المقدمات الأكاديمية والتوثيق التلقائي المنظم والخالي من التكرار"
    sec1_title = "📌 القسم الأول: بيانات التجربة والبحث الأساسية"
    sec2_title = "✍️ القسم الثاني: مركز صياغة المقدمة والتوثيق العلمي التلقائي"
    t_paper_title = "عنوان الأطروحة أو المقال العلمي:"
    t_target_metal = "المعدن الثقيل / الملوث المستهدف:"
    t_adsorbent = "المادة الماصة / الجديدة المُحضرة:"
    t_tools = "أجهزة التشخيص (مثل: FTIR, SEM, XRD):"
    t_analytical_inst = "جهاز التحليل المخبري لتقدير التراكيز (مثل: AAS, UV-Vis, ICP-OES):"
    t_fields_label = "🎯 اختر مجالات البحث الأساسية:"
    t_field_1 = "الاستخلاص الصلب (Solid-Phase Extraction - SPE)"
    t_field_2 = "الامتزاز (Adsorption)"
    t_field_3 = "الإزالة والمعالجة (Removal / Remediation)"
    t_field_other = "أخرى (اكتبها بنفسك):"
    t_q_style = "📊 مستوى المجلة المستهدفة (Journal Quartile Style):"
    t_citation_style = "📖 أسلوب التوثيق والاستشهاد (Citation Style):"
    t_btn_sec2 = "🚀 صياغة مقدمة نظيفة ومنظمة بدون تكرار أو نجوم"
    t_spinner = "الذكاء الاصطناعي ينظم الاستشهادات ويصيغ محتوى أكاديمياً نظيفاً..."
    t_success_gen = "تمت صياغة المقدمة وتوثيقها بدقة متناهية وبدون أي تكرار!"
    t_download_btn = "📥 تحميل المقدمة وقائمة المراجع كملف Word نظيف (.docx)"

# عرض ترويسة الموقع
st.title(t_title)
st.markdown(t_subtitle)
st.markdown("---")

# ==================== القسم الأول: بيانات التجربة والبحث ====================
st.header(sec1_title)

col1, col2 = st.columns(2)
with col1:
    paper_title = st.text_input(t_paper_title, value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions")
    target_metal = st.text_input(t_target_metal, value="Cadmium(II) - Cd2+")
    analytical_instrument = st.text_input(t_analytical_inst, value="Atomic Absorption Spectrometer (AAS)")
with col2:
    adsorbent_material = st.text_input(t_adsorbent, value="Modified Agricultural Waste Bio-adsorbent")
    characterization_tools = st.text_input(t_tools, value="FTIR, SEM, XRD, BET")

st.markdown("### " + t_fields_label)
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1: f_spe = st.checkbox(t_field_1, value=True)
with col_f2: f_ads = st.checkbox(t_field_2, value=True)
with col_f3: f_rem = st.checkbox(t_field_3, value=True)

other_field_input = st.text_input(t_field_other, value="")
journal_style = st.selectbox(t_q_style, ["Q1 Style (High Impact & Rigorous)", "Q2 Style (Standard Professional)", "Q3 Style (Clear & Direct)"])
citation_format = st.selectbox(t_citation_style, ["Numerical Style [1], [2], [3] (Sequential & Unique)", "Author-Date Style (APA / Harvard)"])

selected_fields = []
if f_spe: selected_fields.append("Solid-Phase Extraction (SPE)")
if f_ads: selected_fields.append("Adsorption")
if f_rem: selected_fields.append("Removal/Remediation")
if other_field_input: selected_fields.append(other_field_input)
fields_text = ", ".join(selected_fields)

st.markdown("---")

# ==================== القسم الثاني: مركز صياغة المقدمة الذكي التلقائي ====================
st.header(sec2_title)

st.markdown("📂 **مستودع مقالات المراجعة (ارفع ملفات الـ PDF هنا):**")
sources_sec2 = st.file_uploader(t_upload_sec2, type=["pdf", "txt"], accept_multiple_files=True, key="sec2_files")

extracted_pdf_text = ""
if sources_sec2:
    for f in sources_sec2:
        try:
            reader = pypdf.PdfReader(f)
            for page_idx, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    extracted_pdf_text += f"\n--- Source File: {f.name} (Page {page_idx+1}) ---\n" + page_text + "\n"
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    st.success(f"Successfully extracted text from {len(sources_sec2)} review files.")

if st.button(t_btn_sec2, key="btn_sec2"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key in the sidebar to enable AI synthesis.")
    else:
        with st.spinner(t_spinner):
            try:
                client = genai.Client(api_key=api_key_input)
                
                # برومبت صارم يمنع النجوم وتكرار المراجع ويضمن تسلسلاً رقمياً فريداً
                prompt = f"""
                You are an expert analytical chemistry researcher and professional academic writer publishing in top Q1 journals.
                Your task is to write a rigorous, comprehensive, and entirely original Introduction section for a PhD-level research article.
                
                CRITICAL FORMATTING & CITATION RULES:
                1. STRICTLY DO NOT use Markdown asterisks (*) or bold/italic markdown symbols anywhere in the text (no *, no **). Keep plain clean text.
                2. Ensure citation numbers or author-date citations are strictly unique, sequential, and non-repetitive (e.g., [1], [2], [3] without duplicate numbers in the same or consecutive phrases).
                3. Analyze the uploaded review paper texts to build a unique funnel introduction (Global environmental impact -> Limitations of conventional methods -> Research Gap -> Novelty of {adsorbent_material}).
                4. At the end of the text, provide a clean "References" section listing unique literature derived from the uploaded sources in correct academic order, without any markdown stars.
                5. Avoid complex LaTeX formatting (use standard text formats like Cu2+, Cd2+, qm, R2 > 0.99).
                
                Research Metadata:
                - Title: {paper_title}
                - Target Pollutant: {target_metal}
                - Prepared Material/Sorbent: {adsorbent_material}
                - Fields: {fields_text}
                - Characterization Tools: {characterization_tools}
                - Journal Standard: {journal_style}
                - Citation Style: {citation_format}
                
                Extracted Text from Uploaded Review Papers:
                {extracted_pdf_text[:25000]}
                
                Write in formal academic English suitable for Q1 journals.
                """
                
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt,
                )
                
                # تنظيف النص البرمجي مباشرة من أي نجوم قد ينتجها النموذج
                cleaned_text = response.text.replace('*', '').replace('###', '')
                st.session_state.intro_output = cleaned_text
            except Exception as e:
                st.error(f"An error occurred during AI generation: {e}")

# عرض النتائج مع الحفاظ عليها عند تغيير اللغة وتنظيف النجوم
if st.session_state.intro_output:
    st.markdown("### 📝 Generated Introduction & Clean Citations Preview:")
    st.markdown(st.session_state.intro_output)
    st.success(t_success_gen)

    # إنشاء مستند Word نظيف تماماً وخالٍ من النجوم ومحمي الخطوط
    doc = Document()
    
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1) if 'Inches' in globals() else doc.sections[0].top_margin
        section.bottom_margin = doc.sections[0].bottom_margin
        section.left_margin = doc.sections[0].left_margin
        section.right_margin = doc.sections[0].right_margin

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(14)
    run_title = p_title.add_run(paper_title + " - Introduction & References")
    run_title.bold = True
    run_title.font.name = "Times New Roman"
    run_title.font.size = Pt(14)

    # تنظيف النص نهائياً من أي نجوم أو رموز تنسيق قبل إضافته للـ Word
    final_clean_text = st.session_state.intro_output.replace('*', '')
    paragraphs = final_clean_text.split('\n\n')
    
    for para_text in paragraphs:
        if para_text.strip():
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(para_text.replace('#', '').strip())
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label=t_download_btn,
        data=buffer,
        file_name="ChemResearch_AI_Clean_Introduction.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        key="dl_sec2"
    )
