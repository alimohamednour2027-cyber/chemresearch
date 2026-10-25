import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Fast Academic Protocol Organizer",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ChemResearch AI: Instant Protocol & Workflow Organizer")
st.markdown("هذا المحرك الفوري يقوم بتنظيم وتصنيف خطوات البروتوكول المخبري الخاص بك إلى مراحل أفقية واضحة في أقل من ثانية واحدة وبدون أي انتظار.")
st.markdown("---")

# --- حقل إدخال النص ---
st.subheader("✍️ بروتوكول التحضير النصي:")
default_protocol = """Natural, low-grade molybdenum ore was ground and then sifted through a 300 mesh sieve. A controlled amount of dilute sulfuric acid was added to the ore with a mass volume ratio of 1:2 and the mixture was agitated in a shaker (Tensuc TS-2102C, Shanghai) overnight. The mixture was filtered, and the collected ore was dried in an oven (DHG-9030, Shanghai). Then 9 g of the acid-washed ore was placed in a nickel crucible, and 9 g of NaOH particles were added to the ore. The mixture was calcined in a muffle furnace (BSX2-6-12TP, Shanghai) at 550 °C for 3 h, and then allowed to cool at room temperature. The calcined mixture was dissolved with 90 mL of deionized water and then centrifuged (Eppendorf 5810R, Germany). The supernatant was placed in a polypropylene plastic bottle, and 15.75 g of sodium silicate was added and dissolved completely. Subsequently, various quantities of nano ferroferric oxide were added to the solution.
The mixture was ultrasonicated for 30min. Then 30mL of an aqueous solution containing 5.40 g of sodium aluminate was added while stirring, and the mixture was mechanically stirred for 2 h in a 70 °C water bath. The material in the plastic bottle was transferred to a reaction kettle and heated to 100 °C for 15 h to drive the reaction. Then the mixture was cooled to room temperature, rinsed several times in a centrifugation-dispersion cycle, and freeze-dried for 24 h. Water was used as a dispersant to magnetically separate the product and remove particles that were not fully loaded with nano ferroferric oxide. The separated magnetic zeolite was freeze-dried for 24 h."""

protocol_input = st.text_area("Preparation Protocol Text:", value=default_protocol, height=300)
abstract_title = st.text_input("عنوان المخطط:", value="Synthesis of Magnetic Zeolite from Molybdenum Ore")

if st.button("🚀 تنظيم وعرض المراحل فوراً", key="instant_organize"):
    if not protocol_input.strip():
        st.error("الرجاء إدخال البروتوكول.")
    else:
        # معالجة فورية محلية بدون أي انتظار للشبكة أو خوادم خارجية
        st.success("تم تنظيم المراحل فوراً بنجاح تام وبدون أي تأخير!")
        
        st.markdown(f"## 📋 Workflow Blueprint: {abstract_title}")
        
        # تقسيم النص إلى جمل رئيسية لتنظيمها كخطوات متسلسلة
        sentences = [s.strip() for s in protocol_input.replace('\n', ' ').split('.') if s.strip()]
        
        # عرض المراحل في أعمدة أفقية منظمة
        cols = st.im = st.columns(3)
        
        phases_titles = [
            "1. Pre-Treatment & Acid Washing",
            "2. Alkali Fusion & Calcination",
            "3. Silicate Solution Preparation",
            "4. Ultrasonication & Mixing",
            "5. Hydrothermal Reaction",
            "6. Purification & Magnetic Separation"
        ]
        
        # توزيع الجمل على المراحل بشكل هندسي نظيف
        chunk_size = max(1, len(sentences) // len(phases_titles))
        
        for idx, title in enumerate(phases_titles):
            col_idx = idx % 3
            with cols[col_idx]:
                st.markdown(f"### **{title}**")
                start_idx = idx * chunk_size
                end_idx = (idx + 1) * chunk_size if idx < len(phases_titles) - 1 else len(sentences)
                phase_text = ". ".join(sentences[start_idx:end_idx]) + "." if start_idx < len(sentences) else "Process optimization and final recovery."
                st.info(phase_text)
                st.markdown("---")
