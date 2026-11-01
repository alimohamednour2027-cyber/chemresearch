import streamlit as st

st.set_page_config(
    page_title="ChemResearch AI: Optimization Parameters Hub",
    layout="wide"
)

st.title("ChemResearch AI: Advanced Optimization Parameters Hub")
st.markdown("وحدة تحليلية متقدمة لدراسة معلمات التحسين والتحليل الميكانيكي.")
st.markdown("---")

# اختيار نظام الدراسة
study_mode = st.selectbox(
    "Select experiment type / اختر نوع التجربة:",
    [
        "Adsorption (Surface capacity, thermodynamics & isotherms)",
        "SPE / MSPE (Solid-phase microextraction and preconcentration)",
        "Removal (Pollutant remediation, real wastewater & reusability)"
    ]
)

st.markdown("---")
st.subheader("إدخال بيانات المعلمة والنتائج الكمية:")

col1, col2 = st.columns(2)

if "Adsorption" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", ["Initial Concentration", "Adsorbent Dosage", "Contact Time", "Temperature", "Initial pH"])
        x_vals = st.text_input("Parameter Values:", value="10, 25, 50, 100, 200")
    with col2:
        y_vals = st.text_input("Performance Values:", value="5.2, 12.5, 24.1, 38.5, 42.0")
        opt_val = st.text_input("Optimum Point:", value="100 mg/L")

elif "SPE" in study_mode:
    with col1:
        param_type = st.selectbox("Select Parameter:", ["Eluent Volume", "Sample Volume", "Extraction Time", "Sample pH"])
        x_vals = st.text_input("Parameter Values:", value="1, 2, 5, 10")
    with col2:
        y_vals = st.text_input("Performance Values (% Recovery):", value="75.2, 98.5, 91.0, 88.4")
        opt_val = st.text_input("Optimum Point:", value="2 mL")

else:
    with col1:
        param_type = st.selectbox("Select Parameter:", [
            "Initial Pollutant Concentration",
            "Adsorbent Dosage",
            "Contact Time",
            "Solution Temperature",
            "Initial pH Optimization",
            "Co-existing Ions",
            "Ionic Strength",
            "Regeneration Cycles",
            "Real Wastewater Application",
            "Fixed-Bed Column Parameters"
        ])
        x_vals = st.text_input("Parameter Values:", value="5, 10, 25, 50, 100")
    with col2:
        y_vals = st.text_input("Performance Values (% Removal):", value="35.0, 62.5, 96.8, 85.0, 68.2")
        opt_val = st.text_input("Optimum Point:", value="pH 6.0 / 25 mg/L")

st.markdown("---")
st.subheader("الملاحظات والمراجع المفهرسة:")
ref_tag = st.text_input("Reference Citation Tag:", value="Ref. [1] (Smith et al., 2024)")
chem_notes = st.text_area("Mechanistic Observations:", value="Confirmed through reproducible triplicate runs.")

if st.button("توليد مسودة المناقشة العلمية", key="btn_opt_gen"):
    st.success("تم توليد التحليل بنجاح!")
    
    discussion_text = f"""
**Dynamic Mechanistic Analysis for {param_type}:**
- Evaluated across the experimental range ({x_vals}), achieving peak performance metrics ({y_vals}) at the optimized threshold of **{opt_val}**.
- *Contextual Scientific Justification:* As documented in **{ref_tag}**, this parameter strictly governs the interfacial mass transfer, surface charge dynamics, and thermodynamic spontaneity of the system.
- *Specific Empirical Note:* {chem_notes}
    """.strip()
    
    st.info(discussion_text)
