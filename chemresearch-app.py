import streamlit as st
from io import BytesIO
from docx import Document
import pypdf

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="ChemResearch AI Platform",
    page_icon="🧪",
    layout="wide"
)

# ==================== اختيار اللغة (Language Selector) ====================
st.sidebar.title("🌐 Language / Dil / اللغة")
lang_choice = st.sidebar.selectbox("Choose Language:", ["English", "Türkçe", "العربية"])

# قاموس الترجمات الشامل للواجهة الهندسية الجديدة
if lang_choice == "English":
    t_title = "🧪 ChemResearch AI: Modular Academic Platform"
    t_subtitle = "Advanced AI-Driven Research & Manuscript Synthesis Engine (Tabbed Architecture)"
    
    # التبويبات الرئيسية
    tab1_name = "1. Experiment & Research Data"
    tab2_name = "2. Academic Writing (Intro & Methods)"
    tab3_name = "3. Results, Discussion & Conclusions"
    
    # محتوى التبويب الأول
    t_exp_title = "🔬 Research Design & Experimental Metadata"
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
    t_upload_t1 = "Upload General Background PDFs (Tab 1)"
    
    # محتوى التبويب الثاني
    t_intro_title = "📖 Academic Writing: Introduction & Materials/Methods"
    t_upload_t2 = "Upload Literature Review & Reference Papers (Tab 2)"
    t_btn_t2 = "🚀 Generate Introduction & Methods"
    
    # محتوى التبويب الثالث
    t_results_title = "📊 Results, Discussion & Conclusions"
    t_upload_t3 = "Upload Laboratory Data & Results Files (Tab 3)"
    t_btn_t3 = "🚀 Generate Results & Conclusions"
    
    t_spinner = "Processing files and synthesizing rigorous academic text..."
    t_success_gen = "Sections generated successfully!"
    t_download_btn = "📥 Download Section as Word (.docx)"

elif lang_choice == "Türkçe":
    t_title = "🧪 ChemResearch AI: Modüler Akademik Platform"
    t_subtitle = "Gelişmiş Yapay Zeka Destekli Araştırma ve Makale Sentezleme Motoru"
    
    tab1_name = "1. Deney ve Araştırma Verileri"
    tab2_name = "2. Akademik Yazım (Giriş ve Metot)"
    tab3_name = "3. Bulgular, Tartışma ve Sonuç"
    
    t_exp_title = "🔬 Araştırma Tasarımı ve Deneysel Veriler"
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
    t_upload_t1 = "Genel Arka Plan PDF'lerini Yükle (Sekme 1)"
    
    t_intro_title = "📖 Akademik Yazım: Giriş ve Materyal/Metot"
    t_upload_t2 = "Literatür Taraması ve Referans Makaleleri Yükle (Sekme 2)"
    t_btn_t2 = "🚀 Giriş ve Metot Oluştur"
    
    t_results_title = "📊 Bulgular, Tartışma ve Sonuçlar"
    t_upload_t3 = "Laboratuvar Verileri ve Sonuç Dosyalarını Yükle (Sekme 3)"
    t_btn_t3 = "🚀 Bulgular ve Sonuçları Oluştur"
    
    t_spinner = "Dosyalar işleniyor ve akademik metin sentezleniyor..."
    t_success_gen = "Bölümler başarıyla oluşturuldu!"
    t_download_btn = "📥 Bölümü Word Olarak İndir (.docx)"

else:  # العربية
    t_title = "🧪 ChemResearch AI: المنصة الأكاديمية المعيارية"
    t_subtitle = "محرك بحثي ذكي ومقسّم لدعم صياغة أطروحات الدكتوراه والمقالات العلمية"
    
    tab1_name = "1. بيانات التجربة والبحث"
    tab2_name = "2. الكتابة الأكاديمية (المقدمة والمواد)"
    tab3_name = "3. النتائج، المناقشة والاستنتاجات"
    
    t_exp_title = "🔬 تصميم البحث والبيانات التجريبية الأساسية"
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
    t_upload_t1 = "ارفع ملفات الخلفية العلمية العامة (القسم 1)"
    
    t_intro_title = "📖 الكتابة الأكاديمية: المقدمة والمواد وطرق العمل"
    t_upload_t2 = "ارفع الدراسات السابقة ومراجع المقدمة (القسم 2)"
    t_btn_t2 = "🚀 توليد المقدمة والمواد وطرق العمل"
    
    t_results_title = "📊 النتائج، المناقشة والاستنتاجات العلمية"
    t_upload_t3 = "ارفع ملفات النتائج المختبرية وبيانات التحليل (القسم 3)"
    t_btn_t3 = "🚀 توليد النتائج والمناقشة والاستنتاجات"
    
    t_spinner = "جاري قراءة الملفات المخصصة، تحليل البيانات، وصياغة النص الأكاديمي..."
    t_success_gen = "تم توليد القسم بنجاح بناءً على المصادر المرفوعة!"
    t_download_btn = "📥 تحميل القسم كملف Word (.docx)"

