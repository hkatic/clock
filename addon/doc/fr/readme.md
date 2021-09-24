# Extension horloge et calendrier  pour NVDA #

* Auteurs : Hrvoje Katić, Abdel et contributeurs de NVDA
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* Compatibilité NVDA : 2019.3 et ultérieure

Cette extension active les fonctions avancées de l'horloge, de minuterie
d'alarme et du calendrier pour NVDA.

You can configure NvDA to announce time and date in formats other than what
Windows provides by default. Additionally, you can obtain the current day,
week number, as well as the remaining days before the end of the current
year, and you can also set automatic time announcement on specified
interval. There's also a stopwatch and Alarm timer features built-in to the
add-on that lets you time your tasks, such as copying files, installing
programs, or cooking meals.

Notes:

* if you install the add-on as an update, during the installation process,
  the wizard detects if the old configuration is compatible with the new one
  and offers to correct it before installing, then you'll just have to
  validate the OK button to confirm that.
* On Windows 10 and later, you can use Alarms and Clock app to manage
  stopwatch and timers.

## Raccourcis clavier

* NVDA+F12: obtenir l'heure actuelle
* NVDA+F12 pressé deux fois rapidement: obtenir la date actuelle
* NVDA+F12 pressed three times quickly: reports the current day, the week
  number, the current year and the remaining days before the end of the year
* NVDA+Shift+F12: enter clock layer

## Unassigned commands

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, open NVDA
menu, Preferences, then Input Gestures. Expand Clock category, then locate
unassigned commands from the list below and select "Add", then type the
gesture you wish to use.

* Elapsed and remaining time before the next alarm. pressing this gesture
  twice quickly will cancel the next alarm.
* Stop currently playing alarm sound.

## Commandes séquentielles

Pour utiliser des commandes séquentielles, appuyez sur NVDA+Maj+F12 suivi de
l'une des touches suivantes :

* S: Starts, resets or stops the stopwatch
* R: Resets stopwatch to 0 without restarting it
* A: gives the elapsed and remaining time before the next alarm
* C: Cancel the next alarm
* Space: Speaks current stopwatch or count-down timer
* p: If an alarm is too long, allows to stop it
* H: List all layered commands (Help)

## Utilisation

* Ouvrez le dialogue de configuration de cette extension à partir de la
  boîte de dialogue Paramètres NVDA.

    * Dans le panneau Réglage de l'horloge les deux premiers contrôles de
      Zone de liste déroulante vous permettent de choisir votre format
      d'affichage préféré pour l'heur et la date.
    * Le contrôle Zone de liste déroulante intitulé "Intervalle" vous permet
      de définir l'intervalle de l'annonce automatique de l'heure (Toutes
      les 15 minutes, Toutes les 30 minutes, Toutes les heures ou
      Désactivé).
    * Le contrôle Zone de liste déroulante intitulé "Annonce de l'heure"
      (visible uniquement si le choix "Désactivé" n'est pas sélectionné dans
      la Zone de liste déroulante intervalle) vous permet de configurer
      comment l'annonce automatique de l’heure devrait être annoncée (Parole
      et son, Parole seulement, ou Son seulement) lorsque l'annonce
      automatique de l’heure fonctionne.
    * Le contrôle Zone de liste déroulante intitulé "Son de carillon
      d'horloge" (visible uniquement si le choix "Désactivé" n'est pas
      sélectionné dans la Zone de liste déroulante intervalle) vous permet
      de choisir entre différents sons d'horloge qui sera joué lorsque
      l'annonce automatique de l’heure fonctionne et annoncée avec le son.
    * Le contrôle Case à cocher intitulé ""Heures silencieuses" (visible
      uniquement si le choix "Désactivé" n'est pas sélectionné dans la Zone
      de liste déroulante intervalle) vous permet de configurer l'intervalle
      de temps dans laquelle l'annonce automatique ne doit pas se produire.
    * Le contrôle Case à cocher intitulé "Entrée au format 24 heures"
      (visible uniquement si les heures silencieuses sont activées) vous
      permet de configurer si vous voulez entrer l'heure pour les heures
      silencieuses en format 12 heures (A.M. ou P.M.) ou européen 24 heures.
    * Les contrôles de Zone d'édition pour le début et fin de la durée
      ((visible uniquement si les heures silencieuses sont activées) vous
      permettent de configurer l'intervalle de temps pour les heures
      silencieuses. L'heure doit être entrée au format HH:MM si la case à
      cocher "Entrée au format 24 heures" est cochée, sinon vous devez
      utiliser un format 12 heures comme décrit ci-dessous.
    * Une fois terminé, faire tab jusqu'au bouton OK et activer celui-ci en
      appuyant sur Entrée pour enregistrer vos paramètres.
    * Dans le dialogue Réglage de l'alarme, le premier contrôle de Zone de
      liste déroulante vous permet de choisir votre compte à rebours préféré
      de la minuterie avant que l'alarme sonne.
    * Le contrôle de zone d'édition vous permet de saisir votre temps
      d'attente avant que l'alarme sonne. Cette durée doit être spécifiée en
      1 ou plusieurs chiffres, pas un nombre décimal.
    * Le contrôle Zone de liste déroulante intitulé "Son de l'alarme" vous
      permet de choisir entre différents sons d'alarme qui sera joué lorsque
      l’heure de l’alarme sonnera.
    * Le bouton  Pause vous permet de  mettre en pause / reprendre les
      alarmes trop longues.
    * Le bouton  Arrêter vous permet d'arrêter les alarmes trop longues.
    * Une fois terminé, faire tab jusqu'au bouton OK et activer celui-ci en
      appuyant sur Entrée. Un message devrait être affiché pour vous
      rappeler le temps d'attente avant l'alarme.

* Appuyer sur NVDA+F12 une fois pour obtenir l'heure actuelle, deux fois
  pour obtenir la date actuelle, ou trois fois pour obtenir le jour actuel,
  le numéro de la semaine, ainsi que les jours restants avant la fin de
  l'année en cours.

## Syntaxe à utiliser pour les heures silencieuses

1. Pour éviter les bugs, les heures silencieuses doivent suivre une syntaxe
   rigoureuse et précise.
2. Si vous cochez la case "Entrée au format 24 heures", le format doit être
   "HH:MM".
3. Si vous décochez la case "Entrée au format 24 heures", le format doit
   être "HH:MM AM" ou "HH:MM PM", le HH doit contenir un format 12 heures,
   de 0 à 12 et le suffixe "AM"|"PM" peut être en minuscule ou en majuscule.
4. Si vous cochez la case "Heures silencieuses" et que vous laissez le champ
   "Début de la durée des heures silencieuses" ou "Heure de fin des heures
   silencieuses", ou tapez une valeur erronée, la case "Heures silencieuses"
   sera automatiquement décochée pour éviter les erreurs et un message sera
   affiché.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
