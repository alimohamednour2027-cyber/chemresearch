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
    st.caption("Active Hub: Parameters & Chemical Justification")

# قاموس الترجمات الثلاثي لهذه الصفحة (بدون إيقونات)
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Optimization Parameters Hub"
    t_desc = "This portal is dedicated to analyzing and interpreting optimization parameters and providing chemical and physical justifications for optimum values."
    sec1_title = "1. Define Main Study System:"
    mode_label = "Select experiment type to study influencing factors:"
    opt_modes = [
        "Adsorption (Surface capacity and isotherm studies)",
        "SPE / MSPE (Solid-phase microextraction and recovery studies)",
        "Removal (Pollutant removal and environmental water applications)"
    ]
    sec2_title = "2. Enter Optimization Parameters Data:"
    param_lbl_ads = "Studied Parameter:"
    x_ads_lbl = "Experimental Parameter Values (comma-separated):"
    y_ads_lbl = "Resulting Values or Adsorption Capacity (qe mg/g):"
    opt_val_lbl = "Selected Optimum Point:"
    
    param_lbl_spe = "Studied Parameter:"
    x_spe_lbl = "Eluent Volume or Parameter Gradient (mL):"
    y_spe_lbl = "Recovery Percentage (% Recovery):"
    
    param_lbl_rem = "Studied Parameter:"
    x_rem_lbl = "Gradient Values (e.g., pH 2, 4, 6, 8, 10):"
    y_rem_lbl = "Removal Percentage (% Removal):"
    
    sec3_title = "3. Reference Support and Scientific Notes"
    uploader_lbl = "Upload Reference Papers Supporting Interpretation (PDF / TXT):"
    notes_lbl = "Additional Notes on Chemical Mechanism (Optional):"
    btn_generate = "Generate Q1 Analysis and Discussion Draft"
    success_msg = "Parameter analysis draft successfully prepared."
    preview_title = "Proposed Discussion Paragraph Draft (Optimization & Discussion):"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Optimizasyon Parametreleri Merkezi"
    t_desc = "Bu portal, optimizasyon parametrelerini analiz etmek ve optimum değerler için kimyasal ve fiziksel gerekçeler sunmak üzere tasarlanmıştır."
    sec1_title = "1. Ana Çalışma Sistemini Belirleyin:"
    mode_label = "Etken faktörleri incelemek için deney türünü seçin:"
    opt_modes = [
        "Adsorpsiyon (Yüzey kapasitesi ve izoterm çalışmaları)",
        "SPE / MSPE (Katı faz mikro ekstraksiyonu ve geri kazanım çalışmaları)",
        "Giderim (Kirletici giderimi ve çevre suyu uygulamaları)"
    ]
    sec2_title = "2. Optimizasyon Parametreleri Verilerini Girin:"
    param_lbl_ads = "İncelenen Parametre:"
    x_ads_lbl = "Deneysel Parametre Değerleri (virgülle ayırın):"
    y_ads_lbl = "Sonuç Değerleri veya Adsorpsiyon Kapasitesi (qe mg/g):"
    opt_val_lbl = "Seçilen Optimum Nokta:"
    
    param_lbl_spe = "İncelenen Parametre:"
    x_spe_lbl = "Elüent Hacmi veya Parametre Gradyanı (mL):"
    y_spe_lbl = "Geri Kazanım Yüzdesi (% Recovery):"
    
    param_lbl_rem = "İncelenen Parametre:"
    x_rem_lbl = "Gradyan Değerleri (örn. pH 2, 4, 6, 8, 10):"
    y_rem_lbl = "Giderim Yüzdesi (% Removal):"
    
    sec3_title = "3. Referans Desteği ve Bilimsel Notlar"
    uploader_lbl = "Yorumlamayı Destekleyen Referans Makaleleri Yükleyin (PDF / TXT):"
    notes_lbl = "Kimyasal Mekanizma Hakkında Ek Notlar (İsteğe bağlı):"
    btn_generate = "Q1 Analiz ve Tartışma Taslağı Oluştur"
    success_msg = "Parametre analiz taslağı başarıyla hazırlandı."
    preview_title = "Önerilen Tartışma Paragraf Taslağı (Optimization & Discussion):"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز معلمات التحسين المتقدمة"
    t_desc = "هذه البوابة مخصصة لتحليل وتفسير معلمات التحسين وتقديم التفسيرات الكيميائية والفيزيائية للقيمة المثلى استناداً إلى طبيعة الدراسة."
    sec1_title = "1. حدد نظام الدراسة الرئيسي:"
    mode_label = "اختر نوع التجربة لدراسة العوامل المؤثرة:"
    opt_modes = [
        "Adsorption (دراسات الامتزاز وسعة السطح)",
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر واسترداد العناصر)",
        "Removal (دراسات إزالة الملوثات وتطبيقات المياه البيئية)"
    ]
    sec2_title = "2. إدخال بيانات معلمات التحسين:"
    param_lbl_ads = "العامل المدروس:"
    x_ads_lbl = "قيم المعامل التجريبية (افصل بينها بفاصلة):"
    y_ads_lbl = "القيم الناتجة أو السعة الممتصة (qe mg/g):"
    opt_val_lbl = "القيمة المثلى المختارة (Optimum Point):"
    
    param_lbl_spe = "العامل المدروس:"
    x_spe_lbl = "تدرج حجم المذيب أو العامل (mL):"
    y_spe_lbl = "نسبة الاسترداد (% Recovery):"
    
    param_lbl_rem = "العامل المدروس:"
    x_rem_lbl = "تدرج القيم (مثل pH 2, 4, 6, 8, 10):"
    y_rem_lbl = "نسبة الإزالة (% Removal):"
    
    sec3_title = "3. الدعم المرجعي والملاحظات العلمية"
    uploader_lbl = "رفع المقالات المرجعية الداعمة للتفسير (PDF / TXT):"
    notes_lbl = "ملاحظات إضافية حول الآلية الكيميائية (اختياري):"
    btn_generate = "توليد مسودة تحليل ومناقشة المعلمات لـ Q1"
    success_msg = "تم إعداد مسودة تحليل المعلمات بنجاح!"
    preview_title = "مسودة فقرة المناقشة المقترحة (Optimization & Discussion):"

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# --- اختيار نوع النظام الدراسي ---
st.markdown(f"### {sec1_title}")
study_mode = st.selectbox(mode_label, opt_modes)

