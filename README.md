
# Ay'ın Karanlık Yüzünde Tam Otonomi: Milli Keşif Aracımız İçin Akıllı Navigasyon Sistemi

İnsanoğlunun Ay'a dönüş yolculuğunda hedefler artık daha stratejik; özellikle su buzunun bulunduğu tahmin edilen Güney Kutbu bölgesi, küresel uzay ajanslarının birincil odak noktası haline geldi. Ancak bu bölge, keşif araçları için tam bir "ölüm tarlası" niteliğindedir: Zifiri karanlık krater gölgeleri (PSR), anlık iletişim kesintileri (blackout) ve yörünge uydularından tespit edilemeyecek kadar küçük ancak bir keşif aracını saniyeler içinde devirebilecek sinsi Ay kayaları...

Türkiye Uzay Ajansı'nın (TUA) **Milli Uzay Programı** ve **AYAP-2** misyonu vizyonuyla birebir örtüşen projemiz, keşif araçlarının Ay yüzeyinde sadece ilerlemesini değil, en zorlu koşullarda dahi **"hayatta kalmasını"** garanti altına alan, uçuşa hazır (mission-ready) tam otonom bir karar destek ve seyrüsefer mimarisi (VFLAI) sunmaktadır.

### 1. Etki ve Milli Uzay Programı Uyumluluğu

Projemiz, sadece teknik bir iyileştirme değil, TUA'nın stratejik hedeflerine doğrudan hizmet eden yüksek etkili bir çözümdür. Milli Uzay Programı'nın en kritik aşamalarından biri olan AYAP-2 kapsamında Ay'a indirilecek milli keşif aracımızın, milyonlarca dolarlık yatırımın ve yıllarca süren emeğin sonucunda bir krater gölgesinde donarak veya uyduda görünmeyen bir kayaya çarparak "görev kaybı" (mission failure) yaşama riskini minimize ediyoruz. Çözümümüz, Türkiye'nin uzayda bağımsız hareket kabiliyetini artırırken, "New Space" olarak adlandırılan küresel ticari uzay pazarında Türkiye'yi yüksek katma değerli bir yazılım ihracatçısı konumuna taşıma potansiyeline sahiptir.

### 2. Problemin Özü: Statik Haritaların Limitleri

Klasik keşif araçları, yörünge uydularından gelen statik haritalara (LRO NAC gibi) güvenir. Ancak bu haritaların çözünürlüğü sınırlıdır; 5 metreden küçük bir kaya, uydu görüntüsünde sadece birkaç pikseldir ve genellikle gürültü olarak algılanır. Literatürde Venu & Gurusamy (2025) tarafından da vurgulandığı üzere; dinamik zemin yapısı ve iletişim kısıtları, statik planlamayı Ay yüzeyinde işlevsiz kılmaktadır. Araç, ilerlediğini sanırken tekerlekleri Ay tozu (regolit) üzerinde boşa dönebilir veya dondurucu bir gölgenin içine girip bataryasını saniye saniyeler içinde tüketebilir. İşte bu "kör noktalar", projemizin çıkış noktasını oluşturmaktadır.

### 3. Yaratıcılık ve İnovasyon: "Ezber Bozan" Kapalı Çevrim Mimarisi

Projemizin özgünlüğü (novelty), literatürdeki klasik açık-çevrim planlayıcıların aksine, statik küresel veri ile anlık saha reflekslerini tek bir potada eriten **"Kapalı Çevrim (Closed-Loop) Hibrit Otonomi"** mimarisinden gelmektedir.

-   **Hibrit Zeka:** NASA'nın LOLA (Topoğrafya) ve LRO DIVINER (Termal) verileriyle "büyük resmi" çizerken, YOLO ve STELLA VSLAM ile "mikro detayı" sahada yakalıyoruz.
    
-   *_Dinamik-Hibrit A_:** Bu özgün algoritmamız, rotayı sadece mesafeye göre değil; eğim, güneş aydınlanma süresi ve anlık tespit edilen engelleri içeren "Çoklu Kısıtlı Maliyet Fonksiyonu" ile anlık olarak günceller. Bu, literatüre kazandırdığımız "termal-farkındalıklı" dinamik bir soluktur.
    

### 4. Bilimsel ve Teknik Geçerlilik (Fizibilite)

Sistemimiz, uzay endüstrisi standartlarında olan ROS2 LunarSim simülasyon ortamında, gerçek dünya fizik kuralları altında test edilmiştir.

-   **YOLO tabanlı Engel Segmentasyonu:** Uyduda görünmeyen engelleri milisaniyeler içinde tespit ederek çarpışma riskini ortadan kaldırır.
    
-   **STELLA VSLAM:** İletişim koptuğunda veya sensörler arızalandığında "Görsel Odometri" ile aracın nerede olduğunu milimetrik hesaplayarak "Güvenli Bölge" seyrüseferini başlatır. Testlerimiz sonucunda, Mutlak Yörünge Hatası (RMSE) ve işlem gecikmesi (latency) değerleri, AYAP-2 gibi gerçek görev isterlerinin çok altında kalarak teknik fizibilitesini kanıtlamıştır.
    

### 5. Görev Uyumluluğu ve Sunum Başarısı

Hackathon kapsamında verilen "Challenge" içeriğine, Ay'ın en kritik kısıtları olan **Termal Değişimler**, **Engel Lokalizasyonu** ve **Sinyal Kesintileri** başlıklarını adresleyerek tam sadık kaldık. Hazırladığımız prototip, karmaşık matematiksel modelleri (Dinamik A*) kullanıcı dostu bir arayüz ve simülasyon görselleriyle hikayeleştirerek sunmaktadır. Projemiz; mühendislik derinliğini, operasyonel gerçekçilikle birleştirerek Ay yüzeyi otonomisi için eksiksiz bir çözüm sunar.

**Sonuç olarak;** VFLAI projesi, Türkiye'nin Ay'daki ayak izini kalıcı ve güvenli kılmak için tasarlanmış; bilimsel temelleri sağlam, inovatif ve Milli Uzay Programı vizyonuyla tam uyumlu bir derin teknoloji ürünüdür.
