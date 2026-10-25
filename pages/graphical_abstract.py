import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Local Professional Graphical Abstract Engine",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 ChemResearch AI: Professional Local Graphical Abstract Engine")
st.markdown("هذا المحرك يرسم مخططاً بصرياً أكاديمياً احترافياً (Q1 style) محلياً داخل المنصة كصورة PNG عالية الدقة فوراً وبدون أي أخطاء أو انتظار.")
st.markdown("---")

# --- حقل إدخال البروتوكول ---
default_protocol = """1. Pre-treatment & Acid Washing: Ore grinding, 300 mesh sifting, H2SO4 agitation, filtering, oven drying (DHG-9030).
2. Alkali Fusion: Mixing ore with NaOH, nickel crucible calcination (BSX2-6-12TP) at 550 °C for 3 h.
3. Silicate Solution: Dissolution in deionized water, centrifugation (Eppendorf 5810R), sodium silicate addition to supernatant.
4. Ultrasonication & Mixing: Adding Fe3O4, ultrasonication for 30 min, adding sodium aluminate with stirring (70 °C).
5. Hydrothermal Reaction: Reaction kettle heating at 100 °C for 15 h, cooling to room temp.
6. Purification & Product: Magnetic separation, rinsing, freeze-drying for final zeolite."""

protocol_input = st.text_area("خطوات البروتوكول (مقسمة على 6 مراحل):", value=default_protocol, height=250)
abstract_title = st.text_input("عنوان المخطط الرئيسي:", value="SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE")

# --- زر التوليد ---
if st.button("🚀 رسم وتوليد المخطط البصري الاحترافي الآن", key="gen_local_abstract"):
    if not protocol_input.strip():
        st.error("الرجاء إدخال الخطوات.")
    else:
        with st.spinner("جاري رسم المخطط البصري الأكاديمي بدقة عالية..."):
            # 1. إعداد لوحة الرسم (تصميم شبكي بصفين لضمان الوضوح)
            img_width = 1500
            img_height = 950
            image = Image.new("RGB", (img_width, img_height), color=(248, 249, 250))
            draw = ImageDraw.Draw(image)
            
            # 2. تحميل الخطوط (الافتراضية لتجنب أخطاء المسارات)
            try:
                font_title = ImageFont.truetype("arial.ttf", 28)
                font_box_title = ImageFont.truetype("arial.ttf", 16)
                font_desc = ImageFont.truetype("arial.ttf", 12)
            except:
                font_title = ImageFont.load_default()
                font_box_title = ImageFont.load_default()
                font_desc = ImageFont.load_default()

            # 3. رسم الشريط العلوي للعنوان
            draw.rectangle([0, 0, img_width, 90], fill=(30, 60, 100))
            draw.text((50, 28), abstract_title, fill=(255, 255, 255), font=font_title)
            
            # 4. تحليل المراحل المدخلة
            phases = [p.strip() for p in protocol_input.split('\n') if p.strip()]
            num_phases = len(phases)
            
            if num_phases > 0:
                # تصميم شبكي: 3 صناديق في الصف الواحد
                cols_per_row = 3
                margin_x = 60
                margin_y = 140
                spacing_x = 40
                spacing_y = 50
                
                total_w = img_width - (2 * margin_x)
                box_w = (total_w - (cols_per_row - 1) * spacing_x) / cols_per_row
                box_h = 350 # صندوق لكل مرحلة
                
                for i, phase_text in enumerate(phases[:6]): # أقصى حد 6 مراحل رئيسية
                    row = i // cols_per_row
                    col = i % cols_per_row
                    
                    bx = margin_x + col * (box_w + spacing_x)
                    by = margin_y + row * (box_h + spacing_y)
                    
                    # أ. رسم الصندوق الخارجي للمرحلة
                    draw.rectangle([bx, by, bx + box_w, by + box_h], fill=(255, 255, 255), outline=(180, 190, 200), width=2)
                    
                    # ب. رسم صندوق الأيقونة في الأعلى
                    icon_h = 100
                    draw.rectangle([bx + 15, by + 15, bx + box_w - 15, by + 15 + icon_h], fill=(235, 243, 250), outline=(140, 160, 180), width=1)
                    
                    # أيقونة تعبيرية رمزية للمعدات
                    draw.text((bx + (box_w/2) - 55, by + 55), f"LAB EQUIPMENT {i+1}", fill=(70, 100, 130), font=font_box_title)
                    
                    # ج. معالجة وعرض النصوص
                    if ":" in phase_text:
                        parts = phase_text.split(":", 1)
                        p_title = parts[0].strip()
                        p_desc = parts[1].strip()
                    else:
                        p_title = f"Phase {i+1}"
                        p_desc = phase_text
                        
                    # عنوان المرحلة (خط عريض أزرق)
                    draw.text((bx + 15, by + 130), p_title, fill=(40, 80, 140), font=font_box_title)
                    
                    # وصف المرحلة مع التفاف النص
                    words = p_desc.split()
                    lines = []
                    current_line = ""
                    for word in words:
                        test_line = current_line + " " + word if current_line else word
                        # تقدير عرض النص
                        if len(test_line) * 7 < box_w - 30:
                            current_line = test_line
                        else:
                            lines.append(current_line)
                            current_line = word
                    if current_line:
                        lines.append(current_line)
                        
                    text_y = by + 160
                    for line in lines[:10]: # طباعة حتى 10 أسطر
                        draw.text((bx + 15, text_y), line, fill=(60, 60, 60), font=font_desc)
                        text_y += 18
                    
                    # د. رسم سهم التتابع الأفقي
                    if col < cols_per_row - 1 and i < num_phases - 1:
                        arrow_x = bx + box_w + 8
                        arrow_y = by + (box_h / 2) - 25
                        draw.polygon([
                            (arrow_x, arrow_y - 8),
                            (arrow_x + 22, arrow_y),
                            (arrow_x, arrow_y + 8)
                        ], fill=(100, 110, 120))
                        
                    # رسم سهم التتابع بين الصفوف (بعد المرحلة الثالثة)
                    if i == 2 and num_phases > 3:
                        arrow_x = bx + (box_w / 2) - 10
                        arrow_y = by + box_h + 5
                        draw.polygon([
                            (arrow_x - 8, arrow_y),
                            (arrow_x, arrow_y + 22),
                            (arrow_x + 8, arrow_y)
                        ], fill=(100, 110, 120))

            # 5. حفظ الصورة في الذاكرة
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)
            
            # 6. عرض الصورة
            st.success("تم رسم وتوليد المخطط البصري الاحترافي محلياً بنجاح تام!")
            st.image(image, caption="Local Generated Graphical Abstract", use_column_width=True)
            
            # 7. زر التحميل
            st.download_button(
                label="📥 تنزيل صورة Graphical Abstract النهائية (PNG)",
                data=buf,
                file_name="Graphical_Abstract_Local.png",
                mime="image/png"
            )
