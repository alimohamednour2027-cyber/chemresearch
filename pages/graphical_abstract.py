import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Graphical Abstract Bridge",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 ChemResearch AI: Quick-Bridge to Free Abstract Generators")
st.markdown("هذا الجسر الذكي يقوم بتجهيز وصياغة الوصف الهندسي الاحترافي (Master Prompt) الخاص ببحثك، وينقلك بضغطة زر واحدة إلى أدوات توليد الصور المجانية لتستخرج صورتك وتجلبها إلى هنا.")
st.markdown("---")

# --- حقل إدخال البروتوكول والمراحل ---
default_protocol = """SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE: A SEQUENTIAL PROCESS
Row 1:
- Phase 1 (Pre-treatment & Acid Washing): Low-grade ore rock, mechanical grinder, beaker with H2SO4 and stirrer, funnel, and drying oven (DHG-9030).
- Phase 2 (Alkali Fusion): Dried ore + NaOH particles, nickel crucible, and muffle furnace (BSX2-6-12TP) at 550 °C.
- Phase 3 (Silicate Solution Prep): Dissolution, centrifugation (Eppendorf 5810R), and adding sodium silicate to the supernatant in a plastic bottle.
Row 2:
- Phase 4 (Ultrasonication & Mixing): Nano Fe3O4 addition, ultrasonic bath, and sodium aluminate stirring at 70 °C.
- Phase 5 (Hydrothermal Reaction): Reaction kettle at 100 °C for 15 h, followed by cooling.
- Phase 6 (Purification & Final Product): Magnetic separation with water dispersant, removal of unloaded particles, freeze-drying, and final porous magnetic zeolite structure."""

protocol_input = st.text_area("تفاصيل البروتوكول والمراحل:", value=default_protocol, height=250)
abstract_title = st.text_input("عنوان المخطط الرئيسي:", value="SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE")

# --- بناء الوصف الاحترافي الجاهز ---
generated_prompt = f"""
A professional Q1-journal style scientific graphical abstract, horizontal two-row grid layout, clean white background, academic color palette (blues and greys). 
Title banner across the top: "{abstract_title}".
Based on the following protocol:
{protocol_input}
High resolution, sharp vector illustration style, clear English labels, distinct vector icons for laboratory equipment (grinder, oven, crucible, centrifuge, ultrasonic bath, reaction kettle, magnet), and directional arrows connecting all steps sequentially.
""".strip()

st.markdown("### 📋 الوصف الهندسي الجاهز للاستخدام (Prompt):")
st.code(generated_prompt, language="text")

st.markdown("---")
st.markdown("### 🚀 الانتقال السريع إلى الأدوات المجانية:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 1️⃣ Microsoft Designer / Copilot (مجاني بالكامل بـ DALL-E 3)")
    st.markdown("انقر أدناه لفتح المنصة المجانية، ثم قم بلصق الوصف أعلاه:")
    st.markdown("[🔗 افتح Bing Image Creator / Copilot](https://www.bing.com/create)", unsafe_allow_html=True)

with col2:
    st.markdown("#### 2️⃣ ChatGPT (النسخة المجانية)")
    st.markdown("انقر أدناه لفتح ChatGPT واطلب منه توليد الصورة بناءً على الوصف:")
    st.markdown("[🔗 افتح موقع ChatGPT](https://chatgpt.com/)", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📥 نافذة استيراد وعرض الصورة النهائية في المنصة:")
uploaded_image = st.file_uploader("قم برفع الصورة بعد تحميلها من الأدوات الخارجية لعرضها وحفظها في تقرير بحثك:", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    st.success("تم رفع الصورة بنجاح وتوثيقها في منصتك البحثية!")
    st.image(uploaded_image, caption=f"Graphical Abstract: {abstract_title}", use_column_width=True)
