import streamlit as st
from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

st.set_page_config(
    page_title="Visual Synthesis Graphical Abstract Generator",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 ChemResearch AI: Visual Laboratory Graphical Abstract Generator")
st.markdown("هذا المحرك يترجم خطوات التخليق الخاصة بك إلى **مخطط بصري احترافي يحتوي على أدوات مختبرية مرسومة (كؤوس زجاجية، مواقد، أجهزة طرد مركزي)**، وكلها عناصر هندسية **قابلة للتعديل والتحريك بنسبة 100%** داخل برنامج PowerPoint.")
st.markdown("---")

st.subheader("✍️ Enter Synthesis Laboratory Steps (One step per line):")
default_steps = """1. Biomass Preparation: Grinding and sieving agricultural waste precursor.
2. Chemical Impregnation: Mixing with activating agent (KOH) in a glass beaker.
3. Thermal Pyrolysis: Carbonization in a tube furnace at 600 °C under N2.
4. Washing & Drying: Filtration, neutralization, and drying to yield final bio-adsorbent."""

synthesis_input = st.text_area("Laboratory Synthesis Protocol:", value=default_steps, height=180)
material_name = st.text_input("Material / Sorbent Name:", value="Novel Bio-Adsorbent Synthesis Flowchart")

if st.button("🚀 Generate Visual Lab-Style PowerPoint Abstract", key="gen_visual_ppt"):
    if not synthesis_input.strip():
        st.error("Please enter at least one synthesis step.")
    else:
        with st.spinner("Generating professional visual laboratory graphical abstract..."):
            prs = Presentation()
            prs.slide_width = Inches(13.33)  # عرض قياسي 16:9
            prs.slide_height = Inches(7.5)
            
            blank_slide_layout = prs.slide_layouts[6]
            slide = prs.slides.add_slide(blank_slide_layout)
            
            # عنوان الشريحة الأكاديمي
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.73), Inches(0.8))
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_title = tf_title.paragraphs[0]
            p_title.text = f"Visual Graphical Abstract: {material_name}"
            p_title.font.name = "Times New Roman"
            p_title.font.size = Pt(24)
            p_title.font.bold = True
            p_title.font.color.rgb = RGBColor(20, 20, 20)
            
            steps = [line.strip() for line in synthesis_input.split('\n') if line.strip()]
            num_steps = len(steps)
            
            if num_steps > 0:
                start_left = Inches(0.8)
                start_top = Inches(2.2)
                total_width = Inches(11.73)
                
                box_width = total_width / num_steps - Inches(0.3) if num_steps <= 4 else Inches(2.6)
                box_height = Inches(4.5)
                spacing = Inches(0.3)
                
                # قائمة الأشكال المعبرة عن أدوات المختبر لكل مرحلة
                lab_icons = [
                    MSO_SHAPE.CAN,          # يمثل دورق أو وعاء تفاعل
                    MSO_SHAPE.HEXAGON,      # يمثل عملية خلط كيميائي
                    MSO_SHAPE.CHEVRON,      # يمثل وحدة تسخين / فرن حراري
                    MSO_SHAPE.ROUNDED_RECTANGLE # يمثل الناتج النهائي المغسول والجاف
                ]
                
                for i, step_text in enumerate(steps):
                    current_left = start_left + i * (box_width + spacing)
                    
                    # 1. رسم صندوق الإطار الرئيسي للخطوة
                    card_bg = slide.shapes.add_shape(
                        MSO_SHAPE.ROUNDED_RECTANGLE, 
                        current_left, start_top, box_width, box_height
                    )
                    card_bg.fill.solid()
                    card_bg.fill.fore_color.rgb = RGBColor(250, 252, 255) # خلفية بيضاء زرقة خفيفة جداً
                    card_bg.line.color.rgb = RGBColor(70, 130, 180)  # إطار أزرق أكاديمي
                    card_bg.line.width = Pt(1.5)
                    
                    # 2. رسم أيقونة أداة المختبر التعبيرية في أعلى صندوق الخطوة
                    icon_shape_type = lab_icons[i % len(lab_icons)]
                    icon_size = Inches(0.9)
                    icon_left = current_left + (box_width / 2) - (icon_size / 2)
                    icon_top = start_top + Inches(0.3)
                    
                    icon_shape = slide.shapes.add_shape(icon_shape_type, icon_left, icon_top, icon_size, icon_size)
                    icon_shape.fill.solid()
                    icon_shape.fill.fore_color.rgb = RGBColor(70, 130, 180) # لون أداة المختبر
                    icon_shape.line.color.rgb = RGBColor(30, 80, 120)
                    
                    # 3. إضافة النصوص (عنوان الخطوة والمحتوى)
                    text_box = slide.shapes.add_textbox(
                        current_left + Inches(0.15), 
                        start_top + Inches(1.3), 
                        box_width - Inches(0.3), 
                        Inches(3.0)
                    )
                    tf = text_box.text_frame
                    tf.word_wrap = True
                    
                    # رقم المرحلة أو عنوانها
                    p_step = tf.paragraphs[0]
                    p_step.text = f"Stage {i+1}"
                    p_step.font.name = "Times New Roman"
                    p_step.font.size = Pt(15)
                    p_step.font.bold = True
                    p_step.font.color.rgb = RGBColor(30, 80, 120)
                    p_step.alignment = PP_ALIGN.CENTER
                    
                    # وصف تفاصيل الخطوة المخبرية
                    p_desc = tf.add_paragraph()
                    p_desc.text = step_text
                    p_desc.font.name = "Times New Roman"
                    p_desc.font.size = Pt(12)
                    p_desc.font.color.rgb = RGBColor(50, 50, 50)
                    p_desc.alignment = PP_ALIGN.CENTER
                    
                    # 4. إضافة سهم اتجاهي هندسي بين المراحل (ما عدا المرحلة الأخيرة)
                    if i < num_steps - 1:
                        arrow_left = current_left + box_width + Inches(0.02)
                        arrow_top = start_top + box_height / 2 - Inches(0.2)
                        arrow = slide.shapes.add_shape(
                            MSO_SHAPE.RIGHT_ARROW,
                            arrow_left, arrow_top, Inches(0.26), Inches(0.26)
                        )
                        arrow.fill.solid()
                        arrow.fill.fore_color.rgb = RGBColor(120, 120, 120)
                        arrow.line.color.rgb = RGBColor(100, 100, 100)

            # حفظ ملف الـ PowerPoint في الذاكرة لتنزيله الفوري
            pptx_buffer = BytesIO()
            prs.save(pptx_buffer)
            pptx_buffer.seek(0)
            
            st.success("Visual laboratory graphical abstract successfully generated!")
            
            st.download_button(
                label="📥 Download Visual Editable PowerPoint (.pptx)",
                data=pptx_buffer,
                file_name="Lab_Visual_Graphical_Abstract.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
