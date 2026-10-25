import streamlit as st
import io
from PIL import Image

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="AI-Visual Lab Graphical Abstract Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ChemResearch AI: AI-Powered Visual Graphical Abstract Generator")
st.markdown("هذا المحرك يستخدم الذكاء الاصطناعي لتحويل خطواتك المخبرية إلى مخطط بصري احترافي متسلسل.")
st.markdown("---")

# --- القائمة الجانبية لإدخال المفتاح ---
st.sidebar.title("🔑 Gemini API Configuration")
api_key_input = st.sidebar.text_input("Enter Gemini API Key:", type="password", value="")

# --- حقل إدخال النص ---
st.subheader("✍️ أدخل خطوات العملية المخبرية (باللغة الإنجليزية لأفضل النتائج):")
default_steps = """1. Precursor Preparation: Grinding and washing raw agricultural waste.
2. Chemical Impregnation: Mixing with KOH activating agent in aqueous solution.
3. Thermal Pyrolysis: Carbonization in a tube furnace at 800°C under N2 atmosphere.
4. Final Product: High-surface area porous carbon yield."""

synthesis_input = st.text_area("Laboratory Synthesis Steps Protocol:", value=default_steps, height=220)
abstract_title = st.text_input("عنوان المخطط:", value="Synthesis Workflow of Porous Carbon from Biomass")

if st.button("🚀 Generate AI-Visual Graphical Abstract", key="gen_ai_image_safe"):
    if not synthesis_input.strip():
        st.error("الرجاء إدخال خطوات التجربة.")
    elif not api_key_input:
        st.error("الرجاء إدخال Gemini API Key في القائمة الجانبية.")
    else:
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key_input)
            
            with st.spinner("جاري توليد المخطط البصري عبر الذكاء الاصطناعي... (قد يستغرق بضع ثوانٍ)"):
                # استخدام النموذج المناسب للصور أو النصوص التوجيهية المتقدمة
                model = genai.GenerativeModel('gemini-1.5-pro')
                
                prompt = f"""
                Act as an expert scientific illustrator. Generate a detailed description and prompt layout for a professional graphical abstract for an academic journal (Q1 chemistry paper).
                Title: "{abstract_title}"
                Protocol:
                {synthesis_input}
                Provide a structured breakdown of how the visual steps (flowchart with lab icons like beakers, furnaces, and arrows) should be arranged.
                """
                
                response = model.generate_content(prompt)
                
                st.success("تم تحليل الخطوات بنجاح عبر الذكاء الاصطناعي!")
                st.markdown("### 📋 التقرير والتصميم المقترح للخطوات:")
                st.write(response.text)
                
        except Exception as e:
            st.error(fحدث خطأ أثناء الاتصال: {e}")
