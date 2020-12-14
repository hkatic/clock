# Rozšírené hodiny a kalendár #

* Autori: Hrvoje Katić, Abdel a ďalší
* stiahnuť [stabilnú verziu][1]
* stiahnuť [vývojovú verziu][2]


Poskytuje rozšírený kalendár, stopky a hodiny pre NVDA.

Môžete nastaviť spôsob oznamovania času hlasovým výstupom a na braillovskom
riadku.

Doplnok dokáže oznamovať počet dní do konca roka, číslo týždňa a automaticky
oznamovať čas.

Poskytuje tiež stopky a minútnik.

## Poznámka:

Doplnok automaticky rozpozná staršiu verziu a na túto skutočnosť
upozorní. Správu len stačí potvrdiť.

## Použitie

* Nastavenia doplnku nájdete v strome nastavení, alebo v menu nástroje (v
  závislosti od verzie NVDA);

    * Prvé dva zoznamy určujú spôsob, akým bude NVDA oznamovať dátum a čas;
    * Políčko "interval" určuje, ako často bude doplnok automaticky
      oznamovať čas (vypnuté, každých 10 minút, 15 minút, 30 minút a každú
      hodinu);
    * Ak nastavíte interval oznamovania času, pribudnú v dialógu nasledujúce
      možnosti: Nastavenie spôsobu oznámenia (zvuk, reč, zvuk a reč);
    * Zvuk oznámenia: Môžete vybrať zvuk, ktorý sa prehrá pri každom
      automatickom oznámení;
    * Začiarkávacie políčko Tiché hodiny: Umožňuje určiť hodiny, v ktorých
      sa automatické oznamovanie času vypne;
    * Ak ste začiarkli tiché hodiny, pribudne začiarkávacie pole
      "24-hodinový formát". Ak je odčiarknuté, zadávajte čas v americkom
      formáte času (a.m, p.m). Ak ho začiarknete, zadajte čas v európskom,
      24-hodinovom formáte;
    * Do políčok "neoznamovať čas od" a "neoznamovať čas do" zadajte rozsah
      hodín, v ktorých nechcete automaticky oznamovať čas. Ak ste začiarkli
      v predchádzajúcom kroku 24-hodinový formát, zadávajte čas v
      24-hodinovom formáte;
    * Nastavenia uložíte aktivovaním tlačidla OK;
    * V dialógu Minutník môžete nastaviť, či chcete odpočítavať hodiny,
      minúty alebo sekundy;
    * Do nasledujúceho editačného poľa zadajte čas, ktorý chcete
      odpočítavať. Nepoužívajte desatinné čísla;
    * V zozname "zvuk" vyberte zvuk, ktorý sa ozve po skončení
      odpočítavania;
    * Tlačidlo Pozastaviť umožňuje pozastaviť a prípadne znovu spustiť
      odpočítavanie;
    * Tlačidlom zastaviť vynulujete minútnik;
    * Odpočítavanie spustíte tlačidlom OK;

* NVDA+F12: Oznámi aktuálny čas. Stlačené dvakrát rýchlo za sebou oznámi
  dnešný dátum. Stlačené trikrát rýchlo za sebou oznámi číslo dňa v roku,
  číslo týždňa a počet dní do konca roka.

## Klávesové skratky

* NVDA+f12: Oznámi aktuálny čas;
* Stlačené dvakrát rýchlo za sebou oznámi dnešný dátum;
* Stlačené trikrát rýchlo za sebou oznámi číslo týždňa, číslo dňa a počet
  dní do konca roka.
* Je možné nastaviť skratku na oznámenie uplynutého a zostávajúceho času;
* Skratku nastavíte v dialógu Klávesové skratky.
* Dvojité stlačenie skratky ukončí odpočítavanie;
* Tiež môžete definovať skratku na prerušenie prehrávaného zvuku;
* Zvuk môžete prerušiť zloženými príkazmi, ktoré si ešte vysvetlíme.

## Zložené Klávesové skratky

Zložené príkazy pozostávajú zo skratky nvda+shift+F12 nasledovanej písmnom:

* S: Spusti, vynuluj alebo zastav stopky;
* R: Vynuluj a zastav stopky;
* A: Oznámi uplynutý a zostávajúci čas minutníka;
* C: Prerušiť odpočítavanie minutníka;
* Medzera: Povedz čas stopiek alebo minutníka;
* P: Zruš odpočítavanie minutníka;
* H: Oznám dostupné zložené príkazy.

## Spôsob zadávania času tichých hodín

* Aby edochádzalo k chybám, zadávajte čas v presnom formáte;
* Ak začiarknete "24-hodinový formát", musíte použiť tvar hh:mm, napríklad
  15:15.
* V opačnom prípade zadajte čas ako "hh:mm AM" alebo "hh:mm PM". Napríklad
  "03:15 PM" pre 15:15 alebo "03:15AM" pre 03:15 ráno.
* Ak začiarknete políčko tiché hodiny a súčasne nezadáte žiadny čas alebo je
  zadanie nesprávne, políčko sa odčiarkne a automatické oznamovanie času
  bude aktívne po celý deň;
* NVDA vás na chybu upozorní.

## Systémové požiadavky

* Doplnok funguje s NVDA od verzie 2014.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

