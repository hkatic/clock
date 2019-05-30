# Extension horloge et calendrier  pour NVDA #

* Auteurs : Hrvoje Katić, Abdel et contributeurs de NVDA;
* Télécharger [version stable][1];
* Télécharger [version de développement][2].


Cette extension active les fonctions avancées de l'horloge, de minuterie
d'alarme et du calendrier pour NVDA.

Au lieu de toujours obtenir la date et l'heure depuis Windows, vous pouvez
personnaliser comment les dates et les heures doivent être annoncées et
affichées en braille par NVDA.

En outre, vous pouvez obtenir le jour actuel, le numéro de la semaine, ainsi
que les jours restants avant la fin de l'année en cours, et vous pouvez
également définir une annonce automatique de l'heure sur un intervalle
spécifié.

Il existe également des fonctionnalités pour le chronomètre et minuterie
d'alarme intégrés à l'extension qui vous permettent de chronométrer vos
tâches, telles que la copie de fichiers, l'installation de programmes ou la
préparation de repas.

## Note:

Si vous installez l'extension en tant que mise à jour, lors du processus
d'installation, l'assistant détecte si l'ancienne configuration est
compatible avec la nouvelle et vous propose de la corriger avant
l'installation. Il vous suffira alors de valider le bouton OK pour confirmer
cela.

## Utilisation

