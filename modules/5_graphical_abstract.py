import streamlit as st

st.set_page_config(page_title="Graphical Abstract Hub", layout="wide")

st.markdown("""
    <style>
    .main-header {
        background-color: #1a365d;
        color: white;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h2>🎨 Q1 Graphical Abstract & Visual Workflow Generator</h2>
        <p>Transform raw experimental protocols and core findings into publication-ready visual workflows and structured prompts.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 📝 Enter Experimental Protocol or Core Findings:")

# استخدام key فريد لضمان قراءة التعديلات والنصوص الجديدة فوراً
experimental_input = st.text_area(
    "Paste your experimental procedure, adsorption process, or synthesis steps here:",
    height=220,
    placeholder="e.g., Synthesis of magnetic zeolite from molybdenum ore, followed by batch adsorption of heavy metals at optimized pH 6.0...",
    key="graphical_abstract_text_input"
)

style_option = st.selectbox(
    "Select Graphical Abstract Layout Style:",
    ["Step-by-Step Workflow (Synthesis -> Adsorption -> Characterization)", "Central Core Sorbent & Pollutant Removal", "Comparative Kinetic & Thermodynamic Flow"]
)

if st.button("Generate Visual Prompt & Workflow Structure", use_container_width=True, key="generate_ga_btn"):
    if not experimental_input.strip():
        st.warning("Please enter your experimental protocol first.")
    else:
        with st.spinner("Generating dynamic graphical abstract workflow and prompt..."):
            
            # توليد الـ Prompt مباشرة بناءً على النص الجديد الذي كتبه الباحث
            dynamic_prompt = f"""
            [Generated GA Prompt for Style: {style_option}]
            Create a high-resolution, professional scientific illustration representing the following protocol:
            "{experimental_input}"
            Ensure clean vector-style icons, a logical left-to-right or circular workflow, clear labels for materials, and a polished Q1 journal visual standard.
            """
            
            # تخزين النص المولد في الـ session state لضمان استمراريته
            st.session_state.latest_ga_prompt = dynamic_prompt

            st.markdown("---")
            st.markdown("### 📊 Generated Graphical Abstract Structure & Prompt:")
            
            st.markdown(f"""
                <div class="card">
                    <h4 style='color: #2b4c7e;'>✨ Active Prompt & Design Blueprint</h4>
                    <p><b>Selected Style:</b> {style_option}</p>
                    <p><b>Analyzed Input Source:</b> {experimental_input[:100]}...</p>
                    <hr>
                    <p><b>Generated Prompt for Image/Workflow:</b></p>
                    <pre style="background-color: #ffffff; padding: 10px; border-radius: 5px; border: 1px solid #cbd5e1;">{dynamic_prompt}</pre>
                </div>
            """, unsafe_allow_html=True)
            
            st.success("Prompt and workflow updated successfully based on your new input!")
            
            st.download_button(
                label="Download GA Prompt & Workflow (.txt)",
                data=dynamic_prompt,
                file_name="graphical_abstract_prompt.txt",
                mime="text/plain",
                key="download_ga_prompt_btn"
            )