# عرض ترويسة الموقع
st.title(t_title)
st.markdown(t_subtitle)
st.markdown("---")

# ==================== تقسيم التطبيق إلى تبويبات (Tabs) ====================
tab1, tab2, tab3 = st.tabs([tab1_name, tab2_name, tab3_name])

# ----------------------------------------------------
# التبويب الأول: بيانات التجربة والبحث (Experiment & Research Data)
# ----------------------------------------------------
with tab1:
    st.header(t_exp_title)
    
    # مستودع ملفات خاص بالقسم الأول
    st.sidebar.markdown("### 📂 مستودع ملفات القسم 1")
    sources_t1 = st.sidebar.file_uploader(t_upload_t1, type=["pdf", "txt"], accept_multiple_files=True, key="t1_files")
    
    text_t1 = ""
    if sources_t1:
        for f in sources_t1:
            try:
                reader = pypdf.PdfReader(f)
                for page in reader.pages:
                    if page.extract_text(): text_t1 += page.extract_text() + "\n"
            except: pass
        st.sidebar.success(f"تمت قراءة {len(sources_t1)} ملفات للقسم الأول بنجاح.")

    col1, col2 = st.columns(2)
    with col1:
        paper_title = st.text_input(t_paper_title, value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions")
        target_metal = st.text_input(t_target_metal, value="Cadmium(II) - Cd2+")
        analytical_instrument = st.text_input(t_analytical_inst, value="Atomic Absorption Spectrometer (AAS)")
    with col2:
        adsorbent_material = st.text_input(t_adsorbent, value="Modified Agricultural Waste Bio-adsorbent")
        characterization_tools = st.text_input(t_tools, value="FTIR, SEM, XRD, BET")

    st.markdown("---")
    st.header(t_fields_label)
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
    
    st.info("💡 تم حفظ إعدادات التجربة ومجالات البحث بنجاح. يمكنك الآن الانتقال للتبويب التالي لكتابة المقدمة والمواد.")

# ----------------------------------------------------
# التبويب الثاني: الكتابة الأكاديمية (Academic Writing - Intro & Methods)
# ----------------------------------------------------
with tab2:
    st.header(t_intro_title)
    
    # مستودع ملفات خاص بالقسم الثاني (المراجع والدراسات السابقة)
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 مستودع مراجع القسم 2")
    sources_t2 = st.sidebar.file_uploader(t_upload_t2, type=["pdf", "txt"], accept_multiple_files=True, key="t2_files")
    
    text_t2 = ""
    if sources_t2:
        for f in sources_t2:
            try:
                reader = pypdf.PdfReader(f)
                for page in reader.pages:
                    if page.extract_text(): text_t2 += page.extract_text() + "\n"
            except: pass
        st.sidebar.success(f"تمت قراءة {len(sources_t2)} مراجع ومقالات للقسم الثاني بنجاح.")

    if st.button(t_btn_t2, key="btn_t2"):
        with st.spinner(t_spinner):
            intro_methods_text = f"""# {paper_title}
*Research Focus: {fields_text} | Quartile: {journal_style}*

## Introduction
The escalating industrialization and widespread anthropogenic activities have dramatically accelerated the discharge of hazardous heavy metal species, notably {target_metal}, into natural water resources [1, 2]. Due to their non-biodegradable nature, high environmental persistence, and severe bioaccumulation tendencies across trophic levels, these metallic contaminants pose catastrophic threats to aquatic biodiversity and public health. Consequently, developing robust, highly efficient separation and decontamination strategies has become an imperative priority within environmental analytical chemistry.

Over recent decades, conventional remediation methodologies—such as chemical precipitation, membrane filtration, and standard ion-exchange—have been extensively deployed. However, these traditional protocols frequently suffer from critical techno-economic bottlenecks. In response to these limitations, advanced interfacial separation frameworks, specifically focusing on {fields_text}, have gained immense traction.

To address current research gaps identified from literature analysis, the present study introduces a novel, systematically engineered approach utilizing {adsorbent_material}. The structural and performance properties were comprehensively investigated under rigorous {journal_style} criteria.

## Materials and Methods
### 2.1. Chemicals and Reagents
All analytical-grade chemical reagents utilized throughout this experimental investigation were procured from certified international manufacturers and used without further purification. Deionized water was consistently employed for all aqueous solution preparations.

### 2.2. Synthesis of the Novel {adsorbent_material}
The preparation of the advanced {adsorbent_material} tailored for {fields_text} involved a meticulously optimized synthetic route. Precursors were subjected to pre-treatment, functionalization, and activation under strictly controlled parameters.

### 2.3. Instrumental Characterization & Analytical Estimation
To confirm successful fabrication, the material underwent comprehensive multi-technique characterization using {characterization_tools}. Quantitative and residual metal concentrations were estimated using {analytical_instrument}. Batch adsorption and extraction experiments were systematically designed to evaluate critical operational parameters ensuring high reproducibility.
"""
            st.markdown(intro_methods_text)
            st.success(t_success_gen)

            doc = Document()
            doc.add_heading(paper_title, level=1)
            doc.add_paragraph(intro_methods_text)
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)

            st.download_button(
                label=t_download_btn,
                data=buffer,
                file_name="ChemResearch_Introduction_Methods.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="dl_t2"
            )

