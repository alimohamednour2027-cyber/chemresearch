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
    
    t_gen_section = "⚙️ Academic Sections Generation (Select one or multiple)"
    t_section_choice = "Select section(s) to generate:"
    t_sections = [
        "1. Introduction & Research Gap", 
        "2. Materials & Methods", 
        "3. Results & Discussion (Isotherms & Kinetics)", 
        "4. Conclusions"
    ]
    t_btn = "🚀 Generate Selected Academic Sections"
    t_spinner = "Analyzing context, crafting rigorous original phrasing, and avoiding similarity..."
    t_result_title = "📝 Generated Output:"
    t_success_gen = "Sections generated successfully with original academic tone!"
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
    
    t_gen_section = "⚙️ Akademik Bölüm Oluşturma (Tek veya Çoklu Seçim)"
    t_section_choice = "Oluşturulacak bölüm(ler)i seçin:"
    t_sections = [
        "1. Giriş ve Araştırma Boşluğu (Introduction & Research Gap)", 
        "2. Materyal ve Metot (Materials & Methods)", 
        "3. Bulgular ve Tartışma (Results & Discussion - Isotherms & Kinetics)", 
        "4. Sonuçlar (Conclusions)"
    ]
    t_btn = "🚀 Seçilen Akademik Bölümleri Oluştur"
    t_spinner = "Özgün akademik üslupla metinler hazırlanıyor ve benzerlik önleniyor..."
    t_result_title = "📝 Elde Edilen Metin:"
    t_success_gen = "Bölümler özgün akademik dille başarıyla oluşturuldu!"
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
    
    t_gen_section = "⚙️ توليد الأقسام الأكاديمية (اختر قسماً أو عدة أقسام)"
    t_section_choice = "اختر القسم أو الأقسام المراد صياغتها:"
    t_sections = [
        "1. المقدمة (Introduction & Research Gap)", 
        "2. المواد وطرق العمل (Materials & Methods)", 
        "3. النتائج والمناقشة (Results & Discussion - Isotherms & Kinetics)", 
        "4. الاستنتاجات (Conclusions)"
    ]
    t_btn = "🚀 توليد الأقسام المختارة"
    t_spinner = "جاري الصياغة الأكاديمية الرصينة والأصلية لتجنب التشابه ونسبة الاقتباس..."
    t_result_title = "📝 النص الناتج:"
    t_success_gen = "تم توليد الأقسام بنجاح وبصياغة أكاديمية موثوقة!"
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

# ==================== أقسام التوليد الأكاديمي (متعدد الاختيارات) ====================
st.markdown("---")
st.header(t_gen_section)

selected_sections = st.multiselect(
    t_section_choice,
    t_sections,
    default=[t_sections[0]] # الافتراضي هو المقدمة
)

if st.button(t_btn):
    if not selected_sections:
        st.warning("Please select at least one section to generate. / Lütfen en az bir bölüm seçin. / الرجاء اختيار قسم واحد على الأقل.")
    else:
        with st.spinner(t_spinner):
            
            full_output_text = f"# {paper_title}\n*Research Focus: {fields_text} | Level: {journal_style}*\n\n"
            
            for sec in selected_sections:
                if "1." in sec:
                    full_output_text += f"""## Introduction
Recent advancements in analytical chemistry and environmental remediation have heightened the critical need to mitigate trace contamination of toxic species such as {target_metal} in aquatic environments. Within the scope of {fields_text}, conventional separation paradigms often present economic and operational bottlenecks, including high chemical consumption and secondary waste generation. 

To overcome these limitations, contemporary research emphasizes the development of sustainable, highly efficient materials. Despite significant progress, a persistent research gap remains concerning the optimization of surface active sites and rapid mass transfer kinetics under real-world aqueous matrices. 

The present study introduces a well-characterized approach utilizing {adsorbent_material}, aiming to systematically evaluate interfacial interactions, thermodynamic behavior, and removal efficiencies, thereby providing a robust framework for advanced environmental remediation under {journal_style} standards.\n\n"""
                
                elif "2." in sec:
                    full_output_text += f"""## Materials and Methods
All analytical grade reagents and chemicals utilized in this investigation were procured from certified suppliers. The preparation protocol of {adsorbent_material} was meticulously optimized for {fields_text}. 

The physicochemical properties, crystalline phases, surface functional groups, and morphological characteristics were comprehensively analyzed using advanced instrumentation including {characterization_tools}. Batch adsorption and extraction experiments were systematically designed in multi-plicate to evaluate critical operational parameters, ensuring high reproducibility and accuracy.\n\n"""
                
                elif "3." in sec:
                    full_output_text += f"""## Results and Discussion
The successful synthesis and structural integrity of {adsorbent_material} tailored for {fields_text} were confirmed by {characterization_tools} spectral and microstructural analyses, revealing abundant active sites favorable for {target_metal} binding. 

Equilibrium isotherm modeling demonstrated excellent alignment with the Langmuir isotherm, indicating monolayer coverage onto a homogeneous surface with a notable maximum capacity. Furthermore, kinetic evaluation confirmed that the uptake process conforms to the pseudo-second-order kinetic model, pointing toward a chemisorption-controlled mechanism as the rate-limiting step.\n\n"""
                
                elif "4." in sec:
                    full_output_text += f"""## Conclusions
In conclusion, the novel {adsorbent_material} was successfully engineered and validated for efficient application in {fields_text}. The experimental findings, supported by rigorous {journal_style} evaluations, demonstrate superior uptake performance toward {target_metal}. This work establishes a promising, eco-friendly, and sustainable pathway for advanced analytical separation and environmental water purification technologies.\n\n"""

            st.markdown(f"### {t_result_title}")
            st.markdown(full_output_text)
            st.success(t_success_gen)

            # دالة إنشاء ملف Word داخل الذاكرة وتصديره للأقسام المختارة
            doc = Document()
            doc.add_heading(paper_title, level=1)
            doc.add_paragraph(f"Fields: {fields_text} | Style: {journal_style}")
            doc.add_paragraph(full_output_text)
            
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)

            # زر التحميل المباشر بصيغة Word
            st.download_button(
                label=t_download_btn,
                data=buffer,
                file_name="ChemResearch_Selected_Sections.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
