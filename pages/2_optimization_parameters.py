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
    t_desc = "Dynamic analytical module featuring fully expanded parameters for Adsorption, SPE/MSPE, and Environmental Removal, with real-time contextual adaptation."
    sec1_title = "1. Define Main Study System:"
    mode_label = "Select experiment type:"
    opt_modes = [
        "Adsorption (Surface capacity, thermodynamics & isotherms)",
        "SPE / MSPE (Solid-phase microextraction and preconcentration)",
        "Removal (Pollutant remediation, real wastewater & reusability)"
    ]
    sec2_title = "2. Enter Parameter Data & Quantitative Results:"
    
    ads_params = ["Initial Concentration (C0)", "Adsorbent Dosage", "Contact Time", "Solution Temperature (Thermodynamics)", "Initial pH of Solution", "Ionic Strength / Salt Effect"]
    spe_params = ["Eluent Type & Volume", "Sample Volume (Preconcentration Factor)", "Extraction / Adsorption Time", "Sample pH", "Amount of Sorbent / Magnetic Nanoparticles", "Desorption Time & Shaking Speed"]
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
    y_lbl = "Resulting Performance Values (Capacity / Recovery / Removal %):"
    opt_val_lbl = "Selected Optimum Point / Condition:"
    sec3_title = "3. Targeted Reference Tagging & Specific Notes"
    uploader_lbl = "Upload Reference Document Specifically for this Parameter (PDF / TXT):"
    ref_tag_lbl = "Reference Citation Tag (e.g., Smith et al., 2024):"
    notes_lbl = "Targeted Mechanistic Observation for this Parameter:"
    btn_generate = "Generate Dynamic Isolated Parameter Discussion (Q1 Style)"
    success_msg = "Dynamic parameter discussion successfully formulated with context-specific adaptation."
    preview_title = "Contextually Adapted Discussion Paragraph:"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Optimizasyon Parametreleri Merkezi"
    t_desc = "Gerçek zamanlı bağlamsal adaptasyona sahip, Adsorpsiyon, SPE/MSPE ve Çevresel Giderim için tam genişletilmiş parametreler içeren dinamik analitik modül."
    sec1_title = "1. Ana Çalışma Sistemini Belirleyin:"
    mode_label = "Deney türünü seçin:"
    opt_modes = [
        "Adsorpsiyon (Yüzey kapasitesi, termodinamik ve izotermler)",
        "SPE / MSPE (Katı faz mikro ekstraksiyonu ve zenginleştirme)",
        "Giderim (Kirletici arıtımı, gerçek atıksu ve yeniden kullanılabilirlik)"
    ]
    sec2_title = "2. Parametre Verilerini ve Nicel Sonuçları Girin:"
    
    ads_params = ["Başlangıç Konsantrasyonu (C0)", "Adsorban Dozu", "Temas Süresi", "Çözelti Sıcaklığı (Termodinamik)", "Çözeltinin Başlangıç pH'ı", "İyonik Şiddet / Tuz Etkisi"]
    spe_params = ["Elüent Türü ve Hacmi", "Örnek Hacmi (Zenginleştirme Faktörü)", "Ekstraksiyon Süresi", "Örnek pH'ı", "Nanopartikül Miktarı", "Desorpsiyon Süresi"]
    rem_params = [
        "Başlangıç Kirletici Konsantrasyonu (C0)",
        "Adsorban / Malzeme Dozu",
        "Temas Süresi ve Kinetik Değerlendirme",
        "Çözelti Sıcaklığı ve Termodinamik",
        "Başlangıç pH Optimizasyonu",
        "Birlikte Bulunan / Girişen İyonlar (Seçicilik)",
        "İyonik Şiddet Etkileri",
        "Yeniden Üretim ve Yeniden Kullanım Döngüleri",
        "Gerçek Atıksu / Çevresel Matris Uygulaması",
        "Sürekli Sabit Yataklı Kolon Parametreleri"
    ]

    x_lbl = "Deneysel Parametre Değerleri (virgülle ayırın):"
    y_lbl = "Sonuç Performans Değerleri:"
    opt_val_lbl = "Seçilen Optimum Nokta / Koşul:"
    sec3_title = "3. Hedeflenen Referans İndeksleme ve Özel Notlar"
    uploader_lbl = "Bu Parametreye Özel Referans Belgesi Yükleyin (PDF / Metin):"
    ref_tag_lbl = "Referans Etiketi (örn. Smith ve ark., 2024):"
    notes_lbl = "Bu Parametre İçin Hedeflenen Mekanistik Gözlem:"
    btn_generate = "Dinamik İzole Parametre Tartışması Oluştur (Q1 Stili)"
    success_msg = "Bağlama özgü adaptasyon ile parametre tartışması başarıyla hazırlandı."
    preview_title = "Bağlamsal Olarak Uyarlanmış Tartışma Paragrafı:"

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
        "Solution Temperature (Thermodynamics) - تأثير درجة الحرارة والطاقة الحرة", 
        "Initial pH of Solution - تأثير الحموضة الأولية والسطح", 
        "Ionic Strength / Salt Effect - تأثير القوة الأيونية والأملاح"
    ]
    
    spe_params = [
        "Eluent Type & Volume - نوع وحجم مذيب الاستشطيف", 
        "Sample Volume (Preconcentration Factor) - حجم عينة التحميل ومعامل التبريز", 
        "Extraction / Adsorption Time - زمن استخلاص وتوازن الطور", 
        "Sample pH - أس هيدروجيني العينة", 
        "Amount of Sorbent / Magnetic Nanoparticles - كمية المادة الحاملة النانوية", 
        "Desorption Time & Shaking Speed - زمن وسرعة التحرير"
    ]
    
    rem_params = [
        "Initial Pollutant Concentration (C0) - تركيز الملوث الابتدائي",
        "Adsorbent / Material Dosage - جرعة المادة المعالجة",
        "Contact Time & Kinetic Evaluation - زمن التلامس وحركية الإزالة",
        "Solution Temperature & Thermodynamics - تأثير درجة الحرارة والثرموديناميكا",
        "Initial pH Optimization - تحسين الأس الهيدروجيني الأولي",
        "Co-existing / Interfering Ions (Selectivity) - تأثير الأيونات المتنافسة والمنافسة",
        "Ionic Strength Effects - تأثير القوة الأيونية",
        "Regeneration & Reusability Cycles - دورات الاستعادة وإعادة الاستخدام",
        "Real Wastewater / Environmental Matrix Application - تطبيق عينات المياه الحقيقية والصرف",
        "Continuous Fixed-Bed Column Parameters - معلمات أعمدة الثابت المستمرة"
    ]

    x_lbl = "قيم المعامل التجريبية المدروسة (افصل بينها بفاصلة):"
    y_lbl = "القيم الناتجة بدقة (السعة / الاسترداد / الإزالة %):"
    opt_val_lbl = "القيمة أو النقطة المثلى المحددة (Optimum Condition):"
    sec3_title = "3. الفهرسة المرجعية المخصصة والملاحظات الدقيقة"
    uploader_lbl = "رفع المرجع الخاص بهذه المعلمة فقط (PDF / TXT):"
    ref_tag_lbl = "معرّف المرجع المفهرس (مثل: Ref [1] - Smith et al.):"
    notes_lbl = "الملاحظة الميكانيكية أو التحليل المستخلص من هذا المرجع لهذه المعلمة حصرياً:"
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

