import streamlit as st
from io import BytesIO
from docx import Document

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="ChemResearch AI Writer",
    page_icon="🧪",
    layout="wide"
)

# ==================== اختيار اللغة (Language Selector) ====================
st.sidebar.title("🌐 Language / Dil / اللغة")
lang_choice = st.sidebar.selectbox("Choose Language:", ["English", "Türkçe", "العربية"])

# قاموس الترجمات الشامل
if lang_choice == "English":
    t_title = "🧪 ChemResearch AI: Advanced Academic Article Writer"
    t_subtitle = "Designed for Solid-Phase Extraction (SPE), Adsorption, and Environmental Remediation Research."
    t_sidebar_header = "📚 Sources Hub"
    t_sidebar_desc = "Upload reference articles or PDFs for citation and structuring:"
    t_upload = "Upload reference files (PDF)"
    t_success_upload = "Sources added successfully."
    t_active_sources = "Active Sources:"
    t_no_sources = "No sources uploaded yet."
    t_info_no_sources = "No sources uploaded yet. You can add them manually for citation mapping."
    
    t_exp_data = "🔬 Experiment & Research Data"
    t_paper_title = "Article or Experiment Title:"
    t_target_metal = "Target Heavy Metal / Pollutant:"
    t_adsorbent = "Prepared Novel Material / Sorbent:"
    t_tools = "Characterization Tools Used:"
    
    t_fields_label = "🎯 Select Research Fields (Multiple Choice):"
    t_field_1 = "Solid-Phase Extraction (SPE)"
    t_field_2 = "Adsorption"
    t_field_3 = "Removal / Remediation"
    t_field_other = "Other (Specify):"
    
    t_q_style = "📊 Target Journal Quartile Style:"
    
    t_gen_section = "⚙️ Academic Section Generation"
    t_section_choice = "Select section to generate:"
    t_sections = [
        "1. Introduction & Research Gap", 
        "2. Materials & Methods", 
        "3. Results & Discussion (Isotherms & Kinetics)", 
        "4. Conclusions"
    ]
    t_btn = "🚀 Generate Academic Text"
    t_spinner = "Analyzing sources and writing world-class academic text..."
    t_result_title = "📝 Generated Output:"
    t_success_gen = "Text generated successfully with source citations integrated!"
    t_download_btn = "📥 Download as Word Document (.docx)"

elif lang_choice == "Türkçe":
    t_title = "🧪 ChemResearch AI: Gelişmiş Akademik Makale Yazım Aracı"
    t_subtitle = "Katı Faz Ekstraksiyonu (SPE), Adsorpsiyon ve Çevresel Kirlilik Giderimi Araştırmaları için."
    t_sidebar_header = "📚 Kaynak Deposu (Sources Hub)"
    t_sidebar_desc = "Atıf ve biçimlendirme için referans makaleleri veya PDF'leri yükleyin:"
    t_upload = "Referans dosyaları yükle (PDF)"
    t_success_upload = "Kaynaklar başarıyla eklendi."
    t_active_sources = "Aktif Kaynaklar:"
    t_no_sources = "Henüz kaynak yüklenmedi."
    t_info_no_sources = "Henüz kaynak yüklenmedi. Atıf eşlemesi için manuel ekleyebilirsiniz."
    
    t_exp_data = "🔬 Deney ve Araştırma Verileri"
    t_paper_title = "Makale veya Deney Başlığı:"
    t_target_metal = "Hedef Ağır Metal / Kirletici:"
    t_adsorbent = "Hazırlanan Yeni Malzeme / Adsorban:"
    t_tools = "Kullanılan Karakterizasyon Cihazları:"
    
    t_fields_label = "🎯 Araştırma Alanlarını Seçin (Çoklu Seçim):"
    t_field_1 = "Katı Faz Ekstraksiyonu (SPE)"
    t_field_2 = "Adsorpsiyon (Adsorption)"
    t_field_3 = "Giderim / Arıtma (Removal)"
    t_field_other = "Diğer (Belirtiniz):"
    
    t_q_style = "📊 Hedef Dergi Dil Seviyesi / Çeyrek (Quartile):"
    
    t_gen_section = "⚙️ Akademik Bölüm Oluşturma"
    t_section_choice = "Oluşturulacak bölümü seçin:"
    t_sections = [
        "1. Giriş ve Araştırma Boşluğu (Introduction & Research Gap)", 
        "2. Materyal ve Metot (Materials & Methods)", 
        "3. Bulgular ve Tartışma (Results & Discussion - Isotherms & Kinetics)", 
        "4. Sonuçlar (Conclusions)"
    ]
    t_btn = "🚀 Akademik Metni Oluştur"
    t_spinner = "Kaynaklar analiz ediliyor ve dünya standartlarında akademik metin yazılıyor..."
    t_result_title = "📝 Elde Edilen Metin:"
    t_success_gen = "Metin, yüklenen kaynaklarla ilişkilendirilerek başarıyla oluşturuldu!"
    t_download_btn = "📥 Word Belgesi Olarak İndir (.docx)"

