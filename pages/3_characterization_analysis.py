import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="ChemResearch AI: Characterization Analysis Hub",
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
    st.markdown("### Characterization Hub Navigation")
    st.caption("Active Hub: XRD, FTIR, SEM, and BET Analysis")

# قاموس الترجمات الثلاثي لهذه الصفحة (بدون إيقونات)
if lang_choice == "English":
    t_title = "ChemResearch AI: Advanced Characterization Analysis Hub"
    t_desc = "This portal is dedicated to analyzing and interpreting spectroscopic and microscopic test results (XRD, FTIR, SEM/FE-SEM, BET) based on uploaded scientific articles and references."
    tab1_name = "XRD (X-Ray Diffraction)"
    tab2_name = "FTIR (Infrared Spectroscopy)"
    tab3_name = "SEM / FE-SEM (Morphology)"
    tab4_name = "BET (Surface Area & Pores)"
    
    # XRD texts
    xrd_title = "X-Ray Diffraction (XRD) Analysis and Characterization"
    xrd_desc = "Upload the XRD curve image or data of the adsorbent, along with matching reference articles to interpret crystalline phases."
    xrd_img_lbl = "Upload XRD curve or image of the adsorbent:"
    xrd_ref_lbl = "Upload reference articles (PDF / Text) to support interpretation:"
    xrd_notes_lbl = "Additional notes on diffraction angles (2θ) or observed impurities:"
    xrd_btn = "Analyze and Formulate XRD Discussion"
    xrd_warn = "Please upload the XRD curve image first."
    xrd_succ = "XRD analysis and discussion draft successfully prepared."
    xrd_preview = "Proposed XRD Discussion Draft for Research Article:"

    # FTIR texts
    ftir_title = "Fourier-Transform Infrared Spectroscopy (FTIR) Analysis"
    ftir_desc = "Upload the FTIR spectrum to identify functional groups and chemical bonds before and after the modification process."
    ftir_img_lbl = "Upload FTIR spectrum image:"
    ftir_ref_lbl = "Upload FTIR-related references:"
    ftir_notes_lbl = "Notes on absorption peaks (e.g., O-H, Si-O, Fe-O bands):"
    ftir_btn = "Analyze and Formulate FTIR Discussion"
    ftir_warn = "Please upload the FTIR spectrum image first."
    ftir_succ = "FTIR analysis and discussion draft successfully prepared."
    ftir_preview = "Proposed FTIR Discussion Draft for Research Article:"

    # SEM texts
    sem_title = "Scanning Electron Microscopy (SEM / FE-SEM) Analysis"
    sem_desc = "Upload surface morphology and porous structure images of the adsorbent for comparison with literature."
    sem_img_lbl = "Upload SEM images of the material:"
    sem_ref_lbl = "Upload references related to surface morphology:"
    sem_notes_lbl = "Notes on surface shape, pores, and particles:"
    sem_btn = "Analyze and Formulate SEM Discussion"
    sem_warn = "Please upload SEM images first."
    sem_succ = "SEM analysis and discussion draft successfully prepared."
    sem_preview = "Proposed SEM Discussion Draft for Research Article:"

    # BET texts
    bet_title = "Specific Surface Area and Pore Size Analysis (BET)"
    bet_desc = "Upload nitrogen adsorption-desorption isotherms or BET measurement data for the adsorbent."
    bet_img_lbl = "Upload BET curve or data report:"
    bet_ref_lbl = "Upload BET reference articles:"
    bet_notes_lbl = "Derived surface area and pore volume values:"
    bet_btn = "Analyze and Formulate BET Discussion"
    bet_warn = "Please upload the BET file or image first."
    bet_succ = "BET analysis and discussion draft successfully prepared."
    bet_preview = "Proposed BET Discussion Draft for Research Article:"

elif lang_choice == "Türkçe":
    t_title = "ChemResearch AI: Gelişmiş Karakterizasyon Analiz Merkezi"
    t_desc = "Bu portal, yüklenen bilimsel makalelere ve referanslara dayanarak Spektroskopik ve mikroskobik test sonuçlarını (XRD, FTIR, SEM/FE-SEM, BET) analiz etmek ve yorumlamak için tasarlanmıştır."
    tab1_name = "XRD (X-Ray Diffraction)"
    tab2_name = "FTIR (Infrared Spectroscopy)"
    tab3_name = "SEM / FE-SEM (Morphology)"
    tab4_name = "BET (Surface Area & Pores)"
    
    xrd_title = "X-Işını Kırınımı (XRD) Analizi ve Karakterizasyonu"
    xrd_desc = "Kristal fazları yorumlamak için eşleşen referans makalelerle birlikte adsorbanın XRD eğrisini veya veri resmini yükleyin."
    xrd_img_lbl = "Adsorbanın XRD eğrisini veya resmini yükleyin:"
    xrd_ref_lbl = "Yorumlamayı desteklemek için referans makaleleri yükleyin (PDF / Metin):"
    xrd_notes_lbl = "Kırınım açıları (2θ) veya gözlenen safsızlıklar hakkında ek notlar:"
    xrd_btn = "XRD Tartışmasını Analiz Et ve Oluştur"
    xrd_warn = "Lütfen önce XRD eğrisi resmini yükleyin."
    xrd_succ = "XRD analizi ve tartışma taslağı başarıyla hazırlandı."
    xrd_preview = "Araştırma Makalesi İçin Önerilen XRD Tartışma Taslağı:"

    ftir_title = "Fourier Dönüşümlü Kızılötesi Spektroskopisi (FTIR) Analizi"
    ftir_desc = "Modifikasyon sürecinden önce ve sonra fonksiyonel grupları ve kimyasal bağları belirlemek için FTIR spektrumunu yükleyin."
    ftir_img_lbl = "FTIR spektrum resmini yükleyin:"
    ftir_ref_lbl = "FTIR ile ilgili referansları yükleyin:"
    ftir_notes_lbl = "Absorpsiyon pikleri hakkında notlar (örn. O-H, Si-O, Fe-O bantları):"
    ftir_btn = "FTIR Tartışmasını Analiz Et ve Oluştur"
    ftir_warn = "Lütfen önce FTIR spektrum resmini yükleyin."
    ftir_succ = "FTIR analizi ve tartışma taslağı başarıyla hazırlandı."
    ftir_preview = "Araştırma Makalesi İçin Önerilen FTIR Tartışma Taslağı:"

    sem_title = "Taramalı Elektron Mikroskobu (SEM / FE-SEM) Analizi"
    sem_desc = "Literatürle karşılaştırma yapmak için adsorbanın yüzey morfolojisini ve gözenekli yapı resimlerini yükleyin."
    sem_img_lbl = "Malzemenin SEM resimlerini yükleyin:"
    sem_ref_lbl = "Yüzey morfolojisi ile ilgili referansları yükleyin:"
    sem_notes_lbl = "Yüzey şekli, gözenekler ve parçacıklar hakkında notlar:"
    sem_btn = "SEM Tartışmasını Analiz Et ve Oluştur"
    sem_warn = "Lütfen
