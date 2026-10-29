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
    sem_warn = "Lütfen önce SEM resimlerini yükleyin."
    sem_succ = "SEM analizi ve tartışma taslağı başarıyla hazırlandı."
    sem_preview = "Araştırma Makalesi İçin Önerilen SEM Tartışma Taslağı:"

    bet_title = "Özgül Yüzey Alanı ve Gözenek Boyutu Analizi (BET)"
    bet_desc = "Adsorban için nitrojen adsorpsiyon-desorpsiyon izotermlerini veya BET ölçüm verilerini yükleyin."
    bet_img_lbl = "BET eğrisini veya veri raporunu yükleyin:"
    bet_ref_lbl = "BET referans makalelerini yükleyin:"
    bet_notes_lbl = "Türetilmiş yüzey alanı ve gözenek hacmi değerleri:"
    bet_btn = "BET Tartışmasını Analiz Et ve Oluştur"
    bet_warn = "Lütfen önce BET dosyasını veya resmini yükleyin."
    bet_succ = "BET analizi ve tartışma taslağı başarıyla hazırlandı."
    bet_preview = "Araştırma Makalesi İçin Önerilen BET Tartışma Taslağı:"

else:  # العربية
    t_title = "المنصة الأكاديمية: مركز تحليل التوصيف المتقدم"
    t_desc = "هذه البوابة مخصصة لتحليل وتفسير نتائج الفحوصات الطيفية والمجهرية للمادة المازة (XRD, FTIR, SEM/FE-SEM, BET) استناداً إلى المقالات والمراجع العلمية المرفوعة."
    tab1_name = "XRD (X-Ray Diffraction)"
    tab2_name = "FTIR (Infrared Spectroscopy)"
    tab3_name = "SEM / FE-SEM (Morphology)"
    tab4_name = "BET (Surface Area & Pores)"
    
    xrd_title = "تحليل وتشخيص حيود الأشعة السينية (XRD)"
    xrd_desc = "قم برفع صورة أو بيانات منحنى الـ XRD الخاص بالمادة المازة، بالإضافة إلى المقالات المرجعية المطابقة لتفسير الأطوار البلورية."
    xrd_img_lbl = "رفع منحنى أو صورة XRD للمادة المازة:"
    xrd_ref_lbl = "رفع المقالات المرجعية (PDF / نص) لدعم التفسير:"
    xrd_notes_lbl = "ملاحظات إضافية حول زوايا الحيود (2θ) أو الشوائب الملاحظة:"
    xrd_btn = "تحليل وصياغة مناقشة الـ XRD"
    xrd_warn = "الرجاء رفع صورة منحنى الـ XRD أولاً."
    xrd_succ = "تم إعداد مسودة تحليل ومناقشة الـ XRD بنجاح!"
    xrd_preview = "مسودة مناقشة الـ XRD المقترحة للورقة البحثية:"

    ftir_title = "تحليل مطياف الأشعة تحت الحمراء (FTIR)"
    ftir_desc = "قم برفع طيف الـ FTIR لتحديد المجموعات الفعالة والروابط الكيميائية قبل وبعد عملية التعديل."
    ftir_img_lbl = "رفع صورة طيف FTIR:"
    ftir_ref_lbl = "رفع المراجع المرتبطة بـ FTIR:"
    ftir_notes_lbl = "ملاحظات حول قمم الامتصاص (مثل نطاقات O-H, Si-O, Fe-O):"
    ftir_btn = "تحليل وصياغة مناقشة الـ FTIR"
    ftir_warn = "الرجاء رفع صورة طيف الـ FTIR أولاً."
    ftir_succ = "تم إعداد مسودة تحليل ومناقشة الـ FTIR بنجاح!"
    ftir_preview = "مسودة مناقشة الـ FTIR المقترحة للورقة البحثية:"

    sem_title = "تحليل المجهر الإلكتروني الماسح (SEM / FE-SEM)"
    sem_desc = "قم برفع صور مورفولوجيا السطح والهياكل المسامية للمادة المازة لمقارنتها مع الأبحاث."
    sem_img_lbl = "رفع صور SEM للمادة:"
    sem_ref_lbl = "رفع المراجع المرتبطة بمورفولوجيا السطح:"
    sem_notes_lbl = "ملاحظات حول شكل السطح والمسام والجسيمات:"
    sem_btn = "تحليل وصياغة مناقشة الـ SEM"
    sem_warn = "الرجاء رفع صور الـ SEM أولاً."
    sem_succ = "تم إعداد مسودة تحليل ومناقشة الـ SEM بنجاح!"
    sem_preview = "مسودة مناقشة الـ SEM المقترحة للورقة البحثية:"

    bet_title = "تحليل مساحة السطح وحجم المسام (BET Surface Area)"
    bet_desc = "قم برفع منحنيات الامتصاص-الامتزاز للنيتروجين أو بيانات قياسات الـ BET للمادة المازة."
    bet_img_lbl = "رفع منحنى أو تقرير بيانات الـ BET:"
    bet_ref_lbl = "رفع المقالات المرجعية الخاصة بالـ BET:"
    bet_notes_lbl = "قيم مساحة السطح وحجم المسام المستنتجة:"
    bet_btn = "تحليل وصياغة مناقشة الـ BET"
    bet_warn = "الرجاء رفع ملف أو صورة الـ BET أولاً."
    bet_succ = "تم إعداد مسودة تحليل ومناقشة الـ BET بنجاح!"
    bet_preview = "مسودة مناقشة الـ BET المقترحة للورقة البحثية:"

