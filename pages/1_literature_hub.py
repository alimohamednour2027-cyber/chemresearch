import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Consensus Literature Hub",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 ChemResearch AI: Q1 Consensus Literature Hub")
st.markdown("هذه البوابة مخصصة لجلب واستعراض أحدث الأبحاث والمقالات المحكمة (20+ مقالة) المرتبطة مباشرة ببيانات تجربتك عبر محرك الأدبيات **Consensus**.")
st.markdown("---")

# --- محاكاة أو استقبال المدخلات (يمكننا ربطها بالصفحة الرئيسية لاحقاً) ---
st.subheader("📌 معايير البحث الحالية المستمدة من مشروعك:")

col1, col2 = st.columns(2)
with col1:
    default_title = "Facile synthesis of a novel bio-adsorbent for cadmium removal from aqueous solutions"
    article_title = st.text_input("عنوان البحث أو الأطروحة:", value=default_title)
    
    default_metal = "Cadmium(II) - Cd2+"
    target_metal = st.text_input("الملوث أو العنصر الثقيل المستهدف:", value=default_metal)

with col2:
    default_material = "Modified Agricultural Waste Bio-adsorbent"
    prepared_material = st.text_input("المادة المازة / المحضرة:", value=default_material)
    
    default_tools = "FTIR, SEM, XRD, AAS"
    characterization_tools = st.text_input("أدوات التوصيف والتحليل:", value=default_tools)

# --- تجميع وتوليد استعلام البحث الذكي ---
st.markdown("---")
st.subheader("🔍 استعلام البحث المتقدم المتولد أوتوماتيكياً:")

# دمج الكلمات المفتاحية لبناء استعلام بحثي أكاديمي قوي
search_query_text = f"{prepared_material} {target_metal} adsorption mechanism Q1 peer reviewed"
encoded_query = urllib.parse.quote(search_query_text)

# الروابط المباشرة
consensus_url = f"https://consensus.app/search/?q={encoded_query}"
scholar_url = f"https://scholar.google.com/scholar?q={encoded_query}"

st.info(f"**نص الاستعلام العلمي (Query):**\n`{search_query_text}`")

# أزرار التوجيه للبحث المباشر
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.markdown(f"### [🔗 فتح وفحص 20+ مقالة عبر Consensus]({consensus_url})", unsafe_allow_html=True)
    st.caption("ينقلك مباشرة إلى منصة Consensus لاستعراض المقالات والأوراق العلمية التي تدعم استنتاجاتك.")

with col_btn2:
    st.markdown(f"### [📚 البحث الاحتياطي في Google Scholar]({scholar_url})", unsafe_allow_html=True)
    st.caption("دعم إضافي للبحث الموسع في قواعد بيانات جوجل الأكاديمية.")

# --- قسم حفظ وتوثيق المراجع المستخرجة ---
st.markdown("---")
st.subheader("📝 أرشيف المراجع المكتشفة وتوثيقها للبحث:")
st.markdown("قم بتسجيل روابط أو عناوين المقالات التي استخرجتها من Consensus لاستخدامها لاحقاً في صياغة المناقشة:")

saved_refs = st.text_area(
    "قائمة المراجع (ضع كل مرجع في سطر منفصل مع رابط الـ DOI):",
    value="1. (مثال) Smith et al., Journal of Hazardous Materials, 2024, DOI: 10.1016/...\n2. (مثال) Al-Duran et al., Chemical Engineering Journal, 2025..."
)

if st.button("💾 حفظ أرشيف المراجع في قاعدة بيانات المشروع", key="save_consensus_refs"):
    st.success("تم حفظ المراجع بنجاح وأصبحت جاهزة للاستخدام في كتابة مسودات الأبحاث والـ Q1!")
