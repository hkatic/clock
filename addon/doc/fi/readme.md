# Kello ja kalenteri

- Tekijät: Hrvoje Katić, Abdel sekä muut NVDA-yhteisön jäsenet
- Lataa [vakaa versio][1]
- Yhteensopivuus: NVDA 2019.3 ja uudemmat
- NVDA compatibility: 2019.3 and later

Tämä lisäosa lisää NVDA:han edistyneen kellon, ajastimen sekä kalenterin.

You can configure NVDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

Huomautuksia

- Mikäli asennat lisäosan päivityksenä, ohjattu asennustoiminto tunnistaa,
  ovatko vanhat asetuksesi yhteensopivia uuden lisäosaversion kanssa ja
  ehdottaa tarvittaessa niiden korjaamista ennen asennusta, minkä voit
  hyväksyä painamalla OK-painiketta.
- Windows 10:ssä ja uudemmissa voit käyttää sekuntikelloa ja ajastinta
  Hälytykset ja kello -sovelluksella.

## Näppäinkomennot

- NVDA+F12: Puhu nykyinen kellonaika
- NVDA+F12 kahdesti painettuna: Puhu nykyinen päivämäärä
- NVDA+F12 kolmesti painettuna: Ilmoittaa nykyisen päivän, viikon numeron,
  kuluvan vuoden sekä sen jäljellä olevat päivät
- NVDA+Vaihto+F12: ota käyttöön kellon komentokerros

## Määrittämättömät komennot

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.

- Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
- Pysäytä tällä hetkellä soiva hälytysääni.
- Näytä hälytysten ajastusvalintaikkuna.
- Show layered commands (keys to be pressed after NVDA+Shift+F12).

## Komentokerroksen komennot

Käytä komentokerroskomentoja painamalla NVDA+Vaihto+F12 ja sitten jotakin
seuraavista näppäimistä:

- S: Käynnistää, nollaa tai pysäyttää sekuntikellon
- R: Nollaa sekuntikellon uudelleenkäynnistämättä sitä
- A: Puhuu kuluneen ja jäljellä olevan ajan ennen seuraavaa hälytystä
- T: Avaa hälytysten ajoitusvalintaikkunan
- C: Peruuta seuraava hälytys
- Välilyönti: Puhuu nykyisen sekuntikellon tai ajastimen
- P: Lopettaa hälytyksen, mikäli se kestää liian kauan
- H: Luetteloi kaikki komentokerroksen komennot

## Määrittäminen ja käyttö

Määritä kello siirtymällä NVDA-valikkoon, avaamalla Asetukset-alivalikko,
valitsemalla Asetukset ja määrittämällä seuraavat asetukset
Kello-paneelista:

- Kellonajan ja päivämäärän näyttömuoto: Määritä näistä yhdistelmäruuduista,
  miten NVDA puhuu kellonajan ja päivämäärän painaessasi kerran tai kahdesti
  NVDA+F12.
- Kellonajan ilmoitus: Valitse tästä yhdistelmäruudusta kellonajan
  ilmoittamisen aikaväli (pois käytöstä, 10 minuutin välein, 15 minuutin
  välein, 30 minuutin välein tai tunnin välein).
- Kellonajan ilmoittaminen (käytössä, mikäli kellonajan ilmoituksen
  aikaväliksi ei ole määritetty "pois käytöstä"): Valitse vaihtoehtojen
  "puheella ja äänellä", "vain äänellä" tai "vain puheella" väliltä.
- Kellon ääni (käytössä, mikäli kellonajan ilmoituksen aikaväliksi ei ole
  määritetty "pois käytöstä"): Valitse kellon ääni.
- Hiljaiset tunnit (käytössä, mikäli kellonajan ilmoituksen aikaväliksi ei
  ole määritetty "pois käytöstä"): Valitse tämä valintaruutu määrittääksesi
  hiljaiset tunnit, joiden aikana automaattinen kellonajan puhuminen ei ole
  käytössä.
  - Intermediate minutes chime sound (enabled if "Separate hour and intermediate minute chimes" is checked): Select the clock chime sound specifically for intermediate minutes.
- Hiljaisten tuntien ajan muoto (käytössä, mikäli hiljaiset tunnit ovat
  käytössä): Valitse, miten hiljaisten tuntien vaihtoehdot näytetään (12
  tunnin tai 24 tunnin muoto).
- Hiljaisten tuntien alkamis- ja päättymisajat: Valitse tunnit- ja
  minuutit-yhdistelmäruuduista hiljaisten tuntien alkamis- ja päättymisaika.
- Quiet hours start and end times: select hour and minute range for quiet hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The dialog contents include:

- Hälytyksen keston yksikkö: Valitse hälytyksen/ajastimen kesto tuntien,
  minuuttien ja sekuntien väliltä.
- Kesto: Anna hälytyksen kesto yllä mainitussa yksikössä.
- Hälytysääni: Valitse soitettava hälytysääni.
- Lopeta- ja pysäytä-painikkeet: Lopeta tai pysäytä pitkän hälytysäänen
  soittaminen.

Paina OK, jonka jälkeen näytetään nykyisen hälytyksen keston kertova
ilmoitus.

[1]: https://addons.nvda-project.org/files/get.php?file=cac
[2]: https://www.nvaccess.org/addonStore/legacy?file=clock
