# Kello ja kalenteri #

* Authors: Hrvoje Katić, Abdel and NVDA contributors
* Download [stable version][1]
* Download [development version][2]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat

Tämä lisäosa lisää NVDA:han edistyneen kellon, ajastimen sekä kalenterin.

You can configure NvDA to announce time and date in formats other than what
Windows provides by default. Additionally, you can obtain the current day,
week number, as well as the remaining days before the end of the current
year, and you can also set automatic time announcement on specified
interval. There's also a stopwatch and Alarm timer features built-in to the
add-on that lets you time your tasks, such as copying files, installing
programs, or cooking meals.

Huomautuksia

* Mikäli asennat lisäosan päivityksenä, ohjattu asennustoiminto tunnistaa,
  ovatko vanhat asetuksesi yhteensopivia uuden lisäosaversion kanssa ja
  ehdottaa tarvittaessa niiden korjaamista ennen asennusta, minkä voit
  hyväksyä painamalla OK-painiketta.
* Windows 10:ssä ja uudemmissa voit käyttää sekuntikelloa ja ajastinta
  Hälytykset ja kello -sovelluksella.

## Näppäinkomennot

* NVDA+F12: puhu nykyinen kellonaika
* NVDA+F12 kahdesti painettuna: puhu nykyinen päivämäärä
* NVDA+F12 pressed three times quickly: reports the current day, the week
  number, the current year and the remaining days before the end of the year
* NVDA+Vaihto+F12: ota käyttöön kellon komentokerros

## Unassigned commands

Seuraavia komentoja ei ole oletusarvoisesti määritetty. Mikäli haluat
määrittää ne, käytä Syötekomennot-valintaikkunaa haluamiesi komentojen
lisäämiseen. Tämä tehdään avaamalla NVDA-valikko ja valitsemalla sitten
Asetukset-alivalikosta Syötekomennot. Laajenna Kello-kategoria, etsi
määrittämättömät komennot alla olevasta luettelosta, valitse "Lisää" ja
paina sitten syötekomentoa, jota haluat käyttää.

* Kulunut ja jäljellä oleva aika ennen seuraavaa hälytystä. Tämän
  syötekomennon kahdesti painaminen peruuttaa seuraavan hälytyksen.
* Keskeytä tällä hetkellä soiva hälytysääni.
* Näytä hälytysten ajastusvalintaikkuna.

## Layered commands

Käytä komentokerroskomentoja painamalla NVDA+Vaihto+F12 ja sitten jotakin
seuraavista näppäimistä:

* S: Käynnistää, nollaa tai pysäyttää sekuntikellon
* R: Nollaa sekuntikellon uudelleenkäynnistämättä sitä
* A: Puhuu kuluneen ja jäljellä olevan ajan ennen seuraavaa hälytystä
* T: Avaa hälytysten ajastusvalintaikkunan
* C: Peruuta seuraava hälytys
* Space: Speaks current stopwatch or count-down timer
* p: If an alarm is too long, allows to stop it
* H: List all layered commands (Help)

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
* Stop and pause buttons: stop or pause a long alarm sound.

Click OK, and a message will inform you the curretnly selected alarm
duration.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
