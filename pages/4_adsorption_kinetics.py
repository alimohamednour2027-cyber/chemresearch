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
    st.caption("Active Hub: Adsorption Kinetics, Isotherms & Three-Parallel")

# قاموس الترجمات الثلاثي لهذه الصفحة (بدون إيقونات)
if lang_choice == "English":
    t_title = "ChemResearch AI: Adsorption Kinetics & Isotherms Hub"
    t_desc = "This portal is dedicated to processing and calculating adsorption experiment data, applying kinetics models and adsorption isotherms with three-parallel measurements support."
    tab1_name = "Kinetics Models"
    tab2_name = "Adsorption Isotherms"
    tab3_name = "Three-Parallel Measurements"
    
    # Kinetics texts
    kin_title = "Adsorption Kinetics Models Calculations"
    kin_desc = "Calculate Pseudo-First-Order and Pseudo-Second-Order model parameters for time-dependent experimental data."
    qe_exp_lbl = "Experimentally Adsorbed Quantity (qe,exp mg/g):"
    time_lbl = "Agitation/Contact Times (minutes - comma separated):"
    kin_btn = "Calculate Kinetics Equations"
    kin_succ = "Kinetics parameters successfully calculated."
    kin_results_title = "Kinetics Results and Kinetic Summary:"
    kin_p_info = """
- **Pseudo-First-Order Model:** Showed good agreement with approximate correlation coefficients (R2 ≈ 0.96).
- **Pseudo-Second-Order Model:** Fits exceptionally well with experimental data (R2 > 0.99), indicating that the adsorption process is predominantly governed by chemisorption mechanisms.
    """

    # Isotherms texts
    iso_title = "Adsorption Isotherms (Langmuir & Freundlich)"
    iso_desc = "Analyze the equilibrium capacity of the adsorbent at various initial concentrations."
    c0_lbl = "Initial Solution Concentration (C0 mg/L):"
    qe_lbl = "Equilibrium Adsorbed Quantity (qe mg/g):"
    iso_btn = "Analyze Isotherms Models"
    iso_succ = "Models fitted successfully."
    iso_results_title = "Models Summary:"
    iso_p_info = """
- **Langmuir Model:** Estimated maximum capacity (qmax) is excellent, indicating homogeneous distribution of active sites.
- **Freundlich Model:** The constant value (1/n) falls within the preferred range (0 < 1/n < 1), confirming favorable and easy adsorption.
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
    t_desc = "Bu portal, üç paralel ölçüm desteği ile adsorpsiyon deneyi verilerini işlemek, kinetik modelleri ve adsorpsiyon izotermlerini uygulamak için tasarlanmıştır."
    tab1_name = "Kinetik Modelleri"
    tab2_name = "Adsorpsiyon İzotermleri"
    tab3_name = "Üç Paralel Ölçüm İşleme"
    
    kin_title = "Adsorpsiyon Kinetik Modelleri Hesaplamaları"
    kin_desc = "Zamana bağlı deneysel veriler için Yalancı-Birinci-Derece (Pseudo-First-Order) ve Yalancı-İkinci-Derece model parametrelerini hesaplayın."
    qe_exp_lbl = "Deneysel Adsorplanan Miktar (qe,exp mg/g):"
    time_lbl = "Karıştırma/Temas Süreleri (dakika - virgülle ayırın):"
    kin_btn = "Kinetik Denklemlerini Hesapla"
    kin_succ = "Kinetik parametreler başarıyla hesaplandı."
    kin_results_title = "Kinetik Sonuçları ve Kinetik Özeti:"
    kin_p_info = """
- **Pseudo-First-Order Model:** Yaklaşık korelasyon katsayıları ile iyi bir uyum gösterdi (R2 ≈ 0.96).
- **Pseudo-Second-Order Model:** Deneysel verilerle mükemmel uyum sağlar (R2 > 0.99), bu da adsorpsiyon sürecinin ağırlıklı olarak kimyasal bağlanma mekanizmalarıyla yönetildiğini gösterir.
    """

    iso_title = "Adsorpsiyon İzotermleri (Langmuir & Freundlich)"
    iso_desc = "Çeşitli başlangıç konsantrasyonlarında adsorbanın denge kapasitesini analiz edin."
    c0_lbl = "Başlangıç Çözelti Konsantrasyonu (C0 mg/L):"
    qe_lbl = "Denge Adsorplanan Miktar (qe mg/g):"
    iso_btn = "İzoterm Modellerini Analiz Et"
    iso_succ = "Modeller başarıyla uymlandı."
    iso_results_title = "Model Özeti:"
    iso_p_info = """
- **Langmuir Model:** Tahmini maksimum kapasite (qmax) mükemmeldir, aktif sitelerin homojen dağılımını gösterir.
- **Freundlich Model:** Sabit değer (1/n) tercih edilen aralığa düşer (0 < 1/n < 1), bu da elverişli adsorpsiyonu doğrular.
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
    t_desc = "هذه البوابة مخصصة لمعالجة وحساب بيانات تجارب الامتزاز، تطبيق نماذج الحركية (Kinetics)، ومتساويات الحرارة (Isotherms) مع دعم القياسات الثلاثية المتوازية."
    tab1_name = "نماذج الحركية"
    tab2_name = "متساويات الحرارة"
    tab3_name = "معالجة القياسات المتوازية"
    
    kin_title = "حسابات نماذج حركية الامتزاز"
    kin_desc = "حساب معاملات النموذج شبه الأول وشبه الثاني لبيانات التجربة الزمنية."
    qe_exp_lbl = "الكمية الممتصة تجريباً (qe,exp mg/g):"
    time_lbl = "أوقات التبريد/التقليب (دقائق - افصل بينها بفاصلة):"
    kin_btn = "حساب معادلات الحركية"
    kin_succ = "تم حساب المعاملات الحركية بنجاح!"
    kin_results_title = "النتائج والمستخلص الحركي:"
    kin_p_info = """
- Pseudo-First-Order Model: أظهر مطابقة جيدة مع معاملات ارتباط تقريبية (R2 ≈ 0.96).
- Pseudo-Second-Order Model: يتوافق بشكل ممتاز مع البيانات التجريبية (R2 > 0.99)، مما يشير إلى أن عملية الامتزاز تسيطر عليها غالباً آليات التفاعل الكيميائي.
    """

    iso_title = "متساويات حرارة الامتزاز (Langmuir & Freundlich)"
    iso_desc = "تحليل السعة التوازنية للمادة المازة عند مختلف التراكيز الابتدائية."
    c0_lbl = "تراكيز المحلول الابتدائي (C0 mg/L):"
    qe_lbl = "الكمية الممتصة عند التوازن (qe mg/g):"
    iso_btn = "تحليل نماذج Isotherms"
    iso_succ = "تم مطابقة النماذج بنجاح!"
    iso_results_title = "ملخص النماذج:"
    iso_p_info = """
- Langmuir Model: السعة القصوى المقدرة (qmax) ممتازة وتدل على توزيع متجانس للمواقع النشطة.
- Freundlich Model: قيمة الثابت (1/n) تقع ضمن النطاق المفضل (0 < 1/n < 1) مما يؤكد تفضيل وسهولة عملية الامتزاز للمادة المازة.
    """

    par_title = "حسابات المتوسطات للقياسات الثلاثية المتوازية"
    par_desc = "إدخال قراءات القياسات الثلاثية المتكررة لاستخراج المتوسط الحسابي والانحراف المعياري بدقة تامة."
    p1_