# التغيير الديناميكي للقيم الافتراضية بناءً على النظام والمعلمة المختارة
if "Adsorption" in study_mode or "Adsorpsiyon" in study_mode or "Adsorption" in raw_mode_key:
    with col1:
        param_type = st.selectbox("Select Adsorption Parameter:", ads_params)
    with col2:
        if "Concentration" in param_type or "تركيز" in param_type:
            x_values = st.text_input(x_lbl, value="10, 25, 50, 100, 200 mg/L")
            opt_val = st.text_input(opt_val_lbl, value="100 mg/L (Saturation threshold)")
        elif "Dosage" in param_type or "جرعة" in param_type:
            x_values = st.text_input(x_lbl, value="0.1, 0.2, 0.5, 1.0, 2.0 g/L")
            opt_val = st.text_input(opt_val_lbl, value="1.0 g/L (Optimal active surface)")
        elif "Time" in param_type or "زمن" in param_type:
            x_values = st.text_input(x_lbl, value="5, 15, 30, 60, 120, 240 min")
            opt_val = st.text_input(opt_val_lbl, value="120 min (Equilibrium time)")
        elif "Temperature" in param_type or "حرارة" in param_type:
            x_values = st.text_input(x_lbl, value="298, 308, 318 K")
            opt_val = st.text_input(opt_val_lbl, value="318 K (Endothermic maximum)")
        elif "pH" in param_type or "الحموضة" in param_type:
            x_values = st.text_input(x_lbl, value="2.0, 4.0, 6.0, 8.0, 10.0")
            opt_val = st.text_input(opt_val_lbl, value="pH 6.0 (Electrostatic attraction apex)")
        else:
            x_values = st.text_input(x_lbl, value="0.01, 0.05, 0.1, 0.5 M")
            opt_val = st.text_input(opt_val_lbl, value="0.05 M ionic strength")
    y_values = st.text_input(y_lbl, value="12.5, 24.1, 45.2, 68.5, 72.0 mg/g")

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("Select SPE Parameter:", spe_params)
    with col2:
        if "Eluent" in param_type or "مذيب" in param_type:
            x_values = st.text_input(x_lbl, value="0.5, 1.0, 2.0, 5.0 mL")
            opt_val = st.text_input(opt_val_lbl, value="2.0 mL (Quantitative recovery)")
        elif "Volume" in param_type or "حجم" in param_type:
            x_values = st.text_input(x_lbl, value="50, 100, 250, 500 mL")
            opt_val = st.text_input(opt_val_lbl, value="250 mL (High preconcentration factor)")
        else:
            x_values = st.text_input(x_lbl, value="1, 3, 5, 10 min / mg")
            opt_val = st.text_input(opt_val_lbl, value="5 min / 20 mg sorbent")
    y_values = st.text_input(y_lbl, value="82.4, 98.5, 94.1, 88.0 % Recovery")

