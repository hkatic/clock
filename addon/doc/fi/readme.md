# Kello ja kalenteri #

* Tekijät: Hrvoje Katić, Abdel sekä muut NVDA-projektiin osallistujat;
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat

Tämä lisäosa lisää NVDA:han edistyneen kellon, ajastimen sekä kalenterin.

Voit määrittää NVDA:n ilmoittamaan kellonajan ja päivämäärän muissa kuin
Windowsin oletusarvoisesti tarjoamissa muodoissa. Lisäksi voit saada
selville nykyisen päivän, viikon numeron sekä kuluvan vuoden jäljellä olevat
päivät, ja voit myös ottaa käyttöön tietyin väliajoin tapahtuvan
automaattisen kellonajan ilmoittamisen. Lisäosaan on sisäänrakennettu myös
sekuntikello ja ajastin, jonka avulla voit mitata tehtäviesi, kuten
tiedostojen kopioinnin, ohjelmien asentamisen tai aterioiden valmistuksen,
keston.

Huomautuksia

* Mikäli asennat lisäosan päivityksenä, ohjattu asennustoiminto tunnistaa,
  ovatko vanhat asetuksesi yhteensopivia uuden lisäosaversion kanssa ja
  ehdottaa tarvittaessa niiden korjaamista ennen asennusta, minkä voit
  hyväksyä painamalla OK-painiketta.
* Windows 10:ssä ja uudemmissa voit käyttää sekuntikelloa ja ajastinta
  Hälytykset ja kello -sovelluksella.

## Näppäinkomennot

* NVDA+F12: Puhu nykyinen kellonaika
* NVDA+F12 kahdesti painettuna: Puhu nykyinen päivämäärä
* NVDA+F12 kolmesti painettuna: Ilmoittaa nykyisen päivän, viikon numeron,
  kuluvan vuoden sekä sen jäljellä olevat päivät
* NVDA+Vaihto+F12: ota käyttöön kellon komentokerros

## Määrittämättömät komennot

Seuraavia komentoja ei ole oletusarvoisesti määritetty. Mikäli haluat
määrittää ne, käytä Syötekomennot-valintaikkunaa haluamiesi komentojen
lisäämiseen. Tämä tehdään avaamalla NVDA-valikko ja valitsemalla sitten
Asetukset-alivalikosta Syötekomennot. Laajenna Kello-kategoria, etsi
määrittämättömät komennot alla olevasta luettelosta, valitse "Lisää" ja
paina sitten syötekomentoa, jota haluat käyttää.

* Kulunut ja jäljellä oleva aika ennen seuraavaa hälytystä. Tämän
  syötekomennon kahdesti painaminen peruuttaa seuraavan hälytyksen.
* Pysäytä tällä hetkellä soiva hälytysääni.
* Näytä hälytysten ajastusvalintaikkuna.

## Komentokerroksen komennot

Käytä komentokerroskomentoja painamalla NVDA+Vaihto+F12 ja sitten jotakin
seuraavista näppäimistä:

* S: Käynnistää, nollaa tai pysäyttää sekuntikellon
* R: Nollaa sekuntikellon uudelleenkäynnistämättä sitä
* A: Puhuu kuluneen ja jäljellä olevan ajan ennen seuraavaa hälytystä
* T: Avaa hälytysten ajastusvalintaikkunan
* C: Peruuta seuraava hälytys
* Välilyönti: Puhuu nykyisen sekuntikellon tai ajastimen
* P: Lopettaa hälytyksen, mikäli se kestää liian kauan
* H: Luetteloi kaikki komentokerroksen komennot

## Määrittäminen ja käyttö

Määritä kello siirtymällä NVDA-valikkoon, avaamalla Asetukset-alivalikko,
valitsemalla Asetukset ja määrittämällä seuraavat asetukset
Kello-paneelista:

* Kellonajan ja päivämäärän näyttömuoto: Määritä näistä yhdistelmäruuduista,
  miten NVDA puhuu kellonajan ja päivämäärän painaessasi kerran tai kahdesti
  NVDA+F12.
* Aikaväli: Valitse tästä yhdistelmäruudusta kellonajan ilmoittamisen
  aikaväli (pois käytöstä, 10 minuutin välein, 15 minuutin välein, 30
  minuutin välein tai tunnin välein).
* Kellonajan ilmoittaminen (käytössä, mikäli aikaväliksi ei ole määritetty
  "pois käytöstä"): Valitse vaihtoehtojen puhe ja ääni, vain ääni tai vain
  puhe väliltä.
* Kellon ääni (käytössä, mikäli aikaväliksi ei ole määritetty "pois
  käytöstä"): Valitse kellon ääni.
* Hiljaiset tunnit (käytössä, mikäli aikaväliksi ei ole määritetty "pois
  käytöstä"): Valitse tämä valintaruutu määrittääksesi hiljaiset tunnit,
  joiden aikana automaattinen kellonajan puhuminen ei ole käytössä.
* Hiljaisten tuntien ajan muoto (käytössä, mikäli hiljaiset tunnit ovat
  käytössä): Valitse, miten hiljaisten tuntien vaihtoehdot näytetään (12
  tunnin tai 24 tunnin muoto).
* Hiljaisten tuntien alkamis- ja päättymisajat: Valitse tunnit- ja
  minuutit-yhdistelmäruuduista hiljaisten tuntien alkamis- ja päättymisaika.

Ajasta hälytyksiä menemällä NVDA-valikkoon, Avaamalla Työkalut-alivalikon ja
valitsemalla sitten Ajasta hälytyksiä. Valintaikkunassa ovat käytettävissä
seuraavat vaihtoehdot:

* Hälytyksen keston yksikkö: Valitse hälytyksen/ajastimen kesto tuntien,
  minuuttien ja sekuntien väliltä.
* Kesto: Anna hälytyksen kesto yllä mainitussa yksikössä.
* Hälytysääni: Valitse soitettava hälytysääni.
* Lopeta- ja pysäytä-painikkeet: Lopeta tai pysäytä pitkän hälytysäänen
  soittaminen.

Paina OK, jonka jälkeen näytetään nykyisen hälytyksen keston kertova
ilmoitus.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
