import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Smart Graphical Abstract Bridge",
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
    st.markdown("### Graphical Abstract Navigation")
    st.caption("Active Hub: Protocol Organizer & Master Prompt Bridge")

# قاموس الترجمات الثلاثي لهذه الصفحة (بدون إيقونات)
if lang_choice == "English":
    t_title = "ChemResearch AI: Smart Protocol Organizer & Bridge"
    t_desc = "Input any random or unstructured experimental text, and the system will instantly analyze and formulate it into precise academic stages, preparing the final prompt for free tools."
    sec1_label = "Enter Experimental Details (Free or unstructured writing):"
    default_text = "Natural low grade molybdenum ore was ground and sifted. We added sulfuric acid and agitated it overnight then dried in oven DHG-9030. Next we mixed with NaOH in nickel crucible and calcined at 550 C. Dissolved in water, centrifuged with Eppendorf 5810R, added sodium silicate and nano Fe3O4, ultrasonicated, stirred with sodium aluminate at 70 C, heated in reaction kettle at 100 C for 15 hours, and finally magnetically separated and freeze dried."
    title_label = "Main Graphical Abstract Title:"
    default_abs_title = "SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE"
    btn_process = "Process and Organize Text into Academic Stages"
    spinner_text = "Analyzing unstructured text and classifying it into sequential scientific stages..."
    success_process = "Text successfully analyzed and organized into precise academic stages."
    sec2_label = "Organized Stages and Master Prompt Readiness:"
    sec3_label = "Quick Transition to Free Design Tools:"
    tool1_title = "Microsoft Designer / Copilot (Fully Free)"
    tool1_link = "Open Bing Image Creator / Copilot"
    tool2_title = "ChatGPT (Free Version)"
    tool2_link = "Open ChatGPT"
    sec4_label = "Final Image Import and Display Window:"
    uploader_label = "Upload the image after generating it from free tools to document it in your research report:"
    success_upload = "Image successfully approved and linked to the platform."

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Akıllı Protokol Düzenleyici ve Köprü"
    t_desc = "Herhangi bir rastgele veya yapılandırılmamış deneysel metni girin; sistem bunu hemen analiz ederek hassas akademik aşamalara dönüştürür ve ücretsiz araçlar için son komut istemini hazırlar."
    sec1_label = "Deneysel Detayları Girin (Serbest veya yapılandırılmamış yazı):"
    default_text = "Natural low grade molybdenum ore was ground and sifted. We added sulfuric acid and agitated it overnight then dried in oven DHG-9030. Next we mixed with NaOH in nickel crucible and calcined at 550 C. Dissolved in water, centrifuged with Eppendorf 5810R, added sodium silicate and nano Fe3O4, ultrasonicated, stirred with sodium aluminate at 70 C, heated in reaction kettle at 100 C for 15 hours, and finally magnetically separated and freeze dried."
    title_label = "Ana Grafik Özet Başlığı:"
    default_abs_title = "SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE"
    btn_process = "Metni Akademik Aşamalara Dönüştür ve Düzenle"
    spinner_text = "Yapılandırılmamış metin analiz ediliyor ve ardışık bilimsel aşamalara sınıflandırılıyor..."
    success_process = "Metin başarıyla analiz edildi ve hassas akademik aşamalara düzenlendi."
    sec2_label = "Düzenlenmiş Aşamalar ve Master Prompt Hazırlığı:"
    sec3_label = "Ücretsiz Tasarım Araçlarına Hızlı Geçiş:"
    tool1_title = "Microsoft Designer / Copilot (Tamamen Ücretsiz)"
    tool1_link = "Bing Image Creator / Copilot'u Aç"
    tool2_title = "ChatGPT (Ücretsiz Sürüm)"
    tool2_link = "ChatGPT'yi Aç"
    sec4_label = "Final Resim İçe Aktarma ve Görüntüleme Penceresi:"
    uploader_label = "Araştırma raporunuzda belgelendirmek için ücretsiz araçlardan aldıktan sonra resmi yükleyin:"
    success_upload = "Görsel başarıyla onaylandı ve platforma bağlandı."

else:  # العربية
    t_title = "المنصة الأكاديمية: منظم البروتوكول الذكي وجسر الربط"
    t_desc = "قم بإدخال أي نص تجريبي عشوائي أو غير منظم، وسيقوم النظام فوراً بتحليله وصياغته في مراحل أكاديمية دقيقة، وتجهيز الوصف النهائي لتصديره للأدوات المجانية."
    sec1_label = "أدخل تفاصيل التجربة العملية (يمكنك كتابتها بشكل حر أو غير منظم):"
    default_text = "Natural low grade molybdenum ore was ground and sifted. We added sulfuric acid and agitated it overnight then dried in oven DHG-9030. Next we mixed with NaOH in nickel crucible and calcined at 550 C. Dissolved in water, centrifuged with Eppendorf 5810R, added sodium silicate and nano Fe3O4, ultrasonicated, stirred with sodium aluminate at 70 C, heated in reaction kettle at 100 C for 15 hours, and finally magnetically separated and freeze dried."
    title_label = "عنوان المخطط الرئيسي:"
    default_abs_title = "SYNTHESIS OF MAGNETIC ZEOLITE FROM LOW-GRADE MOLYBDENUM ORE"
    btn_process = "معالجة وتنظيم النص إلى مراحل أكاديمية"
    spinner_text = "جاري تحليل النص العشوائي وتصنيفه إلى مراحل علمية متسلسلة..."
    success_process = "تم تحليل النص وتنظيمه بنجاح إلى مراحل أكاديمية دقيقة!"
    sec2_label = "المراحل المنظمة وجاهزية الوصف (Master Prompt):"
    sec3_label = "الانتقال السريع إلى الأدوات المجانية:"
    tool1_title = "Microsoft Designer / Copilot (مجاني بالكامل)"
    tool1_link = "افتح Bing Image Creator / Copilot"
    tool2_title = "ChatGPT (النسخة المجانية)"
    tool2_link = "افتح موقع ChatGPT"
    sec4_label = "نافذة استيراد وعرض الصورة النهائية في المنصة:"
    uploader_label = "قم برفع الصورة بعد استخراجها من الأدوات المجانية لتوثيقها في تقرير بحثك:"
    success_upload = "تم اعتماد الصورة وربطها بالمنصة بنجاح!"

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header
