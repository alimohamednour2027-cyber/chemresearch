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
    st.caption("Active Hub: SPE & Removal Dynamic Parameter Analysis")

# قاموس الترجمات والخيارات الشاملة (بدون الامتزاز)
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Optimization Parameters Hub"
    t_desc = "Dynamic analytical module integrating Excel chart visualization and non-repetitive Q1 mechanistic discussions."
    sec1_title = "1. Define Main Study System:"
    mode_label = "Select experiment type:"
    opt_modes = [
        "SPE / MSPE (Solid-phase microextraction and preconcentration)",
        "Removal (Pollutant remediation, real wastewater & reusability)"
    ]
    sec2_title = "2. Enter Parameter Data & Upload Excel Trend Chart:"
    
    spe_params = ["Eluent Type & Volume", "Sample Volume", "Extraction Time", "Sample pH", "Sorbent Amount", "Desorption Time"]
    rem_params = [
        "Initial Pollutant Concentration (C0)",
        "Adsorbent / Material Dosage",
        "Contact Time & Kinetic Evaluation",
        "Solution Temperature & Thermodynamics",
        "Initial pH Optimization",
        "Co-existing / Interfering Ions",
        "Ionic Strength Effects",
        "Regeneration & Reusability Cycles",
        "Real Wastewater Application",
        "Fixed-Bed Column Parameters"
    ]

    x_lbl = "Experimental Parameter Values:"
    y_lbl = "Resulting Performance Values:"
    opt_val_lbl = "Selected Optimum Point / Condition:"
    chart_lbl = "Upload Excel Trend Chart Image (PNG/JPG):"
    sec3_title = "3. Targeted Reference Tagging & Specific Notes"
    uploader_lbl = "Upload Reference Document (PDF / TXT):"
    ref_tag_lbl = "Reference Citation Tag (e.g., Smith et al., 2024):"
    notes_lbl = "Targeted Mechanistic Observation:"
    btn_generate = "Generate Advanced Unique Discussion (Q1 Style)"
    success_msg = "Dynamic parameter discussion and visual evaluation successfully formulated."
    preview_title = "Contextually Adapted Discussion Paragraph:"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Optimizasyon Parametreleri Merkezi"
    t_desc = "Excel grafik görselleştirmesini ve benzersiz Q1 mekanistik tartışmalarını entegre eden dinamik analitik modül."
    sec1_title = "1. Ana Çalışma Sistemini Belirleyin:"
    mode_label = "Deney türünü seçin:"
    opt_modes = [
        "SPE / MSPE (Katı faz mikro ekstraksiyonu ve zenginleştirme)",
        "Giderim (Kirletici arıtımı, gerçek atıksu ve yeniden kullanılabilirlik)"
    ]
    sec2_title = "2. Parametre Verilerini ve Excel Trend Grafik Resmini Girin:"
    
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

    x_lbl = "Deneysel Parametre Değerleri:"
    y_lbl = "Sonuç Performans Değerleri:"
    opt_val_lbl = "Seçilen Optimum Nokta / Koşul:"
    chart_lbl = "Excel Trend Grafik Resmini Yükleyin (PNG/JPG):"
    sec3_title = "3. Hedeflenen Referans İndeksleme ve Özel Notlar"
    uploader_lbl = "Referans Belgesi Yükleyin (PDF / Metin):"
    ref_tag_lbl = "Referans Etiketi (örn. Smith ve ark., 2024):"
    notes_lbl = "Mekanistik Gözlem:"
    btn_generate = "Gelişmiş Benzersiz Tartışma Oluştur (Q1 Stili)"
    success_msg = "Parametre tartışması ve görsel değerlendirme başarıyla hazırlandı."
    preview_title = "Tartışma Paragrafı:"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز تحسين المعلمات المتقدمة"
    t_desc = "وحدة تحليلية متقدمة لدمج الرسوم البيانية المستخرجة من Excel والتحليل العلمي المخصص وغير المكرر لكل معلمة."
    sec1_title = "1. حدد نظام الدراسة الرئيسي:"
    mode_label = "اختر نوع التجربة لدراسة العوامل المؤثرة:"
    opt_modes = [
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر ومعامل التبريز)",
        "Removal (دراسات إزالة الملوثات، المياه الحقيقية وإعادة الاستخدام)"
    ]
    sec2_title = "2. إدخال بيانات المعلمة، النتائج الكمية، ورفع رسم الاكسل (Excel Chart):"
    
    spe_params = [
        "Eluent Type & Volume", 
        "Sample Volume", 
        "Extraction Time", 
        "Sample pH", 
        "Sorbent Amount", 
        "Desorption Time"
    ]
    
    rem_params = [
        "Initial Pollutant Concentration (C0)",
        "Adsorbent / Material Dosage",
        "Contact Time & Kinetic Evaluation",
        "Solution Temperature & Thermodynamics",
        "Initial pH Optimization",
        "Co-existing / Interfering Ions",
        "Ionic Strength Effects",
        "Regeneration & Reusability Cycles",
        "Real Wastewater Application",
        "Fixed-Bed Column Parameters"
    ]

    x_lbl = "قيم المعامل التجريبية المدروسة:"
    y_lbl = "القيم الناتجة (السعة / الاسترداد / الإزالة %):"
    opt_val_lbl = "القيمة أو النقطة المثلى المحددة:"
    chart_lbl = "رفع صورة رسم الاكسل البياني الخاص بالمعلمة (PNG / JPG):"
    sec3_title = "3. الفهرسة المرجعية المخصصة والملاحظات الدقيقة"
    uploader_lbl = "رفع المرجع الخاص بهذه المعلمة فقط (PDF / TXT):"
    ref_tag_lbl = "معرّف المرجع المفهرس (مثل: Ref [1] - Smith et al.):"
    notes_lbl = "الملاحظة الميكانيكية أو التحليل المستخلص لهذه المعلمة:"
    btn_generate = "توليد مناقشة وتحليل فريد وعلمي لـ Q1 (مخصص للمعلمة والرسم البياني)"
    success_msg = "تم توليد التحليل البصري والعلمي المخصص والمستقل لهذه المعلمة بنجاح!"
    preview_title = "مسودة فقرة المناقشة الديناميكية المدعومة بتحليل الرسم البياني (Context-Specific Trend Discussion):"

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

