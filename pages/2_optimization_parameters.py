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
    st.caption("Active Hub: Fully Dynamic Parameter & Example Adaptation")

# قاموس الترجمات والخيارات الشاملة
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Optimization Parameters Hub"
    t_desc = "Dynamic analytical module where examples and default values automatically adapt based on the selected parameter."
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

    x_lbl = "Experimental Parameter Values:"
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
    t_desc = "Örneklerin ve varsayılan değerlerin seçilen parametreye göre otomatik olarak uyarlandığı dinamik analitik modül."
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

    x_lbl = "Deneysel Parametre Değerleri:"
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
    t_desc = "وحدة تحليلية ديناميكية متقدمة تتغير فيها الأمثلة والقيم الافتراضية تلقائياً فور تغيير المعلمة المدروسة."
    sec1_title = "1. حدد نظام الدراسة الرئيسي:"
    mode_label = "اختر نوع التجربة لدراسة العوامل المؤثرة:"
    opt_modes = [
        "Adsorption (دراسات الامتزاز، الديناميكا الحرارية والسعة)",
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر ومعامل التبريز)",
        "Removal (دراسات إزالة الملوثات، المياه الحقيقية وإعادة الاستخدام)"
    ]
    sec2_title = "2. إدخال بيانات المعلمة والنتائج الكمية:"
    
    ads_params = [
        "Initial Concentration (C0)", 
        "Adsorbent Dosage", 
        "Contact Time", 
        "Solution Temperature", 
        "Initial pH of Solution", 
        "Ionic Strength"
    ]
    
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
    sec3_title = "3. الفهرسة المرجعية المخصصة والملاحظات الدقيقة"
    uploader_lbl = "رفع المرجع الخاص بهذه المعلمة فقط (PDF / TXT):"
    ref_tag_lbl = "معرّف المرجع المفهرس (مثل: Ref [1] - Smith et al.):"
    notes_lbl = "الملاحظة الميكانيكية أو التحليل المستخلص لهذه المعلمة:"
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

# --- التكيف الديناميكي الكامل للمعلمات والأمثلة بناءً على المعلمة المختارة ---
if "Adsorption" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", ads_params)
    
    # تعيين الأمثلة ديناميكياً بناءً على المعلمة المختارة في الامتزاز
    if "Concentration" in param_type:
        default_x = "10, 25, 50, 100, 200 mg/L"
        default_y = "12.5, 24.1, 45.2, 68.5, 72.0 mg/g"
        default_opt = "100 mg/L (Saturation threshold)"
    elif "Dosage" in param_type:
        default_x = "0.1, 0.2, 0.5, 1.0, 2.0 g/L"
        default_y = "15.0, 32.1, 55.4, 78.2, 79.0 mg/g"
        default_opt = "1.0 g/L (Optimal active surface)"
    elif "Time" in param_type:
        default_x = "5, 15, 30, 60, 120, 240 min"
        default_y = "10.2, 28.5, 50.1, 71.4, 75.0, 75.2 mg/g"
        default_opt = "120 min (Equilibrium time)"
    elif "Temperature" in param_type:
        default_x = "298, 308, 318 K"
        default_y = "45.0, 62.3, 81.5 mg/g"
        default_opt = "318 K (Endothermic maximum)"
    elif "pH" in param_type:
        default_x = "2.0, 4.0, 6.0, 8.0, 10.0"
        default_y = "18.2, 35.4, 76.8, 52.1, 30.5 mg/g"
        default_opt = "pH 6.0 (Electrostatic attraction apex)"
    else:
        default_x = "0.01, 0.05, 0.1, 0.5 M"
        default_y = "72.0, 68.4, 61.2, 45.0 mg/g"
        default_opt = "0.05 M ionic strength"

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", spe_params)
    
    # تعيين الأمثلة ديناميكياً بناءً على المعلمة المختارة في الاستخلاص
    if "Eluent" in param_type:
        default_x = "0.5, 1.0, 2.0, 5.0 mL"
        default_y = "65.0, 82.1, 98.5, 90.2 % Recovery"
        default_opt = "2.0 mL (Quantitative recovery)"
    elif "Volume" in param_type:
        default_x = "50, 100, 250, 500 mL"
        default_y = "99.1, 98.8, 97.5, 82.0 % Recovery"
        default_opt = "250 mL (High preconcentration factor)"
    elif "Time" in param_type:
        default_x = "1, 3, 5, 10 min"
        default_y = "70.5, 88.2, 98.5, 98.4 % Recovery"
        default_opt = "5 min (Mass transfer equilibrium)"
    elif "pH" in param_type:
        default_x = "2.0, 4.0, 6.0, 8.0, 10.0"
        default_y = "45.0, 78.2, 98.5, 85.1, 62.0 % Recovery"
        default_opt = "pH 6.0 (Optimal complexation)"
    elif "Sorbent" in param_type:
        default_x = "5, 10, 20, 50 mg"
        default_y = "72.0, 89.5, 98.5, 98.6 % Recovery"
        default_opt = "20 mg (Quantitative retention)"
    else:
        default_x = "1, 2, 5, 10 min"
        default_y = "98.5, 98.2, 91.0, 82.4 % Recovery"
        default_opt = "2 min rapid desorption"

