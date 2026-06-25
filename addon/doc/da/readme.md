# Ur- og kalender-tilføjelse til NVDA #

* Forfattere: Hrvoje Katić, Abdel og NVDA-bidragydere
* NVDA-kompatibilitet: 2019.3 og nyere

Denne tilføjelse aktiverer avancerede funktioner til ur, alarm-timer og kalender i NVDA.

Du kan konfigurere NVDA til at annoncere tid og dato i formater, der er forskellige fra dem, Windows som standard tilbyder. Derudover kan du få den aktuelle dag, ugenummer samt de resterende dage til årets slutning, og du kan også indstille automatisk tidsmeddelelse med et angivet interval. Tilføjelsen indeholder også stopur- og alarm-timerfunktioner, som gør det muligt at tidsmåle dine opgaver, såsom kopiering af filer, installation af programmer eller madlavning.

## Noter:

* hvis du installerer tilføjelsen som en opdatering, vil installationsguiden under installationen opdage, om den gamle konfiguration er kompatibel med den nye og tilbyde at rette den før installationen, derefter skal du blot bekræfte OK-knappen.
* På Windows 10 og nyere kan du bruge appen Alarmer og Ur til at administrere stopur og timere.

## Tastaturkommandoer

* NVDA+F12: få aktuel tid
* NVDA+F12 trykket to gange hurtigt: få aktuel dato
* NVDA+F12 trykket tre gange hurtigt: rapporterer den aktuelle dag, ugenummer, det aktuelle år og de resterende dage til årets slutning
* NVDA+Shift+F12: gå ind i ur-laget

## Ikke-tildelte kommandoer

Følgende kommandoer er ikke tildelt som standard; hvis du vil tildele dem, skal du bruge dialogen Inputbevægelser til at tilføje brugerdefinerede kommandoer. For at gøre dette skal du åbne NVDA-menuen, Indstillinger, og derefter Inputbevægelser. Udvid kategorien Ur, find de ikke-tildelte kommandoer i listen nedenfor, vælg "Tilføj", og indtast derefter den ønskede bevægelse.

* Forløbet og resterende tid før næste alarm. dobbelttryk på denne bevægelse annullerer den næste alarm.
* Stop den aktuelt afspillede alarmlyd.
* Vis dialogen til planlægning af alarmer.
* Vis lagdelte kommandoer (taster efter NVDA+Shift+F12).

## Lagdelte kommandoer

For at bruge lagdelte kommandoer skal du trykke NVDA+Shift+F12 efterfulgt af en af følgende taster:

* S: starter, nulstiller eller stopper stopuret
* R: nulstiller stopuret til 0 uden at genstarte det
* A: angiver forløbet og resterende tid før næste alarm
* T: åbner dialogen til planlægning af alarmer
* C: annullerer den næste alarm
* Mellemrum: oplæser det aktuelle stopur eller nedtælling
* P: hvis en alarm er for lang, kan den stoppes
* H: viser alle lagdelte kommandoer (hjælp)

## Konfiguration og brug

For at konfigurere ur-funktionen skal du åbne NVDA-menuen, Indstillinger, derefter Indstillinger, og konfigurere følgende indstillinger i Ur-panelet:

* Visningsformat for tid og dato: brug disse kombinationsfelter til at konfigurere, hvordan NVDA annoncerer tid og dato, når du trykker NVDA+F12 én eller to gange hurtigt.
* Interval: vælg tidsintervallet for tidsmeddelelse i denne kombinationsboks (fra, hvert 10. minut, 15 minutter, 30 minutter eller hver time).
* Tidsmeddelelse (aktiveret hvis interval ikke er fra): vælg mellem tale og lyd, kun lyd eller kun tale.
* Ur-klokkelyd (aktiveret hvis interval ikke er fra): vælg standard klokkelyd.
* Separate time- og mellemlokalminut-klokker (aktiveret hvis interval ikke er fra, deaktiveret som standard): aktiver dette afkrydsningsfelt for at tilpasse mellemlokalminut-lyde separat fra timeklokken.
  * Mellemlokalminut-klokkelyd (aktiveret hvis "separate time- og mellemlokalminut-klokker" er markeret): vælg lyd for mellemlokalminutter.
* Stille timer (aktiveret hvis interval ikke er fra): vælg dette afkrydsningsfelt for at konfigurere intervallet for stille timer.
* Stille timer-format (aktiveret hvis stille timer er aktiveret): vælg hvordan indstillingerne vises (12- eller 24-timers format).
* Start- og sluttid for stille timer: vælg time- og minutinterval for stille timer.

For at planlægge alarmer skal du åbne NVDA-menuen, Værktøjer, og vælge Planlæg alarmer. Dialogen indeholder:

* Alarmvarighed i: vælg varighed for alarm/timer i timer, minutter og sekunder.
* Varighed: indtast alarmens varighed i den angivne enhed ovenfor.
* Alarmlyd: vælg alarmlyden der skal afspilles.
* Stop- og pauseknapper: stop eller sæt en lang alarm på pause.

Klik OK, og en besked vil informere dig om den aktuelt valgte alarmvarighed.
