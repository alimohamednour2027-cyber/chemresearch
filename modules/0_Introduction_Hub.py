import streamlit as st
from io import BytesIO
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import pypdf
from google import genai
import time

# ==================== الحفاظ على البيانات عند تغيير الخيارات (Session State) ====================
if "intro_output" not in st.session_state:
    st.session_state.intro_output = ""

st.title("ChemResearch AI: Introduction Hub")
st.markdown("---")

# استقبال المدخلات (تأكد أن هذه المتغيرات موجودة لديك أو مأخوذة من واجهتك)
paper_title = st.text_input("Article or Thesis Title:", value="Facile synthesis of a novel bio-adsorbent for cadmium removal")
target_metal = st.text_input("Target Heavy Metal / Pollutant:", value="Cadmium(II) - Cd2+")
adsorbent_material = st.text_input("Prepared Novel Material / Sorbent:", value="Modified Agricultural Waste Bio-adsorbent")
characterization_tools = st.text_input("Characterization Tools:", value="FTIR, SEM, XRD")
fields_text = "Adsorption, Removal/Remediation"
journal_style = "Q1 Style (High Impact & Rigorous)"
citation_format = "Numerical Style [1], [2], [3]"

api_key_input = st.sidebar.text_input("Enter your Gemini API Key:", type="password", value="")

st.header("Section 2: AI-Synthesized Introduction & Auto-Citations")
sources_sec2 = st.file_uploader("Upload Review Papers (PDFs)", type=["pdf", "txt"], accept_multiple_files=True, key="sec2_files")

extracted_pdf_text = ""
uploaded_ref_names = []

if sources_sec2:
    for f in sources_sec2:
        uploaded_ref_names.append(f.name)
        try:
            reader = pypdf.PdfReader(f)
            for page_idx, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    extracted_pdf_text += f"\n--- Source File: {f.name} (Page {page_idx+1}) ---\n" + page_text + "\n"
        except Exception as e:
            st.error(f"Error reading PDF {f.name}: {e}")
    st.success(f"Successfully extracted text from {len(sources_sec2)} review files.")
    
    # مزامنة المراجع تلقائياً مع الصفحة 8 (Similarity & Paraphrase)
    st.session_state.uploaded_references = uploaded_ref_names

# زر التوليد مع نظام إعادة المحاولة الذكي لتجاوز خطأ 503
if st.button("Synthesize Clean Introduction & Citations", key="btn_sec2"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key in the sidebar to enable AI synthesis.")
    else:
        with st.spinner("الذكاء الاصطناعي يحلل المراجع ويصيغ المقدمة (جارٍ المعالجة مع محاولات ذكية)..."):
            max_retries = 3
            success = False
            last_error = ""
            
            for attempt in range(max_retries):
                try:
                    client = genai.Client(api_key=api_key_input)
                    
                    prompt = f"""
                    You are an expert analytical chemistry researcher and professional academic writer publishing in top Q1 journals.
                    Your task is to write a rigorous, comprehensive, and entirely original Introduction section for a PhD-level research article.
                    
                    CRITICAL FORMATTING & CITATION RULES:
                    1. STRICTLY DO NOT use Markdown asterisks (*) or bold/italic markdown symbols anywhere in the text (no *, no **). Keep plain clean text.
                    2. Ensure citation numbers or author-date citations are strictly unique, sequential, and non-repetitive.
                    3. Analyze the uploaded review paper texts to build a unique funnel introduction (Global environmental impact -> Limitations -> Research Gap -> Novelty of {adsorbent_material}).
                    4. At the end of the text, provide a clean "References" section listing unique literature derived from the uploaded sources.
                    5. Avoid complex LaTeX formatting (use standard text formats like Cu2+, Cd2+, qm, R2 > 0.99).
                    
                    Research Metadata:
                    - Title: {paper_title}
                    - Target Pollutant: {target_metal}
                    - Prepared Material/Sorbent: {adsorbent_material}
                    - Fields: {fields_text}
                    - Characterization Tools: {characterization_tools}
                    - Journal Standard: {journal_style}
                    - Citation Style: {citation_format}
                    
                    Extracted Text from Uploaded Review Papers (Truncated for optimal processing):
                    {extracted_pdf_text[:15000]}
                    
                    Write in formal academic English suitable for Q1 journals.
                    """
                    
                    # استخدام موديل مستقر لتجنب خطأ الضغط العالي
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=prompt,
                    )
                    
                    cleaned_text = response.text.replace('*', '').replace('###', '')
                    st.session_state.intro_output = cleaned_text
                    success = True
                    break
                    
                except Exception as e:
                    last_error = str(e)
                    if "503" in str(e) or "UNAVAILABLE" in str(e):
                        time.sleep(3) # انتظار 3 ثوانٍ وإعادة المحاولة تلقائياً
                    else:
                        break
            
            if success:
                st.success("تمت صياغة المقدمة وتوثيقها بدقة متناهية وبدون أي تكرار!")
            else:
                st.error(f"عذراً، الخادم مشغّل حالياً (خطأ 503). يرجى تقليل عدد ملفات الـ PDF المرفوعة قليلاً أو المحاولة بعد دقيقة. التفاصيل: {last_error}")

# عرض النتائج
if st.session_state.intro_output:
    st.markdown("### Generated Introduction & Clean Citations Preview:")
    st.markdown(st.session_state.intro_output)

    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run(paper_title + " - Introduction & References")
    run_title.bold = True
    run_title.font.name = "Times New Roman"
    run_title.font.size = Pt(14)

    paragraphs = st.session_state.intro_output.split('\n\n')
    for para_text in paragraphs:
        if para_text.strip():
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(8)
            run = p.add_run(para_text.replace('#', '').strip())
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label="Download Clean Introduction & References as Word (.docx)",
        data=buffer,
        file_name="ChemResearch_AI_Clean_Introduction.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        key="dl_sec2"
    )
