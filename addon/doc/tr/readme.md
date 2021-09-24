# NVDA için saat ve takvim Eklentisi #

* Yazarlar: Hrvoje Katić, Abdel ve NVDA'ya katkıda bulunanlar
* [Kararlı Sürüm][1]ü indir
* [geliştirici sürümü][2].nü indir
* NVDA uyumluluğu: 2019.3 ve sonrası

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
istediğiniz hareketi yapın.

* Bir sonraki alarmdan önce geçen ve kalan süre. bu harekete hızlıca iki kez
  basmak bir sonraki alarmı iptal edecektir.
* Çalmakta olan alarm sesini durdurun.

## Katman komutları

Katman komutlarını kullanmak için NVDA+Shift+F12 tuşlarına ve ardından
aşağıdaki tuşlardan birine basın:

* S: Kronometreyi başlatır, sıfırlar veya durdurur
* R: Kronometreyi yeniden başlatmadan sıfırlar
* A: bir sonraki alarmdan önce kalan ve geçen süreyi verir
* C: Sonraki alarmı iptal eder
* Boşluk: Geçerli kronometreyi veya geri sayım sayacını söyler
* p: Bir alarm çok uzunsa, onu durdurmaya olanak tanır
* H: Tüm katman komutlarını listeler. (Yardım)

## kullanım

* NVDA ayarlar iletişim kutusunda eklenti ile ilgili kategori altından
  gerekli ayarları yapabilirsiniz.

    * Saat ayarı iletişim kutusunda, ilk iki seçim kutusu denetimi, tercih
      ettiğiniz saat ve tarih görüntüleme biçimlerini seçmenize olanak
      tanır.
    * "saat anons Aralığı" etiketli seçim kutusu, otomatik zaman duyurusu
      aralığını ayarlamanıza olanak tanır (Her 10 dakikada bir, Her 15
      dakikada bir, Her 30 dakikada bir, Her saatte bir veya Kapalı);
    * "saat anons" etiketli seçim kutusu denetimi (yalnızca Seçim Kutusu
      aralığında "kapalı" seçeneği seçilmemişse görünür) otomatik saat
      duyurusu çalışırken otomatik saat duyurusunun nasıl raporlanacağını
      (Konuşma ve ses, Yalnızca konuşma veya Yalnızca ses) yapılandırmanıza
      olanak tanır;
    * "Saat zil sesi" etiketli seçim kutusu denetimi (yalnızca Birleşik
      Giriş Kutusu aralığında "kapalı" seçeneği seçilmediğinde görünür)
      otomatik zaman anonsu çalışırken çalınacak ve sesli olarak
      bildirilecek çeşitli saat sesleri arasında seçim yapmanızı sağlar;
    * "Sessiz saatler" etiketli Onay Kutusu denetimi (yalnızca Açılan Kutu
      aralığında "kapalı" seçeneği seçili değilse görünür), otomatik zaman
      duyurusunun gerçekleşmemesi gereken zaman aralığını yapılandırmanıza
      olanak tanır;
    * "24 saat biçiminde giriş" etiketli Onay Kutusu denetimi (yalnızca
      sessiz saatler etkinleştirildiğinde görünür) sessiz saatler için 12
      saatlik (A.M. veya P.M.) veya Avrupa 24 saatlik formatta zaman girmek
      isteyip istemediğinizi yapılandırmanıza olanak tanır;
    * Başlangıç ve bitiş zamanı için yazı alanı denetimleri (yalnızca sessiz
      saatler etkinse görünür), sessiz saatler için zaman aralığını
      yapılandırmanıza olanak tanır. "24 saatlik formatta giriş" onay kutusu
      işaretliyse, saat SS:DD formatında girilmelidir, aksi takdirde aşağıda
      açıklandığı gibi 12 saatlik bir format kullanmanız gerekir;
    * Bittiğinde, Tamam düğmesine tıklayın ve ayarlarınızı kaydetmek için
      Enter'a basarak etkinleştirin;
    * Alarm kurma iletişim kutusunda, ilk seçim kutusu denetimi alarm
      çalmadan önce tercih ettiğiniz geri sayım sayacını seçmenize olanak
      tanır;
    * Düzenleme kutusu kontrolü, alarm çalmadan önce beklediğiniz süreyi
      yazmanıza olanak tanır. Bu süre ondalık sayı olarak değil, 1 veya daha
      fazla basamakla belirtilmelidir;
    * "Alarm sesi" etiketli seçim kutusu denetimi, alarm zamanı geldiğinde
      çalınacak çeşitli alarm sesleri arasında seçim yapmanızı sağlar;
    * Duraklat düğmesi, çok uzun alarmları duraklatmanıza/devam ettirmenize
      olanak tanır;
    * Durdur düğmesi, çok uzun alarmları durdurmanıza olanak tanır;
    * Bittiğinde, Tamam düğmesine gidin ve Enter'a basarak
      etkinleştirin. Alarmdan önceki bekleme süresini hatırlatmak için bir
      mesaj görüntülenmelidir;

* Geçerli saati almak için NVDA+F12'ye bir kez, güncel tarihi almak için iki
  kez veya geçerli günü, hafta numarasını ve mevcut yılın bitiminden önceki
  kalan günleri almak için üç kez basın.

## Sessiz saatler için kullanılacak sözdizimi

1. Hatalardan kaçınmak için, sessiz saatler titiz ve kesin bir sözdizimi
   izlemelidir;
2. "24 saatlik formatta gir" onay kutusunu işaretlerseniz, format "SS:DD"
   olmalıdır;
3. "24 saatlik biçimde gir" onay kutusunun işaretini kaldırırsanız, biçim
   "SS:DD ÖÖ" veya "SS:DD ÖÖ" olmalıdır, SS 0'dan 12 saatlik bir biçim
   içermelidir 12'ye kadar ve "AM"|"PM" soneki küçük veya büyük harf
   olabilir
4. Sessiz saatler" onay kutusunu işaretlediğiniz halde "Sessiz saatler
   başlangıç zamanı" veya "Sessiz saatler bitiş zamanı" alanını boş
   tutarsanız veya yanlış bir değer girerseniz, "Sessiz saatler" onay
   kutusunun işareti otomatik olarak kaldırılır , hataları önlemek için;

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
