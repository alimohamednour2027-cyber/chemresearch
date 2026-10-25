import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="AI-Visual Lab Graphical Abstract Generator",
    page_icon="🤖",
    layout="wide"
)

# --- العنوان والمقدمة ---
st.title("🤖 ChemResearch AI: AI-Powered Visual Graphical Abstract Generator")
st.markdown("هذا المحرك يستخدم الذكاء الاصطناعي المتقدم لتحويل وصفك النصي إلى مخطط بصري احترافي بأيقونات مختبرية حقيقية (مشابه للمقالات المنشورة).")
st.markdown("---")

# --- إعدادات القائمة الجانبية (مهمة لـ API Key) ---
st.sidebar.title("🔑 Gemini API Configuration")
st.sidebar.markdown("لتوليد الصور، يرجى إدخال مفتاح الـ API الخاص بك هنا:")
api_key_input = st.sidebar.text_input("Enter Gemini API Key (Required for Image Generation):", type="password", value="")

# --- حقل إدخال النص ---
st.subheader("✍️ أدخل خطوات العملية المخبرية (الرجاء استخدام اللغة الإنجليزية لأفضل النتائج):")
default_steps = """1. Precursor Preparation: Grinding and washing raw agricultural waste.
2. Chemical Impregnation: Mixing with KOH activating agent.
3. Pyrolysis: Carbonization in a tube furnace at 800°C under N2 flow.
4. Washing & Drying: Neutralization and oven drying to obtain final bio-adsorbent."""

synthesis_input = st.text_area("Laboratory Synthesis Steps Protocol:", value=default_steps, height=220)
abstract_title = st.text_input("عنوان المخطط:", value="Extraction Process Flowchart of Bio-Adsorbent")

# --- زر التوليد ---
if st.button("🚀 Generate AI-Visual Graphical Abstract (Image)", key="gen_ai_image_abstract"):
    if not synthesis_input.strip():
        st.error("الرجاء إدخال خطوات التجربة.")
    elif not api_key_input:
        st.error("الرجاء إدخال Gemini API Key في القائمة الجانبية لتوليد الصور.")
    else:
        with st.spinner("جاري استخدام الذكاء الاصطناعي لتوليد المخطط البصري... (قد يستغرق وقتاً)"):
            # --- في المرحلة القادمة سنقوم بربط هذا الجزء بـ Gemini Image API ---
            # حالياً، سنعرض رسالة توضيحية بأن النظام جاهز للعمل
            
            st.success("تم تحليل خطواتك بنجاح. النظام الآن جاهز للاتصال بمولد الصور!")
            
            # هذه رسالة مؤقتة للتأكد من أن الكود يعمل
            st.info(f"Title: {abstract_title}")
            st.info(f"Steps to visualize: {synthesis_input}")
            
            st.warning("⚠️ ملاحظة للمستخدم: نظراً لأن هذه الأداة هي النموذج الأولي (Prototype)، سأقوم بربطها الفعلي بمولد صور Gemini في الخطوة التالية. هل أنت مستعد لتجربة التوليد الفعلي؟")
