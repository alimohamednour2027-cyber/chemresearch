import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Optimization Parameters Hub",
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
    st.markdown("### Optimization Hub Navigation")
    st.caption("Active Hub: Dynamic Isolated Parameters & Contextual Q1 Synthesis")

# قاموس الترجمات والخيارات الشاملة
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Optimization Parameters Hub"
    t_desc = "Dynamic analytical module featuring fully expanded parameters for Adsorption, SPE/MSPE, and Environmental Removal."
    sec1_title = "1. Define Main Study System:"
    mode_label = "Select experiment type:"
    opt_modes = [
        "Adsorption (Surface capacity, thermodynamics & isotherms)",
        "SPE / MSPE (Solid-phase microextraction and preconcentration)",
        "Removal (Pollutant remediation, real wastewater & reusability)"
    ]
    sec2_title = "2. Enter Parameter Data & Quantitative Results:"
    
    ads_params = ["Initial Concentration (C0)", "Adsorbent Dosage", "Contact Time", "Solution Temperature", "Initial pH", "Ionic Strength"]
    spe_params = ["Eluent Type & Volume", "Sample Volume", "Extraction Time", "Sample pH", "Sorbent Amount", "Desorption Time"]
    rem_params = [
        "Initial Pollutant Concentration (C0)",
        "Adsorbent / Material Dosage",
        "Contact Time & Kinetic Evaluation",
        "Solution Temperature & Thermodynamics",
        "Initial pH Optimization",
        "Co-existing / Interfering Ions (Selectivity)",
        "Ionic Strength Effects",
        "Regeneration & Reusability Cycles",
        "Real Wastewater / Environmental Matrix Application",
        "Continuous Fixed-Bed Column Parameters"
    ]

    x_lbl = "Experimental Parameter Values (comma-separated):"
    y_lbl = "Resulting Performance Values:"
    opt_val_lbl = "Selected Optimum Point / Condition:"
    sec3_title = "3. Targeted Reference Tagging & Specific Notes"
    uploader_lbl = "Upload Reference Document (PDF / TXT):"
    ref_tag_lbl = "Reference Citation Tag (e.g., Smith et al., 2024):"
    notes_lbl = "Targeted Mechanistic Observation:"
    btn_generate = "Generate Dynamic Isolated Parameter Discussion (Q1 Style)"
    success_msg = "Dynamic parameter discussion successfully formulated."
    preview_title = "Contextually Adapted Discussion Paragraph:"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Optimizasyon Parametreleri Merkezi"
    t_desc = "Adsorpsiyon, SPE/MSPE ve Çevresel Giderim için tam genişletilmiş parametreler içeren dinamik analitik modül."
    sec1_title = "1. Ana Çalışma Sistemini Belirleyin:"
    mode_label = "Deney türünü seçin:"
    opt_modes = [
        "Adsorpsiyon (Yüzey kapasitesi, termodinamik ve izotermler)",
        "SPE / MSPE (Katı faz mikro ekstraksiyonu ve zenginleştirme)",
        "Giderim (Kirletici arıtımı, gerçek atıksu ve yeniden kullanılabilirlik)"
    ]
    sec2_title = "2. Parametre Verilerini ve Nicel Sonuçları Girin:"
    
    ads_params = ["Başlangıç Konsantrasyonu", "Adsorban Dozu", "Temas Süresi", "Sıcaklık", "Başlangıç pH", "İyonik Şiddet"]
    spe_params = ["Elüent Türü ve Hacmi", "Örnek Hacmi", "Ekstraksiyon Süresi", "Örnek pH", "Nanopartikül Miktarı", "Desorpsiyon Süresi"]
    rem_params = [
        "Başlangıç Kirletici Konsantrasyonu",
        "Adsorban / Malzeme Dozu",
        "Temas Süresi ve Kinetik",
        "Sıcaklık ve Termodinamik",
        "pH Optimizasyonu",
        "Birlikte Bulunan İyonlar",
        "İyonik Şiddet Etkileri",
        "Yeniden Kullanım Döngüleri",
        "Gerçek Atıksu Uygulaması",
        "Kolon Parametreleri"
    ]

    x_lbl = "Deneysel Parametre Değerleri (virgülle ayırın):"
    y_lbl = "Sonuç Performans Değerleri:"
    opt_val_lbl = "Seçilen Optimum Nokta / Koşul:"
    sec3_title = "3. Hedeflenen Referans İndeksleme ve Özel Notlar"
    uploader_lbl = "Referans Belgesi Yükleyin (PDF / Metin):"
    ref_tag_lbl = "Referans Etiketi (örn. Smith ve ark., 2024):"
    notes_lbl = "Mekanistik Gözlem:"
    btn_generate = "Dinamik İzole Parametre Tartışması Oluştur (Q1 Stili)"
    success_msg = "Parametre tartışması başarıyla hazırlandı."
    preview_title = "Tartışma Paragrafı:"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز تحسين المعلمات المتقدمة"
    t_desc = "وحدة تحليلية ديناميكية متقدمة تغطي المعلمات الشاملة للامتزاز، الاستخلاص، ومعالجة المياه البيئية، مع التكيف الفوري والمعزول لكل معلمة."
    sec1_title = "1. حدد نظام الدراسة الرئيسي:"
    mode_label = "اختر نوع التجربة لدراسة العوامل المؤثرة:"
    opt_modes = [
        "Adsorption (دراسات الامتزاز، الديناميكا الحرارية والسعة)",
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر ومعامل التبريز)",
        "Removal (دراسات إزالة الملوثات، المياه الحقيقية وإعادة الاستخدام)"
    ]
    sec2_title = "2. إدخال بيانات المعلمة والنتائج الكمية:"
    
    ads_params = [
        "Initial Concentration (C0) - تأثير التركيز الابتدائي للملوث", 
        "Adsorbent Dosage - تأثير جرعة المادة المازة", 
        "Contact Time - تأثير زمن التلامس والحركية", 
        "Solution Temperature - تأثير درجة الحرارة والطاقة الحرة", 
        "Initial pH of Solution - تأثير الحموضة الأولية والسطح", 
        "Ionic Strength - تأثير القوة الأيونية والأملاح"
    ]
    
    spe_params = [
        "Eluent Type & Volume - نوع وحجم مذيب الاستشطيف", 
        "Sample Volume - حجم عينة التحميل ومعامل التبريز", 
        "Extraction Time - زمن استخلاص وتوازن الطور", 
        "Sample pH - أس هيدروجيني العينة", 
        "Sorbent Amount - كمية المادة الحاملة النانوية", 
        "Desorption Time - زمن وسرعة التحرير"
    ]
    
    rem_params = [
        "Initial Pollutant Concentration (C0) - تركيز الملوث الابتدائي",
        "Adsorbent / Material Dosage - جرعة المادة المعالجة",
        "Contact Time & Kinetic Evaluation - زمن التلامس وحركية الإزالة",
        "Solution Temperature & Thermodynamics - تأثير درجة الحرارة والثرموديناميكا",
        "Initial pH Optimization - تحسين الأس الهيدروجيني الأولي",
        "Co-existing Ions (Selectivity) - تأثير الأيونات المتنافسة والمنافسة",
        "Ionic Strength Effects - تأثير القوة الأيونية",
        "Regeneration & Reusability Cycles - دورات الاستعادة وإعادة الاستخدام",
        "Real Wastewater Application - تطبيق عينات المياه الحقيقية والصرف",
        "Fixed-Bed Column Parameters - معلمات أعمدة الثابت المستمرة"
    ]

    x_lbl = "قيم المعامل التجريبية المدروسة (افصل بينها بفاصلة):"
    y_lbl = "القيم الناتجة بدقة (السعة / الاسترداد / الإزالة %):"
    opt_val_lbl = "القيمة أو النقطة المثلى المحددة (Optimum Condition):"
    sec3_title = "3. الفهرسة المرجعية المخصصة والملاحظات الدقيقة"
    uploader_lbl = "رفع المرجع الخاص بهذه المعلمة فقط (PDF / TXT):"
    ref_tag_lbl = "معرّف المرجع المفهرس (مثل: Ref [1] - Smith et al.):"
    notes_lbl = "الملاحظة الميكانيكية أو التحليل المستخلص من هذا المرجع:"
    btn_generate = "توليد مناقشة ديناميكية ومعزولة لـ Q1 (مخصصة للمعلمة المختارة)"
    success_msg = "تم توليد المناقشة العلمية المتكيّفة والمخصصة لهذه المعلمة بنجاح!"
    preview_title = "مسودة فقرة المناقشة الديناميكية (Context-Specific Parameter Discussion):"

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# --- اختيار نظام الدراسة ---
st.markdown(f"### {sec1_title}")
study_mode = st.selectbox(mode_label, opt_modes)

