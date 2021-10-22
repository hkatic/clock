# Uhr- und Kalender-Erweiterung für NVDA #

* Autoren: Hrvoje Katić, Abdel und NVDA-Community
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2019.3 und neuer

Diese Erweiterung aktiviert die erweiterte Uhr-, Alarm-Timer- und
Kalenderfunktion für NVDA.

Sie können NVDA so konfigurieren, dass Uhrzeit und Datum in anderen als den
von Windows standardmäßig bereitgestellten Formaten angesagt werden. Darüber
hinaus können Sie den aktuellen Tag, die Wochennummer sowie die
verbleibenden Tage bis zum Ende des laufenden Jahres abrufen und die
automatische Zeitansage in bestimmten Intervallen einstellen. In die
Erweiterung sind auch eine Stoppuhr und ein Wecker integriert, mit denen Sie
Ihre Aufgaben wie das Kopieren von Dateien, das Installieren von Programmen
oder das Kochen von Mahlzeiten planen können.

Anmerkungen:

* Wenn Sie die Erweiterung als Update installieren, erkennt der Assistent
  während des Installationsvorgangs, ob die alte Konfiguration mit der neuen
  kompatibel ist und bietet an, die Angaben während der Installation zu
  berichtigen, dann müssen Sie zur Bestätigung nur auf die Schaltfläche "OK"
  klicken.
* Unter Windows 10 und neuer können Sie die Wecker- und Uhr-App verwenden,
  um Stoppuhr und Timer zu verwalten.

## Tastenbefehle

* NVDA+F12: Aktuelle Uhrzeit abrufen
* NVDA+F12 zweimal schnell drücken: Aktuelles Datum abrufen
* NVDA+F12 dreimal schnell gedrückt: Zeigt den aktuellen Tag, die
  Wochennummer, das aktuelle Jahr und die verbleibenden Tage bis zum
  Jahresende an
* NVDA+Umschalt+F12: Befehl für die Uhr eingeben

## Nicht zugewiesene Befehle

Die folgenden Befehle sind standardmäßig nicht zugewiesen; Wenn Sie sie
zuweisen möchten, verwenden Sie das Dialogfeld Eingabegesten, um
benutzerdefinierte Befehle hinzuzufügen. Öffnen Sie dazu das NVDA-Menü,
Einstellungen und dann Tastenbefehle. Erweitern Sie die Kategorie Uhr,
suchen Sie dann in der Liste unten nach nicht zugewiesenen Befehlen und
wählen Sie "Hinzufügen" aus. Geben Sie dann den Tastenbefehl ein, den Sie
verwenden möchten.

* Verstrichene und verbleibende Zeit bis zum nächsten Alarm. Durch
  zweimaliges schnelles Drücken diesen Tastenbefehls wird der nächste Alarm
  abgebrochen.
* Unterbricht den aktuellen Alarmton.

## Befehle

Um die Befehle zu verwenden, drücken Sie NVDA+Umschalt+F12 gefolgt von einer
der folgenden Tasten:

* S: Startet oder stoppt oder setzt die Stoppuhr zurück
* R: Setzt die Stoppuhr auf 0 zurück, ohne sie neu zu starten
* A: Gibt die verstrichene und verbleibende Zeit bis zum nächsten Alarm aus
* C: Abbrechen des nächsten Alarms
* Leertaste: Sagt die aktuelle Stoppuhr oder den Countdown-Timer an
* p: Wenn ein Alarm anhält, kann dieser damit gestoppt werden
* H: Alle Befehle auflisten (Hilfe)

## Verwendung

