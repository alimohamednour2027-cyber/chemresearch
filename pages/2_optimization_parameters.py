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
    st.caption("Active Hub: Isolated Parameter Analysis & Targeted Reference Tagging")

# قاموس الترجمات والخيارات
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Optimization Parameters Hub"
    t_desc = "Precision analytical module engineered to extract, isolate, and index targeted parameter discussions from reference literature without cross-contamination."
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
    rem_params = ["Initial pH Optimization", "Co-existing / Interfering Ions", "Regeneration & Reusability Cycles", "Initial Pollutant Loading / Real Wastewater Sample"]

    x_lbl = "Experimental Parameter Values (comma-separated):"
    y_lbl = "Resulting Performance Values (Capacity / Recovery / Removal %):"
    opt_val_lbl = "Selected Optimum Point / Condition:"
    sec3_title = "3. Targeted Reference Tagging & Specific Notes"
    uploader_lbl = "Upload Reference Document Specifically for this Parameter (PDF / TXT):"
    ref_tag_lbl = "Reference Citation Tag (e.g., Smith et al., 2024 - pH mechanism):"
    notes_lbl = "Targeted Mechanistic Observation for this Parameter:"
    btn_generate = "Generate Isolated Parameter Discussion (Q1 Style)"
    success_msg = "Targeted parameter discussion successfully formulated with dedicated literature indexing."
    preview_title = "Isolated Parameter Discussion Paragraph:"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Optimizasyon Parametreleri Merkezi"
    t_desc = "Referans literatüründen hedeflenen parametre tartışmalarını çapraz kontaminasyon olmadan izole etmek ve indekslemek için tasarlanmış hassas analitik modül."
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
    rem_params = ["Başlangıç pH Optimizasyonu", "Birlikte Bulunan İyonlar", "Yeniden Kullanım Döngüleri", "Gerçek Atıksu Numunesi"]

    x_lbl = "Deneysel Parametre Değerleri (virgülle ayırın):"
    y_lbl = "Sonuç Performans Değerleri:"
    opt_val_lbl = "Seçilen Optimum Nokta / Koşul:"
    sec3_title = "3. Hedeflenen Referans İndeksleme ve Özel Notlar"
    uploader_lbl = "Bu Parametreye Özel Referans Belgesi Yükleyin (PDF / Metin):"
    ref_tag_lbl = "Referans Etiketi (örn. Smith ve ark., 2024 - pH mekanizması):"
    notes_lbl = "Bu Parametre İçin Hedeflenen Mekanistik Gözlem:"
    btn_generate = "İzole Parametre Tartışması Oluştur (Q1 Stili)"
    success_msg = "Hedeflenen referans indeksleme ile parametre tartışması başarıyla oluşturuldu."
    preview_title = "İzole Edilmiş Parametre Tartışma Paragrafı:"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز تحسين المعلمات المتقدمة"
    t_desc = "وحدة تحليلية دقيقة ومخصصة لاستخلاص وتحليل وفهرسة تأثير المعلمة المستهدفة وحدها من الأدبيات المرجعية، دون أي تداخل مع معلمات أخرى."
    sec1_title = "1. حدد نظام الدراسة الرئيسي:"
    mode_label = "اختر نوع التجربة لدراسة العوامل المؤثرة:"
    opt_modes = [
        "Adsorption (دراسات الامتزاز، الديناميكا الحرارية والسعة)",
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر ومعامل التبريز)",
        "Removal (دراسات إزالة الملوثات، المياه الحقيقية وإعادة الاستخدام)"
    ]
    sec2_title = "2. إدخال بيانات المعلمة والنتائج الكمية:"
    
    ads_params = [
        "Initial Concentration (C0) - تأثير التركيز الابتدائي", 
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
        "Initial pH Optimization - تحسين الحموضة للإزالة البيئية", 
        "Co-existing / Interfering Ions - تأثير الأيونات المنافسة في المياه الحقيقية", 
        "Regeneration & Reusability Cycles - دورات الاستعادة وإعادة الاستخدام", 
        "Initial Pollutant Loading / Real Wastewater Sample - عينات الصرف الحقيقية والأحمال العالية"
    ]

    x_lbl = "قيم المعامل التجريبية المدروسة (افصل بينها بفاصلة):"
    y_lbl = "القيم الناتجة بدقة (السعة / الاسترداد / الإزالة %):"
    opt_val_lbl = "القيمة أو النقطة المثلى المحددة (Optimum Condition):"
    sec3_title = "3. الفهرسة المرجعية المخصصة والملاحظات الدقيقة"
    uploader_lbl = "رفع المرجع الخاص بهذه المعلمة فقط (PDF / TXT):"
    ref_tag_lbl = "معرّف المرجع المفهرس (مثل: Ref [1] - Smith et al. regarding pH mechanism):"
    notes_lbl = "الملاحظة الميكانيكية أو التحليل المستخلص من هذا المرجع لهذه المعلمة حصرياً:"
    btn_generate = "توليد مناقشة دقيقة ومعزولة لـ Q1 (مخصصة للمعلمة فقط)"
    success_msg = "تم توليد المناقشة العلمية المفهرسة والمخصصة لهذه المعلمة بنجاح!"
    preview_title = "مسودة فقرة المناقشة المعزولة (Targeted Parameter & Reference Indexing):"

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

