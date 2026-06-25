# Uhr- und Kalender-Add-on für NVDA #

* Autoren: Hrvoje Katić, Abdel und NVDA-Mitwirkende
* NVDA-Kompatibilität: 2019.3 und höher

Dieses Add-on aktiviert erweiterte Funktionen für Uhr, Alarm-Timer und Kalender in NVDA.

Sie können NVDA so konfigurieren, dass Uhrzeit und Datum in anderen Formaten als den standardmäßig von Windows bereitgestellten angesagt werden. Zusätzlich können Sie den aktuellen Tag, die Wochennummer sowie die verbleibenden Tage bis zum Jahresende abrufen und außerdem eine automatische Zeitankündigung in festgelegten Intervallen einstellen. Das Add-on enthält außerdem eine Stoppuhr- und Alarm-Timer-Funktion, mit der Sie Ihre Aufgaben zeitlich messen können, z. B. das Kopieren von Dateien, das Installieren von Programmen oder das Kochen von Mahlzeiten.

## Hinweise:

* Wenn Sie das Add-on als Update installieren, erkennt der Installationsassistent während der Installation, ob die alte Konfiguration mit der neuen kompatibel ist, und bietet an, sie vor der Installation zu korrigieren. Danach müssen Sie nur noch die OK-Schaltfläche bestätigen.
* Unter Windows 10 und neuer können Sie die App „Alarme und Uhr“ verwenden, um Stoppuhr und Timer zu verwalten.

## Tastenkombinationen

* NVDA+F12: aktuelle Uhrzeit abrufen
* NVDA+F12 zweimal schnell gedrückt: aktuelles Datum abrufen
* NVDA+F12 dreimal schnell gedrückt: meldet den aktuellen Tag, die Wochennummer, das aktuelle Jahr und die verbleibenden Tage bis zum Jahresende
* NVDA+Shift+F12: Uhr-Schicht aktivieren

## Nicht zugewiesene Befehle

Die folgenden Befehle sind standardmäßig nicht zugewiesen; wenn Sie sie zuweisen möchten, verwenden Sie den Dialog „Eingabegesten“, um benutzerdefinierte Befehle hinzuzufügen. Öffnen Sie dazu das NVDA-Menü, Einstellungen und dann Eingabegesten. Erweitern Sie die Kategorie „Uhr“, suchen Sie die unten aufgeführten nicht zugewiesenen Befehle und wählen Sie „Hinzufügen“, dann geben Sie die gewünschte Geste ein.

* Verstrichene und verbleibende Zeit bis zum nächsten Alarm. ein zweimaliges schnelles Drücken dieser Geste bricht den nächsten Alarm ab.
* Aktuell abgespielten Alarmton stoppen.
* Dialog zur Planung von Alarmen anzeigen.
* Geschichtete Befehle anzeigen (Tasten nach NVDA+Shift+F12).

## Geschichtete Befehle

Um geschichtete Befehle zu verwenden, drücken Sie NVDA+Shift+F12 gefolgt von einer der folgenden Tasten:

* S: startet, setzt zurück oder stoppt die Stoppuhr
* R: setzt die Stoppuhr auf 0 zurück, ohne sie neu zu starten
* A: gibt die verstrichene und verbleibende Zeit bis zum nächsten Alarm aus
* T: öffnet den Dialog zur Alarmplanung
* C: bricht den nächsten Alarm ab
* Leertaste: spricht die aktuelle Stoppuhr oder den Countdown-Timer
* P: wenn ein Alarm zu lang ist, kann er gestoppt werden
* H: listet alle geschichteten Befehle auf (Hilfe)

## Konfiguration und Verwendung

Um die Uhrfunktion zu konfigurieren, öffnen Sie das NVDA-Menü, Einstellungen, dann Einstellungen, und konfigurieren Sie die folgenden Optionen im Uhr-Bereich:

* Anzeigeformat für Uhrzeit und Datum: verwenden Sie diese Kombinationsfelder, um festzulegen, wie NVDA Uhrzeit und Datum ansagt, wenn Sie NVDA+F12 einmal oder zweimal schnell drücken.
* Intervall: wählen Sie das Zeitansageintervall in diesem Kombinationsfeld (aus, alle 10 Minuten, 15 Minuten, 30 Minuten oder jede Stunde).
* Zeitankündigung (aktiviert, wenn Intervall nicht aus ist): wählen Sie zwischen Sprache und Ton, nur Ton oder nur Sprache.
* Uhrenschlagton (aktiviert, wenn Intervall nicht aus ist): wählen Sie den Standard-Uhrenschlagton.
* Getrennte Stunden- und Zwischenminuten-Schläge (aktiviert, wenn Intervall nicht aus ist, standardmäßig deaktiviert): aktivieren Sie dieses Kontrollkästchen, um die Töne für Zwischenminuten getrennt vom Stundenschlag anzupassen.
  * Zwischenminuten-Schlagton (aktiviert, wenn „getrennte Stunden- und Zwischenminuten-Schläge“ aktiviert ist): wählen Sie den Ton für Zwischenminuten.
* Ruhezeiten (aktiviert, wenn Intervall nicht aus ist): aktivieren Sie dieses Kontrollkästchen, um den Zeitraum für Ruhezeiten festzulegen.
* Ruhezeiten-Zeitformat (aktiviert, wenn Ruhezeiten aktiviert sind): wählen Sie die Darstellung (12- oder 24-Stunden-Format).
* Beginn- und Endzeiten der Ruhezeiten: wählen Sie den Stunden- und Minutenbereich für Ruhezeiten in den Kombinationsfeldern.

Um Alarme zu planen, öffnen Sie das NVDA-Menü, Werkzeuge, und wählen Sie „Alarme planen“. Der Dialog enthält:

* Alarmdauer in: wählen Sie die Dauer des Alarms/Timers in Stunden, Minuten und Sekunden.
* Dauer: geben Sie die Alarmdauer in der oben angegebenen Einheit ein.
* Alarmton: wählen Sie den abzuspielenden Alarmton.
* Stop- und Pause-Schaltflächen: stoppen oder pausieren eines langen Alarmtons.

Klicken Sie auf OK, und eine Meldung informiert Sie über die aktuell ausgewählte Alarmdauer.
