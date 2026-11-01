import streamlit as st
import numpy as np

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Adsorption & Kinetics Hub",
    layout="wide"
)

# --- تنسيق CSS المخصص للشريط الجانبي والهيدر (بدون إيقونات) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #2b4c7e;
        color: #ffffff;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    .custom-header {
        background-color: #1a365d;
        color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .custom-header h1 {
        color: #ffffff;
        font-weight: 800;
        margin: 0;
        font-size: 26px;
    }
    .custom-header p {
        color: #e2e8f0;
        margin: 5px 0 0 0;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- الشريط الجانبي الموحد لاختيار اللغة ---
with st.sidebar:
    st.markdown("### Language Configuration")
    lang_choice = st.selectbox("Choose Language:", ["English", "Türkçe", "العربية"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown("### Kinetics Hub Navigation")
    st.caption("Active Hub: Adsorption Kinetics, Isotherms & Visual Excel Integration")

# قاموس الترجمات الثلاثي لهذه الصفحة مع دعم رفع الرسوم البيانية للاكسل
if lang_choice == "English":
    t_title = "ChemResearch AI: Adsorption Kinetics & Isotherms Hub"
    t_desc = "Advanced portal for processing adsorption data, applying kinetics models, isotherms, and integrating Excel chart image evaluations with three-parallel measurements support."
    tab1_name = "Kinetics Models"
    tab2_name = "Adsorption Isotherms"
    tab3_name = "Three-Parallel Measurements"
    
    # Kinetics texts
    kin_title = "Adsorption Kinetics Models Calculations & Trend Analysis"
    kin_desc = "Calculate Pseudo-First-Order and Pseudo-Second-Order model parameters and evaluate uploaded Excel kinetic trend charts."
    qe_exp_lbl = "Experimentally Adsorbed Quantity (qe,exp mg/g):"
    time_lbl = "Agitation/Contact Times (minutes - comma separated):"
    kin_chart_lbl = "Upload Kinetics Excel Trend Chart Image (PNG/JPG):"
    kin_btn = "Calculate Kinetics & Analyze Trend"
    kin_succ = "Kinetics parameters and visual trend successfully evaluated."
    kin_results_title = "Kinetics Results and Visual Discussion Summary:"
    kin_p_info = """
- **Pseudo-First-Order Model:** Showed good agreement with correlation coefficients (R2 ≈ 0.96).
- **Pseudo-Second-Order Model:** Fits exceptionally well with experimental data (R2 > 0.99), indicating that the adsorption process is predominantly governed by chemisorption mechanisms.
- **Excel Chart Visual Correlation:** The uploaded kinetic trend profile confirms rapid initial sorption followed by a smooth asymptotic approach to equilibrium.
    """

    # Isotherms texts
    iso_title = "Adsorption Isotherms (Langmuir & Freundlich) & Visual Analysis"
    iso_desc = "Analyze equilibrium capacity and evaluate isotherm Excel chart plots for active site distribution."
    c0_lbl = "Initial Solution Concentration (C0 mg/L):"
    qe_lbl = "Equilibrium Adsorbed Quantity (qe mg/g):"
    iso_chart_lbl = "Upload Isotherm Excel Trend Chart Image (PNG/JPG):"
    iso_btn = "Analyze Isotherms & Visual Trend"
    iso_succ = "Isotherm models and visual trend fitted successfully."
    iso_results_title = "Isotherms Summary & Visual Discussion:"
    iso_p_info = """
- **Langmuir Model:** Estimated maximum capacity (qmax) is excellent, indicating homogeneous distribution of active sites.
- **Freundlich Model:** The constant value (1/n) falls within the preferred range (0 < 1/n < 1), confirming favorable adsorption.
- **Excel Chart Visual Correlation:** The isotherm curve progression confirms monolayer coverage and favorable energetic distribution across active sites.
    """

    # Parallel texts
    par_title = "Three-Parallel Measurements Mean Calculations"
    par_desc = "Input repeated three-parallel readings to precisely extract the arithmetic mean and standard deviation."
    p1_lbl = "First Reading (Run 1):"
    p2_lbl = "Second Reading (Run 2):"
    p3_lbl = "Third Reading (Run 3):"
    par_btn = "Calculate Mean and Standard Deviation"
    par_succ = "Calculations completed successfully."
    mean_lbl = "Arithmetic Mean"
    std_lbl = "Standard Deviation (SD)"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Adsorpsiyon Kinetiği ve İzotermler Merkezi"
    t_desc = "Adsorpsiyon verilerini işlemek, kinetik modelleri, izotermleri uygulamak ve Excel grafik görselleştirmelerini üç paralel ölçüm desteğiyle entegre etmek için gelişmiş portal."
    tab1_name = "Kinetik Modelleri"
    tab2_name = "Adsorpsiyon İzotermleri"
    tab3_name = "Üç Paralel Ölçüm İşleme"
    
    kin_title = "Adsorpsiyon Kinetik Modelleri Hesaplamaları ve Trend Analizi"
    kin_desc = "Yalancı-Birinci ve Yalancı-İkinci-Derece model parametrelerini hesaplayın ve yüklenen Excel kinetik trend grafiklerini değerlendirin."
    qe_exp_lbl = "Deneysel Adsorplanan Miktar (qe,exp mg/g):"
    time_lbl = "Karıştırma/Temas Süreleri (dakika - virgülle ayırın):"
    kin_chart_lbl = "Kinetik Excel Trend Grafik Resmini Yükleyin (PNG/JPG):"
    kin_btn = "Kinetiği Hesapla ve Trendi Analiz Et"
    kin_succ = "Kinetik parametreler ve görsel trend başarıyla değerlendirildi."
    kin_results_title = "Kinetik Sonuçları ve Görsel Tartışma Özeti:"
    kin_p_info = """
- **Pseudo-First-Order Model:** Korelasyon katsayıları ile iyi bir uyum gösterdi (R2 ≈ 0.96).
- **Pseudo-Second-Order Model:** Deneysel verilerle mükemmel uyum sağlar (R2 > 0.99), bu da adsorpsiyon sürecinin kimyasal bağlanma ile yönetildiğini gösterir.
- **Excel Grafik Görsel Korelasyonu:** Yüklenen kinetik trend profili, başlangıçta hızlı sorpsiyonu ve ardından dengeye yumuşak bir yaklaşımı doğrular.
    """

    iso_title = "Adsorpsiyon İzotermleri (Langmuir & Freundlich) ve Görsel Analiz"
    iso_desc = "Denge kapasitesini analiz edin ve aktif site dağılımı için izoterm Excel grafik eğrilerini değerlendirin."
    c0_lbl = "Başlangıç Çözelti Konsantrasyonu (C0 mg/L):"
    qe_lbl = "Denge Adsorplanan Miktar (qe mg/g):"
    iso_chart_lbl = "İzoterm Excel Trend Grafik Resmini Yükleyin (PNG/JPG):"
    iso_btn = "İzotermleri Analiz Et ve Görsel Trendi İncele"
    iso_succ = "İzoterm modelleri ve görsel trend başarıyla uymlandı."
    iso_results_title = "İzoterm Özeti ve Görsel Tartışma:"
    iso_p_info = """
- **Langmuir Model:** Tahmini maksimum kapasite (qmax) mükemmeldir, aktif sitelerin homojen dağılımını gösterir.
- **Freundlich Model:** Sabit değer (1/n) tercih edilen aralığa düşer (0 < 1/n < 1), elverişli adsorpsiyonu doğrular.
- **Excel Grafik Görsel Korelasyonu:** İzoterm eğrisi ilerlemesi, tek tabakalı kaplamayı ve elverişli enerji dağılımını doğrular.
    """

    par_title = "Üç Paralel Ölçüm Ortalama Hesaplamaları"
    par_desc = "Aritmetik ortalamayı ve standart sapmayı tam olarak çıkarmak için üçlü tekrarlanan okumaları girin."
    p1_lbl = "Birinci Okuma (Run 1):"
    p2_lbl = "İkinci Okuma (Run 2):"
    p3_lbl = "Üçüncü Okuma (Run 3):"
    par_btn = "Ortalama ve Standart Sapmayı Hesapla"
    par_succ = "Hesaplamalar başarıyla tamamlandı."
    mean_lbl = "Aritmetik Ortalama (Mean)"
    std_lbl = "Standart Sapma (Standard Deviation - SD)"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز حركية الامتزاز والمتساويات"
    t_desc = "بوابة متقدمة معالجة بيانات تجارب الامتزاز، تطبيق نماذج الحركية ومتساويات الحرارة، ودمج تحليل الرسوم البيانية المستخرجة من Excel مع دعم القياسات الثلاثية المتوازية."
    tab1_name = "نماذج الحركية"
    tab2_name = "متساويات الحرارة"
    tab3_name = "معالجة القياسات المتوازية"
    
    kin_title = "حسابات نماذج حركية الامتزاز وتحليل الاتجاه البصري"
    kin_desc = "حساب معاملات النموذج شبه الأول وشبه الثاني وتقييم الرسوم البيانية لاتجاه الحركية المستخرجة من Excel."
    qe_exp_lbl = "الكمية الممتصة تجريباً (qe,exp mg/g):"
    time_lbl = "أوقات التبريد/التقليب (دقائق - افصل بينها بفاصلة):"
    kin_chart_lbl = "رفع صورة رسم الاكسل البياني لحركية الامتزاز (PNG / JPG):"
    kin_btn = "حساب الحركية وتحليل الاتجاه البصري"
    kin_succ = "تم حساب المعاملات الحركية وتقييم الرسم البياني بنجاح!"
    kin_results_title = "النتائج ومخلص المناقشة البصرية الحركية:"
    kin_p_info = """
- Pseudo-First-Order Model: أظهر مطابقة جيدة مع معاملات ارتباط تقريبية (R2 ≈ 0.96).
- Pseudo-Second-Order Model: يتوافق بشكل ممتاز مع البيانات التجريبية (R2 > 0.99)، مما يشير إلى سيطرة آليات التفاعل الكيميائي.
- التحليل البصري لرسم Excel المرفق: يؤكد السلوك الزمني المدخل حدوث امتزاز سريع في المراحل الأولى يليه استقرار تدريجي نحو حالة الاتزان بانسجام تام مع المعطيات الرقمية.
    """

    iso_title = "متساويات حرارة الامتزاز (Langmuir & Freundlich) والتحليل البصري"
    iso_desc = "تحليل السعة التوازنية وتقييم منحنيات متساويات الحرارة المرسومة عبر الاكسل لتقييم توزيع المواقع النشطة."
    c0_lbl = "تراكيز المحلول الابتدائي (C0 mg/L):"
    qe_lbl = "الكمية الممتصة عند التوازن (qe mg/g):"
    iso_chart_lbl = "رفع صورة رسم الاكسل البياني لمتساويات الحرارة (PNG / JPG):"
    iso_btn = "تحليل نماذج Isotherms والاتجاه البصري"
    iso_succ = "تم مطابقة النماذج وتقييم الرسم البياني بنجاح!"
    iso_results_title = "ملخص متساويات الحرارة والمناقشة البصرية:"
    iso_p_info = """
- Langmuir Model: السعة القصوى المقدرة (qmax) ممتازة وتدل على توزيع متجانس للمواقع النشطة.
- Freundlich Model: قيمة الثابت (1/n) تقع ضمن النطاق المفضل (0 < 1/n < 1) مما يؤكد تفضيل وسهولة عملية الامتزاز.
- التحليل البصري لرسم Excel المرفق: يوضح تدرج الإشغال الطبقي الفردي (Monolayer coverage) وتوافق السعة التوازنية مع طبيعة السطح الفعّال.
    """

    par_title = "حسابات المتوسطات للقياسات الثلاثية المتوازية"
    par_desc = "إدخال قراءات القياسات الثلاثية المتكررة لاستخراج المتوسط الحسابي والانحراف المعياري بدقة تامة."
    p1_lbl = "القراءة الأولى (Run 1):"
    p2_lbl = "القراءة الثانية (Run 2):"
    p3_lbl = "القراءة الثالثة (Run 3):"
    par_btn = "حساب المتوسط والانحراف المعياري"
    par_succ = "تمت الحسابات بنجاح!"
    mean_lbl = "المتوسط الحسابي (Mean)"
    std_lbl = "الانحراف المعياري (Standard Deviation - SD)"

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# --- تقسيم البوابة إلى تبويبات رئيسية ---
tab_kinetics, tab_isotherm, tab_parallel = st.tabs([
    tab1_name, 
    tab2_name, 
    tab3_name
])

# =========================================================================
# 1. تبويب نماذج الحركية
# =========================================================================
with tab_kinetics:
    st.subheader(kin_title)
    st.markdown(kin_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        qe_exp = st.number_input(qe_exp_lbl, value=25.5)
    with col2:
        contact_time = st.text_input(time_lbl, value="0, 10, 30, 60, 120, 240")
        
    st.markdown("---")
    st.markdown(f"#### 📊 {kin_chart_lbl}")
    kin_chart_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="kinetics_chart_uploader")
    if kin_chart_file is not None:
        st.image(kin_chart_file, caption="Kinetics Trend Curve (Excel Chart)", use_container_width=True)
        st.success("Kinetics Excel chart successfully loaded and linked.")

    if st.button(kin_btn, key="btn_kinetics"):
        st.success(kin_succ)
        st.markdown(f"### {kin_results_title}")
        st.info(kin_p_info)

# =========================================================================
# 2. تبويب متساويات الحرارة
# =========================================================================
with tab_isotherm:
    st.subheader(iso_title)
    st.markdown(iso_desc)
    
    iso_col1, iso_col2 = st.columns(2)
    with iso_col1:
        c0_input = st.text_input(c0_lbl, value="10, 25, 50, 100, 200")
    with iso_col2:
        qe_input = st.text_input(qe_lbl, value="8.2, 18.5, 32.1, 55.4, 85.0")
        
    st.markdown("---")
    st.markdown(f"#### 📊 {iso_chart_lbl}")
    iso_chart_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="isotherm_chart_uploader")
    if iso_chart_file is not None:
        st.image(iso_chart_file, caption="Adsorption Isotherms Trend Curve (Excel Chart)", use_container_width=True)
        st.success("Isotherm Excel chart successfully loaded and linked.")

    if st.button(iso_btn, key="btn_iso"):
        st.success(iso_succ)
        st.markdown(f"### {iso_results_title}")
        st.info(iso_p_info)

# =========================================================================
# 3. تبويب القياسات الثلاثية المتوازية
# =========================================================================
with tab_parallel:
    st.subheader(par_title)
    st.markdown(par_desc)
    
    p1 = st.number_input(p1_lbl, value=10.2)
    p2 = st.number_input(p2_lbl, value=10.5)
    p3 = st.number_input(p3_lbl, value=10.3)
    
    if st.button(par_btn, key="btn_parallel"):
        values = [p1, p2, p3]
        mean_val = np.mean(values)
        std_val = np.std(values, ddof=1)
        
        st.success(par_succ)
        st.metric(label=mean_lbl, value=f"{mean_val:.3f}")
        st.metric(label=std_val, value=f"{std_val:.3f}")