st.markdown("---")
raw_mode_key = study_mode.split(' ')[0]
st.markdown(f"### {sec2_title} [{raw_mode_key}]")

col1, col2 = st.columns(2)

if "Adsorption" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", ads_params)
    with col2:
        x_values = st.text_input(x_lbl, value="10, 25, 50, 100, 200 mg/L")
        opt_val = st.text_input(opt_val_lbl, value="100 mg/L (Saturation threshold)")
    y_values = st.text_input(y_lbl, value="12.5, 24.1, 45.2, 68.5, 72.0 mg/g")

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", spe_params)
    with col2:
        x_values = st.text_input(x_lbl, value="0.5, 1.0, 2.0, 5.0 mL")
        opt_val = st.text_input(opt_val_lbl, value="2.0 mL (Quantitative recovery)")
    y_values = st.text_input(y_lbl, value="82.4, 98.5, 94.1, 88.0 % Recovery")

else:  # Removal
    with col1:
        param_type = st.selectbox("Select Parameter:", rem_params)
    with col2:
        x_values = st.text_input(x_lbl, value="5, 10, 25, 50, 100 mg/L")
        opt_val = st.text_input(opt_val_lbl, value="25 mg/L initial loading")
    y_values = st.text_input(y_lbl, value="35.0, 62.5, 96.8, 85.0, 68.2 % Removal")

# --- رفع المرجع والفهرسة ---
st.markdown("---")
st.markdown(f"### {sec3_title}")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    param_ref_file = st.file_uploader(uploader_lbl, type=["pdf", "txt"], key="param_specific_ref")
with col_ref2:
    ref_citation_tag = st.text_input(ref_tag_lbl, value="Ref. [1] (Smith et al., 2024)")

chem_notes = st.text_area(notes_lbl, placeholder="e.g., This specific reference confirms the unique mechanistic trend...", key="param_specific_notes")

# --- محرك الصياغة الديناميكي ---
if st.button(btn_generate, key="btn_optimization"):
    st.success(success_msg)
    st.markdown(f"### {preview_title}")
    
    dynamic_text = f"**Dynamic Mechanistic Analysis for {param_type}:** Evaluated across the experimental range ({x_values}) against performance metrics ({y_values}), identifying the critical operational threshold at **{opt_val}**. Supported by **{ref_citation_tag}**, this parameter dictates interfacial mass transfer and thermodynamic behavior. Note: {chem_notes if chem_notes else 'Standard analytical reproducibility confirmed in accordance with Q1 literature.'}"
    
    st.info(dynamic_text)