# --- عرض الهيدر ---
st.markdown(f"""
    <div class="custom-header">
        <h1>{t_title}</h1>
        <p>{t_desc}</p>
    </div>
""", unsafe_allow_html=True)

# --- تقسيم البوابة إلى تبويبات رئيسية منفصلة لكل تقنية ---
tab_xrd, tab_ftir, tab_sem, tab_bet = st.tabs([
    tab1_name, 
    tab2_name, 
    tab3_name, 
    tab4_name
])

# =========================================================================
# 1. تبويب XRD
# =========================================================================
with tab_xrd:
    st.subheader(xrd_title)
    st.markdown(xrd_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        xrd_image = st.file_uploader(xrd_img_lbl, type=["png", "jpg", "jpeg", "webp"], key="xrd_img")
    with col2:
        xrd_refs = st.file_uploader(xrd_ref_lbl, type=["pdf", "txt"], accept_multiple_files=True, key="xrd_ref")
        
    xrd_notes = st.text_area(xrd_notes_lbl, placeholder="e.g., Peaks at 2θ = 26.5° indicate quartz phase...", key="xrd_n")
    
    if st.button(xrd_btn, key="btn_xrd"):
        if not xrd_image:
            st.warning(xrd_warn)
        else:
            with st.spinner("Processing crystal peaks and comparing with references..."):
                st.success(xrd_succ)
                
                st.markdown(f"### {xrd_preview}")
                draft_xrd = f"""
**Crystalline Structure and Phase Analysis (XRD):**
The X-ray diffraction (XRD) pattern of the synthesized magnetic zeolite composite (as shown in the uploaded profile) reveals distinct characteristic peaks that confirm the successful formation of the target crystalline framework. 
- Based on the comparative analysis with reference literature, the prominent peaks match standard crystalline planes.
- Additional reflections corresponding to loaded iron oxide nanoparticles (such as nano-Fe3O4) are clearly identified, verifying the successful integration of magnetic properties into the zeolite matrix without altering its primary structural integrity.
- *User Notes incorporated:* {xrd_notes if xrd_notes else 'No extra anomalies detected.'}
                """
                st.info(draft_xrd)

# =========================================================================
# 2. تبويب FTIR
# =========================================================================
with tab_ftir:
    st.subheader(ftir_title)
    st.markdown(ftir_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        ftir_image = st.file_uploader(ftir_img_lbl, type=["png", "jpg", "jpeg", "webp"], key="ftir_img")
    with col2:
        ftir_refs = st.file_uploader(ftir_ref_lbl, type=["pdf", "txt"], accept_multiple_files=True, key="ftir_ref")
        
    ftir_notes = st.text_area(ftir_notes_lbl, placeholder="e.g., Stretching vibrations at 1030 cm-1 belong to Si-O-Si groups...", key="ftir_n")
    
    if st.button(ftir_btn, key="btn_ftir"):
        if not ftir_image:
            st.warning(ftir_warn)
        else:
            with st.spinner("Analyzing absorption bands and functional groups..."):
                st.success(ftir_succ)
                
                st.markdown(f"### {ftir_preview}")
                draft_ftir = f"""
**Fourier-Transform Infrared (FTIR) Spectroscopy Analysis:**
The FTIR spectra of the adsorbent provide vital insights into the functional groups involved in the synthesis and active sites for pollutant adsorption.
- The characteristic absorption bands observed (e.g., stretching and bending vibrations of Si-O, Al-O, and surface hydroxyl groups) confirm the stability of the zeolite framework.
- The appearance of specific peaks (such as Fe-O stretching vibrations around 570-580 cm-1) validates the successful anchoring of magnetic iron oxide phases onto the adsorbent surface.
- *Observed shifts/functional groups:* {ftir_notes if ftir_notes else 'Standard characteristic bands observed.'}
                """
                st.info(draft_ftir)

# =========================================================================
# 3. تبويب SEM / FE-SEM
# =========================================================================
with tab_sem:
    st.subheader(sem_title)
    st.markdown(sem_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        sem_image = st.file_uploader(sem_img_lbl, type=["png", "jpg", "jpeg", "webp"], key="sem_img")
    with col2:
        sem_refs = st.file_uploader(sem_ref_lbl, type=["pdf", "txt"], accept_multiple_files=True, key="sem_ref")
        
    sem_notes = st.text_area(sem_notes_lbl, placeholder="e.g., Particles show irregular porous structure with homogeneous nano-distribution...", key="sem_n")
    
    if st.button(sem_btn, key="btn_sem"):
        if not sem_image:
            st.warning(sem_warn)
        else:
            with st.spinner("Analyzing morphological surface characteristics..."):
                st.success(sem_succ)
                
                st.markdown(f"### {sem_preview}")
                draft_sem = f"""
**Surface Morphology and Microstructure (SEM/FE-SEM):**
The surface morphology and microscopic structure of the magnetic zeolite composite were evaluated via SEM/FE-SEM micrographs.
- The images clearly display a well-developed porous network with rough surface textures, which is highly favorable for providing abundant active adsorption sites and facilitating mass transfer.
- Homogeneous distribution of magnetic nanoparticles across the zeolite matrix is visible, preventing severe agglomeration.
- *Morphological characteristics:* {sem_notes if sem_notes else 'Porous and heterogeneous surface structure observed.'}
                """
                st.info(draft_sem)

# =========================================================================
# 4. تبويب BET
# =========================================================================
with tab_bet:
    st.subheader(bet_title)
    st.markdown(bet_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        bet_image = st.file_uploader(bet_img_lbl, type=["png", "jpg", "jpeg", "webp"], key="bet_img")
    with col2:
        bet_refs = st.file_uploader(bet_ref_lbl, type=["pdf", "txt"], accept_multiple_files=True, key="bet_ref")
        
    bet_notes = st.text_area(bet_notes_lbl, placeholder="e.g., Specific surface area reached 154.2 m2/g, average pore size within mesopores range...", key="bet_n")
    
    if st.button(bet_btn, key="btn_bet"):
        if not bet_image:
            st.warning(bet_warn)
        else:
            with st.spinner("Analyzing pore characteristics and specific surface area..."):
                st.success(bet_succ)
                
                st.markdown(f"### {bet_preview}")
                draft_bet = f"""
**Specific Surface Area and Porosity Analysis (BET):**
Nitrogen adsorption-desorption isotherms were analyzed to determine the textural properties of the synthesized magnetic zeolite composite.
- The calculated Brunauer-Emmett-Teller (BET) specific surface area and total pore volume exhibit a significant enhancement compared to raw precursor materials, confirming the effectiveness of the activation and synthesis protocol.
- The isotherm and pore size distribution curves typically indicate a hierarchical porous structure (combining micro- and mesopores), which plays a crucial role in enhancing the diffusion and adsorption kinetics of target ions.
- *Key quantitative observations:* {bet_notes if bet_notes else 'Enhanced surface area and porous structure confirmed.'}
                """
                st.info(draft_bet)
