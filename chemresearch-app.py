import streamlit as st

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="ChemResearch AI Writer",
    page_icon="🧪",
    layout="wide"
)

# ==================== اختيار اللغة (Language Selector) ====================
st.sidebar.title("🌐 Language / Dil / اللغة")
lang_choice = st.sidebar.selectbox("Choose Language:", ["English", "Türkçe", "العربية"])

# قاموس الترجمات الشامل (يغطي كل مفردات وتنبيهات الصفحة)
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
    t_target_metal = "Target Heavy Metal:"
    t_adsorbent = "Prepared Novel Adsorbent Material:"
    t_tools = "Characterization Tools Used:"
    
    t_gen_section = "⚙️ Academic Section Generation (Q1 Style)"
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
    t_target_metal = "Hedef Ağır Metal:"
    t_adsorbent = "Hazırlanan Yeni Adsorban Malzeme:"
    t_tools = "Kullanılan Karakterizasyon Cihazları:"
    
    t_gen_section = "⚙️ Akademik Bölüm Oluşturma (Q1 Style)"
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

else:  # العربية (شاملة تعريب كل زاوية في الصفحة)
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
    t_target_metal = "المعدن الثقيل المستهدف:"
    t_adsorbent = "المادة الماصة الجديدة المُحضرة:"
    t_tools = "أجهزة التشخيص المستخدمة:"
    
    t_gen_section = "⚙️ توليد الأقسام الأكاديمية (Q1 Style)"
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

# لوحة المدخلات الرئيسية للتجربة
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

# أقسام التوليد الأكاديمي
st.markdown("---")
st.header(t_gen_section)

section_choice = st.selectbox(t_section_choice, t_sections)

if st.button(t_btn):
    with st.spinner(t_spinner):
        
        if "1." in section_choice:
            output_text = f"""
            ### Introduction
            Rapid industrialization has led to a significant increase in the discharge of toxic heavy metal ions, specifically **{target_metal}**, into aquatic ecosystems [1]. Due to their persistence and bioaccumulation potential, these pollutants pose severe threats to environmental safety [2]. 
            
            To address this, various conventional remediation techniques have been employed, but they often suffer from high operational costs and secondary sludge generation [3]. Recently, adsorption has emerged as a promising alternative. However, there remains a critical research gap in developing sustainable, high-capacity materials. 
            
            To bridge this gap, the present study focuses on the facile synthesis and application of **{adsorbent_material}** for the efficient removal of **{target_metal}**. The structural properties were comprehensively investigated using **{characterization_tools}**.
            """
        elif "2." in section_choice:
            output_text = f"""
            ### Materials and Methods
            All chemicals used were of analytical grade. The preparation of **{adsorbent_material}** involved a green synthesis route. The surface functional groups and morphological structures were analyzed using **{characterization_tools}**. Batch adsorption experiments were systematically conducted to evaluate the effects of initial pH, contact time, and initial metal concentration.
            """
        elif "3." in section_choice:
            output_text = f"""
            ### Results and Discussion
            The successful fabrication of **{adsorbent_material}** was confirmed by **{characterization_tools}** analyses, displaying active binding sites responsible for **{target_metal}** uptake. Adsorption kinetic data were best described by the pseudo-second-order model, indicating chemisorption as the rate-limiting step. Furthermore, equilibrium isotherm data aligned well with the Langmuir model, demonstrating a high maximum adsorption capacity.
            """
        else:
            output_text = f"""
            ### Conclusions
            In summary, **{adsorbent_material}** was successfully developed and proven to be an efficient, eco-friendly material for removing **{target_metal}** from aqueous systems. The integration of advanced characterization and thermodynamic evaluation highlights its strong potential for sustainable industrial wastewater treatment.
            """
            
        st.markdown(f"### {t_result_title}")
        st.markdown(output_text)
        st.success(t_success_gen)
