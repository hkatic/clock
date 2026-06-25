# Sat i kalendar, dodatak za NVDA

* Autori: Hrvoje Katić, Abdel i suradnici na NVDA-u
* Kompatibilnost s NVDA-om: 2019.3 i novije verzije

Ovaj dodatak omogućuje napredne funkcije sata, mjerača vremena za alarme i kalendara u NVDA-u.

Možete konfigurirati NVDA da najavljuje vrijeme i datum u formatima koji se razlikuju od zadanih formata sustava Windows. Osim toga, možete saznati trenutačni dan, broj tjedna, kao i broj preostalih dana do kraja tekuće godine, a možete postaviti i automatsku najavu vremena u određenim vremenskim intervalima. Dodatak također uključuje štopericu i mjerač vremena za alarme koji vam omogućuju mjerenje trajanja raznih zadataka, poput kopiranja datoteka, instalacije programa ili kuhanja.

Napomene:

* Ako dodatak instalirate kao nadogradnju, tijekom instalacije čarobnjak će otkriti je li stara konfiguracija kompatibilna s novom te će prije instalacije ponuditi njezino ispravljanje. Za potvrdu će biti dovoljno pritisnuti gumb U redu.
* U sustavu Windows 10 i novijim verzijama možete koristiti aplikaciju Alarmi i sat za upravljanje štopericom i mjeračima vremena.

## Tipkovnički prečaci

* NVDA+F12: izgovara trenutačno vrijeme
* Dvaput brzo pritisnite NVDA+F12: izgovara trenutačni datum
* Triput brzo pritisnite NVDA+F12: izgovara trenutačni dan, broj tjedna, tekuću godinu i broj preostalih dana do kraja godine
* NVDA+Shift+F12: ulazi u sloj naredbi sata

## Nedodijeljene naredbe

Sljedeće naredbe nisu dodijeljene prema zadanim postavkama. Ako ih želite dodijeliti, upotrijebite dijaloški okvir Ulazne geste za dodavanje prilagođenih naredbi. Da biste to učinili, otvorite izbornik NVDA, Postavke, zatim Ulazne geste. Proširite kategoriju Sat, pronađite jednu od nedodijeljenih naredbi s donjeg popisa, odaberite „Dodaj”, a zatim pritisnite željenu gestu.

* Izgovara proteklo i preostalo vrijeme do sljedećeg alarma. Dvostrukim brzim pritiskom ove geste otkazuje se sljedeći alarm.
* Zaustavlja trenutačno reproducirani zvuk alarma.
* Prikazuje dijaloški okvir za zakazane alarme.
* Prikazuje slojevite naredbe (tipke koje treba pritisnuti nakon NVDA+Shift+F12).

## Slojevite naredbe

Za korištenje slojevitih naredbi pritisnite NVDA+Shift+F12, a zatim jednu od sljedećih tipki:

* S: Pokreće, ponovno postavlja ili zaustavlja štopericu
* R: Ponovno postavlja štopericu na 0 bez njezina ponovnog pokretanja
* A: Izgovara proteklo i preostalo vrijeme do sljedećeg alarma
* T: Otvara dijaloški okvir za zakazivanje alarma.
* C: Otkazuje sljedeći alarm
* Razmaknica: Izgovara trenutačno stanje štoperice ili mjerača vremena za odbrojavanje
* P: Ako alarm traje predugo, omogućuje njegovo zaustavljanje
* H: Prikazuje popis svih slojevitih naredbi (Pomoć)

## Konfiguracija i korištenje

Za konfiguriranje funkcija sata otvorite izbornik NVDA, Postavke, zatim Postavke, a potom u kategoriji Sat podesite sljedeće mogućnosti:

* Format prikaza vremena i datuma: pomoću ovih kombiniranih okvira odredite kako će NVDA izgovarati vrijeme i datum kada jednom ili dvaput brzo pritisnete NVDA+F12.
* Interval: u ovom kombiniranom okviru odaberite interval automatske najave vremena (isključeno, svakih 10 minuta, 15 minuta, 30 minuta ili svakog sata).
* Najava vremena (omogućeno ako interval nije isključen): odaberite između govora i zvuka, samo zvuka ili samo govora.
* Zvuk zvonjave sata (omogućeno ako interval nije isključen): odaberite zadani zvuk zvonjave sata za međuminute i puni sat.
* Odvojeni zvukovi za puni sat i međuminute (omogućeno ako interval nije isključen, prema zadanim postavkama onemogućeno): označite ovaj potvrdni okvir kako biste zasebno prilagodili zvukove za međuminute i puni sat.
  * Zvuk zvonjave za međuminute (omogućeno ako je označena mogućnost „Odvojeni zvukovi za puni sat i međuminute”): odaberite zvuk koji će se koristiti posebno za međuminute.
* Tihi sati (omogućeno ako interval nije isključen): označite ovaj potvrdni okvir kako biste odredili razdoblje tijekom kojeg se automatska najava vremena neće izvršavati.
* Format vremena za tihe sate (omogućeno ako su tihi sati uključeni): odaberite način prikaza mogućnosti tihih sati (12-satni ili 24-satni format).
* Vrijeme početka i završetka tihih sati: u kombiniranim okvirima za sate i minute odaberite početak i završetak razdoblja tihih sati.

Za zakazivanje alarma otvorite izbornik NVDA, Alati, a zatim odaberite Zakazani alarmi. Dijaloški okvir sadrži sljedeće elemente:

* Trajanje alarma u: odaberite trajanje alarma ili mjerača vremena u satima, minutama ili sekundama.
* Trajanje: unesite trajanje alarma u prethodno odabranoj jedinici.
* Zvuk alarma: odaberite zvuk koji će se reproducirati.
* Gumbi Zaustavi i Pauza: zaustavljaju ili privremeno prekidaju dugačak zvuk alarma.

Kliknite U redu, a poruka će vas obavijestiti o trenutačno odabranom trajanju alarma.
