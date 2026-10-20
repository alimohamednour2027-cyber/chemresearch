import streamlit as st
from io import BytesIO
from docx import Document
from docx.shared import Inches, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import pypdf
from google import genai

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="ChemResearch AI Platform",
    page_icon="🧪",
    layout="wide"
)

# ==================== الحفاظ على البيانات عند تغيير الخيارات (Session State) ====================
if "intro_output" not in st.session_state:
    st.session_state.intro_output = ""
if "methods_output" not in st.session_state:
    st.session_state.methods_output = ""

# ==================== الشريط الجانبي وإعدادات الـ API ====================
st.sidebar.title("🌐 Language / Dil / اللغة")
lang_choice = st.sidebar.selectbox("Choose Language:", ["English", "Türkçe", "العربية"])

st.sidebar.markdown("---")
st.sidebar.subheader("🔑 Gemini API Configuration")
api_key_input = st.sidebar.text_input("Enter your Gemini API Key:", type="password", value="")

st.sidebar.markdown("---")
st.sidebar.subheader("📚 Sources Hub")
t_upload_sec2 = "Upload Review Papers (for Introduction)"
t_upload_sec3 = "Upload Lab Data & Results (for Discussion)"

# قاموس الترجمات الشامل
if lang_choice == "English":
    t_title = "🧪 ChemResearch AI: Advanced AI-Powered Platform"
    t_subtitle = "True LLM-Driven Synthesis Engine (NotebookLM Style)"
    sec1_title = "📌 Section 1: Experiment & Research Data"
    sec2_title = "✍️ Section 2: AI-Synthesized Introduction (From Your PDFs)"
    sec3_title = "📊 Section 3: Materials, Methods, Results & Conclusions"
    t_exp_title = "🔬 Research Metadata & Parameters"
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
    t_btn_sec2 = "🚀 Synthesize Rigorous Introduction via AI"
    t_btn_sec3 = "🚀 Generate Methods, Results & Conclusions"
    t_spinner = "AI is reading your uploaded PDFs and synthesizing deep academic text..."
    t_success_gen = "Introduction successfully synthesized from your sources!"
    t_download_btn = "📥 Download as Word (.docx)"

elif lang_choice == "Türkçe":
    t_title = "🧪 ChemResearch AI: Gelişmiş Yapay Zeka Destekli Platform"
    t_subtitle = "Gerçek LLM Destekli Sentez Motoru (NotebookLM Tarzı)"
    sec1_title = "📌 Bölüm 1: Deney ve Araştırma Verileri"
    sec2_title = "✍️ Bölüm 2: Yapay Zeka Destekli Giriş (PDF'lerinizden)"
    sec3_title = "📊 Bölüm 3: Materyal, Metot, Bulgular ve Sonuçlar"
    t_exp_title = "🔬 Araştırma Meta Verileri ve Parametreleri"
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
    t_btn_sec2 = "🚀 Yapay Zeka ile Kapsamlı Giriş Sentezle"
    t_btn_sec3 = "🚀 Metot, Bulgular ve Sonuçları Oluştur"
    t_spinner = "Yapay zeka PDF'lerinizi okuyor ve derinlemesine akademik metin sentezliyor..."
    t_success_gen = "Giriş kaynaklarınızdan başarıyla sentezlendi!"
    t_download_btn = "📥 Word Olarak İndir (.docx)"

else:  # العربية
    t_title = "🧪 ChemResearch AI: المنصة الأكاديمية المدعومة بالذكاء الاصطناعي"
    t_subtitle = "محرك صياغة حقيقي مدعوم بنماذج اللغات الكبيرة (على غرار NotebookLM)"
    sec1_title = "📌 القسم الأول: بيانات التجربة والبحث الأساسية"
    sec2_title = "✍️ القسم الثاني: صياغة المقدمة الحقيقية عبر الذكاء الاصطناعي (من مصادرك المرفوعة)"
    sec3_title = "📊 القسم الثالث: المواد، طرق العمل، النتائج والاستنتاجات"
    t_exp_title = "🔬 إعدادات المعلمات والبيانات الأساسية للتجربة"
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
    t_btn_sec2 = "🚀 صياغة مقدمة عميقة بالذكاء الاصطناعي استناداً للمراجع"
    t_btn_sec3 = "🚀 توليد المواد، النتائج والاستنتاجات"
    t_spinner = "الذكاء الاصطناعي يقرأ مصادرك المرفوعة ويحللها ويصيغ مقدمة فريدة..."
    t_success_gen = "تمت صياغة المقدمة بنجاح بالاعتماد الحقيقي على مصادرك المرفوعة!"
    t_download_btn = "📥 تحميل كملف Word (.docx)"

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

selected_fields = []
if f_spe: selected_fields.append("Solid-Phase Extraction (SPE)")
if f_ads: selected_fields.append("Adsorption")
if f_rem: selected_fields.append("Removal/Remediation")
if other_field_input: selected_fields.append(other_field_input)
fields_text = ", ".join(selected_fields)

st.markdown("---")

# ==================== القسم الثاني: المقدمة الذكية القائمة على الـ LLM والمراجع ====================
st.header(sec2_title)

st.markdown("📂 **مستودع ملفات القسم الثاني (ارفع ملفات الـ PDF الخاصة بمراجعك هنا):**")
sources_sec2 = st.file_uploader(t_upload_sec2, type=["pdf", "txt"], accept_multiple_files=True, key="sec2_files")

extracted_pdf_text = ""
if sources_sec2:
    for f in sources_sec2:
        try:
            reader = pypdf.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_pdf_text += page_text + "\n"
        except Exception as e:
            st.error(f"Error reading file: {e}")
    st.success(f"Successfully extracted text from {len(sources_sec2)} uploaded reference files.")

