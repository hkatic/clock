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

*	Ouvrez le dialogue de configuration du module complémentaire à partir du menu Outils de NVDA ou à partir du panneau de configuration selon votre version de NVDA;
	*	Dans le dialogue Réglage de l'horloge les deux premiers contrôles de Zone de liste déroulante vous permettent de choisir votre format d'affichage préféré pour l'heur et la date;
	*	Le contrôle Case à cocher intitulé "Entrée au format 24 heures" vous permet de configurer si vous voulez entrer l'heure pour les heures silencieuses en format 12 heures (A.M. ou P.M.) ou européen 24 heures;
	*	Le contrôle Zone de liste déroulante intitulé "Intervalle" vous permet de définir l'intervalle de l'annonce automatique de l'heure (Toutes les 15 minutes, Toutes les 30 minutes, Toutes les heures ou Désactivé);
	*	Le contrôle Zone de liste déroulante intitulé "Annonce de l'heure" vous permet de configurer comment l'annonce automatique de l’heure devrait être annoncée (Parole et son, Parole seulement, ou Son seulement) lorsque l'annonce automatique de l’heure fonctionne;
	*	Le contrôle Zone de liste déroulante intitulé "Son de carillon d'horloge" vous permet de choisir entre différents sons d'horloge qui sera joué lorsque l'annonce automatique de l’heure fonctionne et annoncée avec le son;
	*	Le contrôle Case à cocher intitulé ""Heures silencieuses" vous permet de configurer l'intervalle de temps lorsque l'annonce automatique de l'heure ne doit pas se produire, que l'annonce automatique de l'heure soit activée ou non;
	*	Les contrôles de Zone d'édition pour le début et fin de la durée (uniquement visible si les heures de silence sont activées) vous permettent de configurer l'intervalle de temps pour les heures silencieuses. L'heure doit être entrée au format HH:MM;
	*	Une fois terminé, faire tab jusqu'au bouton OK et activer celui-ci en appuyant sur Entrée pour enregistrer vos paramètres;
	*	Dans le dialogue Réglage de l'alarme, le premier contrôle de Zone de liste déroulante vous permet de choisir votre compte à rebours préféré de la minuterie avant que l'alarme sonne;
	*	Le contrôle de zone d'édition vous permet de saisir votre temps d'attente avant que l'alarme sonne. Cette durée doit être spécifiée en 1 ou plusieurs chiffres, pas un nombre décimal;
	*	Le contrôle Zone de liste déroulante intitulé "Son de l'alarme" vous permet de choisir entre différents sons d'alarme qui sera joué lorsque l’heure de l’alarme sonnera;
	*	Une fois terminé, faire tab jusqu'au bouton OK et activer celui-ci en appuyant sur Entrée. Un message doit être affiché pour vous rappeler le temps d'attente avant l'alarme;
*	Appuyer sur NVDA+F12 une fois pour obtenir l'heure actuelle, deux fois pour obtenir la date actuelle, ou trois fois pour obtenir le jour actuel, le numéro de la semaine, ainsi que les jours restants avant la fin de l'année en cours.

## Raccourcis clavier

- NVDA+F12, pour obtenir l'heure actuelle;
- NVDA+F12 pressé deux fois rapidement, pour obtenir la date actuelle;
- NVDA+F12 pressé trois fois rapidement, pour annoncer le jour actuel, le
numéro de la semaine, l'année en cours et les jours qui restent avant la fin
de l'année.

- Contrôle+F12, donne le temps restant et écoulé avant la prochaine alarme;
- Contrôle+F12 pressé deux fois rapidement, annule la prochaine alarme.

## Commandes en couches

Pour utiliser des commandes en couches, appuyez sur NVDA+Maj+F12 suivi de
l'une des touches suivantes :

- S: Démarre, réinitialise ou arrête le chronomètre;
- R: Réinitialise le chronomètre à 0 sans le démarrer;
- A: Donne le temps restant et écoulé avant la prochaine alarme;
- C: Annule la prochaine alarme;
- Barre d'espace : Annonce le chronomètre actuel ou le compte à rebours de
la minuterie;
- H: Liste toutes les commandes en couches (Aide).

## Compatibilité

- Ce module complémentaire est compatible avec les versions de NVDA allant
de 2014.3 à 2019.1.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
