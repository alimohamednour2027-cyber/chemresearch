import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Local PIL Graphical Abstract Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 ChemResearch AI: Local Visual Graphical Abstract Engine")
st.markdown("هذا المحرك يرسم المخطط البصري كصورة PNG احترافية مباشرة محلياً داخل المنصة، وبدون أي أخطاء أو انتظار طويل.")
st.markdown("---")

# --- حقل إدخال الخطوات ---
st.subheader("✍️ أدخل خطوات البروتوكول المخبري (كل خطوة في سطر منفصل):")
default_steps = """1. Precursor Prep: Washing raw biomass and drying
2. Activation: Mixing with KOH activating agent
3. Pyrolysis: Heating at 800°C under N2 atmosphere
4. Final Yield: High-surface area porous carbon"""

steps_input = st.text_area("Laboratory Synthesis Steps Protocol:", value=default_steps, height=180)
abstract_title = st.text_input("عنوان المخطط الرئيسي:", value="Synthesis Workflow of Porous Carbon")

if st.button("🚀 رسم وتوليد المخطط البصري الآن", key="draw_pil_abstract"):
    if not steps_input.strip():
        st.error("الرجاء إدخال خطوة واحدة على الأقل.")
    else:
        with st.spinner("جاري رسم المخطط البصري بدقة عالية..."):
            # إعداد أبعاد الصورة القياسية للمجلات
            img_width = 1200
            img_height = 600
            image = Image.new("RGB", (img_width, img_height), color="white")
            draw = ImageDraw.Draw(image)
            
            # تحميل الخطوط (الافتراضية لتجنب أخطاء المسارات)
            try:
                font_title = ImageFont.truetype("arial.ttf", 26)
                font_bold = ImageFont.truetype("arial.ttf", 15)
                font_desc = ImageFont.truetype("arial.ttf", 12)
            except:
                font_title = ImageFont.load_default()
                font_bold = ImageFont.load_default()
                font_desc = ImageFont.load_default()

            # رسم العنوان الرئيسي في الأعلى
            draw.text((50, 30), abstract_title, fill=(20, 20, 20), font=font_title)
            
            # تحليل الخطوات وترتيبها أفقياً
            steps = [line.strip() for line in steps_input.split('\n') if line.strip()]
            num_steps = len(steps)
            
            if num_steps > 0:
                start_x = 50
                start_y = 120
                total_width = img_width - 100
                box_w = (total_width - (num_steps - 1) * 20) / num_steps
                box_h = 430
                
                for i, step_text in enumerate(steps):
                    bx = start_x + i * (box_w + 20)
                    by = start_y
                    
                    # 1. رسم صندوق الإطار الأبيض النظيف لكل مرحلة
                    draw.rectangle([bx, by, bx + box_w, by + box_h], fill=(255, 255, 255), outline=(160, 170, 180), width=2)
                    
                    # 2. رسم صندوق الأيقونة العلوي (مستطيل بلون أزرق فاتح هادئ)
                    icon_h = 110
                    draw.rectangle([bx + 15, by + 15, bx + box_w - 15, by + 15 + icon_h], fill=(235, 243, 250), outline=(130, 150, 170), width=1)
                    
                    # رمز تخطيطي داخل مربع الأيقونة (إشارة بصرية)
                    draw.text((bx + (box_w/2) - 30, by + 55), f"ICON {i+1}", fill=(100, 130, 160), font=font_bold)
                    
                    # 3. معالجة النص وفصله إلى عنوان ووصف (تم تصحيح الخطأ هنا)
                    if ":" in step_text:
                        parts = step_text.split(":", 1)
                        label = parts.strip()
                        desc = parts.strip()
                    else:
                        label = f"Step {i+1}"
                        desc = step_text
                        
                    # كتابة عنوان المرحلة بخط عريض وأزرق داكن
                    draw.text((bx + 15, by + 140), label, fill=(40, 80, 140), font=font_bold)
                    
                    # كتابة الوصف المختصر داخل الصندوق مع التفاف النصوص
                    words = desc.split()
                    lines = []
                    current_line = ""
                    for word in words:
                        test_line = current_line + " " + word if current_line else word
                        if len(test_line) * 7 < box_w - 30:
                            current_line = test_line
                        else:
                            lines.append(current_line)
                            current_line = word
                    if current_line:
                        lines.append(current_line)
                        
                    text_y = by + 175
                    for line in lines[:10]:
                        draw.text((bx + 15, text_y), line, fill=(50, 50, 50), font=font_desc)
                        text_y += 18
                    
                    # 4. رسم سهم الاتجاه الهندسي بين المراحل
                    if i < num_steps - 1:
                        arrow_x = bx + box_w + 3
                        arrow_y = by + (box_h / 2)
                        draw.polygon([
                            (arrow_x, arrow_y - 6),
                            (arrow_x + 14, arrow_y),
                            (arrow_x, arrow_y + 6)
                        ], fill=(100, 100, 100))
            
            # حفظ الصورة النهائية في الذاكرة المؤقتة
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)
            
            st.success("تم رسم وتوليد المخطط البصري بنجاح تام!")
            st.image(image, caption=f"Local Abstract: {abstract_title}", use_column_width=True)
            
            # زر التحميل المباشر للصورة
            st.download_button(
                label="📥 تنزيل الصورة النهائية بصيغة PNG",
                data=buf,
                file_name="Graphical_Abstract_Final.png",
                mime="image/png"
            )
