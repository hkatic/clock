# Kello- ja kalenterilisäosa NVDA:lle #

* Tekijät: Hrvoje Katić, Abdel ja NVDA-yhteisön osallistujat
* Yhteensopivuus: NVDA 2019.3 ja uudemmat

Tämä lisäosa mahdollistaa NVDA:ssa kehittyneet kello-, ajastin- ja kalenteritoiminnot.

NVDA voidaan määrittää ilmoittamaan aika ja päivämäärä muodoissa, jotka poikkeavat Windowsin oletusmuodoista. Lisäksi on mahdollista ilmoittaa päivä, viikon numero sekä kuluvan vuoden jäljellä olevat päivät ja ottaa käyttöön automaattinen ajan ilmoitus määritetyin aikavälein. Lisäosassa on myös sekuntikello ja ajastin, joita on mahdollista käyttää esim. tiedostojen kopioinnin ja ohjelmien asennuksen keston mittaamiseen tai ruoanlaiton apuna.

Huomautukset:

* jos lisäosa asennetaan päivityksenä, ohjattu toiminto havaitsee, ovatko aiemmat asetukset yhteensopivia uuden lisäosaversion kanssa ja tarjoaa ennen asennuksen suorittamista tarvittaessa asetusten korjausmahdollisuutta, joka voidaan vahvistaa OK-painikkeella.
* Windows 10:ssä ja uudemmissa sekuntikellon ja ajastimien hallintaan voidaan käyttää Kello-sovellusta.

## Näppäinkomennot

* NVDA+F12: puhu kellonaika
* NVDA+F12 kahdesti painettuna: puhu päivämäärä
* NVDA+F12 kolmesti painettuna: ilmoittaa päivän, viikon numeron, kuluvan vuoden sekä sen jäljellä olevat päivät
* NVDA+Vaihto+F12: siirry Kellon komentokerrokseen

## Määrittämättömät komennot

Seuraavia komentoja ei ole oletusarvoisesti määritetty. Ne on mahdollista määrittää Näppäinkomennot-valintaikkunassa, joka voidaan avata menemällä NVDA-valikkoon, avaamalla Mukautukset-alivalikko ja valitsemalla Näppäinkomennot-vaihtoehto. Seuraavaksi laajennetaan Kello-kategoria, etsitään alla olevat määrittämättömät komennot, valitaan Lisää ja painetaan sen jälkeen haluttua näppäinkomentoa.

* Kulunut ja jäljellä oleva aika ennen seuraavaa hälytystä. tämän näppäinkomennon kaksoispainallus peruuttaa seuraavan hälytyksen.
* Pysäytä toistettava hälytysääni.
* Näytä Hälytysten ajastus -valintaikkuna.
* Näytä komentokerroksen komennot NVDA+Vaihto+F12-painalluksen jälkeen.

## Komentokerroksen komennot

Komentokerroksen komentoja käytetään painamalla NVDA+Vaihto+F12 ja sen jälkeen jotain seuraavista näppäimistä:

* S: käynnistää, nollaa tai pysäyttää sekuntikellon
* R: nollaa sekuntikellon käynnistämättä sitä uudelleen
* A: ilmoittaa kuluneen ja jäljellä olevan ajan ennen seuraavaa hälytystä
* T: avaa hälytysten ajastusvalintaikkunan
* C: peruuttaa seuraavan hälytyksen
* Väli: ilmoittaa nykyisen sekuntikellon tai ajastimen
* P: pysäyttää liian kauan kestävän hälytyksen
* H: luettelee kaikki komentokerroksen komennot

## Asetukset ja käyttö

Lisäosan asetuksia muutetaan avaamalla NVDA-valikko, valitsemalla Mukautukset, sen jälkeen Asetukset, ja lopuksi Kello-kategoria:

* Kellonajan ja päivämäärän näyttömuoto: Näistä yhdistelmäruuduista määritetään, miten NVDA puhuu kellonajan ja päivämäärän painettaessa kerran tai kahdesti NVDA+F12.
* Ilmoitusväli: tästä yhdistelmäruudusta valitaan kellonajan ilmoitusväli, jonka vaihtoehtoja ovat pois käytöstä, 10 minuutin välein, 15 minuutin välein, 30 minuutin välein tai tunnin välein.
* Ajan ilmoitus (käytössä, jos ilmoitusväliä ei ole poistettu käytöstä): vaihtoehtoja ovat puhe ja ääni, vain ääni tai vain puhe.
  * Puheella ja merkkiäänellä: merkkiääni toistetaan tarkasti ajoitettuna siten, että se päättyy täsmälleen minuutin vaihtuessa, ja kellonaika puhutaan heti sen jälkeen. Merkkiäänen kuullaan siis laskevan aikaa tiettyyn hetkeen, jota seuraa puhuttu kellonaika radion aikamerkin tavoin.
  * BBC:n aikamerkkiäänet: kun tämä on valittuna merkkiääneksi, viisi lyhyttä piippausta johtavat kuudenteen pitkään piippaukseen, joka osuu täsmälleen minuutin vaihtumisen kohdalle jäljitellen tarkasti radion aikamerkkiä. Kellonaika puhutaan kuudennen piippauksen yhteydessä.
  * Vain äänellä: toistaa merkkiäänen minuutin vaihtuessa. BBC:n aikamerkkiäänet säilyttävät tarkan ajoituksensa, joten kuudes piippaus kuuluu täsmälleen minuutin vaihtumisen hetkellä.
  * Vain puheella: puhuu nykyisen kellonajan minuutin vaihtuessa ilman merkkiääntä.
* Kellon merkkiääni (käytössä, jos ilmoituksen aikaväliä ei ole poistettu käytöstä): valitse oletusmerkkiääni väliminuuteille ja tasatunneille.
* Erilliset tasatuntien ja väliminuuttien merkkiäänet (käytössä, jos ilmoituksen aikaväliä ei ole poistettu käytöstä, oletuksena poissa käytöstä): ota käyttöön tämä valintaruutu muokataksesi väliminuuttien ääniä erillään tasatunnin merkkiäänestä.
  * Väliminuttien äänimerkki (käytössä, jos "erilliset tunnin ja väliminuttien äänimerkit" on valittu): valitse väliminuttien ääni.
* Hiljaiset tunnit (käytössä, jos väli ei ole pois käytöstä): valitse tämä valintaruutu hiljaisten tuntien alueen määrittämiseksi.
* Hiljaisten tuntien aikamuoto (käytössä, jos hiljaiset tunnit ovat käytössä): valitse esitysmuoto (12 tai 24 tunnin muoto).
* Hiljaisten tuntien aloitus- ja lopetusaika: valitse tunti- ja minuuttialue hiljaisille tunneille yhdistelmäruuduista.

Hälytysten aikatauluttamiseksi avaa NVDA-valikko, Työkalut ja valitse Aikatauluta hälytykset. Valintaikkuna sisältää:

* Hälytyksen kesto: valitse hälytyksen/ajastimen kesto tunneissa, minuuteissa ja sekunneissa.
* Kesto: syötä hälytyksen kesto yllä määritellyssä yksikössä.
* Hälytysääni: valitse toistettava hälytysääni.
* Pysäytys- ja taukopainikkeet: pysäytä tai keskeytä pitkä hälytysääni.

Napsauta OK, ja viesti ilmoittaa valitun hälytyksen keston.
