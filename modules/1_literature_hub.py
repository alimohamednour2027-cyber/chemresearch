import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Consensus Literature Hub",
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
    st.markdown("### Literature Hub Navigation")
    st.caption("Active Hub: Consensus & Literature Retrieval (Independent)")

# قاموس الترجمات الثلاثي لهذه الصفحة
if lang_choice == "English":
    t_title = "ChemResearch AI: Q1 Consensus Literature Hub"
    t_desc = "This portal is dedicated to retrieving and reviewing peer-reviewed articles directly connected to your experiment data via Consensus."
    sec_meta = "Current Research Parameters:"
    t_title_lbl = "Article or Thesis Title:"
    sec_query = "Automated Advanced Search Query (Prompt Format):"
    query_label = "Generated Scientific Search Prompt:"
    btn_consensus = "Open and Review 20+ Articles via Consensus"
    cap_consensus = "Directly transports you to Consensus to review supporting scientific papers."
    btn_scholar = "Backup Search in Google Scholar"
    cap_scholar = "Extended auxiliary search in Google academic databases."

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Q1 Konsensus Literatür Merkezi"
    t_desc = "Bu portal, deney verilerinizle doğrudan bağlantılı en son hakemli makaleleri Consensus aracıyla incelemek için tasarlanmıştır."
    sec_meta = "Mevcut Araştırma Parametreleri:"
    t_title_lbl = "Makale veya Tez Başlığı:"
    sec_query = "Otomatik Oluşturulan Gelişmiş Arama Sorgusu (Prompt Formatı):"
    query_label = "Oluşturulan Bilimsel Arama Promptu:"
    btn_consensus = "Consensus Üzerinden 20+ Makaleyi İncele"
    cap_consensus = "Destekleyici bilimsel makaleleri incelemek için sizi doğrudan Consensus'a yönlendirir."
    btn_scholar = "Google Scholar Yedek Araması"
    cap_scholar = "Google akademik veritabanlarında genişletilmiş ek arama."

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز أدبيات الأبحاث Consensus"
    t_desc = "هذه البوابة مخصصة لجلب واستعراض أحدث الأبحاث والمقالات المحكمة (20+ مقالة) المرتبطة مباشرة ببيانات تجربتك عبر محرك الأدبيات Consensus."
    sec_meta = "معايير البحث الحالية:"
    t_title_lbl = "عنوان البحث أو الأطروحة:"
    sec_query = "استعلام البحث المتقدم المتولد أوتوماتيكياً (صيغة Prompt):"
    query_label = "نص الـ Prompt البحثي المتولد:"
    btn_consensus = "فتح وفحص 20+ مقالة عبر منصة Consensus"
    cap_consensus = "ينقلك مباشرة إلى منصة Consensus لاستعراض المقالات والأوراق العلمية التي تدعم استنتاجاتك."
    btn_scholar = "البحث الاحتياطي في Google Scholar"
    cap_scholar = "دعم إضافي للبحث الموسع في قواعد بيانات جوجل الأكاديمية."

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# --- إدخال خانة عنوان البحث فقط في القسم الأول ---
st.markdown(f"### {sec_meta}")

article_title = st.text_input(
    t_title_lbl, 
    value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions",
    key="independent_article_title"
)

# --- توليد استعلام البحث المتقدم على شكل Prompt فوري ومتغير بناءً على العنوان فقط ---
st.markdown("---")
st.markdown(f"### {sec_query}")

search_prompt_text = f"Find peer-reviewed Q1 literature investigating '{article_title}' focusing on adsorption mechanisms, heavy metal removal, and advanced characterization."
encoded_query = urllib.parse.quote(article_title + " adsorption mechanism Q1 peer reviewed")

consensus_url = f"https://consensus.app/search/?q={encoded_query}"
scholar_url = f"https://scholar.google.com/scholar?q={encoded_query}"

# عرض الـ Prompt المحدث لحظياً بمجرد تعديل عنوان البحث
st.info(f"**{query_label}**\n\n`{search_prompt_text}`")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.markdown(f"### [{btn_consensus}]({consensus_url})", unsafe_allow_html=True)
    st.caption(cap_consensus)

with col_btn2:
    st.markdown(f"### [{btn_scholar}]({scholar_url})", unsafe_allow_html=True)
    st.caption(cap_scholar)
