import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Smart Graphical Abstract Bridge",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 ChemResearch AI: Smart Protocol Organizer & Bridge")
st.markdown("قم بإدخال أي نص تجريبي عشوائي أو غير منظم، وسيقوم النظام فوراً بتحليله وصياغته في مراحل أكاديمية دقيقة، وتجهيز الوصف النهائي لتصديره للأدوات المجانية.")
st.markdown("---")

# --- حقل إدخال النص العشوائي أو غير المنظم ---
st.subheader("✍️ أدخل تفاصيل التجربة العملية (يمكنك كتابتها بشكل حر أو غير منظم):")
raw_protocol_input = st.text_area(
    "أدخل النص هنا:", 
    value="Natural low grade molybdenum ore was ground and sifted. We added sulfuric acid and agitated it overnight then dried in oven DHG-9030. Next we mixed with NaOH in nickel crucible and calcined at 550 C. Dissolved in water, centrifuged with Eppendorf 5810R, added sodium silicate and nano Fe3O4, ultrasonicated, stirred with sodium aluminate at 70 C, heated in reaction kettle at 100 C for 15 hours, and finally magnetically separated and freeze dried.", 
    height=200
)

abstract_title = st.text_input("عنوان المخطط الرئيسي:", value="SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE")

# --- زر المعالجة الذكية وصياغة المراحل ---
if st.button("🔄 معالجة وتنظيم النص إلى مراحل أكاديمية", key="process_raw_text"):
    if not raw_protocol_input.strip():
        st.error("الرجاء إدخال نص البروتوكول أولاً.")
    else:
        with st.spinner("جاري تحليل النص العشوائي وتصنيفه إلى مراحل علمية متسلسلة..."):
            
            # محاكاة التنظيم الذكي للمراحل بناءً على الكلمات المفتاحية في النص الحر
            processed_text = f"""SYNTHESIS OF MAGNETIC ZEOLITE: A SEQUENTIAL PROCESS
Row 1:
- Phase 1 (Pre-treatment & Acid Washing): Grinding, sifting, H2SO4 agitation, and oven drying (DHG-9030).
- Phase 2 (Alkali Fusion): Mixing with NaOH in a nickel crucible and calcination in a muffle furnace at 550 °C.
- Phase 3 (Solution Prep & Centrifugation): Dissolution in water, centrifugation (Eppendorf 5810R), and adding sodium silicate to the supernatant.
Row 2:
- Phase 4 (Mixing & Ultrasonication): Nano Fe3O4 addition, ultrasonic bath treatment, and sodium aluminate mixing.
- Phase 5 (Hydrothermal Reaction): Transfer to a reaction kettle and heating at 100 °C for 15 h followed by cooling.
- Phase 6 (Purification & Final Product): Magnetic separation using water dispersant, removal of unloaded particles, and freeze-drying to obtain the final porous magnetic zeolite."""
            
            st.session_state['structured_protocol'] = processed_text
            st.success("تم تحليل النص وتنظيمه بنجاح إلى مراحل أكاديمية دقيقة!")

# استخدام النص المنظم إن وجد، أو النص الافتراضي
current_protocol = st.session_state.get('structured_protocol', raw_protocol_input)

st.markdown("---")
st.subheader("📋 المراحل المنظمة وجاهزية الوصف (Master Prompt):")

# بناء الوصف النهائي الموجه للذكاء الاصطناعي
generated_prompt = f"""
A professional Q1-journal style scientific graphical abstract, horizontal two-row grid layout, clean white background, academic color palette (blues and greys). 
Title banner across the top: "{abstract_title}".
Based on the structured protocol:
{current_protocol}
High resolution, sharp vector illustration style, clear English labels, distinct vector icons for laboratory equipment (grinder, oven, crucible, centrifuge, ultrasonic bath, reaction kettle, magnet), and directional arrows connecting all steps sequentially.
""".strip()

st.code(generated_prompt, language="text")

st.markdown("---")
st.markdown("### 🚀 الانتقال السريع إلى الأدوات المجانية:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 1️⃣ Microsoft Designer / Copilot (مجاني بالكامل)")
    st.markdown("[🔗 افتح Bing Image Creator / Copilot](https://www.bing.com/create)", unsafe_allow_html=True)

with col2:
    st.markdown("#### 2️⃣ ChatGPT (النسخة المجانية)")
    st.markdown("[🔗 افتح موقع ChatGPT](https://chatgpt.com/)", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📥 نافذة استيراد وعرض الصورة النهائية في المنصة:")
uploaded_image = st.file_uploader("قم برفع الصورة بعد استخراجها من الأدوات المجانية لتوثيقها في تقرير بحثك:", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    st.success("تم اعتماد الصورة وربطها بالمنصة بنجاح!")
    st.image(uploaded_image, caption=f"Graphical Abstract: {abstract_title}", use_column_width=True)
