# Doplnok Hodiny a kalendár pre NVDA #

* Autori: Hrvoje Katić, Abdel a prispievatelia NVDA
* Kompatibilita s NVDA: 2019.3 a novšie

Tento doplnok umožňuje pokročilé funkcie hodín, budíka, časovača a kalendára pre NVDA.

Môžete nastaviť NVDA tak, aby oznamoval čas a dátum v iných formátoch, než aké štandardne poskytuje Windows. Navyše môžete získať aktuálny deň, číslo týždňa, ako aj zostávajúce dni do konca aktuálneho roka a tiež nastaviť automatické oznamovanie času v zadaných intervaloch. V doplnku je tiež stopky a funkcia budíka, ktoré umožňujú merať čas vašich úloh, ako je kopírovanie súborov, inštalácia programov alebo varenie jedál.

## Poznámky:

* ak nainštalujete doplnok ako aktualizáciu, počas inštalácie sprievodca zistí, či je stará konfigurácia kompatibilná s novou a ponúkne jej opravu pred inštaláciou, potom stačí potvrdiť tlačidlo OK.
* V systéme Windows 10 a novších môžete použiť aplikáciu Budíky a hodiny na správu stopiek a časovačov.

## Klávesové skratky

* NVDA+F12: získa aktuálny čas
* NVDA+F12 stlačené dvakrát rýchlo: získa aktuálny dátum
* NVDA+F12 stlačené trikrát rýchlo: hlási aktuálny deň, číslo týždňa, aktuálny rok a zostávajúce dni do konca roka
* NVDA+Shift+F12: vstup do vrstvy hodín

## Nepriradené príkazy

Nasledujúce príkazy nie sú predvolene priradené; ak ich chcete priradiť, použite dialóg „Gestá vstupu“ na pridanie vlastných príkazov. Na to otvorte ponuku NVDA, Nastavenia, potom Gestá vstupu. Rozbaľte kategóriu Hodiny, vyhľadajte nepriradené príkazy zo zoznamu nižšie a zvoľte „Pridať“, potom zadajte gesto, ktoré chcete použiť.

* Uplynutý a zostávajúci čas pred ďalším budíkom. dvojité rýchle stlačenie tohto gesta zruší ďalší budík.
* Zastaviť aktuálne prehrávaný zvuk budíka.
* Zobraziť dialóg plánovania budíkov.
* Zobraziť vrstvené príkazy (klávesy po NVDA+Shift+F12).

## Vrstvené príkazy

Na používanie vrstvených príkazov stlačte NVDA+Shift+F12 a potom jednu z nasledujúcich kláves:

* S: spúšťa, resetuje alebo zastavuje stopky
* R: resetuje stopky na 0 bez reštartu
* A: poskytuje uplynutý a zostávajúci čas pred ďalším budíkom
* T: otvorí dialóg plánovania budíkov
* C: zruší ďalší budík
* Medzerník: oznamuje aktuálne stopky alebo odpočítavanie
* P: ak je budík príliš dlhý, umožňuje ho zastaviť
* H: zoznam všetkých vrstvených príkazov (Pomoc)

## Konfigurácia a použitie

Na konfiguráciu funkcií hodín otvorte ponuku NVDA, Nastavenia, potom Nastavenia, a nakonfigurujte nasledujúce možnosti v paneli Hodiny:

* Formát zobrazenia času a dátumu: použite tieto rozbaľovacie polia na nastavenie, ako bude NVDA oznamovať čas a dátum po stlačení NVDA+F12 raz alebo dvakrát rýchlo.
* Interval: vyberte interval oznamovania času z tohto zoznamu (vypnuté, každých 10 minút, 15 minút, 30 minút alebo každú hodinu).
* Oznamovanie času (aktivované, ak interval nie je vypnutý): vyberte medzi rečou a zvukom, iba zvukom alebo iba rečou.
* Zvuk zvonenia hodín (aktivované, ak interval nie je vypnutý): vyberte predvolený zvuk zvonenia hodín.
* Samostatné zvonenia hodín a medziminút (aktivované, ak interval nie je vypnutý, predvolene vypnuté): povoľte toto začiarkavacie políčko na prispôsobenie zvonení pre medziminúty.
  * Zvuk medziminútového zvonenia (ak je zapnuté „Samostatné zvonenia hodín a medziminút“): vyberte zvuk pre medziminúty.
* Tiché hodiny (aktivované, ak interval nie je vypnutý): vyberte toto začiarkavacie políčko na nastavenie obdobia tichých hodín.
* Formát času tichých hodín (aktivované, ak sú tiché hodiny zapnuté): vyberte, ako sa zobrazujú možnosti (12-hodinový alebo 24-hodinový formát).
* Začiatok a koniec tichých hodín: vyberte rozsah hodín a minút pre tiché hodiny z rozbaľovacích polí.

Na plánovanie budíkov otvorte ponuku NVDA, Nástroje, potom vyberte Plánovanie budíkov. Dialóg obsahuje:

* Trvanie budíka v: vyberte trvanie budíka/časovača v hodinách, minútach a sekundách.
* Trvanie: zadajte trvanie budíka v jednotke uvedenej vyššie.
* Zvuk budíka: vyberte zvuk budíka, ktorý sa prehrá.
* Tlačidlá zastaviť a pozastaviť: zastavia alebo pozastavia dlhý budík.

Kliknite na OK a zobrazí sa správa s aktuálne zvoleným trvaním budíka.
