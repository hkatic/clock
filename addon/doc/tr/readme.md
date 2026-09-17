# NVDA için Saat ve Takvim Eklentisi #

* Yazarlar: Hrvoje Katić, Abdel ve NVDA katkıda bulunanlar
* NVDA uyumluluğu: 2019.3 ve sonrası

Bu eklenti, NVDA için gelişmiş saat, alarm zamanlayıcısı ve takvim işlevleri sağlar.

NVDA'yı, saat ve tarihi Windows'un varsayılan olarak sunduğundan farklı biçimlerde duyuracak şekilde yapılandırabilirsiniz. Ayrıca geçerli günü, hafta numarasını ve içinde bulunulan yılın sonuna kadar kalan gün sayısını öğrenebilir, belirli aralıklarla otomatik saat duyurusunu da ayarlayabilirsiniz. Eklenti ayrıca dosya kopyalama, program yükleme veya yemek pişirme gibi görevlerinizi zamanlamanıza yardımcı olan yerleşik kronometre ve alarm zamanlayıcısı özelliklerini de içerir.

Notlar:

* eklentiyi güncelleme olarak yüklerseniz, kurulum sırasında sihirbaz eski yapılandırmanın yenisiyle uyumlu olup olmadığını algılar ve kuruluma başlamadan önce düzeltmeyi önerir; ardından onaylamak için yalnızca Tamam düğmesine basmanız yeterlidir.
* Windows 10 ve sonraki sürümlerde kronometreleri ve zamanlayıcıları yönetmek için Alarmlar ve Saat uygulamasını kullanabilirsiniz.

## Tuş komutları

* NVDA+F12: geçerli saati bildirir
* NVDA+F12 tuşuna hızlıca iki kez basıldığında: geçerli tarihi bildirir
* NVDA+F12 tuşuna hızlıca üç kez basıldığında: geçerli günü, hafta numarasını, geçerli yılı ve yıl sonuna kadar kalan gün sayısını bildirir
* NVDA+Shift+F12: saat katmanına girer

## Atanmamış komutlar

Aşağıdaki komutlar varsayılan olarak atanmamıştır; bunları atamak istiyorsanız, özel komutlar eklemek için Girdi Hareketleri iletişim kutusunu kullanın. Bunun için NVDA menüsünü açın, Tercihler'i ve ardından Girdi Hareketleri'ni seçin. Saat kategorisini genişletin, aşağıdaki listede bulunan atanmamış komutlardan birini seçip "Ekle" düğmesine basın, ardından kullanmak istediğiniz hareketi girin.

* Bir sonraki alarma kadar geçen ve kalan süre. Bu harekete hızlıca iki kez basılması bir sonraki alarmı iptal eder.
* Çalmakta olan alarm sesini durdurur.
* Alarm planlama iletişim kutusunu açar.
* Katman komutlarını gösterir (NVDA+Shift+F12 tuşlarından sonra basılacak tuşlar).

## Katman komutları

Katman komutlarını kullanmak için NVDA+Shift+F12 tuşlarına bastıktan sonra aşağıdaki tuşlardan birine basın:

* S: kronometreyi başlatır, sıfırlar veya durdurur
* R: kronometreyi yeniden başlatmadan 0'a sıfırlar
* A: bir sonraki alarma kadar geçen ve kalan süreyi bildirir
* T: alarm planlama iletişim kutusunu açar.
* C: bir sonraki alarmı iptal eder
* Boşluk: geçerli kronometreyi veya geri sayım zamanlayıcısını seslendirir
* p: alarm çok uzun sürüyorsa durdurulmasını sağlar
* H: tüm katman komutlarını listeler (Yardım)

## Yapılandırma ve kullanım

Saat işlevlerini yapılandırmak için NVDA menüsünü açın, Tercihler'i, ardından Ayarlar'ı seçin ve Saat panelindeki aşağıdaki seçenekleri yapılandırın:

* Saat ve tarih görüntüleme biçimi: NVDA+F12 tuşuna sırasıyla bir veya iki kez hızlıca bastığınızda NVDA'nın saati ve tarihi nasıl duyuracağını yapılandırmak için bu birleşik kutuları kullanın.
* Aralık: bu birleşik kutudan saat duyuru aralığını seçin (kapalı, her 10 dakikada bir, her 15 dakikada bir, her 30 dakikada bir veya her saat başı).
* Saat duyurusu (aralık kapalı değilse etkin): konuşma ve ses, yalnızca ses veya yalnızca konuşma arasında seçim yapın.
  * Konuşma ve ses: Zil, tam dakika sınırında bitecek şekilde hassas bir zamanlamayla çalar, ardından hemen mevcut saat söylenir. Bu, zilin tam ana kadar geri sayımını duyduğunuz ve ardından saatin söylendiği anlamına gelir; tıpkı bir radyo yayınındaki zaman sinyali gibi.
  * BBC bip sesleri (clock_cuckoo7): Zil sesi olarak seçildiğinde, beş kısa bip sesi, dakika sınırına denk gelen altıncı uzun bip sesine yol açarak, yayın tarzı bir zaman sinyalini aslına uygun şekilde yeniden üretir. Konuşulan zaman, altıncı bip sesine eşlik eder.
  * Sadece ses: Dakika sınırında çan sesi çalar. BBC bip sesleri hassas zamanlamasını korur, bu nedenle altıncı bip sesi yine :00'a denk gelir.
  * Sadece konuşma: Dakika sınırında mevcut saati sesli olarak bildirir, zil sesi çıkarmaz.
* Saat zil sesi (aralık kapalı değilse etkinleştirilir): Ara dakikalar ve saat başı için varsayılan saat zil sesini seçin.
* Saat başı ve ara dakikalar için ayrı zil sesleri (aralık kapalı değilse etkin, varsayılan olarak devre dışıdır): ara dakikalar için kullanılacak zil sesini saat başı zil sesinden ayrı olarak özelleştirmek üzere bu onay kutusunu işaretleyin.
  * Ara dakika zil sesi ("Saat başı ve ara dakikalar için ayrı zil sesleri" seçiliyse etkin): yalnızca ara dakikalar için kullanılacak saat zil sesini seçin.
* Sessiz saatler (aralık kapalı değilse etkin): otomatik saat duyurusunun yapılmayacağı sessiz saat aralığını yapılandırmak için bu onay kutusunu işaretleyin.
* Sessiz saat biçimi (sessiz saatler etkinse etkin): sessiz saat seçeneklerinin nasıl gösterileceğini seçin (12 saatlik veya 24 saatlik biçim).
* Sessiz saatlerin başlangıç ve bitiş saatleri: saat ve dakika birleşik kutularını kullanarak sessiz saatlerin başlangıç ve bitiş aralığını seçin.

Alarm planlamak için NVDA menüsünü açın, Araçlar'ı seçin ve ardından Alarm planla'yı seçin. İletişim kutusunda şunlar bulunur:

* Alarm süresi birimi: alarm/zamanlayıcı süresi için saat, dakika veya saniyeyi seçin.
* Süre: alarm süresini yukarıda seçilen birimde girin.
* Alarm sesi: çalınacak alarm sesini seçin.
* Durdur ve Duraklat düğmeleri: uzun süren bir alarm sesini durdurur veya duraklatır.

Tamam düğmesine tıklayın; bir ileti seçili alarm süresini size bildirecektir.