* Öffnet den Konfigurationsdialog für diese Erweiterung über den
  NVDA-Einstellungsdialog.

    * Im Setup-Panel können Sie mit den ersten beiden
      Combo-Box-Steuerelementen Ihre bevorzugten Anzeigeformate für Uhrzeit
      und Datum auswählen.
    * Das mit "Intervall" beschriftete Kombinationsfeld-Steuerelement
      ermöglicht Ihnen das Einstellen des Intervalls für die automatische
      Zeitansage (Alle 10 Minuten, Alle 15 Minuten, Alle 30 Minuten,
      Stündlich oder Ausgeschaltet).
    * Mit dem Combobox-Steuerelement mit der Bezeichnung "Zeitansage" (nur
      sichtbar, wenn in der Intervall-Combobox die Option "Aus" nicht
      ausgewählt ist) können Sie konfigurieren, wie die automatische
      Zeitansage angezeigt werden soll (Sprache und Ton, Nur Sprache oder
      Nur Ton), sofern die automatische Zeitansage funktioniert.
    * Die Combobox-Steuerung mit der Bezeichnung "Glockenschlag" (nur
      sichtbar, wenn in der Intervall-Combobox die Auswahl „off“ nicht
      ausgewählt ist) lässt Sie zwischen verschiedenen Uhrgeräuschen
      auswählen, die bei der automatischen Zeitansage abgespielt und mit Ton
      gemeldet werden.
    * Mit dem Kontrollkästchen "Ruhezeiten" (nur sichtbar, wenn in der
      Intervall-Kombinationsfeld die Option "Aus" nicht ausgewählt ist)
      können Sie den Zeitbereich konfigurieren, in dem keine automatische
      Zeitansage erfolgen soll.
    * Mit dem Kontrollkästchen "Eingabe im 24-Stunden-Format" (nur sichtbar,
      wenn Ruhezeiten aktiviert sind) können Sie konfigurieren, ob Sie die
      Uhrzeit für Ruhezeiten im 12-Stunden-Format (AM oder PM) oder im
      europäischen 24-Stunden-Format eingeben möchten .
    * Über die Steuerelemente des Bearbeitungsfelds für Start- und Endzeit
      (nur sichtbar, wenn Ruhezeiten aktiviert sind) können Sie den
      Zeitbereich für Ruhezeiten konfigurieren. Die Uhrzeit sollte im Format
      HH:MM eingegeben werden, wenn das Kontrollkästchen "Eingabe im
      24-Stunden-Format" aktiviert ist, andernfalls müssen Sie wie unten
      beschrieben ein 12-Stunden-Format verwenden.
    * Wenn Sie fertig sind, klicken Sie auf die Schaltfläche "OK" und
      aktivieren Sie sie, indem Sie die Eingabetaste betätigen, um die
      Einstellungen zu speichern.
    * Im Dialogfeld für die Alarm-Einstellung können Sie mit dem ersten
      Steuerelement des Kombinationsfeldes den bevorzugten Countdown-Timer
      vor dem Alarmton auswählen.
    * Mit dem Steuerelement des Bearbeitungsfeldes können Sie die Wartezeit
      bis zum Klingeln des Weckers eingeben. Diese Dauer muss mit einer oder
      mehreren Stellen angegeben werden, keine Dezimalzahl.
    * Die Steuerung des Kombinationsfeldes mit der Bezeichnung "Weckton"
      lässt Sie zwischen verschiedenen Alarmtönen auswählen, die abgespielt
      werden, wenn die Weckzeit erreicht ist.
    * Mit der Pause-Taste können Sie anhaltende Alarme unterbrechen oder
      fortsetzen.
    * Mit der Stopptaste können Sie anhaltende Alarme stoppen.
    * Wenn Sie fertig sind, klicken Sie auf die Schaltfläche "OK" und
      aktivieren Sie sie durch Drücken der Eingabetaste. Es sollte eine
      Meldung angezeigt werden, die Sie an die Wartezeit vor dem Wecker
      erinnert.

* Drücken Sie NVDA+F12 einmal, um die aktuelle Uhrzeit abzurufen, zweimal,
  um das aktuelle Datum abzurufen, oder dreimal, um den aktuellen Tag, die
  Wochennummer sowie die verbleibenden Tage vor dem Ende des aktuellen
  Jahres abzurufen.

## Syntax für Ruhezeiten

1. Um Fehler zu vermeiden, müssen die Ruhezeiten einer strengen und präzisen
   Syntax folgen.
2. Wenn Sie das Kontrollkästchen "Eingabe im 24-Stunden-Format" aktivieren,
   muss das Format "HH:MM" sein.
3. Wenn Sie das Kontrollkästchen "Eingabe im 24-Stunden-Format"
   deaktivieren, muss das Format "HH:MM AM" oder "HH:MM PM" sein, das HH
   muss ein 12-Stunden-Format von 0 bis 12 und das "AM Das Suffix "|"PM"
   kann klein oder groß geschrieben werden.
4. Wenn Sie das Kontrollkästchen "Ruhezeit" aktivieren und das Feld
   "Ruhezeit Startzeit" oder "Ruhezeit Endzeit" leer lassen oder einen
   falschen Wert eingeben, wird das Kontrollkästchen "Ruhezeit" automatisch
   deaktiviert, um Fehler zu vermeiden, und es wird eine Meldung angezeigt.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