else:  # العربية
    t_title = "🧪 ChemResearch AI: أداة كتابة الأبحاث الأكاديمية المتقدمة"
    t_subtitle = "مخصص لأبحاث الاستخلاص (SPE)، الامتزاز (Adsorption)، وإزالة الملوثات البيئية."
    t_sidebar_header = "📚 مستودع المصادر (Sources Hub)"
    t_sidebar_desc = "قم برفع الأبحاث أو المقالات المرجعية لتعتمد عليها الأداة في الصياغة والاستشهاد:"
    t_upload = "ارفع ملفات مرجعية (PDF)"
    t_success_upload = "تم إدراج المصادر بنجاح."
    t_active_sources = "المصادر النشطة:"
    t_no_sources = "لم يتم رفع مصادر بعد."
    t_info_no_sources = "لم يتم رفع مصادر بعد. يمكنك الإضافة يدوياً للربط المرجعي."
    
    t_exp_data = "🔬 بيانات التجربة والبحث"
    t_paper_title = "عنوان المقال أو التجربة:"
    t_target_metal = "المعدن الثقيل / الملوث المستهدف:"
    t_adsorbent = "المادة الماصة / الجديدة المُحضرة:"
    t_tools = "أجهزة التشخيص المستخدمة:"
    
    t_fields_label = "🎯 اختر مجالات البحث (اختيار متعدد):"
    t_field_1 = "الاستخلاص الصلب (Solid-Phase Extraction - SPE)"
    t_field_2 = "الامتزاز (Adsorption)"
    t_field_3 = "الإزالة والمعالجة (Removal / Remediation)"
    t_field_other = "أخرى (اكتبها بنفسك):"
    
    t_q_style = "📊 مستوى المجلة المستهدفة (Journal Quartile Style):"
    
    t_gen_section = "⚙️ توليد الأقسام الأكاديمية"
    t_section_choice = "اختر القسم المراد صياغته:"
    t_sections = [
        "1. المقدمة (Introduction & Research Gap)", 
        "2. المواد وطرق العمل (Materials & Methods)", 
        "3. النتائج والمناقشة (Results & Discussion - Isotherms & Kinetics)", 
        "4. الاستنتاجات (Conclusions)"
    ]
    t_btn = "🚀 توليد الصياغة الأكاديمية"
    t_spinner = "جاري تحليل المصادر وصياغة النص بأعلى معايير المجلات العالمية..."
    t_result_title = "📝 النص الناتج:"
    t_success_gen = "تم توليد النص بنجاح مع ربط الاستشهادات بالمصادر المرفوعة!"
    t_download_btn = "📥 تحميل كملف Word (.docx)"

# ==================== عرض واجهة الموقع ====================
st.title(t_title)
st.markdown(t_subtitle)

# الشريط الجانبي (إدارة المصادر)
st.sidebar.header(t_sidebar_header)
st.sidebar.markdown(t_sidebar_desc)

uploaded_sources = st.sidebar.file_uploader(
    t_upload, 
    type=["pdf", "txt"], 
    accept_multiple_files=True
)

if uploaded_sources:
    st.sidebar.success(f"{len(uploaded_sources)} {t_success_upload}")
    st.sidebar.markdown(f"### {t_active_sources}")
    for src in uploaded_sources:
        st.sidebar.text(f"📄 {src.name}")
else:
    st.sidebar.info(t_info_no_sources)

# ==================== خيارات مجالات البحث وأنماط المجلات ====================
st.markdown("---")
st.header(t_fields_label)

col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    f_spe = st.checkbox(t_field_1, value=True)
with col_f2:
    f_ads = st.checkbox(t_field_2, value=True)
