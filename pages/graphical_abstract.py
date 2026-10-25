import streamlit as st
import openai

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: DALL-E 3 Graphical Abstract Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 ChemResearch AI: Professional Graphical Abstract Engine")
st.markdown("هذا المحرك يربط منصتك مباشرة بـ DALL-E 3 لتوليد المخطط البصري الأكاديمي الاحترافي (Q1 Style) بصفين وأيقونات دقيقة بضغطة زر واحدة داخل منصتك!")
st.markdown("---")

# --- القائمة الجانبية لإدخال المفتاح ---
st.sidebar.title("🔑 OpenAI API Configuration")
st.sidebar.markdown("أدخل مفتاح الـ OpenAI API الخاص بك لتفعيل توليد الصور بالذكاء الاصطناعي:")
openai_api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password", value="")

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

protocol_input = st.text_area("بروتوكول التحضير والمراحل (لتوجيه الرسم):", value=default_protocol, height=300)
abstract_title = st.text_input("عنوان المخطط الرئيسي:", value="SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE")

# --- زر التوليد ---
if st.button("🚀 توليد المخطط البصري الاحترافي عبر DALL-E 3", key="generate_dalle_abstract"):
    if not protocol_input.strip():
        st.error("الرجاء إدخال تفاصيل البروتوكول والمراحل.")
    elif not openai_api_key:
        st.error("الرجاء إدخال OpenAI API Key في القائمة الجانبية.")
    else:
        try:
            openai.api_key = openai_api_key
            with st.spinner("جاري التواصل مع DALL-E 3 ورسم المخطط البصري الاحترافي خصيصاً لك... (قد يستغرق 10-20 ثانية)"):
                
                # بناء الوصف الهندسي البصري الدقيق (Master Prompt) الموجه لـ DALL-E 3
                master_prompt = f"""
                A professional Q1-journal style scientific graphical abstract, horizontal two-row grid layout, clean white background, academic color palette (blues and greys). 
                Title banner across the top: "{abstract_title}".
                Based on the following protocol details:
                {protocol_input}
                High resolution, sharp vector illustration style, clear English labels, distinct vector icons for laboratory equipment (grinder, oven, crucible, centrifuge, ultrasonic bath, reaction kettle, magnet), and directional arrows connecting all steps sequentially.
                """
                
                # استدعاء واجهة برمجة تطبيقات توليد الصور
                response = openai.images.generate(
                    model="dall-e-3",
                    prompt=master_prompt,
                    size="1792x1024",  # قياس عرضي ممتاز ومناسب للمخططات الهندسية الأفقية
                    quality="hd",
                    n=1,
                )
                
                image_url = response.data[0].url
                
                st.success("تم توليد المخطط البصري بنجاح تام داخل منصتك!")
                st.image(image_url, caption=f"Professional Graphical Abstract: {abstract_title}", use_column_width=True)
                
                st.markdown(f"📥 يمكنك النقر بزر الماوس الأيمن على الصورة واختيار 'حفظ باسم' أو استخدام الرابط المباشر للتحميل: [رابط الصورة المباشر]({image_url})")
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال أو التوليد: {e}")
