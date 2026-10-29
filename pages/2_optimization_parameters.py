import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Optimization Parameters Hub",
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
    st.markdown("### Optimization Hub Navigation")
    st.caption("Active Hub: Parameters & Chemical Justification")

# قاموس الترجمات الثلاثي لهذه الصفحة (بدون إيقونات)
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Optimization Parameters Hub"
    t_desc = "This portal is dedicated to analyzing and interpreting optimization parameters and providing chemical and physical justifications for optimum values."
    sec1_title = "1. Define Main Study System:"
    mode_label = "Select experiment type to study influencing factors:"
    opt_modes = [
        "Adsorption (Surface capacity and isotherm studies)",
        "SPE / MSPE (Solid-phase microextraction and recovery studies)",
        "Removal (Pollutant removal and environmental water applications)"
    ]
    sec2_title = "2. Enter Optimization Parameters Data:"
    param_lbl_ads = "Studied Parameter:"
    x_ads_lbl = "Experimental Parameter Values (comma-separated):"
    y_ads_lbl = "Resulting Values or Adsorption Capacity (qe mg/g):"
    opt_val_lbl = "Selected Optimum Point:"
    
    param_lbl_spe = "Studied Parameter:"
    x_spe_lbl = "Eluent Volume or Parameter Gradient (mL):"
    y_spe_lbl = "Recovery Percentage (% Recovery):"
    
    param_lbl_rem = "Studied Parameter:"
    x_rem_lbl = "Gradient Values (e.g., pH 2, 4, 6, 8, 10):"
    y_rem_lbl = "Removal Percentage (% Removal):"
    
    sec3_title = "3. Reference Support and Scientific Notes"
    uploader_lbl = "Upload Reference Papers Supporting Interpretation (PDF / TXT):"
    notes_lbl = "Additional Notes on Chemical Mechanism (Optional):"
    btn_generate = "Generate Q1 Analysis and Discussion Draft"
    success_msg = "Parameter analysis draft successfully prepared."
    preview_title = "Proposed Discussion Paragraph Draft (Optimization & Discussion):"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Optimizasyon Parametreleri Merkezi"
    t_desc = "Bu portal, optimizasyon parametrelerini analiz etmek ve optimum değerler için kimyasal ve fiziksel gerekçeler sunmak üzere tasarlanmıştır."
    sec1_title = "1. Ana Çalışma Sistemini Belirleyin:"
    mode_label = "Etken faktörleri incelemek için deney türünü seçin:"
    opt_modes = [
        "Adsorpsiyon (Yüzey kapasitesi ve izoterm çalışmaları)",
        "SPE / MSPE (Katı faz mikro ekstraksiyonu ve geri kazanım çalışmaları)",
        "Giderim (Kirletici giderimi ve çevre suyu uygulamaları)"
    ]
    sec2_title = "2. Optimizasyon Parametreleri Verilerini Girin:"
    param_lbl_ads = "İncelenen Parametre:"
    x_ads_lbl = "Deneysel Parametre Değerleri (virgülle ayırın):"
    y_ads_lbl = "Sonuç Değerleri veya Adsorpsiyon Kapasitesi (qe mg/g):"
    opt_val_lbl = "Seçilen Optimum Nokta:"
    
    param_lbl_spe = "İncelenen Parametre:"
    x_spe_lbl = "Elüent Hacmi veya Parametre Gradyanı (mL):"
    y_spe_lbl = "Geri Kazanım Yüzdesi (% Recovery):"
    
    param_lbl_rem = "İncelenen Parametre:"
    x_rem_lbl = "Gradyan Değerleri (örn. pH 2, 4, 6, 8, 10):"
    y_rem_lbl = "Giderim Yüzdesi (% Removal):"
    
    sec3_title = "3. Referans Desteği ve Bilimsel Notlar"
    uploader_lbl = "Yorumlamayı Destekleyen Referans Makaleleri Yükleyin (PDF / TXT):"
    notes_lbl = "Kimyasal Mekanizma Hakkında Ek Notlar (İsteğe bağlı):"
    btn_generate = "Q1 Analiz ve Tartışma Taslağı Oluştur"
    success_msg = "Parametre analiz taslağı başarıyla hazırlandı."
    preview_title = "Önerilen Tartışma Paragraf Taslağı (Optimization & Discussion):"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز معلمات التحسين المتقدمة"
    t_desc = "هذه البوابة مخصصة لتحليل وتفسير معلمات التحسين وتقديم التفسيرات الكيميائية والفيزيائية للقيمة المثلى استناداً إلى طبيعة الدراسة."
    sec1_title = "1. حدد نظام الدراسة الرئيسي:"
    mode_label = "اختر نوع التجربة لدراسة العوامل المؤثرة:"
    opt_modes = [
        "Adsorption (دراسات الامتزاز وسعة السطح)",
        "SPE / MSPE (دراسات الاستخلاص الصلب المصغر واسترداد العناصر)",
        "Removal (دراسات إزالة الملوثات وتطبيقات المياه البيئية)"
    ]
    sec2_title = "2. إدخال بيانات معلمات التحسين:"
    param_lbl_ads = "العامل المدروس:"
    x_ads_lbl = "قيم المعامل التجريبية (افصل بينها بفاصلة):"
    y_ads_lbl = "القيم الناتجة أو السعة الممتصة (qe mg/g):"
    opt_val_lbl = "القيمة المثلى المختارة (Optimum Point):"
    
    param_lbl_spe = "العامل المدروس:"
    x_spe_lbl = "تدرج حجم المذيب أو