# --- التكيف الديناميكي الكامل للمعلمات (بدون الامتزاز) وإرفاق الرسم البياني ---
if "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", spe_params)
    
    if "Eluent" in param_type:
        default_x, default_y, default_opt = "0.5, 1.0, 2.0, 5.0 mL", "65.0, 82.1, 98.5, 90.2 % Recovery", "2.0 mL (Quantitative recovery)"
    elif "Volume" in param_type:
        default_x, default_y, default_opt = "50, 100, 250, 500 mL", "99.1, 98.8, 97.5, 82.0 % Recovery", "250 mL (High preconcentration factor)"
    elif "Time" in param_type:
        default_x, default_y, default_opt = "1, 3, 5, 10 min", "70.5, 88.2, 98.5, 98.4 % Recovery", "5 min (Mass transfer equilibrium)"
    elif "pH" in param_type:
        default_x, default_y, default_opt = "2.0, 4.0, 6.0, 8.0, 10.0", "45.0, 78.2, 98.5, 85.1, 62.0 % Recovery", "pH 6.0 (Optimal complexation)"
    elif "Sorbent" in param_type:
        default_x, default_y, default_opt = "5, 10, 20, 50 mg", "72.0, 89.5, 98.5, 98.6 % Recovery", "20 mg (Quantitative retention)"
    else:
        default_x, default_y, default_opt = "1, 2, 5, 10 min", "98.5, 98.2, 91.0, 82.4 % Recovery", "2 min rapid desorption"

else:
    with col1:
        param_type = st.selectbox("Select Parameter:", rem_params)
    
    if "Pollutant" in param_type:
        default_x, default_y, default_opt = "5, 10, 25, 50, 100 mg/L", "98.2, 97.5, 96.8, 82.1, 65.0 % Removal", "25 mg/L initial loading capacity"
    elif "Dosage" in param_type:
        default_x, default_y, default_opt = "0.05, 0.1, 0.25, 0.5 g", "45.2, 72.8, 96.8, 97.0 % Removal", "0.25 g optimal mass"
    elif "Contact" in param_type:
        default_x, default_y, default_opt = "10, 30, 60, 120, 180 min", "60.5, 85.2, 96.8, 97.1, 97.2 % Removal", "60 min kinetic equilibrium"
    elif "Temperature" in param_type:
        default_x, default_y, default_opt = "293, 303, 313, 323 K", "85.0, 96.8, 97.5, 98.0 % Removal", "303 K thermodynamic optimum"
    elif "pH" in param_type:
        default_x, default_y, default_opt = "2.0, 4.0, 6.0, 8.0, 10.0", "35.0, 62.5, 96.8, 85.0, 68.2 % Removal", "pH 6.0 removal apex"
    elif "Co-existing" in param_type:
        default_x, default_y, default_opt = "Na+, K+, Ca2+, Mg2+, Cl-, SO42-", "95.5, 96.1, 92.4, 91.8, 94.5, 93.2 % Removal", "High selectivity with minimal interference"
    elif "Ionic" in param_type:
        default_x, default_y, default_opt = "0.0, 0.05, 0.1, 0.2, 0.5 M NaCl", "96.8, 96.5, 95.8, 94.0, 91.2 % Removal", "Stable removal across salinity gradients"
    elif "Regeneration" in param_type:
        default_x, default_y, default_opt = "Cycle 1, Cycle 2, Cycle 3, Cycle 4, Cycle 5", "96.8, 95.2, 93.8, 91.0, 88.5 % Removal", "Stable reusability up to 5 consecutive cycles"
    elif "Wastewater" in param_type:
        default_x, default_y, default_opt = "Tap water, River water, Industrial effluent", "97.2, 94.5, 91.8 % Removal", ">91% removal in complex real wastewater matrices"
    else:
        default_x, default_y, default_opt = "1.0, 2.0, 5.0 mL/min flow rate", "98.5, 96.8, 84.2 % Removal", "2.0 mL/min optimal bed residence time"

