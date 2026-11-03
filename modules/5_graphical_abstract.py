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
    .ai-tool-box {
        background-color: #edf2f7;
        border-left: 4px solid #2b4c7e;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h2> Q1 Graphical Abstract & AI Visual Generator Hub</h2>
        <p>Transform your experimental protocols into professional visual workflows and utilize top AI image/text generators (ChatGPT vs. Midjourney vs. Claude).</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### Enter Experimental Protocol or Core Findings:")

# مربع الإدخال مع مفتاح فريد لضمان قراءة النصوص الجديدة فوراً
experimental_input = st.text_area(
    "Paste your experimental procedure, adsorption process, or synthesis steps here:",
    height=200,
    placeholder="e.g., Synthesis of magnetic zeolite from molybdenum ore, followed by batch adsorption of heavy metals at optimized pH 6.0...",
    key="graphical_abstract_text_input"
)

style_option = st.selectbox(
    "Select Graphical Abstract Layout Style:",
    ["Step-by-Step Workflow (Synthesis -> Adsorption -> Characterization)", "Central Core Sorbent & Pollutant Removal", "Comparative Kinetic & Thermodynamic Flow"]
)

if st.button("Generate Visual Prompt & AI Tools", use_container_width=True, key="generate_ga_btn"):
    if not experimental_input.strip():
        st.warning("Please enter your experimental protocol first.")
    else:
        with st.spinner("Generating dynamic graphical abstract workflow and AI prompts..."):
            
            # توليد الـ Prompt مباشرة بناءً على النص الجديد
            dynamic_prompt = f"""
[Q1 Graphical Abstract Prompt - Style: {style_option}]
Create a high-resolution, professional scientific illustration representing the following research protocol:
"{experimental_input}"
Requirements: Clean vector-style icons, logical left-to-right scientific workflow, clear labels for materials, color-coded phases, and polished Q1 journal visual standard.
            """
            
            # تخزين الـ Prompt في الـ session state
            st.session_state.latest_ga_prompt = dynamic_prompt

            st.markdown("---")
            st.markdown("### Generated Prompt & Design Blueprint:")
            
            st.markdown(f"""
                <div class="card">
                    <h4 style='color: #2b4c7e;'> Active Prompt for AI Image Generators</h4>
                    <p><b>Selected Style:</b> {style_option}</p>
                    <hr>
                    <pre style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #cbd5e1; white-space: pre-wrap;">{dynamic_prompt}</pre>
                </div>
            """, unsafe_allow_html=True)
            
            st.success("Prompt generated successfully! You can now copy it and use it in the AI tools below.")

st.markdown("---")

# --- قسم أدوات الـ AI ومقارنتها (ChatGPT vs Midjourney vs Claude) ---
st.markdown("### AI Tools Integration & Comparison (ChatGPT vs. Midjourney vs. Claude)")
st.markdown("Choose your preferred AI platform to render or refine the graphical abstract image based on the generated prompt above:")

col_ai1, col_ai2, col_ai3 = st.columns(3)

with col_ai1:
    st.markdown("""
        <div class="ai-tool-box">
            <h4 style='color: #1a365d; margin-top:0;'>ChatGPT / DALL-E 3</h4>
            <p><b>Best for:</b> Direct prompt execution, iterative design tweaks, and generating clear conceptual diagrams.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open ChatGPT", "https://chatgpt.com", use_container_width=True)

with col_ai2:
    st.markdown("""
        <div class="ai-tool-box">
            <h4 style='color: #1a365d; margin-top:0;'>Midjourney</h4>
            <p><b>Best for:</b> Ultra-realistic, publication-quality 3D scientific renderings and artistic vector precision.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Midjourney", "https://www.midjourney.com", use_container_width=True)

with col_ai3:
    st.markdown("""
        <div class="ai-tool-box">
            <h4 style='color: #1a365d; margin-top:0;'>Claude AI</h4>
            <p><b>Best for:</b> Deep contextual analysis, refining experimental logic, and writing precise structural prompts.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Claude", "https://claude.ai", use_container_width=True)

# زر التحميل العام للـ Prompt
if "latest_ga_prompt" in st.session_state:
    st.markdown("---")
    st.download_button(
        label=" Download Generated GA Prompt (.txt)",
        data=st.session_state.latest_ga_prompt,
        file_name="graphical_abstract_prompt.txt",
        mime="text/plain",
        key="download_ga_prompt_btn"
    )
