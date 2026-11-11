import streamlit as st
from google import genai
import time
import pypdf

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Claude / Q1 Introduction Hub",
    layout="wide"
)

# --- تنسيق CSS المخصص للشريط الجانبي والهيدر ---
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

# --- الشريط الجانبي: إعدادات الـ API ---
with st.sidebar:
    st.markdown("### 🔑 API Configuration")
    api_key_input = st.text_input("Enter your Gemini API Key:", type="password", value="")
    st.markdown("---")
    st.markdown("### Module Status")
    st.caption("Active Hub: Q1 Expert Introduction Synthesis Engine")

# --- عرض الهيدر ---
st.markdown("""
    <div class="custom-header">
        <h1>ChemResearch AI: Q1 Expert Introduction Synthesizer</h1>
        <p>Generate rigorous, high-impact Q1 journal introductions based on uploaded reference papers and precise experimental parameters.</p>
    </div>
""", unsafe_allow_html=True)

# --- استخراج نص ملفات الـ PDF المرفوعة ---
def extract_text_from_pdfs(uploaded_files):
    all_text = ""
    for file in uploaded_files:
        try:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
    return all_text

# --- مدخلات البيانات الخاصة بالبحث ---
st.markdown("### 📋 Research Parameters & Configuration")

col1, col2 = st.columns(2)
with col1:
    paper_title = st.text_input("Research Title:", value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions")
    target_metal = st.text_input("Target Pollutant / Heavy Metal:", value="Cadmium(II) - Cd2+")
    adsorbent_material = st.text_input("Prepared Adsorbent / Material:", value="Modified Agricultural Waste Bio-adsorbent")
    fields_text = st.text_input("Research Fields / Domain:", value="Environmental Chemistry, Wastewater Remediation, Nanomaterial Adsorbents")

with col2:
    characterization_tools = st.text_input("Characterization Tools:", value="FTIR, SEM, XRD, AAS, BET")
    journal_style = st.selectbox("Target Journal Standard:", ["Elsevier - Journal of Hazardous Materials", "Elsevier - Chemical Engineering Journal", "ACS Sustainable Chemistry & Engineering", "RSC Advances"])
    citation_format = st.selectbox("Citation Format Style:", ["[1], [2], [3] (Sequential Numbers)", "Author-Year (e.g., Smith et al., 2024)"])

st.markdown("---")
st.markdown("### 📚 Reference Papers Upload (PDF)")
uploaded_refs = st.file_uploader("Upload review or research reference papers (PDFs):", type=["pdf"], accept_multiple_files=True)

# --- زر التنفيذ والتوليد ---
st.markdown("---")
if st.button("🚀 Synthesize Q1 Introduction Hub", type="primary"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key in the sidebar.")
    else:
        with st.spinner("Analyzing references and drafting rigorous Q1 introduction..."):
            extracted_pdf_text = extract_text_from_pdfs(uploaded_refs) if uploaded_refs else "No specific PDF files provided. Use general expert knowledge matching the parameters."
            
            # صياغة الـ Prompt بدقة متناهية بناءً على وصفك الاحترافي
            expert_prompt = f"""
            You are an expert analytical chemistry researcher and professional academic writer who publishes papers in top-tier Q1 scientific journals.
            Your task is to study and analyze only the Introduction section based on the uploaded references, and write a comprehensive, rigorous, and completely original "Introduction" section tailored for top-tier Q1 scientific journals.

            Strict formatting and citation rules:
            1. Strictly FORBIDDEN to use markdown formatting such as asterisks (*), bold, or italic in any part of the text. The text must be clean and plain.
            2. Ensure that reference numbers or citation formats (author-date) are unique, sequential, and non-repetitive (e.g., [1], [2], [3], without repeating numbers in the same or consecutive phrases).
            3. Analyze the extracted texts from the attached reference papers to build an introduction with a funnel structure (from general to specific):
               - Paragraph 1: Global environmental impact and toxicity of the target pollutant.
               - Paragraph 2: Shortcomings, drawbacks, and high operational costs of conventional treatment methods.
               - Paragraph 3: Identification of the core research gap in current literature.
               - Paragraph 4: Introduction of the innovative material (adsorbent) prepared, highlighting its novelty and excellence.
            4. At the end of the text, include a dedicated "References" section containing unique sources derived from the attached papers, arranged according to academic standards, without any markdown formatting (like asterisks).
            5. Avoid complex LaTeX formulas (use standard text formatting, e.g., Cu2+, Cd2+, qm, R2 > 0.99).

            Research Data:
            - Title: {paper_title}
            - Target Pollutant: {target_metal}
            - Prepared Adsorbent: {adsorbent_material}
            - Fields: {fields_text}
            - Characterization Tools: {characterization_tools}
            - Journal Standards: {journal_style}
            - Citation Format: {citation_format}

            Extracted Text from Reference Papers:
            {extracted_pdf_text[:15000]}

            Write in rigorous academic English suitable for top-tier Q1 journals.
            """

            max_retries = 3
            success = False
            final_output = ""
            last_err = ""

            for attempt in range(max_retries):
                try:
                    client = genai.Client(api_key=api_key_input)
                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=expert_prompt,
                    )
                    # إزالة أي علامات نجمية أو تداخل للتأكد من نظافة النص تماماً
                    cleaned_output = response.text.replace('*', '').replace('###', '')
                    final_output = cleaned_output
                    success = True
                    break
                except Exception as e:
                    last_err = str(e)
                    if "503" in str(e) or "UNAVAILABLE" in str(e):
                        time.sleep(3)
                    else:
                        break

            if success:
                st.success("Q1 Introduction synthesized successfully with zero formatting clutter!")
                st.markdown("### 📄 Generated Q1 Introduction Draft:")
                st.text_area("Copy your final introduction text below:", value=final_output, height=450)
            else:
                st.error(f"Generation failed due to error: {last_err}")