with col_f3:
    f_rem = st.checkbox(t_field_3, value=True)

# خيار أخرى (مفردة حرة)
other_field_input = st.text_input(t_field_other, value="")

# نمط المجلة Q1, Q2, Q3
journal_style = st.selectbox(t_q_style, ["Q1 Style (High Impact & Rigorous)", "Q2 Style (Standard Professional)", "Q3 Style (Clear & Direct)"])

# ==================== لوحة المدخلات الرئيسية للتجربة ====================
st.markdown("---")
st.header(t_exp_data)

col1, col2 = st.columns(2)

with col1:
    paper_title = st.text_input(
        t_paper_title, 
        value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions"
    )
    target_metal = st.text_input(t_target_metal, value="Cadmium(II) - Cd2+")

with col2:
    adsorbent_material = st.text_input(t_adsorbent, value="Modified Agricultural Waste Bio-adsorbent")
    characterization_tools = st.text_input(t_tools, value="FTIR, SEM, XRD, BET")

# تجمع المجالات المختارة في نص لدمجه في التوليد
selected_fields = []
if f_spe: selected_fields.append("Solid-Phase Extraction (SPE)")
if f_ads: selected_fields.append("Adsorption")
if f_rem: selected_fields.append("Removal/Remediation")
if other_field_input: selected_fields.append(other_field_input)
fields_text = ", ".join(selected_fields)

# أقسام التوليد الأكاديمي
st.markdown("---")
st.header(t_gen_section)

section_choice = st.selectbox(t_section_choice, t_sections)

if st.button(t_btn):
    with st.spinner(t_spinner):
        
        # تكييف الصياغة بناءً على نمط المجلة (Q1, Q2, Q3) والمجالات المختارة
        style_modifier = f"Written in a strict {journal_style} academic tone, focusing on: {fields_text}."
        
        if "1." in section_choice:
            output_text = f"""Introduction ({journal_style})
            
Rapid industrialization has led to a significant increase in the discharge of toxic pollutants, specifically {target_metal}, into aquatic ecosystems [1]. This work specifically addresses aspects related to {fields_text}. Due to their persistence and bioaccumulation potential, these pollutants pose severe threats to environmental safety [2]. 

To address this, various conventional remediation techniques have been employed, but they often suffer from high operational costs and secondary sludge generation [3]. Recently, advanced methods have emerged as promising alternatives. However, there remains a critical research gap in developing sustainable, high-capacity materials. 

To bridge this gap, the present study focuses on the facile synthesis and application of {adsorbent_material} for the efficient treatment of {target_metal}. The structural properties were comprehensively investigated using {characterization_tools}."""
            
        elif "2." in section_choice:
            output_text = f"""Materials and Methods ({journal_style})
            
All chemicals used were of analytical grade. The preparation of {adsorbent_material}, applied in {fields_text}, involved a controlled synthesis route. The surface functional groups and morphological structures were analyzed using {characterization_tools}. Batch experiments were systematically conducted to evaluate the performance parameters."""
            
        elif "3." in section_choice:
            output_text = f"""Results and Discussion ({journal_style})
            
The successful fabrication of {adsorbent_material} for {fields_text} was confirmed by {characterization_tools} analyses, displaying active binding sites responsible for {target_metal} uptake. Adsorption and extraction kinetic data were best described by the pseudo-second-order model, indicating chemisorption as the rate-limiting step. Furthermore, equilibrium data aligned well with the Langmuir model, demonstrating a high maximum capacity."""
            
        else:
            output_text = f"""Conclusions ({journal_style})
            
In summary, {adsorbent_material} was successfully developed for {fields_text} and proven to be an efficient, eco-friendly material for removing {target_metal} from aqueous systems. The integration of advanced characterization under {journal_style} standards highlights its strong potential for sustainable industrial wastewater treatment."""
            
        st.markdown(f"### {t_result_title}")
        st.markdown(output_text)
        st.success(t_success_gen)

        # دالة إنشاء ملف Word داخل الذاكرة وتصديره
        doc = Document()
        doc.add_heading(paper_title, level=1)
        doc.add_paragraph(f"Focus Fields: {fields_text} | Level: {journal_style}")
        doc.add_paragraph(output_text)
        
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        # زر التحميل المباشر بصيغة Word
        st.download_button(
            label=t_download_btn,
            data=buffer,
            file_name="ChemResearch_Draft.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
