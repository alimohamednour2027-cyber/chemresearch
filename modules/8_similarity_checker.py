import streamlit as st
from difflip import SequenceMatcher

# --- قواميس اللغات الثلاثة (الإنجليزية، التركية، العربية) ---
translations = {
    "English": {
        "title": "Manuscript Similarity & Plagiarism Screening Hub",
        "desc": "Advanced preliminary screening module for Q1 analytical chemistry journal submissions and academic drafting.",
        "draft_label": "Draft Manuscript Text",
        "draft_placeholder": "Enter draft text here...",
        "ref_label": "Reference Literature Text",
        "ref_placeholder": "Enter reference text here...",
        "btn_text": "Run Similarity Analysis",
        "report_title": "Analysis Report & Q1 Benchmarks",
        "similarity_score": "Similarity Score",
        "draft_words": "Draft Word Count",
        "ref_words": "Reference Word Count",
        "warning": "Warning: Similarity index exceeds the recommended Q1 threshold (typically under 10-15%). Paraphrasing is strongly advised.",
        "success": "Status: Similarity index is within the safe academic threshold for international journal submissions.",
        "error_text": "Please provide both draft and reference texts to execute the comparison.",
        "note": "System Note: This module performs local semantic comparison to assist researchers in refining manuscript phrasing before formal journal submission."
    },
    "Türkçe": {
        "title": "Makale Benzerliği ve İntihal Tarama Merkezi",
        "desc": "Q1 analitik kimya dergisi gönderimleri ve akademik taslaklar için gelişmiş ön tarama modülü.",
        "draft_label": "Taslak Makale Metni",
        "draft_placeholder": "Taslak metni buraya girin...",
        "ref_label": "Referans Literatür Metni",
        "ref_placeholder": "Referans metni buraya girin...",
        "btn_text": "Benzerlik Analizini Çalıştır",
        "report_title": "Analiz Raporu ve Q1 Kriterleri",
        "similarity_score": "Benzerlik Oranı",
        "draft_words": "Taslak Kelime Sayısı",
        "ref_words": "Referans Kelime Sayısı",
        "warning": "Uyarı: Benzerlik oranı önerilen Q1 eşiğini (genellikle %10-15 altı) aşıyor. Yeniden ifade etme şiddetle tavsiye edilir.",
        "success": "Durum: Benzerlik oranı, uluslararası dergi gönderimleri için güvenli akademik eşiktedir.",
        "error_text": "Karşılaştırma yapmak için lütfen hem taslak hem de referans metinlerini girin.",
        "note": "Sistem Notu: Bu modül, araştırmacılara dergi gönderimi öncesinde makale ifadelerini geliştirmelerinde yardımcı olmak için yerel anlamsal karşılaştırma yapar."
    },
    "العربية": {
        "title": "منصة فحص التشابه والاقتباس للأوراق البحثية",
        "desc": "وحدة الفحص المبدئي المتقدمة لتقديمات مجلات الكيمياء التحليلية Q1 والصياغة الأكاديمية.",
        "draft_label": "نص المسودة الأكاديمية",
        "draft_placeholder": "ألصق نص المسودة هنا...",
        "ref_label": "نص الأدبيات والمراجع",
        "ref_placeholder": "ألصق نص المرجع أو الأدبيات هنا...",
        "btn_text": "تشغيل فحص التشابه والاقتباس",
        "report_title": "تقرير التحليل ومعايير Q1",
        "similarity_score": "نسبة التشابه والتطابق",
        "draft_words": "كلمات المسودة",
        "ref_words": "كلمات المرجع",
        "warning": "تنبيه: نسبة التشابه تتجاوز الحد المقبول عموماً في مجلات Q1 (أقل من 10-15%). يوصى بشدة إعادة الصياغة.",
        "success": "حالة ممتازة: نسبة التشابه ضمن النطاق الآمن والمقبول أكاديمياً للنشر الدولي.",
        "error_text": "الرجاء إدخال نص المسودة والنص المرجعي لإتمام المقارنة.",
        "note": "ملاحظة النظام: تقوم هذه الوحدة بمقارنة دلالية محلية لمساعدة الباحثين في تنقيح صياغة المخطوطة قبل التقديم الرسمي للمجلة."
    }
}

# --- اختيار اللغة من الشريط الجانبي ---
selected_lang = st.sidebar.selectbox("Select Language / Dil Seçin / اختر اللغة", ["English", "Türkçe", "العربية"])
t = translations[selected_lang]

# --- تنسيق CSS المخصص الموحد ---
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

# --- ترويسة الصفحة مترجمة ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t['title']}</h1>
        <p>{t['desc']}</p>
    </div>
""", unsafe_allow_html=True)

# --- حقول إدخال النصوص ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### {t['draft_label']}")
    draft_text = st.text_area("", height=280, placeholder=t['draft_placeholder'], key="draft_input")

with col2:
    st.markdown(f"### {t['ref_label']}")
    reference_text = st.text_area("", height=280, placeholder=t['ref_placeholder'], key="ref_input")

st.markdown("<br>", unsafe_allow_html=True)

# --- زر التنفيذ والتحليل ---
if st.button(t['btn_text'], use_container_width=True):
    if draft_text.strip() and reference_text.strip():
        matcher = SequenceMatcher(None, draft_text, reference_text)
        similarity_ratio = matcher.ratio() * 100
        
        st.markdown("---")
        st.markdown(f"### {t['report_title']}")
        
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric(t['similarity_score'], f"{similarity_ratio:.2f}%")
        m_col2.metric(t['draft_words'], len(draft_text.split()))
        m_col3.metric(t['ref_words'], len(reference_text.split()))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if similarity_ratio > 15:
            st.warning(t['warning'])
        else:
            st.success(t['success'])
            
    else:
        st.error(t['error_text'])

st.markdown("---")
st.info(t['note'])