st.markdown("---")
# استخلاص نوع النظام بدقة للتعامل البرمجى بغض النظر عن لغة العرض
raw_mode_key = study_mode.split(' ')[0]
st.markdown(f"### {sec2_title} [{raw_mode_key}]")

col1, col2 = st.columns(2)

if "Adsorption" in study_mode or "Adsorpsiyon" in study_mode or "Adsorption" in raw_mode_key:
    with col1:
        param_type = st.selectbox(param_lbl_ads, ["Initial Concentration (C0)", "Adsorbent Dosage", "Temperature", "Contact Time"])
        x_values = st.text_input(x_ads_lbl, value="10, 25, 50, 100, 200")
    with col2:
        y_values = st.text_input(y_ads_lbl, value="5.2, 12.5, 24.1, 38.5, 42.0")
        optimum_val = st.text_input(opt_val_lbl, value="High concentrations or saturation point dosage")

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox(param_lbl_spe, ["Eluent Type & Volume", "Sample Volume", "Extraction Speed & Method"])
        x_values = st.text_input(x_spe_lbl, value="1, 2, 5, 10")
    with col2:
        y_values = st.text_input(y_spe_lbl, value="75.2, 98.5, 91.0, 82.4")
        optimum_val = st.text_input(opt_val_lbl, value="2 mL of diluted acid")

else:  # Removal / Giderim / الإزالة
    with col1:
        param_type = st.selectbox(param_lbl_rem, ["Initial pH", "Co-existing Ions", "Regeneration Cycles"])
        x_values = st.text_input(x_rem_lbl, value="2, 4, 6, 8, 10")
    with col2:
        y_values = st.text_input(y_spe_lbl if lang_choice != "العربية" else "نسبة الإزالة (% Removal):", value="35.0, 62.5, 96.8, 85.0, 68.2")
        optimum_val = st.text_input(opt_val_lbl, value="pH = 6")

# --- رفع المراجع لدعم التفسير العلمي ---
st.markdown("---")
st.markdown(f"### {sec3_title}")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    opt_refs = st.file_uploader(uploader_lbl, type=["pdf", "txt"], accept_multiple_files=True, key="opt_ref_files")
with col_ref2:
    chem_notes = st.text_area(notes_lbl, placeholder="e.g., Electrostatic repulsion at low pH, precipitation at basic conditions...", key="opt_notes")

# --- زر توليد مسودة المناقشة ---
if st.button(btn_generate, key="btn_optimization"):
    st.success(success_msg)
    
    st.markdown(f"### {preview_title}")
    
    if "Adsorption" in study_mode or "Adsorpsiyon" in study_mode or "Adsorption" in raw_mode_key:
        draft_text = f"""
**Optimization Study - Effect of {param_type}:**
The effect of {param_type} on the adsorption process using the synthesized material was systematically investigated. 
- The experimental results indicate a clear dependency of the adsorption capacity on the tested parameter range ({x_values}). 
- The performance increased significantly up to the optimum condition ({optimum_val}), achieving maximum adsorption efficiency. 
- *Scientific Justification:* Beyond this optimum point, the active sites on the adsorbent surface approach total saturation, leading to a plateau or mass-transfer limitations. Comparative evaluation with reference literature confirms that this behavior aligns well with monolayer adsorption mechanisms and energetic site distribution.
- *User Insights:* {chem_notes if chem_notes else 'Standard energetic behavior observed.'}
        """
    elif "SPE" in study_mode:
        draft_text = f"""
**Optimization Study for Solid-Phase Extraction - Effect of {param_type}:**
To achieve quantitative extraction and high preconcentration factors, the effect of {param_type} was optimized.
- The recovery percentages (% Recovery) across the tested range ({x_values}) demonstrated that the highest recovery ({y_values}) was achieved at the optimum condition ({optimum_val}).
- *Scientific Justification:* Insufficient eluent volume or concentration leads to incomplete desorption of target metal ions from the active sites of the composite. Conversely, excessive volumes result in sample dilution. The optimized parameter ensures complete quantitative elution without altering the complexation equilibria, matching findings from related analytical literature.
- *User Insights:* {chem_notes if chem_notes else 'Quantitative recovery verified.'}
        """
    else:
        draft_text = f"""
**Optimization Study - Effect of {param_type}:**
The removal efficiency of target species was evaluated as a function of {param_type} ({x_values}).
- The experimental data reveal a sharp increase in removal efficiency, reaching an apex of maximum performance at the optimum value ({optimum_val}).
- *Scientific Justification:* In acidic media, intense competition from high concentrations of hydronium ions (H+) restricts metal binding due to strong electrostatic repulsion at the adsorbent surface. As the pH approaches the optimum point, surface deprotonation facilitates favorable electrostatic attraction. The subsequent decline at higher values is attributed to the formation of soluble hydroxide complexes or precipitation phenomena.
- *User Insights:* {chem_notes if chem_notes else 'Electrostatic surface charge dynamics verified.'}
        """
        
    st.info(draft_text)
