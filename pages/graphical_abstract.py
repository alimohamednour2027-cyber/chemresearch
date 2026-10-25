import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="AI-Visual Lab Graphical Abstract Generator",
    page_icon="🤖",
    layout="wide"
)

# --- العنوان والمقدمة ---
st.title("🤖 ChemResearch AI: AI-Powered Visual Graphical Abstract Generator")
st.markdown("هذا المحرك يستخدم الذكاء الاصطناعي المتقدم (Gemini) لتحويل وصفك النصي إلى مخطط بصري احترافي بأيقونات مختبرية حقيقية. (يتطلب مفتاح Gemini API Key).")
st.markdown("---")

# --- إعدادات القائمة الجانبية ---
st.sidebar.title("🔑 Gemini API Configuration")
st.sidebar.markdown("أدخل مفتاح الـ API الخاص بك هنا لتفعيل ميزة توليد الصور:")
api_key_input = st.sidebar.text_input("Enter Gemini API Key:", type="password", value="")

# --- حقل إدخال النص ---
st.subheader("✍️ أدخل الخطوات المخبرية (الرجاء استخدام اللغة الإنجليزية لأفضل النتائج):")
default_steps = """1. Precursor Preparation: Grinding and washing raw agricultural waste.
2. Chemical Impregnation: Mixing with KOH activating agent in aqueous solution.
3. Thermal Pyrolysis: Carbonization in a tube furnace at 800°C under N2 atmosphere.
4. Final Product: High-surface area porous carbon yield."""

synthesis_input = st.text_area("Laboratory Synthesis Steps Protocol:", value=default_steps, height=220)
abstract_title = st.text_input("عنوان المخطط:", value="Synthesis Workflow of Porous Carbon from Biomass")

# --- زر التوليد ---
if st.button("🚀 Generate AI-Visual Graphical Abstract (Image)", key="gen_ai_image_pro"):
    if not synthesis_input.strip():
        st.error("الرجاء إدخال خطوات التجربة.")
    elif not api_key_input:
        st.error("الرجاء إدخال Gemini API Key في القائمة الجانبية لتوليد الصور.")
    else:
        # إعداد الاتصال بـ Gemini
        try:
            genai.configure(api_key=api_key_input)
            model = genai.GenerativeModel('gemini-pro-vision')
            
            with st.spinner("جاري استخدام الذكاء الاصطناعي لتوليد المخطط البصري... (قد يستغرق 30-60 ثانية)"):
                
                # --- صياغة الوصف البصري الشامل (The Master Prompt) ---
                # هذا الجزء هو السر في الحصول على نتيجة احترافية شبيهة بالمقالات
                master_prompt = f"""
                Create a single professional scientific graphical abstract illustrating the following laboratory synthesis protocol:
                Title: "{abstract_title}"

                Protocol Steps:
                {synthesis_input}

                Visual Style Requirements:
                1. Use a linear, sequential flowchart layout (e.g., horizontal flow from left to right).
                2. Use realistic, stylized laboratory equipment icons (e.g., beakers, flasks, oven, furnace, centrifuge) for each step.
                3. Include clear directional arrows between steps.
                4. Integrate the short textual description of each step directly below its corresponding icon.
                5. Use an academic color palette (clean blues, whites, greys).
                6. Ensure high resolution, sharp details, and a clean white background.
                7. The title must be prominently displayed at the top center of the image.
                """
                
                # طلب توليد الصورة
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
                        file_name="AI_Visual_Abstract.png",
                        mime="image/png"
                    )
                else:
                    st.error("لم يتمكن Gemini من توليد الصورة. يرجى التأكد من صحة مفتاح الـ API وتوافر الحصة.")
                    
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بـ Gemini: {e}")
            st.info("تأكد من أن مفتاح الـ API الخاص بك مفعل لنموذج `gemini-pro-vision`.")
