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

*	Open the configuration dialog for this addon from the NVDA tools menu or from the settings panel According to your version of NVDA;
	*	In the Clock setup dialog, the first two Combo Box controls allow you to choose your prefered time and date display formats;
	*	The Combo Box control labeled "Interval" allows you to set the interval for automatic time announcement (Every 10 minutes, Every 15 minutes, Every 30 minutes, Every hour, or Off);
	*	The Combo Box control labeled "Time announcement" (only visible if the choice "off" is not selected in the interval Combo Box) lets you configure how the automatic time announcement should be reported (Speech and sound, Speech only, or Sound only) when automatic time announcement is working;
	*	The Combo box control labeled "Clock chime sound" (only visible if the choice "off" is not selected in the interval Combo Box) lets you choose between various clock sounds that will be played when automatic time announcement is working and reported with sound;
	*	The Checkbox control labeled "Quiet hours" (only visible if the choice "off" is not selected in the interval Combo Box) lets you configure time range when automatic time announcement shouldn't occure;
	*	The Checkbox control labeled "input in 24-hour format" (only visible if quiet hours are enabled) allows you to configure wether you want to input time for quiet hours in 12-hour (A.M. or P.M.), or european 24-hour format;
	*	The Edit box controls for start and end time (only visible if quiet hours are enabled) let you configure time range for quiet hours. The time should be entered in HH:MM format if the "input in 24-hour format" checkbox is checked, otherwise you must use a 12 hour format as described below;
	*	When done, tab to the OK button and activate it by pressing Enter to save your settings;
	*	In the Alarm setup dialog, the first Combo Box control allow you to choose your prefered countdown timer before the alarm ring;
	*	The Edit box control lets you type your time waiting before the alarm ring. This duration must be specified in 1 or more digits, not a decimal number;
	*	The Combo box control labeled "Alarm sound" lets you choose between various alarm sounds that will be played when the alarm time arrives;
	*	The pause button allows you to pause/resume too long alarms;
	*	The stop button allows you to stop too long alarms;
	*	When done, tab to the OK button and activate it by pressing Enter. A message should be displayed to remind you of the waiting time before the alarm;
*	Press NVDA+F12 once to get current time, twice to get current date, or thrice to get the current day, week number, as well as the remaining days before the end of the current year.

## Tastaturkommandoer

- NVDA + F12, få den aktuelle tid; - NVDA + F12 trykket to gange hurtigt, få
den aktuelle dato; - NVDA + F12 tre gange hurtigt, rapporterer den aktuelle
dag, ugenummeret, det aktuelle år og de resterende dage før årets udgang.

- There is a script that gives the remaining and elapsed time before the
next alarm; - There is no keyboard gesture assigned to this script, you will
have to do it yourself in the "Input gestures" dialog box, in the "Clock"
category; - This gesture pressed twice quickly, cancel the next alarm; -
There is another script to stop the sound that is currently playing, its
gesture is also not defined; - That script can also be called using the
clock layer commands described below.

## Lagrede kommandoer

For at bruge lagrede kommandoer skal du trykke på NVDA+Skift+F12 efterfulgt
af en af følgende taster:

- S: Starts, resets or stops the stopwatch; - R: Resets stopwatch to 0
without restarting it; - A: gives the remaining and elapsed time before the
next alarm; - C: Cancel the next alarm; - Space: Speaks current stopwatch or
count-down timer; - p: If an alarm is too long, allows to stop it; - H: List
all layered commands (Help).

## Syntax to use for quiet hours

- To avoid bugs, the quiet hours must follow a rigorous and precise syntax;
- If you check the "Input in 24-hour format" checkbox, the format must be
"HH:MM"; - If you uncheck the "Input in 24-hour format" checkbox, the format
must be "HH:MM AM" or "HH:MM PM", the HH must contain a 12-hour format, from
0 to 12 and the "AM"|"PM" suffix can be in lowercase or uppercase - If you
check the Quiet hours" checkbox and keep the "Quiet hours start time" or
"Quiet hours end time" field empty, or type a mistaken value, the "Quiet
hours" checkbox will be unchecked automatically, to avoid errors; - A
message should be displayed to report your error.

## Kompatibilitet

- Denne tilføjelse er kompatibel med versionerne af NVDA fra 2014.3 til
2019.1.


[[!tag dev stable]]
[[!tag dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

