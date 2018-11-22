# NVDA Dodatak za sat i kalendar #

* Autori: Hrvoje Katić, Abdel i NVDA doprinositelji.
* Preuzimanje [verzije u razvojnoj fazi](https://ci.appveyor.com/project/HrvojeKati/clock/build/artifacts)

Ovaj dodatak omogućuje napredne značajke sata i kalendara za NVDA. Umjesto da dobijate samo informacije o datumu i vremenu od strane Windows sustava, pomoću ovog dodatka možete prilagoditi kako će vam NVDA izgovarati ili prikazati na brajičnom retku datum i vrijeme. Također, možete saznati trenutni broj dana i tjedana u godini, a isto tako možete postaviti automatsku najavu vremena u navedenom intervalu. Uz to, u ovom dodatku dobit ćete ugrađenu mogućnost štoperice koja će vam omogućiti mjerenje zadataka poput kopiranja datoteka, instalacije programa, ili kuhanje.

## Uporaba dodatka

*	Otvorite dijalog za konfiguraciju ovog dodatka u izborniku NVDA postavki.
	*	Prva dva odabirna okvira omogućuju vam odabir željenog oblika prikaza vremena i datuma.
	*	Potvrdni okvir pod nazivom "Unos u 24-satnom formatu" omogućuje vam da konfigurirate želite li unijeti vrijeme za tihe sate u 12 satnom (A.M. ili P.M.), ili u 24-satnom europskom obliku vremena.
	*	Odabirni okvir pod nazivom "Interval za automatsku najavu" omogućuje vam postavljanje intervala za automatsku najavu vremena (Svakih 15 minuta, Svakih pola sata, Svakih sat vremena ili Isključeno).
	*	Odabirni okvir pod nazivom "Najava vremena" omogućuje vam konfiguriranje automatskog najavljivanja vremena (govor i zvuk, samo govor ili samo zvuk) kada je automatska najava vremena uključena.
	*	Odabirni okvir pod nazivom "Zvuk zvonjenja sata" omogućuje vam biranje između različitih zvukova sata koji će se reproducirati kada je automatska najava vremena uključena i kada se najavljuje zvukom.
	*	Potvrdni okvir pod nazivom "Tihi sati" omogućuje vam da konfigurirate vremensko razdoblje kada se automatska najava vremena ne bi trebala dogoditi, bez obzira je li automatska najava vremena omogućena ili nije.
	*	Tekstualna polja za početno i krajnje vrijeme (vidljivo samo onda kada su tihi sati uključeni) omogućuju vam da konfigurirate vremensko razdoblje za tihe sate. Vrijeme treba unijeti u ss:mm obliku npr. 24:00, 06:00.
	*	Kada završite, pritisnite tipku Tab do gumba "U redu" te ga aktivirajte tipkom Enter da biste spremili postavke.
*	Pritisnite NVDA+F12 jednom da biste dobili trenutno vrijeme, dva puta da biste dobili trenutni datum ili triput da biste dobili trenutni broj dana i tjedna u tekućoj godini.

## Tipkovni prečaci

- NVDA+F12, saznaj trenutno vrijeme.
- NVDA+F12 dvaput brzo, saznaj trenutni datum.
- NVDA+F12 triput brzo, saznaj trenutni broj dana i tjedna u tekućoj godini.

## Povezane naredbe

Da biste koristili povezane naredbe, prvo pritisnite NVDA+Shift+F12, a zatim jednu od sljedećih tipki:

- S: Pokreće, resetira ili zaustavlja štopericu.
- R: Resetira štopericu na nulu bez ponovnog pokretanja.
- Razmaknica: Izgovara trenutno stanje štoperice ili odbrojavanja vremena.
- H: Pomoć, izlistava sve povezane naredbe.

