import streamlit as st
from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Professional Lab Workflow Designer",
    page_icon="📐",
    layout="wide"
)

st.title("📐 ChemResearch AI: Professional Graphical Abstract Designer (PPTX)")
st.markdown("هذا المحرك يولد مخططاً رسومياً احترافيًا ونظيفًا (خالياً من النصوص الطويلة)، بمسافات أفقية واسعة ومنظمة، قابل للتعديل بنسبة 100% في PowerPoint.")
st.markdown("---")

# --- إعدادات النص ---
st.subheader("✍️ أدخل خطوات العملية المخبرية (مختصرة ومركزة لكل مرحلة، كل مرحلة في سطر منفصل):")
default_steps = """1. Precursor Preparation: Washing and cleaning fish scales.
2. Drying Process: Open-area drying followed by oven heating at 100°C.
3. Chemical Treatment: Deproteinization and demineralization with NaOH/HCl.
4. Final Product: Chitin/Chitosan powder yield."""

steps_input = st.text_area("خطوات البروتوكول المخبري (الرجاء استخدام الإنجليزية):", value=default_steps, height=200)
abstract_title = st.text_input("عنوان المخطط:", value="Extraction Workflow of Chitosan from Fish Scales")

if st.button("🚀 توليد وتحميل المخطط الاحترافي بصيغة PowerPoint", key="gen_clean_pptx"):
    if not steps_input.strip():
        st.error("الرجاء إدخال خطوة واحدة على الأقل.")
    else:
        with st.spinner("جاري تصميم المخطط الهندسي النظيف..."):
            # إنشاء عرض تقديمي جديد
            prs = Presentation()
            prs.slide_width = Inches(13.33) # قياس الشريحة 16:9
            prs.slide_height = Inches(7.5)
            
            # إضافة شريحة فارغة
            blank_layout = prs.slide_layouts[6]
            slide = prs.slides.add_slide(blank_layout)
            
            # 1. إضافة العنوان الرئيسي
            title_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.5), Inches(11.93), Inches(0.8))
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_title = tf_title.paragraphs[0]
            p_title.text = abstract_title
            p_title.font.name = "Times New Roman"
            p_title.font.size = Pt(28)
            p_title.font.bold = True
            p_title.font.color.rgb = RGBColor(30, 30, 30)
            p_title.alignment = PP_ALIGN.CENTER
            
            # 2. تحليل الخطوات وتوزيعها
            steps = [line.strip() for line in steps_input.split('\n') if line.strip()]
            num_steps = len(steps)
            
            if num_steps > 0:
                start_left = Inches(0.5)
                start_top = Inches(1.9)
                total_width = Inches(12.33)
                
                box_width = (total_width / num_steps) - Inches(0.3)
                box_height = Inches(4.5)
                spacing = Inches(0.3)
                
                for i, step_text in enumerate(steps):
                    current_left = start_left + i * (box_width + spacing)
                    
                    # أ. صندوق الإطار النظيف لكل خطوة
                    card_bg = slide.shapes.add_shape(
                        MSO_SHAPE.ROUNDED_RECTANGLE, 
                        current_left, start_top, box_width, box_height
                    )
                    card_bg.fill.solid()
                    card_bg.fill.fore_color.rgb = RGBColor(255, 255, 255) # خلفية بيضاء
                    card_bg.line.color.rgb = RGBColor(160, 170, 180) # إطار رمادي
                    card_bg.line.width = Pt(1.2)
                    
                    # ب. مساحة الأيقونة في الأعلى (مستطيل رمادي ناعم)
                    icon_size = Inches(1.6)
                    icon_left = current_left + (box_width / 2) - (icon_size / 2)
                    icon_top = start_top + Inches(0.3)
                    
                    icon_box = slide.shapes.add_shape(
                        MSO_SHAPE.RECTANGLE,
                        icon_left, icon_top, icon_size, icon_size
                    )
                    icon_box.fill.solid()
                    icon_box.fill.fore_color.rgb = RGBColor(230, 240, 250) # أزرق فاتح
                    icon_box.line.color.rgb = RGBColor(120, 130, 140)
                    icon_box.line.width = Pt(0.8)
                    
                    # ج. صندوق النصوص (عنوان الخطوة + الوصف المختصر)
                    tb = slide.shapes.add_textbox(
                        current_left + Inches(0.15), 
                        start_top + Inches(2.1), 
                        box_width - Inches(0.3), 
                        Inches(2.1)
                    )
                    tf = tb.text_frame
                    tf.word_wrap = True
                    
                    # معالجة النص: فصل العنوان عن الوصف
                    if ":" in step_text:
                        parts = step_text.split(":", 1)
                        stage_label = parts[0].strip()
                        stage_desc = parts[1].strip()
                    else:
                        stage_label = f"Phase {i+1}"
                        stage_desc = step_text
                    
                    # عنوان المرحلة (خط عريض)
                    p_stage = tf.paragraphs[0]
                    p_stage.text = stage_label
                    p_stage.font.name = "Times New Roman"
                    p_stage.font.size = Pt(14)
                    p_stage.font.bold = True
                    p_stage.font.color.rgb = RGBColor(50, 90, 140) # أزرق داكن
                    p_stage.alignment = PP_ALIGN.CENTER
                    
                    # وصف الخطوة (خط عادي ومختصر)
                    p_desc = tf.add_paragraph()
                    p_desc.text = stage_desc
                    p_desc.font.name = "Times New Roman"
                    p_desc.font.size = Pt(11.5)
                    p_desc.font.color.rgb = RGBColor(40, 40, 40)
                    p_desc.alignment = PP_ALIGN.CENTER
                    
                    # د. سهم التتابع الهندسي
                    if i < num_steps - 1:
                        arrow_left = current_left + box_width + Inches(0.05)
                        arrow_top = start_top + (box_height / 2) - Inches(0.2)
                        arrow = slide.shapes.add_shape(
                            MSO_SHAPE.RIGHT_ARROW,
                            arrow_left, arrow_top, Inches(0.25), Inches(0.25)
                        )
                        arrow.fill.solid()
                        arrow.fill.fore_color.rgb = RGBColor(100, 100, 100)
                        arrow.line.color.rgb = RGBColor(80, 80, 80)

            # حفظ الملف في الذاكرة للتنزيل
            pptx_buffer = BytesIO()
            prs.save(pptx_buffer)
            pptx_buffer.seek(0)
            
            st.success("تم توليد المخطط المخبري البصري بنجاح!")
            
            st.download_button(
                label="📥 تنزيل ملف PowerPoint (.pptx) القابل للتعديل",
                data=pptx_buffer,
                file_name="Professional_Lab_Workflow.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )

st.markdown("---")
st.info("💡 **نصيحة:** بعد تنزيل الملف وفتحه في PowerPoint، يمكنك بسهولة سحب أيقونات حقيقية (مثل صور الأفران أو الكؤوس الزجاجية) ووضعها داخل المستطيلات الزرقاء الفاتحة المخصصة لها.")
