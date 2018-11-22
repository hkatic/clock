# Module complémentaire horloge et calendrier  pour NVDA #

* Auteurs : Hrvoje Katić, Abdel et contributeurs de NVDA.
* Télécharger [version de développement](https://ci.appveyor.com/project/HrvojeKati/clock/build/artifacts)

Ce module complémentaire active les fonctions avancées de l'horloge et du calendrier pour NVDA. Au lieu de toujours obtenir la date et l'heure depuis Windows, vous pouvez personnaliser comment les dates et les heures doivent être annoncées et affichées en braille par NVDA. En outre, vous pouvez obtenir le nombre actuel des jours et semaines de l'année en cours et vous pouvez également définir l'annonce automatique de l'heure sur un intervalle spécifié. Il y a aussi une fonctionnalité de chronomètre intégré au module complémentaire, qui vous permet de chronométrer vos tâches, telles que la copie de fichiers, l'installation de programmes ou la préparation de repas.

## Utilisation

*	Ouvrez le dialogue de configuration du module complémentaire depuis le menu Préférences de NVDA.
	*	Les deux premiers contrôles de Zone de liste déroulante vous permettent de choisir votre format d'affichage préféré pour l'heur et la date.
	*	Le contrôle Case à cocher intitulé "Entrée au format 24 heures" vous permet de configurer si vous voulez entrer l'heure pour les heures silencieuses en format 12 heures (A.M. ou P.M.) ou européen 24 heures.
	*	Le contrôle Zone de liste déroulante intitulé "Intervalle de l'annonce automatique" vous permet de définir l'intervalle de l'annonce automatique de l'heure (Toutes les 15 minutes, Toutes les 30 minutes, Toutes les heures ou Désactivé).
	*	Le contrôle Zone de liste déroulante intitulé "Annonce de l'heure" vous permet de configurer comment l'annonce automatique de l’heure devrait être annoncée (Parole et son, Parole seulement, ou Son seulement) lorsque l'annonce automatique de l’heure fonctionne.
	*	Le contrôle Zone de liste déroulante intitulé "Son de carillon d'horloge" vous permet de choisir entre différents sons d'horloge qui sera joué lorsque l'annonce automatique de l’heure fonctionne et annoncée avec le son.
	*	Le contrôle Case à cocher intitulé ""Heures silencieuses" vous permet de configurer l'intervalle de temps lorsque l'annonce automatique de l'heure ne doit pas se produire, que l'annonce automatique de l'heure soit activée ou non.
	*	Les contrôles de Zone d'édition pour le début et fin de la durée (uniquement visible si les heures de silence sont activées) vous permettent de configurer l'intervalle de temps pour les heures silencieuses. L'heure doit être entrée au format HH:MM.
	*	Une fois terminé, faire tab jusq'au bouton OK et activer celui-ci pour enregistrer vos paramètres.
*	Appuyer sur NVDA+F12 une fois pour obtenir l'heure actuelle, deux fois pour obtenir la date actuelle, ou trois fois pour obtenir le nombre actuel de jour et semaine de l'année en cours.

## Raccourcis clavier

- NVDA+F12, pour obtenir l'heure actuelle.
- NVDA+F12 pressé deux fois rapidement, pour obtenir la date actuelle.
- NVDA+F12 pressé trois fois rapidement, pour obtenir le nombre actuel de jour et semaine de l'année en cours.

## Commandes en couches

Pour utiliser des commandes en couches, appuyez sur NVDA+Maj+F12 suivi de l'une des touches suivantes :

- S : Démarre, arrête ou réinitialise le chronomètre.
- R : Réinitialise le chronomètre à 0 sans le démarrer.
- Barre d'espace : Annonce le chronomètre actuel ou le compte à rebours de la minuterie.
- H : Liste toutes les commandes en couches (Aide).