if st.button(t_btn_sec2, key="btn_sec2"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key in the sidebar to enable AI synthesis.")
    else:
        with st.spinner(t_spinner):
            try:
                client = genai.Client(api_key=api_key_input)
                
                prompt = f"""
                You are an expert analytical chemistry researcher and professional academic writer publishing in top Q1 journals.
                Write a rigorous, comprehensive, and original Introduction section for a PhD-level research article.
                
                Research Metadata:
                - Title: {paper_title}
                - Target Pollutant: {target_metal}
                - Prepared Material/Sorbent: {adsorbent_material}
                - Fields: {fields_text}
                - Characterization Tools: {characterization_tools}
                - Journal Standard: {journal_style}
                
                Context extracted from user's uploaded reference papers (Review PDFs):
                {extracted_pdf_text[:15000]}
                
                Instructions:
                1. Do NOT use generic boilerplate templates. Analyze the provided reference context and synthesize an original, deep academic introduction.
                2. Structure it logically with a funnel approach: global environmental impact of the pollutant, limitations of conventional methods, identification of the research gap, and the specific novelty of {adsorbent_material}.
                3. Ensure the final paragraphs focus strictly on the specific research problem, avoiding any generic descriptions of journal types or article templates.
                4. Write in formal academic English suitable for Q1 journals.
                """
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                
                st.session_state.intro_output = response.text
            except Exception as e:
                st.error(f"An error occurred during AI generation: {e}")

# عرض النص المحفوظ في الذاكرة المؤقتة لكي لا يختفي عند تغيير اللغة
if st.session_state.intro_output:
    st.markdown(st.session_state.intro_output)
    st.success(t_success_gen)

    # إنشاء ملف Word منسق بشكل نظيف يمنع تشابك الأسطر والمعادلات
    doc = Document()
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(12)
    run_title = p_title.add_run(paper_title + " - Introduction")
    run_title.bold = True
    run_title.font.size = Pt(16)

    for line in st.session_state.intro_output.split('\n'):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        p.add_run(line)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label=t_download_btn,
        data=buffer,
        file_name="ChemResearch_AI_Introduction.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        key="dl_sec2"
    )

st.markdown("---")

# ==================== القسم الثالث: المواد، الطرق والنتائج ====================
st.header(sec3_title)

st.markdown("📊 **مستودع ملفات القسم الثالث (خاص بالنتائج وبيانات المختبر):**")
sources_sec3 = st.file_uploader(t_upload_sec3, type=["pdf", "txt"], accept_multiple_files=True, key="sec3_files")

if st.button(t_btn_sec3, key="btn_sec3"):
    methods_results_output = f"""# {paper_title} - Materials, Methods & Discussion
*Research Focus: {fields_text} | Analytical Tool: {analytical_instrument}*

## Materials and Methods
### 2.1. Chemicals and Reagents
All analytical-grade chemical reagents utilized throughout this experimental investigation were procured from certified international manufacturers and used without further purification. Deionized water was consistently employed for all aqueous solution preparations.

### 2.2. Synthesis of the Novel {adsorbent_material}
The preparation of the advanced {adsorbent_material} tailored for {fields_text} involved a meticulously optimized synthetic route. Precursors were subjected to pre-treatment, functionalization, and activation under strictly controlled parameters.

### 2.3. Instrumental Characterization & Analytical Estimation
To confirm successful fabrication, the material underwent comprehensive multi-technique characterization using {characterization_tools}. Quantitative and residual metal concentrations were estimated using {analytical_instrument}. Batch adsorption and extraction experiments were systematically designed to evaluate critical operational parameters ensuring high reproducibility.

## Results and Discussion
### 3.1. Structural and Morphological Characterization
Based on the experimental data obtained via {analytical_instrument}, the successful synthesis and physicochemical restructuring of {adsorbent_material} designed for {fields_text} were comprehensively validated through {characterization_tools} analyses, revealing active binding sites favorable for {target_metal} sequestration.

### 3.2. Adsorption Kinetics, Isotherms, and Thermodynamics
Experimental kinetic data and quantitative measurements performed via {analytical_instrument} were evaluated to elucidate rate-controlling mechanisms. Equilibrium isotherm data analyzed via Langmuir and Freundlich models exhibited exceptional compliance with the Langmuir isotherm, confirming monolayer coverage with a notable maximum adsorption capacity (qm). The high correlation coefficients (R2 > 0.99) indicate that chemisorption acts as the rate-limiting step.

## Conclusions
In summary, this study successfully demonstrated the facile fabrication and high-performance application of {adsorbent_material} tailored specifically for {fields_text}. Comprehensive characterization verified the abundance of active surface functional groups, while analytical measurements via {analytical_instrument} confirmed superior uptake efficiencies toward {target_metal}. Overall, this research establishes an environmentally sustainable framework for advanced analytical separation and industrial wastewater treatment under {journal_style} standards.
"""
    st.session_state.methods_output = methods_results_output

if st.session_state.methods_output:
    st.markdown(st.session_state.methods_output)
    st.success("Sections generated successfully!")

    doc_m = Document()
    p_title_m = doc_m.add_paragraph()
    p_title_m.paragraph_format.space_after = Pt(12)
    run_title_m = p_title_m.add_run(paper_title + " - Manuscript Draft")
    run_title_m.bold = True
    run_title_m.font.size = Pt(16)

    for line in st.session_state.methods_output.split('\n'):
        p = doc_m.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        p.add_run(line)

    buffer_m = BytesIO()
    doc_m.save(buffer_m)
    buffer_m.seek(0)

    st.download_button(
        label=t_download_btn,
        data=buffer_m,
        file_name="ChemResearch_Methods_Results_Conclusions.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        key="dl_sec3"
    )
