# Uhr- und Kalender-Erweiterung für NVDA #

* Autoren: Hrvoje Katić, Abdel und NVDA-Mitwirkende;
* [Stabile Version herunterladen][1];
* Download [development version][2].


Diese Erweiterung bietet die erweiterte Uhren-, Weck- und
Kalenderfunktionalität für NVDA.

Anstatt immer Zeit und Datum von Windows zu bekommen, können Sie anpassen,
wie Zeiten und Daten von NVDA gesprochen und in Braille ausgegeben werden
sollen.

Zusätzlich können Sie den aktuellen Tag, die Wochennummer sowie die Anzahl
der restlichen Tage des laufenden Jahres erhalten, Des weiteren können Sie
eine automatische Zeitankündigung und dessen Intervall einstellen.

In die Erweiterung wurde eine Stoppuhr und ein Wecker integriert, sodass Sie
die Zeit für Ihre Aufgaben  wie das Kopieren von Dateien, die Installation
von Programmen oder das Kochen von Mahlzeiten im Blick haben.

## Anmerkung:

Wenn Sie diese Erweiterung mittels Update installieren, erkennt der
Assistent während des Installationsprozesses, ob die alte Konfiguration mit
der neuen kompatibel ist und bietet vor der Installation an, diese zu
korrigieren. Anschließend müssen Sie nur  mit OK bestätigen, um die
Korrektur auszulösen.

## Verwendung

* Öffnen Sie den Konfigurationsdialog für diesee Erweiterung über das
  Untermenü Extras oder über das Einstellungsfenster Je nach Ihrer Version
  von NVDA;

    * Im Dialogfeld Uhr einrichten können Sie mit den ersten beiden
      Steuerelementen des Kombinationsfeldes Ihre bevorzugten Anzeigeformate
      für Uhrzeit und Datum auswählen;
    * Mit dem Auswahlfeld "Intervall" können Sie das Intervall für die
      automatische Zeitansage einstellen (alle 10 Minuten, alle 15 Minuten,
      alle 30 Minuten, jede Stunde oder Aus);
    * Mit dem Auswahlfeld "Zeitansage", welches nur sichtbar ist, sofern im
      Intervall-Kombinationsfeld die Option "Aus" nicht ausgewählt ist,
      können Sie konfigurieren wie die automatische Zeitansage gemeldet
      werden soll. Dabei haben Sie die Option zwischen Sprache und Ton, nur
      Sprache oder nur Ton;
    * Mit dem Auswahlfeld "Glockenton", welches nur dann sichtbar ist, wenn
      im Intervall-Kombinationsfeld die Option "aus" nicht ausgewählt ist,
      können Sie zwischen verschiedenen Glockengeräuschen wählen. Der
      ausgewählte Sound wird abgespielt, wenn die Zeitansage mit Ton
      gemeldet wird;
    * Mit dem Kontrollkästchen "Ruhezeit", welches nur dann sichtbar ist,
      wenn im Intervall-Kombinationsfeld die Option "Aus" nicht ausgewählt
      ist, können Sie den Zeitbereich konfigurieren, in dem keine
      automatische Zeitansage erfolgen soll;
    * Mit dem Kontrollkästchen "Eingabe im 24-Stunden-Format", welches nur
      dann sichtbarist,  wenn Ruhezeit aktiviert ist, können Sie einstellen,
      ob Sie die Dauer der Ruhezeit im 12-Stunden-Format (morgens oder
      abends) oder im europäischen 24-Stunden-Format eingeben möchten;
    * Im Eingabefeld "steuerung der Start- und Endzeit", welches nur dann
      sichtbar ist, wenn Ruhezeit aktiviert ist, können Sie den Zeitbereich
      für Ruhezeiten konfigurieren. Die Uhrzeit sollte im Format HH:MM
      eingegeben werden, wenn das Kontrollkästchen "Eingabe im
      24-Stunden-Format" aktiviert ist. Andernfalls müssen Sie wie unten
      beschrieben ein 12-Stunden-Format verwenden;
    * Wenn Sie fertig sind, navigieren Sie zur OK-Taste und aktivieren Sie
      sie, indem Sie die Eingabetaste drücken, um Ihre Einstellungen zu
      speichern;
    * Im Dialogfeld Wecker einrichten können Sie mit dem ersten Auswahlfeld
      in der Liste den gewünschten Countdown-Timer auswählen, welcher
      ausgelöst wird, bevor der Wecker klingelt;
    * Mit dem Eingabefeld "Wartezeit" können Sie die Wartezeit eingeben, bis
      der Wecker klingelt. Diese Dauer muss in 1 oder mehr Ziffern angegeben
      werden, nicht in einer Dezimalzahl;
    * Mit dem Auswahlfeld "Weckton" können Sie zwischen verschiedenen
      Alarmtönen wählen, die bei der ausgewählten Weckzeit abgespielt
      werden;
    * Mit der Taste "Pause" können Sie Wecktöne anhalten/fortsetzen, die zu
      lang sind;
    * Mit der Stopptaste können Sie Wecktöne stoppen, wenn sie zu lang sind;
    * Wenn Sie fertig sind, navigieren Sie mit der Tabulatortaste zur
      Schaltfläche OK und aktivieren Sie diese durch Drücken der
      Eingabetaste. Es sollte eine Meldung angezeigt werden, die Sie an die
      Wartezeit vor dem Weckton erinnert;