* Ouvrez le dialogue de configuration de cette extension à partir du menu
  Outils de NVDA ou à partir du panneau de configuration selon votre version
  de NVDA;

    * Dans le dialogue Réglage de l'horloge les deux premiers contrôles de
      Zone de liste déroulante vous permettent de choisir votre format
      d'affichage préféré pour l'heur et la date;
    * Le contrôle Zone de liste déroulante intitulé "Intervalle" vous permet
      de définir l'intervalle de l'annonce automatique de l'heure (Toutes
      les 15 minutes, Toutes les 30 minutes, Toutes les heures ou
      Désactivé);
    * Le contrôle Zone de liste déroulante intitulé "Annonce de l'heure"
      (visible uniquement si le choix "Désactivé" n'est pas sélectionné dans
      la Zone de liste déroulante intervalle) vous permet de configurer
      comment l'annonce automatique de l’heure devrait être annoncée (Parole
      et son, Parole seulement, ou Son seulement) lorsque l'annonce
      automatique de l’heure fonctionne;
    * Le contrôle Zone de liste déroulante intitulé "Son de carillon
      d'horloge" (visible uniquement si le choix "Désactivé" n'est pas
      sélectionné dans la Zone de liste déroulante intervalle) vous permet
      de choisir entre différents sons d'horloge qui sera joué lorsque
      l'annonce automatique de l’heure fonctionne et annoncée avec le son;
    * Le contrôle Case à cocher intitulé ""Heures silencieuses" (visible
      uniquement si le choix "Désactivé" n'est pas sélectionné dans la Zone
      de liste déroulante intervalle) vous permet de configurer l'intervalle
      de temps dans laquelle l'annonce automatique ne doit pas se produire;
    * Le contrôle Case à cocher intitulé "Entrée au format 24 heures"
      (visible uniquement si les heures silencieuses sont activées) vous
      permet de configurer si vous voulez entrer l'heure pour les heures
      silencieuses en format 12 heures (A.M. ou P.M.) ou européen 24 heures;
    * Les contrôles de Zone d'édition pour le début et fin de la durée
      ((visible uniquement si les heures silencieuses sont activées) vous
      permettent de configurer l'intervalle de temps pour les heures
      silencieuses. L'heure doit être entrée au format HH:MM si la case à
      cocher "Entrée au format 24 heures" est cochée, sinon vous devez
      utiliser un format 12 heures comme décrit ci-dessous;
    * Une fois terminé, faire tab jusqu'au bouton OK et activer celui-ci en
      appuyant sur Entrée pour enregistrer vos paramètres;
    * Dans le dialogue Réglage de l'alarme, le premier contrôle de Zone de
      liste déroulante vous permet de choisir votre compte à rebours préféré
      de la minuterie avant que l'alarme sonne;
    * Le contrôle de zone d'édition vous permet de saisir votre temps
      d'attente avant que l'alarme sonne. Cette durée doit être spécifiée en
      1 ou plusieurs chiffres, pas un nombre décimal;
    * Le contrôle Zone de liste déroulante intitulé "Son de l'alarme" vous
      permet de choisir entre différents sons d'alarme qui sera joué lorsque
      l’heure de l’alarme sonnera;
    * Le bouton  Pause vous permet de  mettre en pause / reprendre les
      alarmes trop longues;
    * Le bouton  Arrêter vous permet d'arrêter les alarmes trop longues;
    * Une fois terminé, faire tab jusqu'au bouton OK et activer celui-ci en
      appuyant sur Entrée. Un message devrait être affiché pour vous
      rappeler le temps d'attente avant l'alarme;

* Appuyer sur NVDA+F12 une fois pour obtenir l'heure actuelle, deux fois
  pour obtenir la date actuelle, ou trois fois pour obtenir le jour actuel,
  le numéro de la semaine, ainsi que les jours restants avant la fin de
  l'année en cours.

## Raccourcis clavier

* NVDA+F12, pour obtenir l'heure actuelle;
* NVDA+F12 pressé deux fois rapidement, pour obtenir la date actuelle;
* NVDA+F12 pressé trois fois rapidement, pour annoncer le jour actuel, le
  numéro de la semaine, l'année en cours et les jours qui restent avant la
  fin de l'année.
* Il y a un script qui donne le temps restant et le temps écoulé avant la
  prochaine alarme;
* Aucun geste au clavier n’est assigné à ce script, vous devrez le faire
  vous-même dans la boîte de dialogue "Gestes de commandes", dans la
  catégorie "Clock";
* Ce geste pressé deux fois rapidement, annule la prochaine alarme;
* Il existe un autre script pour arrêter le son en cours de lecture, son
  geste n’est pas non plus défini;
* Ce script peut également  être invoqué à l'aide des commandes en couche de
  l'horloge décrites ci-dessous.

## Commandes en couches

Pour utiliser des commandes en couches, appuyez sur NVDA+Maj+F12 suivi de
l'une des touches suivantes :

* S: Démarre, réinitialise ou arrête le chronomètre;
* R: Réinitialise le chronomètre à 0 sans le démarrer;
* A: donne le temps restant et écoulé avant la prochaine alarme;
* C: Annule la prochaine alarme;
* Espace: Annonce le chronomètre actuel ou le compte à rebours de la
  minuterie;
* p: Si une alarme est trop longue, permet de l'arrêter;
* H: Répertorie toutes les commandes en couches (Aide).

## Syntaxe à utiliser pour les heures silencieuses

* Pour éviter les bugs, les heures silencieuses doivent suivre une syntaxe
  rigoureuse et précise;
* Si vous cochez la case "Entrée au format 24 heures", le format doit être
  "HH:MM";
* Si vous décochez la case "Entrée au format 24 heures", le format doit être
  "HH:MM AM" ou "HH:MM PM", le HH doit contenir un format 12 heures, de 0 à
  12 et le suffixe "AM"|"PM" peut être en minuscule ou en majuscule
* Si vous cochez la case "Heures silencieuses" et que vous laissez le champ
  "Début de la durée des heures silencieuses" ou "Heure de fin des heures
  silencieuses", ou tapez une valeur erronée, la case "Heures silencieuses"
  sera automatiquement décochée pour éviter les erreurs.
* Un message devrait être affiché pour vous signaler votre erreur.

## Compatibilité

* This add-on is compatible with the versions of NVDA ranging from 2014.3
  until 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

