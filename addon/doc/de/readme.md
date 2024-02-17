# NVDA-Erweiterung für Uhr und Kalender #

* Authors: Hrvoje Katić, Abdel and NVDA contributors
* [Stabile Version herunterladen][1]

* NVDA-Kompatibilität: 2019.3 und neuer

Diese NVDA-Erweiterung aktiviert die erweiterten Funktionen für Uhr, Wecker
und Kalender.

Sie können NVDA so konfigurieren, dass Uhrzeit und Datum in anderen als den
von Windows standardmäßig bereitgestellten Formaten mitgeteilt
werden. Darüber hinaus können Sie den aktuellen Tag, die Wochennummer sowie
die verbleibenden Tage bis zum Ende des laufenden Jahres abrufen und die
automatische Zeitansage in bestimmten Intervallen einstellen. In die
Erweiterung sind auch eine Stoppuhr und ein Wecker integriert, mit denen Sie
Ihre Aufgaben wie das Kopieren von Dateien, das Installieren von Programmen
oder das Kochen von Mahlzeiten zeitlich festlegen können.

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
zuweisen möchten, verwenden Sie das Dialogfeld für die Tastenbefehle, um
benutzerdefinierte Befehle hinzuzufügen. Öffnen Sie dazu das NVDA-Menü,
Einstellungen und dann Tastenbefehle. Erweitern Sie die Kategorie "Uhr",
suchen Sie dann in der Liste unten nach nicht zugewiesenen Befehlen und
wählen Sie "Hinzufügen" aus. Geben Sie dann den gewünschte Tastenkombination
ein.

* Verstrichene und verbleibende Zeit bis zum nächsten Alarm. Durch
  zweimaliges schnelles Drücken diesen Tastenbefehls wird der nächste Alarm
  abgebrochen.
* Unterbricht den aktuellen Alarmton.
* Dialogfeld "Geplante Alarme" anzeigen.

## Befehle

Um die Befehle zu verwenden, drücken Sie NVDA+Umschalt+F12 gefolgt von einer
der folgenden Tasten:

* S: Startet oder stoppt oder setzt die Stoppuhr zurück
* R: Setzt die Stoppuhr auf 0 zurück, ohne sie neu zu starten
* A: Gibt die verstrichene und verbleibende Zeit bis zum nächsten Alarm aus
* T: Öffnet das Dialogfenster "Alarme planen".
* C: Abbrechen des nächsten Alarms
* Leertaste: Sagt die aktuelle Stoppuhr oder den Countdown-Timer an
* p: Wenn ein Alarm anhält, kann dieser damit gestoppt werden
* H: Alle Befehle auflisten (Hilfe)

## Konfiguration und Nutzung

Um die Uhr zu konfigurieren, öffnen Sie das NVDA-Menü, Optionen, dann
Einstellungen und konfigurieren Sie die folgenden Optionen im Bedienfeld der
Uhr:

* Anzeigeformat für Uhrzeit und Datum: Verwenden Sie diese
  Kombinationsfelder, um zu konfigurieren, wie NVDA Uhrzeit und Datum
  mitteilt, wenn Sie NVDA+F12 ein- bzw. zweimal schnell drücken.
* Intervall: Wählen Sie das Intervall für die Zeitansage aus diesem
  Kombinationsfeld (Ausgeschaltet, Alle 10 Minuten, 15 Minuten, 30 Minuten
  oder Stündlich).
* Zeitansage (aktiviert, wenn Intervall nicht ausgeschaltet ist): Wählen Sie
  zwischen "Ton und Ansage", "Nur Ton" oder "Nur Ansage" aus.
* Alarmton (aktiviert, wenn Intervall nicht ausgeschaltet ist): Wählen Sie
  den alarmton aus.
* Ruhezeiten (aktiviert, wenn Intervall nicht deaktiviert ist): Aktivieren
  Sie dieses Kontrollkästchen, um den Ruhezeitbereich zu konfigurieren, in
  dem keine automatische Zeitansage erfolgen soll.
* Zeitformat für Ruhezeiten (aktiviert, wenn Ruhezeiten aktiviert sind):
  Wählen Sie aus, wie die Optionen für Ruhezeiten dargestellt werden
  (12-Stunden- oder 24-Stunden-Format).
* Start- und Endzeiten für Ruhezeiten: Wählen Sie den Bereich für Stunden
  und Minuten für die Ruhezeiten aus den Kombinationsfeldern für Stunden und
  Minuten aus.

Um Alarme zu planen, öffnen Sie das NVDA-Menü, Werkzeuge, und wählen Sie
dann den eintrag "Alarme planen" aus. Die Dialogfelder umfassen:

* Alarmdauer in: Wählen Sie die Alarm-/Weckdauer zwischen Stunden, Minuten
  und Sekunden.
* Dauer: Geben Sie die Alarmdauer in der oben angegebenen Einheit ein.
* Alarmton: Wählen Sie den abzuspielenden Alarmton aus.
* Stopp und Pause: Stoppen oder pausieren Sie einen anhaltenden Alarmton.

Klicken Sie auf "OK" und eine Meldung informiert Sie über die aktuell
ausgewählte Alarmdauer.

[[!tag stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=clock
