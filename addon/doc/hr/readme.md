# Sat i kalendar, dodatak za NVDA #

* Autori: Hrvoje Katić, Abdel i NVDA suradnici
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA kompatibilnost: 2019.3 i nadalje

Ovaj dodatak omogućuje funkcionalnosti za napredni sat, postavljanje alarma
i kalendar za NVDA.

You can configure NvDA to announce time and date in formats other than what
Windows provides by default. Additionally, you can obtain the current day,
week number, as well as the remaining days before the end of the current
year, and you can also set automatic time announcement on specified
interval. There's also a stopwatch and Alarm timer features built-in to the
add-on that lets you time your tasks, such as copying files, installing
programs, or cooking meals.

Napomene:

* Ako se dodatak instalira kao nadogradnja, tijekom instalacije čarobnjak
  otkriva je li stara konfiguracija kompatibilna s novom i nudi mogućnost za
  njeno ispravljanja prije instalacije. To se jednostavno potvrđuje gumbom
  „U redu”.
* U sustavu Windows 10 i novijim, možeš koristiti aplikaciju Alarmi i sat za
  upravljanje štopericom i mjeračima vremena.

## Tipkovničke naredbe

* NVDA+F12: saznaj trenutačno vrijeme
* Pritisni NVDA+F12 dvaput brzo: saznaj trenutačni datum
* Pritisni NVDA+F12 triput brzo: izvještava o trenutačnom danu, broju
  tjedna, tekućoj godini i o danima koji su preostali do kraja godine
* NVDA+Shift+F12: uđi u sloj sata

## Nedodijeljene naredbe

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, open NVDA
menu, Preferences, then Input Gestures. Expand Clock category, then locate
unassigned commands from the list below and select "Add", then enter the
gesture you wish to use.

* Elapsed and remaining time before the next alarm. pressing this gesture
  twice quickly will cancel the next alarm.
* Zaustavi trenutačnu reprodukciju zvuka alarma.
* Prikaži dijaloški okvir zakazanih alarma.

## Višeslojne naredbe

Za korištenje višeslojnih naredbi, pritisni NVDA+šift+F12 i zatim jednu od
sljedećih tipki:

* S: Pokreće, resetira ili zaustavlja štopericu
* R: Resetira štopericu na nulu bez ponovnog pokretanja
* A: Izdaje proteklo vrijeme i preostalo vrijeme prije sljedećeg alarma
* T: Otvara dijalog za zakazivanje alarma.
* C: Otkaži sljedeći alarm
* Razmaknica: Izgovara trenutačno stanje štoperice ili odbrojavanja vremena
* p: Ako alarm traje predugo, može ga se zaustaviti
* H: Popis svih višeslojnih prečaca (Pomoć)

## Configuration and usage

To configure clock functionality, open NvDA menu, Preferences, then
Settings, and configure the following options from Clock panel:

* Time and date display format: use these combo boxes to configure how NVDA
  will announce time and date when you press NVDA+F12 once or twice quickly,
  respectively.
* Interval: choose the time announcement interval from this combo box (off,
  every 10 minutes, 15 minutes, 30 minutes, or every hour).
* Time announcement (enabled if interval is not off): choose between speech
  and sound, sound only, or speech only.
* Clock chime sound (enabled if interval is not off): select the clock chime
  sound.
* Quiet hours (enabled if interval is not off): select this checkbox to
  configure quiet hours range when automatic time announcement should not
  occur.
* Quiet hours time format (enabled if quiet hours is enabled): select how
  quiet hours options are presented (12-hour or 24-hour format).
* Quiet hours start and end times: select hour and minute range for quiet
  hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The
dialog contents include:

* Alarm duration in: select alarm/timer duration between hours, minutes, and
  seconds.
* Duration: enter alarm duration in the unit specified above.
* Alarm sound: select the alarm sound to be played.
* Gumbovi „Prekid” i „Pauza”: prekini ili pauziraj duge alarme.

Pritisni U redu i poruka će te obavijestiti o trenutačno odabranom trajanju
alarma.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