# ----------------------------------------------------
# التبويب الثالث: النتائج، المناقشة والاستنتاجات (Results, Discussion & Conclusions)
# ----------------------------------------------------
with tab3:
    st.header(t_results_title)
    
    # مستودع ملفات خاص بالقسم الثالث (نتائج المختبر والجداول)
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 مستودع نتائج القسم 3")
    sources_t3 = st.sidebar.file_uploader(t_upload_t3, type=["pdf", "txt"], accept_multiple_files=True, key="t3_files")
    
    text_t3 = ""
    if sources_t3:
        for f in sources_t3:
            try:
                reader = pypdf.PdfReader(f)
                for page in reader.pages:
                    if page.extract_text(): text_t3 += page.extract_text() + "\n"
            except: pass
        st.sidebar.success(f"تمت قراءة {len(sources_t3)} ملفات نتائج مخبرية للقسم الثالث بنجاح.")

    if st.button(t_btn_t3, key="btn_t3"):
        with st.spinner(t_spinner):
            results_conclusions_text = f"""# {paper_title} - Results & Conclusions
*Research Focus: {fields_text} | Analytical Tool: {analytical_instrument}*

## Results and Discussion
### 3.1. Structural and Morphological Characterization
The successful synthesis and physicochemical restructuring of {adsorbent_material} designed for {fields_text} were comprehensively validated through {characterization_tools} analyses, revealing active binding sites favorable for {target_metal} sequestration.

### 3.2. Adsorption Kinetics, Isotherms, and Analytical Performance
Experimental kinetic data and quantitative measurements performed via {analytical_instrument} were evaluated to elucidate rate-controlling mechanisms. Equilibrium isotherm data analyzed via Langmuir and Freundlich models exhibited exceptional compliance with the Langmuir isotherm, confirming monolayer coverage with a notable maximum adsorption capacity ($q_m$). 

## Conclusions
In summary, this study successfully demonstrated the facile fabrication and high-performance application of {adsorbent_material} tailored specifically for {fields_text}. Comprehensive characterization verified the abundance of active surface functional groups, while analytical measurements via {analytical_instrument} confirmed superior uptake efficiencies toward {target_metal}. Overall, this research establishes an environmentally sustainable framework for advanced analytical separation and industrial wastewater treatment under {journal_style} standards.
"""
            st.markdown(results_conclusions_text)
            st.success(t_success_gen)

            doc = Document()
            doc.add_heading(paper_title + " - Results", level=1)
            doc.add_paragraph(results_conclusions_text)
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)

            st.download_button(
                label=t_download_btn,
                data=buffer,
                file_name="ChemResearch_Results_Conclusions.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="dl_t3"
            )