else:  # Removal (10 معلمات شاملة)
    with col1:
        param_type = st.selectbox("Select Parameter:", rem_params)
    
    # تعيين الأمثلة ديناميكياً بناءً على المعلمة المختارة في الإزالة والمعالجة
    if "Pollutant" in param_type:
        default_x = "5, 10, 25, 50, 100 mg/L"
        default_y = "98.2, 97.5, 96.8, 82.1, 65.0 % Removal"
        default_opt = "25 mg/L initial loading capacity"
    elif "Dosage" in param_type:
        default_x = "0.05, 0.1, 0.25, 0.5 g"
        default_y = "45.2, 72.8, 96.8, 97.0 % Removal"
        default_opt = "0.25 g optimal mass"
    elif "Contact" in param_type:
        default_x = "10, 30, 60, 120, 180 min"
        default_y = "60.5, 85.2, 96.8, 97.1, 97.2 % Removal"
        default_opt = "60 min kinetic equilibrium"
    elif "Temperature" in param_type:
        default_x = "293, 303, 313, 323 K"
        default_y = "85.0, 96.8, 97.5, 98.0 % Removal"
        default_opt = "303 K thermodynamic optimum"
    elif "pH" in param_type:
        default_x = "2.0, 4.0, 6.0, 8.0, 10.0"
        default_y = "35.0, 62.5, 96.8, 85.0, 68.2 % Removal"
        default_opt = "pH 6.0 removal apex"
    elif "Co-existing" in param_type:
        default_x = "Na+, K+, Ca2+, Mg2+, Cl-, SO42-"
        default_y = "95.5, 96.1, 92.4, 91.8, 94.5, 93.2 % Removal"
        default_opt = "High selectivity with minimal matrix interference"
    elif "Ionic" in param_type:
        default_x = "0.0, 0.05, 0.1, 0.2, 0.5 M NaCl"
        default_y = "96.8, 96.5, 95.8, 94.0, 91.2 % Removal"
        default_opt = "Stable removal across salinity gradients"
    elif "Regeneration" in param_type:
        default_x = "Cycle 1, Cycle 2, Cycle 3, Cycle 4, Cycle 5"
        default_y = "96.8, 95.2, 93.8, 91.0, 88.5 % Removal"
        default_opt = "Stable reusability up to 5 consecutive cycles"
    elif "Wastewater" in param_type:
        default_x = "Tap water, River water, Industrial effluent"
        default_y = "97.2, 94.5, 91.8 % Removal"
        default_opt = ">91% removal in complex real wastewater matrices"
    else:
        default_x = "1.0, 2.0, 5.0 mL/min flow rate"
        default_y = "98.5, 96.8, 84.2 % Removal"
        default_opt = "2.0 mL/min optimal bed residence time"