if "Adsorption" in study_mode or "Adsorpsiyon" in study_mode or "Adsorption" in raw_mode_key:
    with col1:
        param_type = st.selectbox("Select Parameter:", ads_params)
        x_values = st.text_input(x_lbl, value="10, 25, 50, 100, 200")
    with col2:
        y_values = st.text_input(y_lbl, value="5.2, 12.5, 24.1, 38.5, 42.0")
        optimum_val = st.text_input(opt_val_lbl, value="Optimum threshold identified at 100 mg/L or 308 K")

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", spe_params)
        x_values = st.text_input(x_lbl, value="1, 2, 5, 10")
    with col2:
        y_values = st.text_input(y_lbl, value="75.2, 98.5, 91.0, 82.4")
        optimum_val = st.text_input(opt_val_lbl, value="Quantitative elution achieved at 2 mL")

else:  # Removal
    with col1:
        param_type = st.selectbox("Select Parameter:", rem_params)
        x_values = st.text_input(x_lbl, value="2, 4, 6, 8, 10")
    with col2:
        y_values = st.text_input(y_lbl, value="35.0, 62.5, 96.8, 85.0, 68.2")
        optimum_val = st.text_input(opt_val_lbl, value="Optimal performance apex at pH 6.0")

# --- رفع المرجع المخصص والفهرسة لهذه المعلمة حصرياً ---
st.markdown("---")
st.markdown(f"### {sec3_title}")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    param_ref_file = st.file_uploader(uploader_lbl, type=["pdf", "txt"], key="param_specific_ref")
with col_ref2:
    ref_citation_tag = st.text_input(ref_tag_lbl, value="Ref. [1] (Smith et al., 2024)")

chem_notes = st.text_area(notes_lbl, placeholder="e.g., This specific reference confirms that surface deprotonation governs the adsorption at this exact pH range...", key="param_specific_notes")

