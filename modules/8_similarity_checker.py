import streamlit as st
from difflib import SequenceMatcher

# --- إعدادات الصفحة ---
st.markdown("""
    <style>
    .custom-header {
        background-color: #1a365d;
        color: #ffffff;
        padding: 25px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .custom-header h1 {
        color: #ffffff;
        font-weight: 800;
        margin: 0;
        font-size: 26px;
    }
    .custom-header p {
        color: #e2e8f0;
        margin: 8px 0 0 0;
        font-size: 14px;
    }
    .card-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    div.stButton > button {
        background-color: #1a365d !important;
        color: white !important;
        font-weight: 600;
        border: 1px solid #2b4c7e;
    }
    div.stButton > button:hover {
        background-color: #2b4c7e !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ترويسة الصفحة العامة للمنصة ---
st.markdown("""
    <div class="custom-header">
        <h1>Manuscript Similarity & Plagiarism Screening Hub</h1>
        <p>Advanced preliminary screening module for Q1 analytical chemistry journal submissions and academic drafting.</p>
    </div>
""", unsafe_allow_html=True)

# --- واجهة إدخال النصوص ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Draft Manuscript Text")
    draft_text = st.text_area("Paste your draft text (Introduction, Discussion, etc.):", height=280, placeholder="Enter draft text here...")

with col2:
    st.markdown("### Reference Literature Text")
    reference_text = st.text_area("Paste reference literature or source text:", height=280, placeholder="Enter reference text here...")

st.markdown("<br>", unsafe_allow_html=True)

# --- عملية التحليل والتقييم ---
if st.button("Run Similarity Analysis", use_container_width=True):
    if draft_text.strip() and reference_text.strip():
        # حساب نسبة التطابق
        matcher = SequenceMatcher(None, draft_text, reference_text)
        similarity_ratio = matcher.ratio() * 100
        
        st.markdown("---")
        st.markdown("### Analysis Report & Q1 Benchmarks")
        
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Similarity Score", f"{similarity_ratio:.2f}%")
        m_col2.metric("Draft Word Count", len(draft_text.split()))
        m_col3.metric("Reference Word Count", len(reference_text.split()))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if similarity_ratio > 15:
            st.warning("Warning: Similarity index exceeds the recommended Q1 threshold (typically under 10-15%). Paraphrasing is strongly advised.")
        else:
            st.success("Status: Similarity index is within the safe academic threshold for international journal submissions.")
            
    else:
        st.error("Please provide both draft and reference texts to execute the comparison.")

st.markdown("---")
st.info("System Note: This module performs local semantic comparison to assist researchers in refining manuscript phrasing before formal journal submission.")