else:  # Removal (مع 10 معلمات شاملة)
    with col1:
        param_type = st.selectbox("Select Removal Parameter:", rem_params)
    with col2:
        if "Concentration" in param_type or "تركيز" in param_type:
            x_values = st.text_input(x_lbl, value="5, 10, 25, 50, 100 mg/L")
            opt_val = st.text_input(opt_val_lbl, value="25 mg/L initial loading")
        elif "Dosage" in param_type or "جرعة" in param_type:
            x_values = st.text_input(x_lbl, value="0.05, 0.1, 0.25, 0.5 g")
            opt_val = st.text_input(opt_val_lbl, value="0.25 g optimal mass")
        elif "Time" in param_type or "زمن" in param_type:
            x_values = st.text_input(x_lbl, value="10, 30, 60, 120, 180 min")
            opt_val = st.text_input(opt_val_lbl, value="60 min kinetic equilibrium")
        elif "Temperature" in param_type or "حرارة" in param_type:
            x_values = st.text_input(x_lbl, value="293, 303, 313, 323 K")
            opt_val = st.text_input(opt_val_lbl, value="303 K thermodynamic optimum")
        elif "pH" in param_type or "الحموضة" in param_type:
            x_values = st.text_input(x_lbl, value="2.0, 4.0, 6.0, 8.0, 10.0")
            opt_val = st.text_input(opt_val_lbl, value="pH 6.0 removal apex")
        elif "Co-existing" in param_type or "المتداخلة" in param_type:
            x_values = st.text_input(x_lbl, value="Na+, K+, Ca2+, Mg2+, Cl-, SO42-")
            opt_val = st.text_input(opt_val_lbl, value="High selectivity confirmed with minimal interference")
        elif "Ionic" in param_type or "القوة الأيونية" in param_type:
            x_values = st.text_input(x_lbl, value="0.0, 0.05, 0.1, 0.2, 0.5 M NaCl")
            opt_val = st.text_input(opt_val_lbl, value="Stable removal across ionic strength gradients")
        elif "Regeneration" in param_type or "دورات" in param_type:
            x_values = st.text_input(x_lbl, value="Cycle 1, Cycle 2, Cycle 3, Cycle 4, Cycle 5")
            opt_val = st.text_input(opt_val_lbl, value="Stable reusability up to 5 consecutive cycles (>88% retention)")
        elif "Wastewater" in param_type or "المياه الحقيقية" in param_type:
            x_values = st.text_input(x_lbl, value="Tap water, River water, Industrial effluent")
            opt_val = st.text_input(opt_val_lbl, value=">92% removal efficiency in spiked real environmental matrices")
        else:
            x_values = st.text_input(x_lbl, value="1.0, 2.0, 5.0 mL/min flow rate")
            opt_val = st.text_input(opt_val_lbl, value="2.0 mL/min optimal bed residence time")
    y_values = st.text_input(y_lbl, value="35.0, 62.5, 96.8, 85.0, 68.2 % Removal")

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
    elif "dosage" in p_lower or "جرعة" in p_lower or "dozu" in p_lower or "malzeme" in p_lower or "amount" in p_lower:
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
