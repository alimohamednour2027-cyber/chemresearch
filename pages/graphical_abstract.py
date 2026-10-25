import streamlit as st
from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# إعدادات الصفحة
st.set_page_config(
    page_title="Synthesis Graphical Abstract Generator",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ChemResearch AI: Synthesis & Methods Graphical Abstract Generator")
st.markdown("قم بإدخال خطوات التخليق الخاصة بمادتك الماصة، وسيقوم النظام فوراً بتوليد مخطط رسومي هندسي نظيف وقابل للتعديل بصيغة PowerPoint (`.pptx`).")
st.markdown("---")

# حقل إدخال النص الخاص بخطوات التخليق
st.subheader("✍️ Enter Synthesis Steps (One step per line):")
default_steps = """1. Preparation of biomass precursor from agricultural waste.
2. Chemical impregnation using activating agent (KOH).
3. Carbonization and pyrolysis at 600 °C under N2 atmosphere.
4. Washing, neutralization, and drying to obtain the novel bio-adsorbent."""

synthesis_input = st.text_area("Synthesis Protocol Text:", value=default_steps, height=180)

material_name = st.text_input("Material / Sorbent Name for Title:", value="Novel Bio-Adsorbent Synthesis Workflow")

if st.button("🚀 Generate Editable PowerPoint Graphical Abstract", key="gen_ppt"):
    if not synthesis_input.strip():
        st.error("Please enter at least one synthesis step.")
    else:
        with st.spinner("Generating professional editable PowerPoint presentation..."):
            # إنشاء عرض تقديمي جديد
            prs = Presentation()
            prs.slide_width = Inches(13.33)  # قياس عريض قياسي Widescreen 16:9
            prs.slide_height = Inches(7.5)
            
            # إضافة شريحة فارغة
            blank_slide_layout = prs.slide_layouts[6]
            slide = prs.slides.add_slide(blank_slide_layout)
            
            # إضافة العنوان الرئيسي
            title_box = slide.shapes.add_textbox(Inches(1), Inches(0.6), Inches(11.33), Inches(0.8))
            tf_title = title_box.text_frame
            tf_title.word_wrap = True
            p_title = tf_title.paragraphs[0]
            p_title.text = f"Graphical Abstract: {material_name}"
            p_title.font.name = "Times New Roman"
            p_title.font.size = Pt(26)
            p_title.font.bold = True
            p_title.font.color.rgb = RGBColor(20, 20, 20)
            
            # تحليل الخطوات المدخلة (كل سطر يعتبر خطوة)
            steps = [line.strip() for line in synthesis_input.split('\n') if line.strip()]
            num_steps = len(steps)
            
            if num_steps > 0:
                # حساب الأبعاد وترتيب الصناديق أفقياً
                start_left = Inches(1)
                start_top = Inches(2.5)
                total_width = Inches(11.33)
                
                box_width = total_width / num_steps - Inches(0.4) if num_steps <= 4 else Inches(2.6)
                box_height = Inches(3.2)
                spacing = Inches(0.4)
                
                for i, step_text in enumerate(steps):
                    current_left = start_left + i * (box_width + spacing)
                    
                    # رسم صندوق الخطوة (شكل مستطيل بزوايا دائرية)
                    shape = slide.shapes.add_shape(
                        MSO_SHAPE.ROUNDED_RECTANGLE, 
                        current_left, start_top, box_width, box_height
                    )
                    
                    # خصائص شكل الصندوق (خلفية بيضاء نقية مع إطار هندسي نظيف)
                    shape.fill.solid()
                    shape.fill.fore_color.rgb = RGBColor(248, 249, 250)
                    shape.line.color.rgb = RGBColor(70, 130, 180)  # لون أزرق أكاديمي هادئ
                    shape.line.width = Pt(1.5)
                    
                    # إضافة النص داخل الصندوق
                    tf = shape.text_frame
                    tf.word_wrap = True
                    
                    # عنوان رقم الخطوة
                    p_step = tf.paragraphs[0]
                    p_step.text = f"Step {i+1}"
                    p_step.font.name = "Times New Roman"
                    p_step.font.size = Pt(16)
                    p_step.font.bold = True
                    p_step.font.color.rgb = RGBColor(70, 130, 180)
                    p_step.alignment = PP_ALIGN.CENTER
                    
                    # محتوى الخطوة
                    p_desc = tf.add_paragraph()
                    p_desc.text = step_text
                    p_desc.font.name = "Times New Roman"
                    p_desc.font.size = Pt(13)
                    p_desc.font.color.rgb = RGBColor(40, 40, 40)
                    p_desc.alignment = PP_ALIGN.CENTER
                    
                    # إضافة سهم اتجاهي بين الصناديق (ما عدا الصندوق الأخير)
                    if i < num_steps - 1:
                        arrow_left = current_left + box_width + Inches(0.05)
                        arrow_top = start_top + box_height / 2 - Inches(0.15)
                        arrow = slide.shapes.add_shape(
                            MSO_SHAPE.RIGHT_ARROW,
                            arrow_left, arrow_top, Inches(0.3), Inches(0.3)
                        )
                        arrow.fill.solid()
                        arrow.fill.fore_color.rgb = RGBColor(100, 100, 100)
                        arrow.line.color.rgb = RGBColor(100, 100, 100)

            # حفظ الملف في الذاكرة لتنزيله مباشرة
            pptx_buffer = BytesIO()
            prs.save(pptx_buffer)
            pptx_buffer.seek(0)
            
            st.success("Graphical abstract PowerPoint successfully generated and editable!")
            
            st.download_button(
                label="📥 Download Editable PowerPoint Graphical Abstract (.pptx)",
                data=pptx_buffer,
                file_name="Synthesis_Graphical_Abstract.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
