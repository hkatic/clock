# Suplimentul Ceas și calendar pentru NVDA #

* Autori: Hrvoje Katić, Abdel și colaboratori NVDA
* Compatibilitate NVDA: 2019.3 și versiuni ulterioare

Acest supliment activează funcționalitățile avansate de ceas, cronometru de alarmă și calendar pentru NVDA.

Puteți configura NVDA să anunțe ora și data în formate diferite de cele furnizate implicit de Windows. În plus, puteți obține ziua curentă, numărul săptămânii, precum și numărul de zile rămase până la sfârșitul anului curent, și puteți seta anunțarea automată a orei la intervale specificate. Suplimentul include și funcții de cronometru și alarmă care vă permit să cronometrați sarcinile dvs., cum ar fi copierea fișierelor, instalarea programelor sau gătitul.

## Note:

* dacă instalați suplimentul ca actualizare, în timpul procesului de instalare, asistentul detectează dacă configurația veche este compatibilă cu cea nouă și oferă corectarea acesteia înainte de instalare, apoi trebuie doar să confirmați butonul OK.
* În Windows 10 și versiunile ulterioare, puteți utiliza aplicația Alarme și Ceas pentru a gestiona cronometrele și alarmele.

## Comenzi rapide

* NVDA+F12: obține ora curentă
* NVDA+F12 apăsat de două ori rapid: obține data curentă
* NVDA+F12 apăsat de trei ori rapid: raportează ziua curentă, numărul săptămânii, anul curent și zilele rămase până la sfârșitul anului
* NVDA+Shift+F12: intrare în stratul ceasului

## Comenzi neatribuite

Următoarele comenzi nu sunt atribuite implicit; dacă doriți să le atribuiți, utilizați dialogul Gesturi de intrare pentru a adăuga comenzi personalizate. Pentru aceasta, deschideți meniul NVDA, Preferințe, apoi Gesturi de intrare. Extindeți categoria Ceas, apoi găsiți comenzile neatribuite din listă și selectați „Adăugare”, apoi introduceți gestul dorit.

* Timpul scurs și rămas până la următoarea alarmă. apăsarea de două ori rapid a acestui gest va anula următoarea alarmă.
* Oprește sunetul alarmei aflate în redare.
* Afișează dialogul pentru programarea alarmelor.
* Afișează comenzile stratificate (tastele după NVDA+Shift+F12).

## Comenzi stratificate

Pentru a utiliza comenzile stratificate, apăsați NVDA+Shift+F12 urmat de una dintre tastele:

* S: pornește, resetează sau oprește cronometrul
* R: resetează cronometrul la 0 fără repornire
* A: afișează timpul scurs și timpul rămas până la următoarea alarmă
* T: deschide dialogul de programare a alarmelor
* C: anulează următoarea alarmă
* Spațiu: anunță cronometrul curent sau numărătoarea inversă
* P: oprește o alarmă prea lungă
* H: listează toate comenzile stratificate (Ajutor)

## Configurare și utilizare

Pentru a configura funcționalitatea ceasului, deschideți meniul NVDA, Preferințe, apoi Setări și configurați următoarele opțiuni din panoul Ceas:

* Format de afișare a orei și datei: utilizați aceste casete combinate pentru a configura modul în care NVDA va anunța ora și data la apăsarea NVDA+F12 o dată sau de două ori rapid.
* Interval: alegeți intervalul de anunțare a orei (dezactivat, la fiecare 10 minute, 15 minute, 30 minute sau la fiecare oră).
* Anunțarea orei (activat dacă intervalul nu este dezactivat): alegeți între vorbire și sunet, doar sunet sau doar vorbire.
* Sunetul clopoțelului ceasului (activat dacă intervalul nu este dezactivat): selectați sunetul implicit al ceasului.
* Clopote separate pentru ore și minute intermediare (activat dacă intervalul nu este dezactivat, implicit dezactivat): activați această casetă pentru a personaliza sunetele pentru minutele intermediare separat de sunetul orei.
  * Sunet pentru minute intermediare (activat dacă „clopote separate pentru ore și minute intermediare” este bifat): selectați sunetul pentru minutele intermediare.
* Ore liniștite (activat dacă intervalul nu este dezactivat): bifați această casetă pentru a configura intervalul de ore liniștite.
* Formatul orelor liniștite (activat dacă orele liniștite sunt activate): selectați modul de afișare (format 12 ore sau 24 ore).
* Ora de început și sfârșit a orelor liniștite: selectați intervalul de ore și minute pentru orele liniștite din casetele combinate.

Pentru a programa alarme, deschideți meniul NVDA, Instrumente, apoi selectați „Programare alarme”. Conținutul dialogului include:

* Durata alarmei: selectați durata alarmei/cronometru în ore, minute și secunde.
* Durată: introduceți durata alarmei în unitatea specificată mai sus.
* Sunet alarmă: selectați sunetul alarmei.
* Butoane oprire și pauză: opriți sau întrerupeți o alarmă lungă.

Apăsați OK, iar un mesaj va informa despre durata alarmei selectate.
