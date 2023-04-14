# NVDA için saat ve takvim Eklentisi #

* Yazarlar: Hrvoje Katić, Abdel ve NVDA'ya katkıda bulunanlar
* [Kararlı Sürüm][1]ü indir

* NVDA uyumluluğu: 2019.3 ve üstü

Bu eklenti, NVDA için gelişmiş saat, alarm zamanlayıcı ve takvim
işlevselliğini etkinleştirir.

NVDA'yı, Windows'un varsayılan olarak sağladığından farklı biçimlerde saat
ve tarihi duyuracak şekilde yapılandırabilirsiniz. Ayrıca içinde bulunulan
gün, hafta numarası ve içinde bulunulan yılın bitmesine kalan gün sayısı
bilgisini alabilir, ayrıca belirtilen aralıkta otomatik saat duyurusu
ayarlayabilirsiniz. Eklentide yerleşik olarak bulunan ve dosya kopyalama,
program yükleme veya yemek pişirme gibi görevlerinizi zamanlamanıza olanak
tanıyan bir kronometre ve Alarm zamanlayıcı özellikleri de vardır.

Notlar:

* Eklentiyi güncelleme olarak yüklerseniz, yükleme işlemi sırasında sihirbaz
  eski konfigürasyonun yenisiyle uyumlu olup olmadığını algılar ve
  yüklemeden önce düzeltmeyi önerir, ardından onaylamak için tamam düğmesini
  seçmeniz yeterlidir.
* Windows 10 ve sonraki sürümlerde, kronometreyi ve zamanlayıcıları yönetmek
  için Alarmlar ve Saat uygulamasını kullanabilirsiniz.

## Tuş komutları

* NVDA+F12, şimdiki zamanı al;
* NVDA+F12'ye iki kez hızlıca basıldığında güncel tarihi alın;
* NVDA+F12'ye hızlı bir şekilde üç kez basıldığında içinde bulunulan günü,
  hafta numarasını, içinde bulunulan yılı ve yılın bitmesi için kalan
  günleri bildirir.
* NVDA+Shift+F12: saat komut katmanına girin

## Atanmamış komutlar

Aşağıdaki komutlar varsayılan olarak atanmamıştır; bunları atamak
istiyorsanız, özel komutlar eklemek için Girdi Hareketleri iletişim kutusunu
kullanın. Bunu yapmak için NVDA menüsünü, Tercihler'i ve ardından Girdi
Hareketlerini açın. Saat kategorisini genişletin, ardından aşağıdaki
listeden atanmamış komutları bulun ve "Ekle"yi seçin, ardından kullanmak
istediğiniz hareketi girin.

* Bir sonraki alarmdan önce geçen ve kalan süre. bu harekete hızlıca iki kez
  basmak bir sonraki alarmı iptal edecektir.
* Çalmakta olan alarm sesini durdurun.
* Alarm ayarı iletişim kutusunu aç.

## Katman komutları

Katman komutlarını kullanmak için NVDA+Shift+F12 tuşlarına ve ardından
aşağıdaki tuşlardan birine basın:

* S: Kronometreyi başlatır, sıfırlar veya durdurur
* R: Kronometreyi yeniden başlatmadan sıfırlar
* A: bir sonraki alarmdan önce kalan ve geçen süreyi verir
* T: Alarm ayarı iletişim kutusunu açar.
* C: Sonraki alarmı iptal eder
* Boşluk: Geçerli kronometreyi veya geri sayım sayacını söyler
* p: Bir alarm çok uzunsa, onu durdurmaya olanak tanır
* H: Tüm katman komutlarını listeler. (Yardım)

## Yapılandırma ve kullanım

Saat işlevini yapılandırmak için NvDA menüsünü, Tercihler'i ve ardından
Ayarlar'ı açın ve Saat panelinden aşağıdaki seçenekleri yapılandırın:

* Saat ve tarih görüntüleme formatı: NVDA+F12'ye sırasıyla bir veya iki kez
  hızlıca bastığınızda NVDA'nın saat ve tarihi nasıl duyuracağını
  yapılandırmak için bu seçim kutularını kullanın.
* Aralık: bu seçim kutusundan saat anons aralığını seçin (kapalı, her 10
  dakikada bir, her 15 dakikada bir, her 30 dakikada bir veya her saat
  başı).
* Saat anonsu (aralık kapalı değilse etkinleştirilir): konuşma ve ses,
  yalnızca ses veya yalnızca konuşma arasında seçim yapın.
* Saat zil sesi (aralık kapalı değilse etkinleştirilir): saat zil sesini
  seçin.
* Sessiz saatler (aralık kapalı değilse etkinleştirilir): Otomatik saat
  anonsunun yapılmaması gerektiğinde sessiz saatler aralığını yapılandırmak
  için bu onay kutusunu işaretleyin.
* Sessiz saat biçimi (sessiz saatler etkinse etkinleştirilir): sessiz saat
  seçeneklerinin nasıl sunulacağını seçin (12 saatlik veya 24 saatlik
  biçim).
* Sessiz saatler başlangıçv e bitiş saatleri: Saat ve dakika seçim
  kutularından sessiz saatler için saat ve dakika aralığını seçin.

Alarm programlamak için, NVDA menüsü, Araçlar'ı açın ve ardından Alarm
ayarla'yı seçin. İletişim kutusu şunları içerir:

* Alarm süre birimi: saat, dakika ve saniye arasında alarm/zamanlayıcı
  süresini seçin.
* Süre: yukarıda belirtilen birimde alarm süresini girin.
* Alarm sesi: çalınacak alarm sesini seçin.
* Durdur ve duraklat düğmeleri: uzun bir alarm sesini durdurun veya
  duraklatın.

Tamam'a bastığınızda şu anda seçilen alarm süresi  bildirilecektir.

[[!tag stable]]

[1]:
https://github.com/hkatic/clock/releases/download/24.04.0/clock-24.04.0.nvda-addon
