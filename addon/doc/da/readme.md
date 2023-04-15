# Ur og kalender for NVDA #

* Forfattere: Hrvoje Katić, Abdel og NVDA-bidragydere
* Download [stabil version][1]

* NVDA-kompatibilitet: 2019.3 og nyere

Denne tilføjelse tilføjer avancerede ur, alarm, tidtagning  og
kalenderfunktionalitet til NVDA.

Du kan konfigurere NvDA til at annoncere klokkeslæt og dato i andre
formater, end hvad Windows leverer som standard. Derudover kan du få den
aktuelle dag, ugenummer samt de resterende dage inden udgangen af det
aktuelle år, og du kan også indstille automatiske tidsannoncering for et
angivet interval. Der er også et stopur og tidtagningsfunktioner indbygget i
tilføjelsen, der lader dig time dine opgaver, såsom kopiering af filer,
installation af programmer eller tilberedning af måltider.

Bemærkninger:

* Hvis du installerer tilføjelsen som en opdatering, opdager guiden under
  installationsprocessen, om den gamle konfiguration er kompatibel med den
  nye, og tilbyder at rette den før installation. Tryk på "ok" for at
  bekræfte.
* I Windows 10 og nyere kan du bruge appen Alarmer og ur til at administrere
  stopur og timere.

## Tastaturkommandoer

* NVDA+F12: Få den aktuelle tid oplyst.
* NVDA+F12 trykket hurtigt to gange: få aktuel dato
* NVDA+F12 trykket tre gange hurtigt: Oplyser den aktuelle dag, ugenummeret,
  det aktuelle år og de resterende dage før årets udgang.
* NVDA+Shift+F12: indtast urlag

## Ikke-tildelte kommandoer

Følgende kommandoer er ikke tildelt som standard. Hvis du ønsker at
tilknytte dem, skal du bruge dialogboksen "Håndter kommandoer" til at
tilføje brugerdefinerede kommandoer. For at gøre det skal du åbne
NVDA-menuen, Opsætning og derefter Håndter kommandoer. Udvid kategorien Ur,
find derefter ikke-tildelte kommandoer fra listen nedenfor, og vælg
"Tilføj", og indtast derefter den kommando, du ønsker at bruge.

* Forløbet og resterende tid før næste alarm. Hvis du trykker denne kommando
  to gange hurtigt, annulleres den næste alarm.
* Stop afspilning af den aktuelle alarmlyd
* Vis dialog til indstilling af alarmer

## Lagrede kommandoer

For at bruge lagrede kommandoer skal du trykke på NVDA+Skift+F12 efterfulgt
af en af følgende taster:

* S: Starter, nulstiller eller stopper stopuret
* R: Nulstiller stopuret til 0 uden at genstarte det
* A: Giver den resterende og forløbet tid før den næste alarm
* T: Åbner dialogen til indstilling af alarmer.
* C: Annuller den næste alarm
* Mellemrum: Udtaler nuværende stopur eller nedtælling
* P: Hvis en alarm er for lang, kan du stoppe den via dette tastetryk.
* H: Liste over alle lagdelte kommandoer (Hjælp)

## Konfiguration og brug

For at konfigurere urfunktionaliteten skal du åbne NvDA-menuen, Opsætning og
derefter Indstillinger og konfigurere følgende muligheder fra
indstillingskategorien Ur:

* Visningsformat for klokkeslæt og dato: Brug disse kombinationsbokse til at
  konfigurere, hvordan NVDA vil annoncere klokkeslæt og dato, når du trykker
  på NVDA+F12 en eller to gange hurtigt.
* Interval: Vælg tidsmeddelelsesintervallet fra denne combo box( fra, hvert
  10. minut, 15. minut, 30. minut eller hver time).
* Tidsannoncering (aktiveret, hvis interval ikke er slået fra): vælg mellem
  tale og lyd, kun lyd eller kun tale.
* Urets ringelyd  (aktiveret, hvis interval ikke er slået fra): vælg lyden
  for uret.
* Checkboxe "Stilletimer" (kun synlig, hvis muligheden "Fra" ikke er valgt i
  boksen) giver dig mulighed for at konfigurere tidsintervallet, hvor den
  automatiske tidsannoncering ikke skal forekomme.
* Tidsformat for stilletimer (aktiveret, hvis stilletimer er aktiveret):
  vælg, hvordan indstillingerne for stilletimer præsenteres (12-timers eller
  24-timers format).
* Stilletimers start- og sluttidspunkter: Vælg time- og minutinterval for
  stilletimer fra combo boxe for timer og minutter.

For at planlægge alarmer skal du åbne NVDA-menuen, Værktøjer, og derefter
vælge Indstil alarmer. Dialogen indeholder følgende indstillinger:

* Alarmens varighed i: Vælg alarm/timer-varighed mellem timer, minutter og
  sekunder.
* Varighed: Indtast alarmvarigheden som anvist ovenfor.
* Alarmlyd: Vælg den alarmlyd, der skal afspilles.
* Knapper til pause og stop giver dig mulighed for at sætte alarmen på pause
  og genoptage lange alarmer.

Klik på OK, og en meddelelse vil informere dig om den aktuelt valgte
alarmvarighed.

[[!tag stable]]

[1]:
https://github.com/hkatic/clock/releases/download/24.04.0/clock-24.04.0.nvda-addon
