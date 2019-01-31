# Module complémentaire horloge et calendrier  pour NVDA #

* Auteurs : Hrvoje Katić, Abdel et contributeurs de NVDA;
* Télécharger [version stable][1];
* Télécharger [version de développement][2].


Ce module complémentaire active les fonctions avancées de l'horloge, de
minuterie d'alarme et du calendrier pour NVDA.

Au lieu de toujours obtenir la date et l'heure depuis Windows, vous pouvez
personnaliser comment les dates et les heures doivent être annoncées et
affichées en braille par NVDA.

En outre, vous pouvez obtenir le jour actuel, le numéro de la semaine, ainsi
que les jours restants avant la fin de l'année en cours, et vous pouvez
également définir une annonce automatique de l'heure sur un intervalle
spécifié.

Il existe également des fonctionnalités pour le chronomètre et minuterie
d'alarme intégrés au module complémentaire qui vous permettent de
chronométrer vos tâches, telles que la copie de fichiers, l'installation de
programmes ou la préparation de repas.

## Note:

Si vous installez le module complémentaire en tant que mise à jour, lors du
processus d'installation, l'assistant détecte si l'ancienne configuration
est compatible avec la nouvelle et vous propose de la corriger avant
l'installation. Il vous suffira alors de valider le bouton OK pour confirmer
cela.

## Utilisation

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

## Raccourcis clavier

- NVDA+F12, pour obtenir l'heure actuelle;
- NVDA+F12 pressé deux fois rapidement, pour obtenir la date actuelle;
- NVDA+F12 pressé trois fois rapidement, pour annoncer le jour actuel, le
numéro de la semaine, l'année en cours et les jours qui restent avant la fin
de l'année.

- There is a script that gives the remaining and elapsed time before the
next alarm; - There is no keyboard gesture assigned to this script, you will
have to do it yourself in the "Input gestures" dialog box, in the "Clock"
category; - This gesture pressed twice quickly, cancel the next alarm; -
There is another script to stop the sound that is currently playing, its
gesture is also not defined; - That script can also be called using the
clock layer commands described below.

## Commandes en couches

Pour utiliser des commandes en couches, appuyez sur NVDA+Maj+F12 suivi de
l'une des touches suivantes :

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

## Compatibilité

- Ce module complémentaire est compatible avec les versions de NVDA allant
de 2014.3 à 2019.1.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

