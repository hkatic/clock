# Kello- ja kalenterilisäosa NVDA:lle #

* Tekijät: Hrvoje Katić, Abdel ja NVDA-yhteisön osallistujat
* NVDA-yhteensopivuus: 2019.3 ja uudemmat

Tämä lisäosa mahdollistaa kehittyneet kello-, hälytysaikastin- ja kalenteritoiminnot NVDA:ssa.

Voit määrittää NVDA:n ilmoittamaan ajan ja päivämäärän muodoissa, jotka poikkeavat Windowsin oletusmuodoista. Lisäksi voit saada nykyisen päivän, viikkonumeron sekä jäljellä olevat päivät kuluvan vuoden loppuun, ja voit myös asettaa automaattisen ajan ilmoituksen määritetyin aikavälein. Lisäosa sisältää myös sekuntikellon ja hälytysaikastimen, joiden avulla voit ajoittaa tehtäviäsi, kuten tiedostojen kopiointia, ohjelmien asennusta tai ruoanlaittoa.

## Huomautukset:

* jos asennat lisäosan päivityksenä, asennuksen aikana ohjattu toiminto havaitsee, onko vanha määritys yhteensopiva uuden kanssa ja tarjoaa sen korjaamista ennen asennusta, minkä jälkeen sinun tarvitsee vain vahvistaa OK-painike.
* Windows 10:ssä ja uudemmissa voit käyttää Herätykset ja kello -sovellusta sekuntikellon ja ajastimien hallintaan.

## Näppäinkomennot

* NVDA+F12: hae nykyinen aika
* NVDA+F12 painettuna kahdesti nopeasti: hae nykyinen päivämäärä
* NVDA+F12 painettuna kolme kertaa nopeasti: ilmoittaa nykyisen päivän, viikkonumeron, kuluvan vuoden sekä jäljellä olevat päivät vuoden loppuun
* NVDA+Shift+F12: siirry kellokerrokseen

## Määrittämättömät komennot

Seuraavia komentoja ei ole oletuksena määritetty; jos haluat määrittää ne, käytä Syöte-eleet-valintaikkunaa mukautettujen komentojen lisäämiseen. Avaa tätä varten NVDA-valikko, Asetukset ja sitten Syöte-eleet. Laajenna Kello-luokka, etsi alla olevat määrittämättömät komennot ja valitse "Lisää", sitten syötä haluamasi ele.

* Kulunut ja jäljellä oleva aika ennen seuraavaa hälytystä. tämän eleen nopea kaksoispainallus peruuttaa seuraavan hälytyksen.
* Pysäytä tällä hetkellä toistuva hälytysääni.
* Näytä hälytysaikataulun valintaikkuna.
* Näytä kerrostetut komennot (näppäimet NVDA+Shift+F12 jälkeen).

## Kerrostetut komennot

Käyttääksesi kerrostettuja komentoja paina NVDA+Shift+F12 ja sen jälkeen yhtä seuraavista näppäimistä:

* S: käynnistää, nollaa tai pysäyttää sekuntikellon
* R: nollaa sekuntikellon ilman uudelleenkäynnistystä
* A: ilmoittaa kuluneen ja jäljellä olevan ajan ennen seuraavaa hälytystä
* T: avaa hälytysaikataulun valintaikkunan
* C: peruuttaa seuraavan hälytyksen
* Väli: ilmoittaa nykyisen sekuntikellon tai ajastimen
* P: jos hälytys on liian pitkä, sen voi pysäyttää
* H: luettelee kaikki kerrostetut komennot (ohje)

## Määritys ja käyttö

Kellotoimintojen määrittämiseksi avaa NVDA-valikko, Asetukset ja sitten Asetukset, ja määritä seuraavat vaihtoehdot Kellopaneelista:

* Ajan ja päivämäärän näyttömuoto: käytä näitä yhdistelmäruutuja määrittääksesi, miten NVDA ilmoittaa ajan ja päivämäärän painettaessa NVDA+F12 kerran tai kahdesti nopeasti.
* Väli: valitse ajan ilmoitusväli tästä yhdistelmäruudusta (pois käytöstä, 10 minuutin välein, 15 minuutin välein, 30 minuutin välein tai joka tunti).
* Ajan ilmoitus (käytössä, jos väli ei ole pois käytöstä): valitse puheen ja äänen, vain äänen tai vain puheen välillä.
* Kellon äänimerkki (käytössä, jos väli ei ole pois käytöstä): valitse oletuskellon äänimerkki.
* Erilliset tunnin ja väliminuttien äänimerkit (käytössä, jos väli ei ole pois käytöstä, oletuksena pois käytöstä): ota käyttöön tämä valintaruutu muokataksesi väliminuttien ääniä erikseen tunnin äänimerkistä.
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
