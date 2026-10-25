import streamlit as st
from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

st.set_page_config(
    page_title="Professional Lab Graphical Abstract Generator",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 ChemResearch AI: Professional Lab-Style Graphical Abstract")
st.markdown("هذا المحرك يصمم مخططات رسومية أكاديمية متكاملة تحاكي المقالات المنشورة في المجلات العالمية، وتحتوي على أشكال وأدوات مختبرية (كؤوس زجاجية، أفران، أدقاق تسخين)، مع إمكانية **التعديل والتحريك الكامل داخل برنامج PowerPoint**.")
st.markdown("---")

st.subheader("✍️ أدخل خطوات العملية المخبرية (كل خطوة في سطر منفصل):")
default_steps = """1. Cleaned Raw Material: Preparation and washing of precursor scales.
2. Drying & Grinding: Open-area drying, thermal treatment at 100°C, and mechanical sieving.
3. Deproteinization: Dissolution in NaOH 3.5%, stirring at 65°C, neutralization, and drying.
4. Demineralization: Treatment with HCl 1M, stirring, neutralization, and drying to obtain Chitin.
5. Deacetylation: Reaction with NaOH 40% at 100°C, final neutralization, and Chitosan Powder yield."""

steps_input = st.text_area("خطوات البروتوكول المخبري:", value=default_steps, height=200)
abstract_title = st.text_input("عنوان المخطط الرسومي:", value="Extraction and Synthesis Workflow of Chitosan from Fish Scales")

if st.button("🚀 توليد المخطط الرسومي الاحترافي بصيغة PowerPoint", key="gen_pro_abstract"):
    if not steps_input.strip():
        st.error("الرجاء إدخال خطوة واحدة على الأقل.")
    else:
        with st.spinner("جاري تصميم المخطط المخبري الاحترافي..."):
            prs = Presentation()
            prs.slide_width = Inches(13.33)
            prs.slide_height = Inches(7.5)
            
            blank_slide_layout = prs.slide_layouts[6]
            slide = prs.slides.add_slide(blank_slide_layout)
            
            # عنوان الشريحة الرئيسي
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.73), Inches(0.8))
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_title = tf_title.paragraphs[0]
            p_title.text = abstract_title
            p_title.font.name = "Times New Roman"
            p_title.font.size = Pt(22)
            p_title.font.bold = True
            p_title.font.color.rgb = RGBColor(20, 20, 20)
            
            steps = [line.strip() for line in steps_input.split('\n') if line.strip()]
            num_steps = len(steps)
            
            if num_steps > 0:
                start_left = Inches(0.6)
                start_top = Inches(1.8)
                total_width = Inches(12.13)
                
                box_width = (total_width / num_steps) - Inches(0.25)
                box_height = Inches(4.8)
                spacing = Inches(0.25)
                
                # أشكال هندسية تحاكي أدوات المختبر (كؤوس، أفران، دورق)
                lab_shapes = [
                    MSO_SHAPE.OVAL,          # يمثل عينة أو مسحوق في طبق بتري
                    MSO_SHAPE.SNIP_2_SAME_RECTANGLE, # يمثل جهاز تسخين أو فرن
                    MSO_SHAPE.CHEVRON,       # يمثل دورق تفاعل كيميائي
                    MSO_SHAPE.CAN,           # يمثل أنبوب أو محلول معالجة
                    MSO_SHAPE.ROUNDED_RECTANGLE # يمثل المنتج النهائي
                ]
                
                for i, step_text in enumerate(steps):
                    current_left = start_left + i * (box_width + spacing)
                    
                    # صندوق الخلفية لكل خطوة
                    card = slide.shapes.add_shape(
                        MSO_SHAPE.ROUNDED_RECTANGLE, 
                        current_left, start_top, box_width, box_height
                    )
                    card.fill.solid()
                    card.fill.fore_color.rgb = RGBColor(245, 248, 252) # خلفية هادئة ونظيفة
                    card.line.color.rgb = RGBColor(65, 130, 185) # إطار أزرق علمي
                    card.line.width = Pt(1.5)
                    
                    # أيقونة الأداة المخبرية في أعلى الصندوق
                    icon_type = lab_shapes[i % len(lab_shapes)]
                    icon_size = Inches(1.1)
                    icon_left = current_left + (box_width / 2) - (icon_size / 2)
                    icon_top = start_top + Inches(0.25)
                    
                    icon = slide.shapes.add_shape(icon_type, icon_left, icon_top, icon_size, icon_size)
                    icon.fill.solid()
                    icon.fill.fore_color.rgb = RGBColor(53, 108, 158)
                    icon.line.color.rgb = RGBColor(20, 60, 100)
                    
                    # صندوق النصوص للوصف
                    tb = slide.shapes.add_textbox(
                        current_left + Inches(0.1), 
                        start_top + Inches(1.45), 
                        box_width - Inches(0.2), 
                        Inches(3.2)
                    )
                    tf = tb.text_frame
                    tf.word_wrap = True
                    
                    # رقم المرحلة
                    p_num = tf.paragraphs[0]
                    p_num.text = f"Phase {i+1}"
                    p_num.font.name = "Times New Roman"
                    p_num.font.size = Pt(14)
                    p_num.font.bold = True
                    p_num.font.color.rgb = RGBColor(40, 90, 140)
                    p_num.alignment = PP_ALIGN.CENTER
                    
                    # نص الخطوة التفصيلي
                    p_desc = tf.add_paragraph()
                    p_desc.text = step_text
                    p_desc.font.name = "Times New Roman"
                    p_desc.font.size = Pt(11.5)
                    p_desc.font.color.rgb = RGBColor(40, 40, 40)
                    p_desc.alignment = PP_ALIGN.CENTER
                    
                    # رسم سهم التتابع بين الخطوات
                    if i < num_steps - 1:
                        arrow_left = current_left + box_width + Inches(0.02)
                        arrow_top = start_top + (box_height / 2) - Inches(0.2)
                        arrow = slide.shapes.add_shape(
                            MSO_SHAPE.RIGHT_ARROW,
                            arrow_left, arrow_top, Inches(0.21), Inches(0.21)
                        )
                        arrow.fill.solid()
                        arrow.fill.fore_color.rgb = RGBColor(110, 110, 110)
                        arrow.line.color.rgb = RGBCode = RGBColor(80, 80, 80) if 'RGBColor' in globals() else RGBColor(80, 80, 80)

            # حفظ الملف في الذاكرة لتنزيله
            buffer = BytesIO()
            prs.save(buffer)
            buffer.seek(0)
            
            st.success("تم توليد المخطط المخبري البصري بنجاح!")
            st.download_button(
                label="📥 تحميل ملف PowerPoint القابل للتعديل (.pptx)",
                data=buffer,
                file_name="Lab_Workflow_Graphical_Abstract.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
