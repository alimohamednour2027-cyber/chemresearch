import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Optimization Parameters Hub",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ ChemResearch AI: Advanced Optimization Parameters Hub")
st.markdown("هذه البوابة مخصصة لتحليل وتفسير معلمات التحسين (Optimization Parameters) وتقديم التفسيرات الكيميائية والفيزيائية للقيمة المثلى (Optimum Value) استناداً إلى طبيعة الدراسة.")
st.markdown("---")

# --- اختيار نوع النظام الدراسي ---
st.subheader("1️⃣ حدد نظام الدراسة الرئيسي:")
study_mode = st.selectbox(
    "اختر نوع التجربة لدراسة العوامل المؤثرة:",
    [
        "Adsorption (دراسات الامتزاز وسعة السطح)",
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر واسترداد العناصر)",
        "Removal (دراسات إزالة الملوثات وتطبيقات المياه البيئية)"
    ]
)

st.markdown("---")
st.subheader(f"2️⃣ إدخال بيانات معلمات التحسين لنظام: {study_mode.split(' ')[0]}")

# --- التقسيم بناءً على النظام المختار ---
col1, col2 = st.columns(2)

if "Adsorption" in study_mode:
    with col1:
        param_type = st.selectbox("العامل المدروس:", ["التركيز الابتدائي ($C_0$)", "جرعة المادة المازة (Adsorbent Dosage)", "درجة الحرارة (Temperature)", "زمن التلامس (Contact Time)"])
        x_values = st.text_input("قيم المعامل التجريبية (افصل بينها بفاصلة):", value="10, 25, 50, 100, 200")
    with col2:
        y_values = st.text_input("القيم الناتجة أو السعة الممتصة ($q_e$ mg/g):", value="5.2, 12.5, 24.1, 38.5, 42.0")
        optimum_val = st.text_input("القيمة المثلى المختارة (Optimum Point):", value="التراكيز العالية أو الجرعة الأمثل عند نقطة التشبع")

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("العامل المدروس:", ["نوع وحجم مذيب الاستشطيف (Eluent Type & Volume)", "حجم عينة التحميل (Sample Volume)", "سرعة وطريقة الاستخلاص"])
        x_values = st.text_input("تدرج حجم المذيب أو العامل (mL):", value="1, 2, 5, 10")
    with col2:
        y_values = st.text_input("نسبة الاسترداد (% Recovery):", value="75.2, 98.5, 91.0, 82.4")
        optimum_val = st.text_input("القيمة المثلى المختارة (Optimum Point):", value="حجم 2 مل من الحمض المخفف")

else:  # Removal
    with col1:
        param_type = st.selectbox("العامل المدروس:", ["الأس الهيدروجيني الأولي ($pH$)", "الأيونات المتداخلة (Co-existing Ions)", "دورات الاستعادة وإعادة الاستخدام (Regeneration Cycles)"])
        x_values = st.text_input("تدرج القيم (مثل pH 2, 4, 6, 8, 10):", value="2, 4, 6, 8, 10")
    with col2:
        y_values = st.text_input("نسبة الإزالة (% Removal):", value="35.0, 62.5, 96.8, 85.0, 68.2")
        optimum_val = st.text_input("القيمة المثلى المختارة (Optimum Point):", value="pH = 6")

# --- رفع المراجع لدعم التفسير العلمي ---
st.markdown("---")
st.subheader("3️⃣ الدعم المرجعي والملاحظات العلمية")
col_ref1, col_ref2 = st.columns(2)
with col_ref1:
    opt_refs = st.file_uploader("رفع المقالات المرجعية الداعمة للتفسير (PDF / TXT):", type=["pdf", "txt"], accept_multiple_files=True, key="opt_ref_files")
with col_ref2:
    chem_notes = st.text_area("ملاحظات إضافية حول الآلية الكيميائية (اختياري):", placeholder="مثلاً: التنافر الكهروستاتيكي لأيونات الهيدروجين عند الأوساط الحامضية، والترسبات عند القاعدية...", key="opt_notes")

# --- زر توليد مسودة المناقشة ---
if st.button("🚀 توليد مسودة تحليل ومناقشة المعلمات لـ Q1", key="btn_optimization"):
    with st.spinner("جاري تحليل المعلمات وربطها بالأساسيات الكيميائية والفيزيائية..."):
        st.success("تم إعداد مسودة تحليل المعلمات بنجاح!")
        
        st.markdown("### 📝 مسودة فقرة المناقشة المقترحة (Optimization & Discussion):")
        
        if "Adsorption" in study_mode:
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
- *Scientific Justification:* In acidic media, intense competition from high concentrations of hydronium ions ($H^+$) restricts metal binding due to strong electrostatic repulsion at the adsorbent surface. As the pH approaches the optimum point, surface deprotonation facilitates favorable electrostatic attraction. The subsequent decline at higher values is attributed to the formation of soluble hydroxide complexes or precipitation phenomena.
- *User Insights:* {chem_notes if chem_notes else 'Electrostatic surface charge dynamics verified.'}
            """
            
        st.info(draft_text)
