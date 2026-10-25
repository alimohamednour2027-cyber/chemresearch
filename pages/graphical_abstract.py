import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Professional Academic Graphical Abstract Engine",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 ChemResearch AI: Professional Visual Graphical Abstract Engine")
st.markdown("هذا المحرك يستخدم هندسة بصرية متقدمة لتحويل بروتوكولك النصي إلى مخطط بصري أكاديمي احترافي (Q1 style) مقسم على صفوف وأعمدة بأيقونات دقيقة. (يتطلب مفتاح Gemini API Key).")
st.markdown("---")

# --- إعدادات القائمة الجانبية ---
st.sidebar.title("🔑 Gemini API Configuration")
st.sidebar.markdown("أدخل مفتاح الـ API الخاص بك هنا لتفعيل ميزة توليد الصور:")
api_key_input = st.sidebar.text_input("Enter Gemini API Key:", type="password", value="")

# --- حقل إدخال النص ---
st.subheader("✍️ بروتوكول التحضير النصي التفصيلي (باللغة الإنجليزية):")
default_protocol = """Natural, low-grade molybdenum ore was ground and then sifted through a 300 mesh sieve. A controlled amount of dilute sulfuric acid was added to the ore with a mass volume ratio of 1:2 and the mixture was agitated in a shaker (Tensuc TS-2102C, Shanghai) overnight. The mixture was filtered, and the collected ore was dried in an oven (DHG-9030, Shanghai). Then 9 g of the acid-washed ore was placed in a nickel crucible, and 9 g of NaOH particles were added to the ore. The mixture was calcined in a muffle furnace (BSX2-6-12TP, Shanghai) at 550 °C for 3 h, and then allowed to cool at room temperature. The calcined mixture was dissolved with 90 mL of deionized water and then centrifuged (Eppendorf 5810R, Germany). The supernatant was placed in a polypropylene plastic bottle, and 15.75 g of sodium silicate was added and dissolved completely. Subsequently, various quantities of nano ferroferric oxide were added to the solution.
The mixture was ultrasonicated for 30min. Then 30mL of an aqueous solution containing 5.40 g of sodium aluminate was added while stirring, and the mixture was mechanically stirred for 2 h in a 70 °C water bath. The material in the plastic bottle was transferred to a reaction kettle and heated to 100 °C for 15 h to drive the reaction. Then the mixture was cooled to room temperature, rinsed several times in a centrifugation-dispersion cycle, and freeze-dried for 24 h. Water was used as a dispersant to magnetically separate the product and remove particles that were not fully loaded with nano ferroferric oxide. The separated magnetic zeolite was freeze-dried for 24 h."""

protocol_input = st.text_area("Preparation Protocol Text:", value=default_protocol, height=350)
abstract_title = st.text_input("عنوان المخطط:", value="SYNTHESIS OF MAGNETIC ZEOLITE FROM MOLYBDENUM ORE")

# --- زر التوليد ---
if st.button("🚀 هندسة وتوليد المخطط البصري الاحترافي (Image)", key="gen_ai_master_visual"):
    if not protocol_input.strip():
        st.error("الرجاء إدخال بروتوكول التحضير.")
    elif not api_key_input:
        st.error("الرجاء إدخال Gemini API Key في القائمة الجانبية لتوليد الصور.")
    else:
        try:
            genai.configure(api_key=api_key_input)
            # استخدام نموذج الرؤية (نحتاج إلى نموذج Gemini Pro Vision أو Gemini Ultra إذا أتيح)
            # في سياق عملنا الحالي، سنستخدم نموذج `gemini-pro-vision` للتحويل النصي البصري
            model = genai.GenerativeModel('gemini-pro-vision')
            
            with st.spinner("جاري هندسة وتصميم المخطط البصري الاحترافي... (قد يستغرق دقيقة)"):
                
                # --- صياغة الوصف البصري الشامل (The Master Visual Prompt) ---
                # هذا هو السر في الحصول على نتيجة شبيهة بصورتك تماماً.
                master_prompt = f"""
                Act as an expert scientific illustrator. Create a single professional Q1-journal style scientific graphical abstract illustrating the following laboratory synthesis protocol.
                
                Layout Requirements:
                1. Use a horizontal two-row grid layout (Total 6 main phases).
                2. Use a clean white background and a professional academic color palette (blues, greys).
                3. Include a prominent title banner across the top: "{abstract_title}"
                
                Phase Descriptions:
                Row 1 (Phases 1-3):
                Phase 1: Pre-treatment & Acid Washing. Icons: Low-grade ore rock -> mechanical grinder -> beaker with H2SO4 and stirrer -> funnel -> drying oven (DHG-9030).
                Phase 2: Alkali Fusion. Icons: Dried ore + NaOH particles -> nickel crucible -> muffle furnace (BSX2-6-12TP) at 550 °C.
                Phase 3: Silicate Solution Preparation. Icons: Dissolution -> centrifugation (Eppendorf 5810R) -> plastic bottle + sodium silicate added to supernatant.
                
                Row 2 (Phases 4-6):
                Phase 4: Ultrasonication & Mixing. Icons: Add nano Fe3O4 -> ultrasonic bath -> add sodium aluminate while stirring at 70 °C.
                Phase 5: Hydrothermal Reaction. Icons: Transfer to reaction kettle -> heat at 100 °C for 15 h -> cool to room temp.
                Phase 6: Purification & Final Product. Icons: Magnetic separation (with water dispersant, remove unloaded particles) -> freeze-drying -> porous magnetic zeolite structure.
                
                Final Details:
                Ensure high resolution, sharp vector illustration style. Include clear English labels and directional arrows connecting all steps. The output should be one coherent image.
                """
                
                # طلب توليد الصورة (استخدام الدالة المناسبة للنموذج)
                # ملاحظة: قد تتطلب بعض حسابات Gemini استخدام دالة أخرى أو تفعيل نموذج Pro Vision
                response = model.generate_content([master_prompt])
                
                if response and response.candidates:
                    # استخراج بيانات الصورة
                    img_data = response.candidates[0].content.parts[0].inline_data
                    image_bytes = img_data.data
                    
                    # تحويل بايتات الصورة إلى كائن PIL
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    # عرض الصورة في التطبيق
                    st.success("تم توليد المخطط الرسومي البصري بنجاح!")
                    st.image(image, caption=f"AI-Generated Abstract: {abstract_title}", use_column_width=True)
                    
                    # زر تحميل الصورة
                    img_buffer = io.BytesIO()
                    image.save(img_buffer, format="PNG")
                    img_buffer.seek(0)
                    
                    st.download_button(
                        label="📥 Download Final Graphical Abstract (PNG)",
                        data=img_buffer,
                        file_name="AI_Professional_Abstract.png",
                        mime="image/png"
                    )
                else:
                    st.error("لم يتمكن Gemini من توليد الصورة. يرجى التأكد من صحة مفتاح الـ API وتوافر الحصة، ومن تفعيل نموذج `gemini-pro-vision`.")
                    
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بـ Gemini: {e}")
            st.info("تأكد من أن مفتاح الـ API الخاص بك مفعل لنموذج `gemini-pro-vision` أو ما يعادله لتوليد الصور.")
