# Complemento de Reloxo e calendario para NVDA #

* Autores: Hrvoje Katić, Abdel e contribuíntes co NVDA;
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]


Este complemento habilita a funcionalidade avanzada de reloxo, contador con
alarma e calendario para NVDA.

No canto de obter hora e data dende Windows, podes personalizar cómo
deberían falarse e braillificarse as datas en NVDA:

Ademais, podes obter o número do día actual, da semana, así como os días que
restan antes do final do ano, e tamén podes establecer anunciado automático
da hora nun intervalo específico.

Tamén están dispoñibles integradas no complemento as características de
cronómetro e temporizador con alarma, que che permitirán temporizar as túas
tarefas, como o copiado de arquivos, a instalación de programas ou o
cociñado de carne.

## Nota:

Se instalas o complemento como unha actualización, durante o proceso de
instalación, o asistente detecta se a configuración vella é compatible coa
nova e ofrece correxila antes da instalación, de forma que só tes que
validar o botón Aceptar para confirmalo.

## Uso

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

## Teclas de ordes

- NVDA+F12, obtén a hora actual.  - NVDA+F12 premeda dúas veces
sucesivamente,  obtén a data actual.  - NVDA+F12 premeda tres veces
sucesivamente, obtén o número de día, o número de semana, o ano actual e o
número de días restante ata o final do ano.

- There is a script that gives the remaining and elapsed time before the
next alarm; - There is no keyboard gesture assigned to this script, you will
have to do it yourself in the "Input gestures" dialog box, in the "Clock"
category; - This gesture pressed twice quickly, cancel the next alarm; -
There is another script to stop the sound that is currently playing, its
gesture is also not defined; - That script can also be called using the
clock layer commands described below.

## Ordes en capa

Para utilizar as ordes en capa, preme NVDA+Shift+F12 seguido dunha das
seguintes teclas:

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

## compatibilidade

- Este complemento é compatible coas versións do NVDA no rango da 2014.3 ata
a 2019.1.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

