# Extension horloge et calendrier  pour NVDA #

* Auteurs : Hrvoje Katić, Abdel et contributeurs de NVDA
* Télécharger [version stable][1]
* Télécharger [version de développement][2]
* Compatibilité NVDA : 2019.3 et ultérieure

Cette extension active les fonctions avancées de l'horloge, de minuterie
d'alarme et du calendrier pour NVDA.

Vous pouvez configurer comment les dates et les heures doivent être
annoncées par NVDA au lieu de toujours obtenir la date et l'heure fournit
par défaut depuis Windows. En outre, vous pouvez obtenir le nombre actuel
des jours et semaines de l'année en cours et vous pouvez également définir
l'annonce automatique de l'heure sur un intervalle spécifié. Il y a aussi
des fonctionnalités pour le chronomètre et minuterie d'alarme intégrés à
l'extension, qui vous permet de chronométrer vos tâches, telles que la copie
de fichiers, l'installation de programmes ou la préparation de repas

Note:

* Si vous installez l'extension en tant que mise à jour, lors du processus
  d'installation, l'assistant détecte si l'ancienne configuration est
  compatible avec la nouvelle et vous propose de la corriger avant
  l'installation. Il vous suffira alors de valider le bouton OK pour
  confirmer cela.
* Sous Windows 10 et ultérieure, vous pouvez utiliser des alarmes et une
  application pour l'horloge pour gérer les chronomètres et les minuteries.

## Raccourcis clavier

* NVDA+F12: obtenir l'heure actuelle
* NVDA+F12 pressé deux fois rapidement: obtenir la date actuelle
* NVDA+F12 pressé trois fois rapidement: annoncer le jour actuel, le numéro
  de la semaine, l'année en cours et les jours qui restent avant la fin de
  l'année.
* NVDA+Maj+F12: Entrée séquentielle de l'horloge

## Commandes non assignées

Les commandes suivantes ne sont assignées par défaut; Si vous souhaitez
assigner un geste personnalisé vous pouvez ajouter un en utilisant la  boîte
de dialogue Gestes de Commandes. Pour ce faire, ouvrez le menu NVDA,
Préférences, puis Gestes de Commandes. Développé la catégorie Horloge, puis
localisez les commandes non assignées dans la liste ci-dessous et
sélectionnez "Ajouter", puis tapez le geste que vous souhaitez utiliser.

* Temps écoulé et temps restant avant la prochaine alarme. Appuyer deux fois
  rapidement sur ce geste annulera rapidement la prochaine alarme.
* Arrêter de lire le son de l'alarme actuelle.

## Commandes séquentielles

Pour utiliser des commandes séquentielles, appuyez sur NVDA+Maj+F12 suivi de
l'une des touches suivantes :

* S: Démarre, réinitialise ou arrête le chronomètre;
* R: Réinitialise le chronomètre à 0 sans le démarrer;
* A: donne le temps écoulé et restant avant la prochaine alarme;
* C: Annule la prochaine alarme;
* Espace: Annonce le chronomètre actuel ou le compte à rebours de la
  minuterie;
* p: Si une alarme est trop longue, permet de l'arrêter;
* H: Répertorie toutes les commandes séquentielles (Aide).

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
