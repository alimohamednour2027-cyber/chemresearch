import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import google.generativeai as genai

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Advanced Academic Graphical Abstract Engine",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 ChemResearch AI: Advanced Academic Graphical Abstract Engine")
st.markdown("هذا المحرك يحلل بروتوكول التحضير النصي ويستخرج الهيكل البصري الأكاديمي بدقة عالية.")
st.markdown("---")

# --- القائمة الجانبية لإدخال المفتاح ---
st.sidebar.title("🔑 Gemini API Configuration")
api_key_input = st.sidebar.text_input("Enter Gemini API Key:", type="password", value="")

# --- حقل إدخال النص ---
st.subheader("✍️ أدخل بروتوكول التحضير النصي التفصيلي (باللغة الإنجليزية):")
default_protocol = """Natural, low-grade molybdenum ore was ground and then sifted through a 300 mesh sieve. A controlled amount of dilute sulfuric acid was added to the ore with a mass volume ratio of 1:2 and the mixture was agitated in a shaker (Tensuc TS-2102C, Shanghai) overnight. The mixture was filtered, and the collected ore was dried in an oven (DHG-9030, Shanghai). Then 9 g of the acid-washed ore was placed in a nickel crucible, and 9 g of NaOH particles were added to the ore. The mixture was calcined in a muffle furnace (BSX2-6-12TP, Shanghai) at 550 °C for 3 h, and then allowed to cool at room temperature. The calcined mixture was dissolved with 90 mL of deionized water and then centrifuged (Eppendorf 5810R, Germany). The supernatant was placed in a polypropylene plastic bottle, and 15.75 g of sodium silicate was added and dissolved completely. Subsequently, various quantities of nano ferroferric oxide were added to the solution.
The mixture was ultrasonicated for 30min. Then 30mL of an aqueous solution containing 5.40 g of sodium aluminate was added while stirring, and the mixture was mechanically stirred for 2 h in a 70 °C water bath. The material in the plastic bottle was transferred to a reaction kettle and heated to 100 °C for 15 h to drive the reaction. Then the mixture was cooled to room temperature, rinsed several times in a centrifugation-dispersion cycle, and freeze-dried for 24 h. Water was used as a dispersant to magnetically separate the product and remove particles that were not fully loaded with nano ferroferric oxide. The separated magnetic zeolite was freeze-dried for 24 h."""

protocol_input = st.text_area("Preparation Protocol Text:", value=default_protocol, height=350)
abstract_title = st.text_input("عنوان المخطط:", value="Synthesis of Magnetic Zeolite from Molybdenum Ore")

if st.button("🚀 توليد المخطط البصري الاحترافي (Graphical Abstract)", key="gen_ai_visual_abstract"):
    if not protocol_input.strip():
        st.error("الرجاء إدخال بروتوكول التحضير.")
    elif not api_key_input:
        st.error("الرجاء إدخال Gemini API Key في القائمة الجانبية.")
    else:
        with st.spinner("جاري تحليل النص وتصميم الهيكل البصري..."):
            try:
                # إعداد الاتصال بـ Gemini باستخدام النموذج المستقر والمحدث
                genai.configure(api_key=api_key_input)
                model = genai.GenerativeModel('gemini-3.8-flash')
                
                analysis_prompt = f"""
                Analyze the following laboratory synthesis protocol and extract the main process flow into sequential phases.
                For each phase, provide a clear title and a detailed visual description for the laboratory equipment and actions.
                
                Protocol:
                "{protocol_input}"
                
                Output format for each phase:
                Phase [X]: [Title]
                Visual Description: [Detailed steps for equipment and workflow]
                """
                
                response = model.generate_content(analysis_prompt)
                
                st.success("تم تحليل البروتوكول واستخراج الهيكل البصري بنجاح!")
                st.markdown("### 📋 الهيكل البصري المنظم للمراحل:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال: {e}")
