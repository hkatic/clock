# Ur og kalender for NVDA #

* Forfattere: Hrvoje Katić, Abdel og NVDA bidragsydere;
* Download [stabil version][1];
* Download [udviklingsversion][2].Download [udviklingsversion][2]


Denne tilføjelse tilføjer avancerede ur, alarm, tidtagning  og
kalenderfunktionalitet til NVDA.

I stedet for altid at få tid og dato fra Windows, kan du tilpasse, hvordan
tider og datoer skal tales og gengives på punkt af NVDA.

Derudover kan du få den aktuelle dag, ugenummer samt de resterende dage
inden udgangen af indeværende år, og du kan også indstille automatisk
tidsmeddelelse ved et angivet interval.

Der er også et stopur og tidtagningsfunktionalitet indbygget i
tilføjelsesprogrammet, der lader dig tage tid på dine opgaver, såsom
kopiering af filer, installation af programmer eller madlavning.

## Bemærk:

Hvis du installere tilføjelsen som en opdatering, vil programmet bekræfte om
din gamle installation er kompatibel med den nye, hvorefter dette vil ettes
hvis dette ikke er tilfældet. Du skal blot trykke på "ok" for at bekræfte.

## Brug

* Åbn konfigurationsdialogen for denne tilføjelse fra menuen værktøjer fra
  NVDA-menuen eller indstillingspanelet, afhængigt af din version af NVDA;

    * I dialogboksen Uropsætning giver de første to combo boxe dig mulighed
      for at vælge dine foretrukne tids- og datoformater.
    * Combo Box-kontrollen "Interval" giver dig mulighed for at indstille
      interval for automatisk tidsannoncering (hvert 10. minut, hvert
      15. minut, hvert 30. minut, hver time eller fra);
    * Combo Boxen "Tidsannoncering" (kun synlig, hvis muligheden "Fra" ikke
      er valgt i boksen) giver dig mulighed for at konfigurere, hvordan den
      automatiske tidsmeddelelse skal rapporteres (tale og lyd, kun tale
      eller lyd alene) når automatisk tidsannoncering er slået til;
    * Boksen "Urets lyd" (kun synlig, hvis muligheden "Fra" ikke er valgt i
      Combo Boxen) giver dig mulighed for at vælge mellem forskellige
      urlyde, der vil blive afspillet, når automatisk tidsannoncering er
      slået til og rapporteres med lyd;
    * Checkboxe "Stilletimer" (kun synlig, hvis muligheden "Fra" ikke er
      valgt i boksen) giver dig mulighed for at konfigurere tidsintervallet,
      hvor den automatiske tidsannoncering ikke skal forekomme;
    * Check boxen "Indtast med 24-timers-format" (kun synlig hvis stille
      timer er aktiveret) giver dig mulighed for at konfigurere, hvorvidt du
      vil indtaste tid til stilletimer i 12 timers-format (AM eller PM)
      eller europæisk 24-timers format ;
    * Rederingsboksen bestemmer start- og sluttidspunkt. Denne mulighed er
      kun tilgængleig, hvis stilletimer er slået til. Denne lader dig
      konfigurere tidspunktet, hvor stilletimer skal være aktiv. Tiden skal
      indtastes i formatet hh:mm hvis boksen "Indtast med 24-timers-format"
      er valgt. Hvis ikke, skal du bruge 24-timers format som beskrevet
      nedenunder;
    * Når du er færdig, skal du trykke tab til du lander på knappen OK og
      aktivere den ved at trykke på Enter for at gemme dine indstillinger;
    * I dialogen med uropsætning lader den første boks dig vælge din
      foretrukne nedtælling;
    * Redigeringsboksen giver dig mulighed for at indtaste den tid der skal
      gå, før alarmen ringer. Denne varighed skal angives i 1 eller flere
      cifre, ikke et decimaltal;
    * Boksen "Alarmens lyd" giver dig mulighed for at vælge mellem
      forskellige alarmlyde, der vil blive afspillet, når alarmen ringer;
    * Pauseknappen giver dig mulighed for at sætte alarmen på pause og
      genoptage lange alarmer;
    * Stopknappen giver dig mulighed for at stoppe for lange alarmer;
    * Når du er færdig, skal du trykke tab indtil du lander på OK-knappen og
      aktivere den ved at trykke på Enter. En besked vises for at minde om
      ventetiden før alarmen;

* Tryk NVDA + F12 for at få den aktuelle tid oplys, to gange hurtigt for at
  få den aktuelle dato, og tre gange hurtigt for at rapporterer den aktuelle
  dag, ugenummeret, det aktuelle år og de resterende dage før årets udgang.

## Tastaturkommandoer

* NVDA+F12, få den aktuelle tid;
* NVDA+F12 trykket to gange hurtigt, få den aktuelle dato;
* NVDA+F12 trykket tre gange hurtigt, rapporterer den aktuelle dag,
  ugenummeret, det aktuelle år og de resterende dage før årets udgang.
* Der er et script, der giver den resterende og forløbet tid før den næste
  alarm;
* Der er ingen tastaturbevægelse tildelt dette script, du skal selv gøre det
  i dialogboksen "Inputbevægelser" i kategorien "Ur".
* Denne bevægelse trykket to gange hurtigt vil annullere den næste alarm;
* Der er et andet script til at stoppe den lyd, der afspilles, men dette
  script har ingen tildelt kommando;
* Dette script kan også benyttes ved brug af de lagdelte kommandoer til
  tilføjelsen som beskrevet nedenunder.

## Lagrede kommandoer

For at bruge lagrede kommandoer skal du trykke på NVDA+Skift+F12 efterfulgt
af en af følgende taster:

* S: Starter, nulstiller eller stopper stopuret;
* R: Nulstiller stopuret til 0 uden at genstarte det;
* A: Giver den resterende og forløbet tid før den næste alarm;
* C: Annuller den næste alarm;
* Mellemrum: Udtaler nuværende stopur eller nedtælling;
* P: Hvis en alarm er for lang, kan du stoppe den via dette tastetryk;
* H: Oplyser alle lagdelte kommandoer (hjælp).

## Syntaks til brug for stille timer

* For at undgå fejl skal stilletimer følge en stringent og præcis syntaks;
* Hvis du markerer afkrydsningsfeltet Indtast i 24-timers format, skal
  formatet være "HH: MM", altså timer:minutter;
* Hvis du fjerner afkrydsningsfeltet Indtast i 24-timers format, skal
  formatet være "HH: MM AM" eller "HH: MM PM", HH skal indeholde et
  12-timers format fra 0 til 12 og "AM "|" PM "suffiks kan være i små eller
  store bogstaver
* Hvis du vælger boksen s"Stilletimer" men felterne for start- og
  sluttidspunkt forbliver tomme, eller indtaster en forkert værdi, fjernes
  markeringen for "Stilletimer" automatisk for at undgå fejl;
* En besked skulle vises for at rapportere din fejl.

## Kompatibilitet

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.3.


[[!tag dev stable]]
[[!tag dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