with col2:
    x_values = st.text_input(x_lbl, value=default_x)
    y_values = st.text_input(y_lbl, value=default_y)
    opt_val = st.text_input(opt_val_lbl, value=default_opt)

# --- رفع المرجع المخصص والفهرسة لهذه المعلمة حصرياً ---
st.markdown("---")
st.markdown(f"### {sec3_title}")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    param_ref_file = st.file_uploader(uploader_lbl, type=["pdf", "txt"], key="param_specific_ref")
with col_ref2:
    ref_citation_tag = st.text_input(ref_tag_lbl, value="Ref. [1] (Smith et al., 2024)")

chem_notes = st.text_area(notes_lbl, placeholder="e.g., This specific reference confirms the unique mechanistic trend for this parameter...", key="param_specific_notes")

# --- محرك الصياغة الديناميكي المتكيف لكل معلمة على حدة ---
if st.button(btn_generate, key="btn_optimization"):
    st.success(success_msg)
    st.markdown(f"### {preview_title}")
    
    p_lower = param_type.lower()
    
    # صياغات فريدة ومتكيّفة بالكامل ديناميكياً بناءً على اختيار المعلمة الفعلي
    if "concentration" in p_lower or "تركيز" in p_lower or "konsantrasyonu" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- The effect of the initial concentration gradient spanning ({x_values}) was evaluated against the resulting capacity metrics ({y_values}), identifying the critical operational threshold at **{opt_val}**.
- *Contextual Scientific Justification:* As explicitly documented in **{ref_citation_tag}**, initial concentration acts as the primary driving force in overcoming mass transfer resistance between the bulk solution and the solid interface. Lower concentrations maintain high active site availability, whereas higher concentrations accelerate diffusion rates until active site saturation is achieved.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Monolayer adsorption capacity verified in accordance with high-impact literature.'}
        """
    elif "dosage" in p_lower or "جرعة" in p_lower or "dozu" in p_lower or "malzeme" in p_lower or "amount" in p_lower or "sorbent" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Solid mass loading variations across ({x_values}) were systematically correlated with removal/capacity performance ({y_values}), determining the optimal dosage apex at **{opt_val}**.
- *Contextual Scientific Justification:* Supported by findings in **{ref_citation_tag}**, expanding the sorbent dosage increases the total surface area and active coordination sites available for pollutant capture. However, exceeding the optimum threshold induces particle aggregation and overlapping boundary layers, which diminishes effective surface area per unit mass.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Optimal active site dispersion confirmed without excessive aggregation.'}
        """
    elif "time" in p_lower or "زمن" in p_lower or "süresi" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Contact duration tracking over structured intervals ({x_values}) established the kinetic evolution ({y_values}), reaching steady-state equilibrium at **{opt_val}**.
- *Contextual Scientific Justification:* In strict accordance with the transport models in **{ref_citation_tag}**, rapid initial uptake stems from abundant unoccupied surface sites. Over time, intra-particle diffusion resistance governs mass transfer as active sites become progressively occupied, establishing dynamic equilibrium.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Equilibrium time reflects surface-controlled chemisorption kinetics.'}
        """
    elif "temperature" in p_lower or "حرارة" in p_lower or "sıcaklığı" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Thermal sensitivity across the range ({x_values}) was analyzed to establish the energetic profile ({y_values}), defining the thermodynamic optimum at **{opt_val}**.
- *Contextual Scientific Justification:* Relying on the thermodynamic principles outlined in **{ref_citation_tag}**, temperature elevation decreases boundary layer viscosity and enhances adsorbate mobility, supplying the necessary thermal activation energy for spontaneous endothermic complexation.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Endothermic spontaneity confirmed through thermodynamic parameter evaluation.'}
        """
    elif "ph" in p_lower or "أس هيدروجيني" in p_lower or "ph'ı" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Interfacial acidity variations ({x_values}) were isolated to determine surface charge dynamics ({y_values}), achieving maximum performance efficiency at **{opt_val}**.
