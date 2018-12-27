# Uhr- und Kalender-Erweiterung für NVDA #

* Autoren: Hrvoje Katić, Abdel und NVDA-Mitwirkende;
* [Stabile Version][1] herunterladen;
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

* Öffnen Sie den Konfigurationsdialog für diese Erweiterung aus dem NVDA-Extras-Menü oder mittels des Einstellungsdialoges je nach  Ihrer verwendeten NVDA-Version.
	* Im Uhren-Einstellungs-Dialog können Sie mittels den ersten beiden Kombinationsfeldern Ihre bevorzugten Zeit-und Datumsformate auswählen;
	* Das Kontrollkästchen mit der Aufschrift "Eingabe im 24-Stunden-Format" ermöglicht  die Einstellung der Zeiteingabe für ruhige Stunden im 12-Stunden-Format (A.M. bzw. P.M.) oder im europäischen 24-Stunden-Format.
	* Das Kombinationsfeld mit der Aufschrift "Intervall" ermöglicht es Ihnen, das Intervall für die automatische Zeitankündigung einzustellen (alle 15 Minuten, alle 30 Minuten, jede Stunde oder aus).
	* Mit dem Kombinationsfeld "Zeitankündigung" können Sie festlegen, wie die automatische Zeitankündigung erfolgen soll (Sprache und Ton, nur Sprache oder nur Ton), sofern die automatische Zeitankündigung aktiv ist.
	* Das Kombinationsfeld mit der Aufschrift "Uhrglockenton" ermöglicht die Wahl zwischen verschiedenen Klängen, die bei aktivierter automatischer Zeitankündigung  abgespielt werden.
	* Mit dem Kontrollkästchen "Ruhige Stunden" können Sie den Zeitbereich einstellen, in dem die automatische Zeitankündigung nicht erfolgen soll, egal ob die automatische Zeitankündigung aktiviert ist oder nicht;
	* Mit dem Eingabefeld  können Sie die Zeitspanne für ruhige Stunden festlegen. Die Uhrzeit muss im Format HH:MM eingegeben werden.
	* Wenn Sie fertig sind, speichern Sie die Änderungen mit OK ab.
	* Im Alarm-Einrichtungs-Dialog können Sie mit dem ersten Kombinationsfeld Ihre bevorzugte Zeiteinheit festlegen, bevor der Alarm ertönen soll.
	* Mit dem nächsten Eingabefeld können Sie die Wartezeit vor dem Alarmton eingeben. Diese Dauer muss in ganzen Zahlen (ohne Dezimalzahlen) angegeben werden.
	* Das Kombinationsfeld mit der Aufschrift "Alarmsignal" ermöglicht die Wahl zwischen verschiedenen Alarmgeräuschen, die bei der Alarmzeit abgespielt werden.
	* Wenn Sie fertig sind, bestätigen Sie mit OK.  Eine Nachricht sollte angezeigt werden, um Sie an die Wartezeit bis zum Alarm zu erinnern;
* Drücken Sie NVDA+F12 einmal, um die aktuelle Zeit zu erhalten, zweimal, um das aktuelle Datum zu bekommen, oder dreimal, um den aktuellen Tag, die Wochennummer, sowie die restlichen Tage bis zum Jahresende zu erhalten.

## Tastenbefehle

- NVDA+F12 liest die aktuelle Uhrzeit vor. - NVDA+F12 (zweimal schnell
gedrückt) liest das aktuelle Datum vor. - NVDA+F12 (dreimal schnell
gedrückt) liest den aktuellen Tag, die Kalenderwoche, das Jahr sowie die
Anzahl der verbleibenden Tage des Jahres vor.

- Steuerung+F12: gibt die verbleibende sowie die  abgelaufene Zeit bis zum
nächsten Alarm aus. - Steuerung+F12 zweimal schnell gedrückt: bricht den
nächsten Alarm ab.

## Zwischenbefehle

Um Zwischenbefehle zu verwenden, drücken Sie NVDA+Shift+F12 gefolgt von
einem der folgenden Tasten:

- S: Stoppuhr Starten, anhalten oder zurücksetzen . - R: Stoppuhr
zurücksetzen ohne sie zu starten. - A: Sagt Informationen über den nächsten
Alarm an. - C: Schaltet den nächsten Alarm aus. - Leertaste: Ansage der
aktuellen Zeit der Stoppuhr oder des Alarms. -
H: Listet alle Zwischenbefehle Befehle auf (hilfe).

## Kompatibilität

- Diese Erweiterung ist mit den NVDA-Versionen 2018.3 bis 2019.1 kompatibel.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