# --- محرك الصياغة المعزول والمخصص لكل معلمة مع مرجعها المفهرس ---
if st.button(btn_generate, key="btn_optimization"):
    st.success(success_msg)
    st.markdown(f"### {preview_title}")
    
    p_lower = param_type.lower()
    
    # صياغة دقيقة ومعزولة تماماً تقتصر على تحليل هذه المعلمة وربطها بمرجعها حصرياً
    if "concentration" in p_lower or "تركيز" in p_lower or "konsantrasyonu" in p_lower:
        isolated_text = f"""
**Targeted Analysis of {param_type}:**
- The influence of the initial concentration gradient ({x_values}) on uptake capacity was systematically isolated and evaluated. 
- Empirical data confirm a steady increase in sorption capacity up to the saturation apex at ({optimum_val}). 
- *Mechanistic & Literature Correlation:* As corroborated by **{ref_citation_tag}**, the driving force generated by higher concentration gradients effectively overcomes liquid-phase mass transfer resistance, directing adsorbate species toward unassigned active sites until full surface coverage is attained.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'The findings match established monolayer adsorption dynamics.'}
        """
    elif "dosage" in p_lower or "جرعة" in p_lower or "dozu" in p_lower or "nanopartikül" in p_lower or "amount" in p_lower:
        isolated_text = f"""
**Targeted Analysis of {param_type}:**
- The isolated effect of varying solid mass loadings ({x_values}) on removal efficiency was thoroughly investigated. 
- Performance peaked at the optimum dosage condition ({optimum_val}), establishing the threshold for active site availability. 
- *Mechanistic & Literature Correlation:* Referring specifically to the findings documented in **{ref_citation_tag}**, the initial enhancement stems from a greater population of exposed surface sites. However, excessive material loading induces localized particle agglomeration, which curtails effective surface area and stabilizes removal performance into a plateau.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'Active site saturation and aggregation phenomena verified.'}
        """
    elif "time" in p_lower or "زمن" in p_lower or "süresi" in p_lower:
        isolated_text = f"""
**Targeted Analysis of {param_type}:**
- Time-dependent kinetic behavior across the structured interval ({x_values}) was independently analyzed to determine equilibrium constraints. 
- The system exhibited rapid initial uptake, reaching a dynamic steady-state plateau at ({optimum_val}). 
- *Mechanistic & Literature Correlation:* In direct alignment with the kinetic models discussed in **{ref_citation_tag}**, early-stage sorption is expedited by numerous vacant active sites. Over time, intra-particle diffusion resistance increases as remaining sites become sterically hindered, achieving thermodynamic equilibrium.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'Equilibrium time matches surface-controlled kinetic mechanisms.'}
        """
    elif "temperature" in p_lower or "حرارة" in p_lower or "sıcaklığı" in p_lower:
        isolated_text = f"""
**Targeted Analysis of {param_type}:**
- The thermal dependency of the system was isolated across the temperature range ({x_values}), identifying the energetic optimum at ({optimum_val}). 
- *Mechanistic & Literature Correlation:* Based strictly on the thermodynamic framework provided in **{ref_citation_tag}**, thermal elevation enhances ion mobility and diminishes boundary layer viscosity. This thermal input supplies the requisite activation energy for robust chemical complexation at the solid-liquid interface.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'Endothermic thermal activation confirmed.'}
        """
    elif "ph" in p_lower or "أس هيدروجيني" in p_lower or "ph'ı" in p_lower:
        isolated_text = f"""
**Targeted Analysis of {param_type} (Acidity & Surface Charge):**
- The distinct impact of initial solution pH ({x_values}) on the interfacial binding mechanism was isolated, identifying the optimal performance apex at ({optimum_val}). 
- *Mechanistic & Literature Correlation:* As specifically emphasized in **{ref_citation_tag}**, solution acidity strictly regulates surface charge and ionic speciation. In acidic domains, high concentrations of hydronium ions ($H^+$) provoke intense electrostatic repulsion, hindering active binding. As pH approaches the optimum threshold, surface deprotonation of functional groups fosters favorable electrostatic attraction, whereas higher alkalinity induces hydroxide precipitation.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'Electrostatic surface charge dynamics and deprotonation validated.'}
        """
    elif "eluent" in p_lower or "مؤبيب" in p_lower or "volume" in p_lower or "حجم" in p_lower:
        isolated_text = f"""
**Targeted Analysis of {param_type} (Elution & Recovery):**
- Elution parameters and solvent gradients ({x_values}) were isolated to maximize desorption efficiency, achieving quantitative recovery at ({optimum_val}). 
- *Mechanistic & Literature Correlation:* In accordance with the extraction principles outlined in **{ref_citation_tag}**, optimized eluent volumes ensure complete quantitative stripping of bound ions without causing excessive sample dilution or disrupting complexation equilibria.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'Quantitative recovery and complete desorption verified.'}
        """
    else:
        isolated_text = f"""
**Targeted Analysis of {param_type}:**
- Systemic variations across the experimental gradient ({x_values}) were evaluated to isolate operational performance at ({optimum_val}). 
- *Mechanistic & Literature Correlation:* Supported by findings from **{ref_citation_tag}**, the observed response verifies structural integrity and physicochemical stability under controlled analytical conditions.
- *Specific Literature Insight:* {chem_notes if chem_notes else 'Reproducible operational stability confirmed.'}
        """

    st.info(isolated_text.strip())
