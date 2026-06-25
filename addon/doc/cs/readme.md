# Doplněk Hodiny a kalendář pro NVDA #

* Autoři: Hrvoje Katić, Abdel a přispěvatelé NVDA
* Kompatibilita s NVDA: 2019.3 a novější

Tento doplněk přidává do NVDA pokročilé funkce hodin, časovače alarmů a kalendáře.

NVDA můžete nastavit tak, aby oznamoval čas a datum v jiných formátech, než jaké standardně poskytuje systém Windows. Kromě toho můžete zjistit aktuální den, číslo týdne i počet zbývajících dnů do konce aktuálního roku a také nastavit automatické oznamování času ve zvoleném intervalu. Doplněk rovněž obsahuje stopky a časovač alarmů, které vám umožní měřit dobu trvání různých úloh, například kopírování souborů, instalace programů nebo vaření.

Poznámky:

* Pokud doplněk instalujete jako aktualizaci, průvodce během instalace zjistí, zda je staré nastavení kompatibilní s novou verzí, a před instalací nabídne jeho opravu. Poté stačí potvrdit tlačítko OK.
* Ve Windows 10 a novějších můžete ke správě stopek a časovačů používat aplikaci Budíky a hodiny.

## Klávesové příkazy

* NVDA+F12: oznámí aktuální čas
* NVDA+F12 stisknuté dvakrát rychle: oznámí aktuální datum
* NVDA+F12 stisknuté třikrát rychle: oznámí aktuální den, číslo týdne, aktuální rok a počet zbývajících dnů do konce roku
* NVDA+Shift+F12: vstoupí do vrstvy příkazů hodin

## Nepřiřazené příkazy

Následující příkazy nejsou ve výchozím nastavení přiřazeny. Chcete-li je přiřadit, použijte dialog Klávesové příkazy a přidejte vlastní příkazy. Otevřete nabídku NVDA, zvolte Předvolby a poté Klávesové příkazy. Rozbalte kategorii Hodiny, vyhledejte v následujícím seznamu nepřiřazené příkazy, vyberte možnost „Přidat“ a poté zadejte požadovanou klávesovou zkratku.

* Oznámí uplynulý a zbývající čas do dalšího alarmu. Dvojité rychlé stisknutí této klávesové zkratky zruší následující alarm.
* Zastaví právě přehrávaný zvuk alarmu.
* Zobrazí dialog pro plánování alarmů.
* Zobrazí příkazy vrstvy (klávesy stisknuté po NVDA+Shift+F12).

## Příkazy vrstvy

Chcete-li používat příkazy vrstvy, stiskněte NVDA+Shift+F12 a poté jednu z následujících kláves:

* S: Spustí, vynuluje nebo zastaví stopky
* R: Vynuluje stopky na 0 bez jejich opětovného spuštění
* A: Oznámí uplynulý a zbývající čas do dalšího alarmu
* T: Otevře dialog pro plánování alarmů
* C: Zruší následující alarm
* Mezerník: Oznámí aktuální čas stopek nebo odpočítávacího časovače
* P: Pokud alarm trvá příliš dlouho, umožní jej zastavit
* H: Zobrazí seznam všech příkazů vrstvy (Nápověda)

## Konfigurace a použití

Chcete-li nastavit funkce hodin, otevřete nabídku NVDA, zvolte Předvolby, poté Nastavení a v panelu Hodiny nastavte následující možnosti:

* Formát zobrazení času a data: Pomocí těchto rozbalovacích seznamů nastavíte, jak bude NVDA oznamovat čas a datum po jednom nebo dvojím rychlém stisknutí NVDA+F12.
* Interval: Z tohoto rozbalovacího seznamu vyberte interval automatického oznamování času (vypnuto, každých 10 minut, 15 minut, 30 minut nebo každou hodinu).
* Oznamování času (povoleno, pokud interval není vypnutý): Vyberte mezi řečí a zvukem, pouze zvukem nebo pouze řečí.
* Zvuk odbíjení hodin (povoleno, pokud interval není vypnutý): Vyberte výchozí zvuk odbíjení pro mezilehlé minuty a celou hodinu.
* Oddělit odbíjení celé hodiny a mezilehlých minut (povoleno, pokud interval není vypnutý, ve výchozím nastavení zakázáno): Zaškrtnutím tohoto políčka můžete nastavit samostatné zvuky odbíjení pro mezilehlé minuty a celou hodinu.
  * Zvuk odbíjení mezilehlých minut (povoleno, pokud je zaškrtnuto „Oddělit odbíjení celé hodiny a mezilehlých minut“): Vyberte zvuk odbíjení určený pro mezilehlé minuty.
* Tiché hodiny (povoleno, pokud interval není vypnutý): Zaškrtnutím tohoto políčka nastavíte časový rozsah, ve kterém nebude automatické oznamování času probíhat.
* Formát času tichých hodin (povoleno, pokud jsou tiché hodiny zapnuté): Vyberte způsob zobrazení možností tichých hodin (12hodinový nebo 24hodinový formát).
* Čas začátku a konce tichých hodin: Pomocí rozbalovacích seznamů hodin a minut nastavte začátek a konec tichých hodin.

Chcete-li naplánovat alarmy, otevřete nabídku NVDA, zvolte Nástroje a poté Plánovat alarmy. Dialog obsahuje:

* Trvání alarmu v: Vyberte jednotku trvání alarmu nebo časovače (hodiny, minuty nebo sekundy).
* Trvání: Zadejte délku alarmu v jednotce vybrané výše.
* Zvuk alarmu: Vyberte zvuk, který se přehraje při alarmu.
* Tlačítka Zastavit a Pozastavit: Zastaví nebo pozastaví dlouhý zvuk alarmu.

Po klepnutí na tlačítko OK vás zpráva bude informovat o právě zvoleném trvání alarmu.
