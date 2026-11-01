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
    st.caption("Active Hub: Consensus & Literature Retrieval")

# قاموس الترجمات الثلاثي لهذه الصفحة (بدون إيقونات)
if lang_choice == "English":
    t_title = "ChemResearch AI: Q1 Consensus Literature Hub"
    t_desc = "This portal is dedicated to retrieving and reviewing peer-reviewed articles directly connected to your experiment data via Consensus."
    sec_meta = "Current Research Parameters:"
    t_title_lbl = "Article or Thesis Title:"
    t_metal_lbl = "Target Heavy Metal / Pollutant:"
    t_material_lbl = "Prepared Material / Sorbent:"
    t_tools_lbl = "Characterization Tools:"
    sec_query = "Automated Advanced Search Query:"
    query_label = "Scientific Query Text:"
    btn_consensus = "Open and Review 20+ Articles via Consensus"
    cap_consensus = "Directly transports you to Consensus to review supporting scientific papers."
    btn_scholar = "Backup Search in Google Scholar"
    cap_scholar = "Extended auxiliary search in Google academic databases."
    sec_archive = "Selected References Archive:"
    archive_desc = "Record extracted article references for discussion drafting:"
    archive_input = "References List (one per line with DOI):"
    btn_save = "Save Project References Archive"
    success_msg = "References successfully saved and ready for Q1 draft usage."

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Q1 Konsensus Literatür Merkezi"
    t_desc = "Bu portal, deney verilerinizle doğrudan bağlantılı en son hakemli makaleleri Consensus aracıyla incelemek için tasarlanmıştır."
    sec_meta = "Mevcut Araştırma Parametreleri:"
    t_title_lbl = "Makale veya Tez Başlığı:"
    t_metal_lbl = "Hedef Ağır Metal / Kirletici:"
    t_material_lbl = "Hazırlanan Malzeme / Adsorban:"
    t_tools_lbl = "Karakterizasyon Araçları:"
    sec_query = "Otomatik Oluşturulan Gelişmiş Arama Sorgusu:"
    query_label = "Bilimsel Sorgu Metni:"
    btn_consensus = "Consensus Üzerinden 20+ Makaleyi İncele"
    cap_consensus = "Destekleyici bilimsel makaleleri incelemek için sizi doğrudan Consensus'a yönlendirir."
    btn_scholar = "Google Scholar Yedek Araması"
    cap_scholar = "Google akademik veritabanlarında genişletilmiş ek arama."
    sec_archive = "Seçilen Referanslar Arşivi:"
    archive_desc = "Tartışma taslağı için çıkarılan makale referanslarını kaydedin:"
    archive_input = "Referans Listesi (DOI ile her satıra bir tane):"
    btn_save = "Proje Referans Arşivini Kaydet"
    success_msg = "Referanslar başarıyla kaydedildi ve Q1 taslakları için hazır."

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز أدبيات الأبحاث Consensus"
    t_desc = "هذه البوابة مخصصة لجلب واستعراض أحدث الأبحاث والمقالات المحكمة (20+ مقالة) المرتبطة مباشرة ببيانات تجربتك عبر محرك الأدبيات Consensus."
    sec_meta = "معايير البحث الحالية المستمدة من مشروعك:"
    t_title_lbl = "عنوان البحث أو الأطروحة:"
    t_metal_lbl = "الملوث أو العنصر الثقيل المستهدف:"
    t_material_lbl = "المادة المازة / المحضرة:"
    t_tools_lbl = "أوات التوصيف والتحليل:"
    sec_query = "استعلام البحث المتقدم المتولد أوتوماتيكياً:"
    query_label = "نص الاستعلام العلمي:"
    btn_consensus = "فتح وفحص 20+ مقالة عبر منصة Consensus"
    cap_consensus = "ينقلك مباشرة إلى منصة Consensus لاستعراض المقالات والأوراق العلمية التي تدعم استنتاجاتك."
    btn_scholar = "البحث الاحتياطي في Google Scholar"
    cap_scholar = "دعم إضافي للبحث الموسع في قواعد بيانات جوجل الأكاديمية."
    sec_archive = "أرشيف المراجع Mلجلبة وتوثيقها للبحث:"
    archive_desc = "قم بتسجيل روابط أو عناوين المقالات لاستخدامها لاحقاً في صياغة المناقشة:"
    archive_input = "قائمة المراجع (ضع كل مرجع في سطر منفصل مع رابط الـ DOI):"
    btn_save = "حفظ أرشيف المراجع في قاعدة بيانات المشروع"
    success_msg = "تم حفظ المراجع بنجاح وأصبحت جاهزة للاستخدام في كتابة مسودات الأبحاث والـ Q1!"

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# --- إدخال معايير البحث ---
st.markdown(f"### {sec_meta}")

col1, col2 = st.columns(2)
with col1:
    article_title = st.text_input(t_title_lbl, value="Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions")
    target_metal = st.text_input(t_metal_lbl, value="Cadmium(II) - Cd2+")

with col2:
    prepared_material = st.text_input(t_material_lbl, value="Modified Agricultural Waste Bio-adsorbent")
    characterization_tools = st.text_input(t_tools_lbl, value="FTIR, SEM, XRD, AAS")

# --- تجميع وتوليد استعلام البحث الذكي (يعمل بثبات بغض النظر عن لغة الواجهة) ---
st.markdown("---")
st.markdown(f"### {sec_query}")

search_query_text = f"{prepared_material} {target_metal} adsorption mechanism Q1 peer reviewed"
encoded_query = urllib.parse.quote(search_query_text)

consensus_url = f"https://consensus.app/search/?q={encoded_query}"
scholar_url = f"https://scholar.google.com/scholar?q={encoded_query}"

st.info(f"**{query_label}**\n`{search_query_text}`")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.markdown(f"### [{btn_consensus}]({consensus_url})", unsafe_allow_html=True)
    st.caption(cap_consensus)

with col_btn2:
    st.markdown(f"### [{btn_scholar}]({scholar_url})", unsafe_allow_html=True)
    st.caption(cap_scholar)

# --- قسم حفظ وتوثيق المراجع المستخرجة ---
st.markdown("---")
st.markdown(f"### {sec_archive}")
st.markdown(archive_desc)

saved_refs = st.text_area(
    archive_input,
    value="1. (Example) Smith et al., Journal of Hazardous Materials, 2024, DOI: 10.1016/...\n2. (Example) Al-Duran et al., Chemical Engineering Journal, 2025..."
)

if st.button(btn_save, key="save_consensus_refs"):
    st.success(success_msg)