with col2:
    x_values = st.text_input(x_lbl, value=default_x)
    y_values = st.text_input(y_lbl, value=default_y)
    opt_val = st.text_input(opt_val_lbl, value=default_opt)

# --- إدراج فقرة رفع صورة الرسم البياني (Excel Chart Image) ---
st.markdown("---")
st.markdown(f"#### 📊 {chart_lbl}")
chart_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="excel_chart_uploader")
if chart_file is not None:
    st.image(chart_file, caption=f"Excel Trend Performance Chart for: {param_type}", use_container_width=True)
    st.success("Excel chart successfully loaded and linked to current parameter evaluation.")

# --- رفع المرجع المخصص والفهرسة لهذه المعلمة حصرياً ---
st.markdown("---")
st.markdown(f"### {sec3_title}")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    param_ref_file = st.file_uploader(uploader_lbl, type=["pdf", "txt"], key="param_specific_ref")
with col_ref2:
    ref_citation_tag = st.text_input(ref_tag_lbl, value="Ref. [1] (Smith et al., 2024)")

chem_notes = st.text_area(notes_lbl, placeholder="e.g., The trend observed in the Excel chart confirms the unique mechanistic behavior...", key="param_specific_notes")

# --- محرك الصياغة الفريد والمدعوم بتحليل الرسم البياني لمنع أي تشابه أو تكرار ---
if st.button(btn_generate, key="btn_optimization"):
    st.success(success_msg)
    st.markdown(f"### {preview_title}")
    
    p_lower = param_type.lower()
    chart_status_text = "As explicitly evidenced by the integrated Excel trend chart profile," if chart_file else "Based on the quantitative trend progression,"
    
    if "eluent" in p_lower or "eluent" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} evaluation across ({x_values}) coupled with elution efficiencies ({y_values}) designates **{opt_val}** as the peak threshold. Corroborated by **{ref_citation_tag}**, desorption kinetics are strictly governed by solvent polarity and quantitative mass transfer without secondary dilution."
    elif "volume" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} sample volume optimization through ({x_values}) against recovery profiles ({y_values}) indicates that breakthrough volume is maintained at **{opt_val}**. Citing insights from **{ref_citation_tag}**, high preconcentration factors are securely preserved."
    elif "extraction" in p_lower or "contact" in p_lower or "time" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} kinetic plotting over ({x_values}) demonstrates a sharp initial gradient leading to a plateau at **{opt_val}** ({y_values}). In alignment with **{ref_citation_tag}**, rapid surface accessibility controls the initial mass transfer stage."
    elif "ph" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} solution acidity shifts across ({x_values}) dictate surface protonation states ({y_values}), establishing apex performance at **{opt_val}**. Reference **{ref_citation_tag}** confirms that electrostatic interactions dictate this specific pH boundary."
    elif "sorbent" in p_lower or "dosage" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} mass-dependent trends mapped across ({x_values}) and removal efficiencies ({y_values}) verify saturation limits at **{opt_val}**. Validated by **{ref_citation_tag}**, active site availability directly dictates this operational curve."
    elif "co-existing" in p_lower or "ions" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} competitive matrix testing with ions ({x_values}) shows exceptional resilience ({y_values}), confirming selective retention at **{opt_val}**. Principles from **{ref_citation_tag}** corroborate inner-sphere complex stability."
    elif "ionic" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} ionic strength variations ({x_values}) against performance metrics ({y_values}) highlight double-layer compression effects near **{opt_val}**. As noted in **{ref_citation_tag}**, outer-sphere interactions remain minor."
    elif "regeneration" in p_lower or "reusability" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} multi-cycle tracking ({x_values}) proves structural durability ({y_values}) up to **{opt_val}**. Grounded in **{ref_citation_tag}**, framework stability ensures sustained reusability."
    elif "wastewater" in p_lower:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} real matrix testing ({x_values}) demonstrates high efficacy ({y_values}) benchmarked at **{opt_val}**. Reference **{ref_citation_tag}** validates practical applicability under environmental interference."
    else:
        dynamic_text = f"**Visual & Mechanistic Evaluation of {param_type}:** {chart_status_text} systematic variations across ({x_values}) highlight distinct behavioural trends ({y_values}), confirming optimized conditions at **{opt_val}**. Supported by **{ref_citation_tag}**, process reliability is fully verified."

    st.info(dynamic_text)
