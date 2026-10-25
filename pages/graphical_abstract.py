import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Advanced Q1 Graphical Abstract Engine",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 ChemResearch AI: Q1-Style Graphical Abstract Engine")
st.markdown("هذا هو الكود النهائي المخصص لإنشاء المخطط البصري الاحترافي بصفين وأيقونات معدات دقيقة وأسهم متسلسلة تماماً كصورتك المرجعية.")
st.markdown("---")

# --- حقل إدخال بروتوكول التحضير الدقيق ---
default_protocol = """1. Pre-treatment & Acid Washing: Ore grinding, 300-mesh sifting, H2SO4 (1:2) agitation, filtration, and oven drying (DHG-9030).
2. Alkali Fusion: 9g ore + 9g NaOH in nickel crucible, calcination in muffle furnace (BSX2-6-12TP) at 550 °C for 3 h.
3. Silicate Solution Prep: Dissolution in 90 mL deionized water, centrifugation (Eppendorf 5810R), sodium silicate addition.
4. Ultrasonication & Mixing: Nano Fe3O4 addition, 30 min sonication, sodium aluminate addition with stirring at 70 °C for 2 h.
5. Hydrothermal Reaction: Transfer to reaction kettle, heating at 100 °C for 15 h, and cooling to room temperature.
6. Purification & Final Product: Magnetic separation with water dispersant, removal of unloaded particles, and freeze-drying."""

protocol_input = st.text_area("خطوات البروتوكول (6 مراحل رئيسية):", value=default_protocol, height=260)
abstract_title = st.text_input("عنوان المخطط الرئيسي:", value="SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE")

if st.button("🚀 بناء وتوليد المخطط البصري المتسلسل الآن", key="build_master_abstract"):
    if not protocol_input.strip():
        st.error("الرجاء إدخال الخطوات.")
    else:
        with st.spinner("جاري بناء المخطط البصري الأكاديمي المتسلسل بدقة عالية..."):
            
            # --- 1. إعداد أبعاد اللوحة الكبيرة (مناسبة للمجلات العلمية Q1) ---
            img_width = 1600
            img_height = 1050
            image = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))
            draw = ImageDraw.Draw(image)
            
            # --- 2. إعداد الخطوط الآمنة ---
            try:
                font_title = ImageFont.truetype("arial.ttf", 26)
                font_phase = ImageFont.truetype("arial.ttf", 15)
                font_desc = ImageFont.truetype("arial.ttf", 12)
                font_icon = ImageFont.truetype("arial.ttf", 13)
            except:
                font_title = ImageFont.load_default()
                font_phase = ImageFont.load_default()
                font_desc = ImageFont.load_default()
                font_icon = ImageFont.load_default()

            # --- 3. رسم شريط العنوان العلوي الأكاديمي ---
            draw.rectangle([0, 0, img_width, 95], fill=(35, 60, 100))
            draw.text((50, 32), abstract_title, fill=(255, 255, 255), font=font_title)
            
            # --- 4. تحليل الخطوات والمراحل بأمان تام ---
            phases = [p.strip() for p in protocol_input.split('\n') if p.strip()]
            num_phases = len(phases)
            
            if num_phases > 0:
                cols_per_row = 3
                margin_x = 50
                margin_y = 140
                spacing_x = 45
                spacing_y = 60
                
                total_w = img_width - (2 * margin_x)
                box_w = (total_w - (cols_per_row - 1) * spacing_x) / cols_per_row
                box_h = 380
                
                equipment_labels = [
                    "Grinder & H2SO4 Beaker\n(DHG-9030 Oven)",
                    "Nickel Crucible\n(Muffle Furnace 550°C)",
                    "Centrifuge 5810R\n& Plastic Bottle",
                    "Ultrasonic Bath\n& Na-Aluminate Stir",
                    "Reaction Kettle\n(100 °C, 15 h)",
                    "Magnetic Separation\n(Final Zeolite Product)"
                ]
                
                for i, phase_text in enumerate(phases[:6]):
                    row = i // cols_per_row
                    col = i % cols_per_row
                    
                    bx = margin_x + col * (box_w + spacing_x)
                    by = margin_y + row * (box_h + spacing_y)
                    
                    # أ. رسم الصندوق الخارجي
                    draw.rectangle([bx, by, bx + box_w, by + box_h], fill=(255, 255, 255), outline=(150, 165, 180), width=2)
                    
                    # ب. رسم صندوق الأيقونة العلوي
                    icon_h = 110
                    draw.rectangle([bx + 15, by + 15, bx + box_w - 15, by + 15 + icon_h], fill=(235, 244, 252), outline=(120, 145, 170), width=1)
                    
                    eq_text = equipment_labels[i] if i < len(equipment_labels) else f"Equipment {i+1}"
                    draw.text((bx + 25, by + 50), eq_text, fill=(45, 80, 130), font=font_icon)
                    
                    # ج. معالجة عنوان ووصف المرحلة بأمان تام باستخدام الفهارس
                    if ":" in phase_text:
                        parts = phase_text.split(":", 1)
                        p_title = parts[0].strip() if len(parts) > 0 else f"Phase {i+1}"
                        p_desc = parts[1].strip() if len(parts) > 1 else phase_text
                    else:
                        p_title = f"Phase {i+1}"
                        p_desc = phase_text
                        
                    draw.text((bx + 15, by + 140), p_title, fill=(30, 50, 90), font=font_phase)
                    
                    # د. التفاف النصوص داخل الصندوق
                    words = p_desc.split()
                    lines = []
                    current_line = ""
                    for word in words:
                        test_line = current_line + " " + word if current_line else word
                        if len(test_line) * 6.8 < box_w - 30:
                            current_line = test_line
                        else:
                            lines.append(current_line)
                            current_line = word
                    if current_line:
                        lines.append(current_line)
                        
                    text_y = by + 175
                    for line in lines[:10]:
                        draw.text((bx + 15, text_y), line, fill=(50, 50, 50), font=font_desc)
                        text_y += 20
                    
                    # هـ. رسم أسهم التتابع الأفقية
                    if col < cols_per_row - 1 and i < num_phases - 1:
                        arrow_x = bx + box_w + 8
                        arrow_y = by + (box_h / 2) - 40
                        draw.polygon([
                            (arrow_x, arrow_y - 8),
                            (arrow_x + 24, arrow_y),
                            (arrow_x, arrow_y + 8)
                        ], fill=(90, 100, 115))
                        
                    # و. رسم سهم الانتقال العمودي بين الصفين
                    if i == 2 and num_phases > 3:
                        arrow_x = bx + (box_w / 2)
                        arrow_y = by + box_h + 8
                        draw.polygon([
                            (arrow_x - 8, arrow_y),
                            (arrow_x, arrow_y + 26),
                            (arrow_x + 8, arrow_y)
                        ], fill=(90, 100, 115))

            # --- 5. حفظ الصورة وعرضها ---
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)
            
            st.success("تم بناء المخطط البصري المتسلسل بنجاح تام!")
            st.image(image, caption="Master Graphical Abstract (Q1 Layout)", use_column_width=True)
            
            # --- 6. زر التحميل المباشر ---
            st.download_button(
                label="📥 تنزيل الصورة النهائية بصيغة PNG عالية الدقة",
                data=buf,
                file_name="Master_Graphical_Abstract_Q1.png",
                mime="image/png"
            )
