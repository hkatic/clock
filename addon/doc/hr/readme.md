# Sat i kalendar, dodatak za NVDA #

* Autori: Hrvoje Katić, Abdel i NVDA suradnici;
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]


Ovaj dodatak omogućuje funkcionalnost za napredni sat, alarm i kalendar za
NVDA.

Umjesto dobivanja podataka za vrijeme i datum od Windowsa, moguće je
prilagoditi način izgovora i prikaza na brajičnom retku za vrijeme i datum
putem NVDA.

Osim toga je moguće saznati trenutačni dan, broj tjedna i broj preostalih
dana tekuće godine. Može se postaviti i automatska najava vremena u
određenim intervalima.

U dodatak su ugrađene i funkcije štoperice i alarma, koje omogućuju mjerenje
vremena za zadatke, poput kopiranja datoteka, instaliranja programa ili
kuhanja obroka.

## Napomena:

Ako se dodatak instalira kao nadogradnja, tijekom instalacije čarobnjak
otkriva je li stara konfiguracija kompatibilna s novom i nudi mogućnost za
njeno ispravljanja prije instalacije. To se jednostavno potvrđuje gumbom „U
redu”.

## Primjena

* Otvori dijalog za konfiguraciju ovog dodatak u NVDA izborniku Alati ili u
  ploči postavaka, ovisno o NVDA verziji;

    * U dijalogu za postavljanje sata, prva dva odabirna okvira omogućuju
      biranje željenog formata za prikaz vremena i datuma;
    * Odabirni okvir s oznakom „Interval” omogućuje postavljanje intervala
      za automatsku najavu vremena (svakih 10 minuta, svakih 15 minuta,
      svakih 30 minuta, svakih sat vremena ili isključeno);
    * Odabirni okvir s oznakom „Najava vremena” (vidljiv je samo, ako u
      odabirnom okviru za interval nije odabrano „isključeno”) dozvoljava
      konfiguriranje automatske najave vremena (govor i zvuk, samo govor ili
      samo zvuk), kad se pokrene automatska najava vremena;
    * Odabirni okvir s oznakom „Zvuk zvona sata” (vidljiv je samo, ako u
      odabirnom okviru za interval nije odabrano „isključeno”) dozvoljava
      biranje raznih zvukova sata, koji se puštaju kad se pokrene automatska
      najava vremena i kad se o najavi izvještava zvukom;
    * Potvrdni okvir s oznakom „Sati mirovanja” (vidljiv je samo, ako u
      odabirnom okviru za interval nije odabrano „isključeno”) dozvoljava
      konfiguriranje vremenskog raspona u kojem se automatska najava vremena
      ne primijenjuje;
    * Potvrdni okvir s oznakom „Sati mirovanja” (vidljiv je samo, ako u
      odabirnom okviru za interval nije odabrano „isključeno”) dozvoljava
      konfiguriranje načina unosa vremena, u 12-satnom formatu (A.M. ili
      P.M.) ili u 24-satnom formatu;
    * Okvir za uređivanje početnog i završnog vremena (vidljivo samo, ako su
      sati mirovanja uključeni) omogućuje konfiguriranje vremenskog raspona
      za sate mirovanja. Vrijeme se treba unijeti u formatu HH:MM, ako je
      potvrdni okvir za „Unos u 24-satnom formatu” odabran. U protivnom
      treba koristiti 12-satni format, kao što je opisano niže dolje;
    * Na kraju prijeđi na gumb „U redu” pomoću tabulatora i aktiviraj gumb
      pritiskom tipke Enter, kako bi se postavke spremile;
    * U dijalogu za postavljanje alarma, prvi odabirni okvir omogućuje
      biranje željenog mjerača vremena za odbrojavanje do alarma;
    * Okvir za uređivanje omogućuje upisivanje vremena čekanja prije
      zvonjave alarma. To se trajanje mora odrediti pomoću jedne ili više
      znamenki, a ne decimalnim brojem;
    * Odabirni okvir s oznakom „Zvuk alarma” omogućuje biranje različitih
      zvukova alarma, koji će se svirati kad dođe vrijeme alarma;
    * Gumb „Pauza” omogućuje pauzu/nastavak dugih alarma;
    * Gumb „Zaustavi” omogućuje zaustavljanje dugih alarma;
    * Na kraju, prijeđi na gumb „U redu” i aktiviraj ga pritiskom na
      Enter. Trebala bi se prikazati poruka koja podsjeća na vrijeme čekanja
      prije alarma;

* Pritisni NVDA+F12 za trenutačno vrijeme, dvaput za trenutačni datum,
  triput za trenutačni dan, tjedan i preostale dane do kraja tekuće godine.

## Tipkovničke naredbe

* NVDA+F12, javi trenutačno vrijeme;
* NVDA+F12 dvaput brzo, javi trenutačni datum;
* NVDA+F12 triput brzo, izvještava o trenutačnom danu, broju tjedna, tekućoj
  godini i o danima koji su preostali do kraja godine.
* Postoji skripta za javljanje preostalog i proteklog vremena do sljedećeg
  alarma;
* Ovoj skripti nije dodijeljen nijedan tipkovnički prečac. To treba obaviti
  u dijalogu za „Ulazni prečaci” u kategoriji „Sat”;
* Ovaj tipkovnički prečac pritisnut dvaput brzo, otkazuje sljedeći alarm;
* Postoji jedna druga skripta za zaustavljanje trenutačnog zvuka,
  tipkovnički prečac za nju također nije definiran;
* Ta skripta se može pokrenuti i pomoću višeslojnih naredbi za sat, opisani
  niže dolje.

## Višeslojne naredbe

Za korištenje višeslojnih naredbi, pritisni NVDA+šift+F12 i zatim jednu od
sljedećih tipki:

* S: Pokreće, zaustavlja ili resetira štopericu;
* R: Resetira štopericu na nulu bez ponovnog pokretanja;
* A: Izdaje proteklo vrijeme i preostalo vrijeme prije sljedećeg alarma;
* C: Otkaži sljedeći alarm;
* Razmaknica: Izgovara trenutačno stanje štoperice ili odbrojavanja vremena;
* p: Ako alarm traje predugo, dozvoli ga zaustaviti;
* H: Popis svih višeslojnih prečaca (Pomoć).

## Sintaksa za sate mirovanja

* Da bi se izbjegle greške, sati mirovanja moraju slijediti strogu i točnu
  sintaksu;
* Ako je „Unos u 24-satnom formatu” aktivirano, format mora biti „HH:MM”;
* Ako je „Unos u 24-satnom formatu” deaktivirano, format mora biti „HH:MM
  AM” ili „HH:MM PM”, HH mora sadržati 12-satni format od 0 do 12, a
  nastavak „AM/PM” se može pisati velikim ili malim slovima
* Ako su „Sati mirovanja” aktivirani, a polja za „Početno vrijeme za sate
  mirovanja” ili „Završno vrijeme za sate mirovanja” prazna ili je unesena
  neispravna vrijednost, „Sati mirovanja” će se automatski deaktivirati,
  kako bi se izbjegle greške;
* Treba se prikazati poruka za izvještavanje o grešci.

## Kompatibilnost

* Ovaj dodatak je kompatibilan s NVDA verzijom 2014.3 do 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

