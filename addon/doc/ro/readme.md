# Suplimentul Clock and calendar pentru NVDA #

* Autori: Hrvoje Katić, Abdel și contribuitorii NVDA;
* Descarcă [versiunea stabilă][1];
* Descarcă [versiunea în dezvoltare][2].


Acest supliment activează ceasul avansat, alarma și calendarul pentru NVDA.

În loc să obțineți mereu data și ora de la Windows, puteți personaliza cum
să fie spuse sau afișate în braille de NVDA.

În plus, puteți obține ziua curentă, numărul săptămânii, dar și câte zile au
mai rămas până la sfârșitul anului curent. Puteți să setați anunțarea
automată a orei într-un interval specificat.

De asemenea, sunt implementate în supliment caracteristicile cronometru și
alarmă, cu ajutorul cărora vă puteți programa activități precum copierea de
fișiere, instalarea de programe sau, de ce nu, luarea micului dejun, a
prânzului, a cinei, sau chiar a unei mici gustări.

## Notă:

Dacă instalați suplimentul ca actualizare, în timpul procesului de
instalare, vrăjitorul vede dacă configurația veche este compatibilă sau nu
cu cea nouă și se oferă să o corecteze înainte de instalare, apoi
dumneavoastră trebuie doar să apăsați butonul OK ca să confirmați această
acțiune.

## Folosire

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

## Comenzi de tastatură

- NVDA+F12, spune ora curentă; - NVDA+F12 apăsat de două ori rapid, spune
data curentă; - NVDA+F12 apăsat rapid de trei ori, spune ziua curentă,
numărul sătpămânii dinn an și câte zile mai sunt până la sfârșitul anului.

- There is a script that gives the remaining and elapsed time before the
next alarm; - There is no keyboard gesture assigned to this script, you will
have to do it yourself in the "Input gestures" dialog box, in the "Clock"
category; - This gesture pressed twice quickly, cancel the next alarm; -
There is another script to stop the sound that is currently playing, its
gesture is also not defined; - That script can also be called using the
clock layer commands described below.

## Comenzi stratificate

Pentru a folosi comenzile stratificate, apăsați NVDA+Shift+F12 urmat de una
din următoarele taste:

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

## Compatibilitate

- Acest supliment este compatibil cu versiunile de NVDA pornind de la
versiunea 2014.3 până la versiunea 2019.1.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