* Drücken Sie NVDA+F12 einmal, um die aktuelle Uhrzeit , zweimal schnell, um
  das aktuelle Datum, dreimal schnell um den aktuellen Tag, die
  Kalenderwoche, das Jahr sowie die Anzahl der verbleibenden Tage des Jahres
  zu erhalten.

## Tastenbefehle

* NVDA+F12, aktuelle Uhrzeit abrufen;
* NVDA+F12 zweimal kurz drücken, um das aktuelle Datum zu erhalten;
* NVDA+F12 (dreimal schnell gedrückt) liest den aktuellen Tag, die
  Kalenderwoche, das Jahr sowie die Anzahl der verbleibenden Tage des Jahres
  vor.
* Ein Befehl kann zugewiesen werden, dwelcher  die verbleibende und
  verstrichene Zeit bis zum nächsten Weckton meldet;
* Sie müssen selbst im Dialogfeld "Eingaben" in der Kategorie "Uhr" eine
  Geste für dieses Skript zuweisen;
* Zweimaliges Drücken dieser Geste löscht den nächsten Wecker;
* Es gibt ein weiteres Skript, um den aktuellen Weckton zu stoppen. Diesem
  Skript ist noch keine Geste zugewiesen;
* Dieses Skript kann durch folgende Befehle aufgerufen werden.

## Zwischenbefehle

Um Zwischenbefehle zu verwenden, drücken Sie NVDA+Shift+F12 gefolgt von
einem der folgenden Tasten:

* S: Startet, stoppt oder setzt die Stoppuhr zurück;
* R: Setzt die Stoppuhr auf 0 zurück, ohne sie neu zu starten;
* A: gibt die verbleibende und verstrichene Zeit bis zum nächsten Wecker an;
* C: Deaktiviert den nächsten Wecker;
* Leertaste: meldet die aktuelle Stoppuhr oder den Countdown-Timer;
* p: stoppt den weckton, wenn der Ton zu lang ist;
* H: Listet alle Befehle auf.

## Syntax für Ruhezeit

* Um Fehler zu vermeiden, muss die Eingabe der Ruhezeit einer strengen und
  präzisen Syntax folgen;
* Wenn Sie das Kontrollkästchen "Eingabe im 24-Stunden-Format" aktivieren,
  muss das Format "HH:MM" sein;
* Wenn Sie das Kontrollkästchen "Eingabe im 24-Stunden-Format" deaktivieren,
  muss das Format "HH:MM AM" oder "HH:MM PM" sein, das HH muss ein
  12-Stunden-Format von 0 bis 12 enthalten und das Suffix "AM"|"PM" kann in
  Klein- oder Großbuchstaben angegeben werden
* Wenn Sie das Kontrollkästchen "Ruhezeit" aktivieren und das Feld "Ruhezeit
  Anfang" oder "Ruhezeit Ende" leer lassen oder einen falschen Wert
  eingeben, wird das Kontrollkästchen "Ruhezeit" automatisch deaktiviert, um
  Fehler zu vermeiden;
* Eine Fehlermeldung sollte  angezeigt werden.

## Kompatibilität

* Diese Erweiterung ist mit den NVDA-Versionen 2014.3 bis 2019.1 kompatibel.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