- *Contextual Scientific Justification:* As emphasized in **{ref_citation_tag}**, solution pH dictates both material zeta potential and pollutant ionic speciation. Highly acidic conditions trigger intense electrostatic repulsion due to excess hydronium ($H^+$) competition, whereas optimizing the pH promotes surface deprotonation and favorable electrostatic attraction.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Surface deprotonation and electrostatic control verified.'}
        """
    elif "co-existing" in p_lower or "interfering" in p_lower or "المتداخلة" in p_lower or "girişen" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type} (Selectivity Study):**
- Matrix selectivity and competitive ion testing ({x_values}) were performed against baseline performance ({y_values}), confirming operational resilience at **{opt_val}**.
- *Contextual Scientific Justification:* In accordance with selective binding criteria reported in **{ref_citation_tag}**, high-performance materials must maintain structural affinity for target species despite high concentrations of background co-existing ions ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Cl}^-$), owing to inner-sphere complexation.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'High selectivity and negligible matrix interference confirmed.'}
        """
    elif "ionic" in p_lower or "القوة الأيونية" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Ionic strength gradients via electrolyte additions ({x_values}) were assessed for performance stability ({y_values}), with optimal behavior observed at **{opt_val}**.
- *Contextual Scientific Justification:* Reference data in **{ref_citation_tag}** indicate that varying ionic strength helps differentiate outer-sphere versus inner-sphere surface complexation mechanisms, ensuring operational stability in saline environments.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Outer-sphere electrostatic stability verified across salt concentrations.'}
        """
    elif "regeneration" in p_lower or "reusability" in p_lower or "دورات" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Multi-cycle adsorption-desorption testing ({x_values}) evaluated reusability retention ({y_values}), establishing stability thresholds at **{opt_val}**.
- *Contextual Scientific Justification:* Lifecycle durability metrics cited in **{ref_citation_tag}** demonstrate that a resilient material must endure repeated chemical regeneration (using mild eluents) without structural degradation or active site collapse.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Exceptional reusability and structural framework stability verified.'}
        """
    elif "wastewater" in p_lower or "environmental" in p_lower or "المياه الحقيقية" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Real environmental matrix applications ({x_values}) were tested to validate practical applicability ({y_values}), confirming performance reliability at **{opt_val}**.
- *Contextual Scientific Justification:* Real-world validation protocols in **{ref_citation_tag}** confirm that synthesized adsorbents successfully overcome complex organic and inorganic competition present in natural waters.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Practical environmental matrix adaptability successfully verified.'}
        """
    elif "column" in p_lower or "continuous" in p_lower or "أعمدة" in p_lower:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Fixed-bed column flow evaluations ({x_values}) established dynamic breakthrough characteristics ({y_values}), optimizing operational parameters at **{opt_val}**.
- *Contextual Scientific Justification:* Continuous column dynamics detailed in **{ref_citation_tag}** govern industrial-scale scaling, where bed residence time and empty bed contact time dictate solute breakthrough behavior.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Continuous flow operational scalability verified.'}
        """
    else:
        dynamic_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Systematic parameter evaluation across ({x_values}) demonstrated distinct performance trends ({y_values}), establishing the optimized condition at **{opt_val}**.
- *Contextual Scientific Justification:* Grounded in analytical principles from **{ref_citation_tag}**, this configuration secures reproducibility and structural integrity.
- *Specific Empirical Note:* {chem_notes if chem_notes else 'Reproducible analytical performance confirmed.'}
        """

    st.info(dynamic_text.strip())
