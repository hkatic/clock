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
sélectionnez "Ajouter", puis entrez le geste que vous souhaitez utiliser.

* Temps écoulé et temps restant avant la prochaine alarme. Appuyer deux fois
  rapidement sur ce geste annulera rapidement la prochaine alarme.
* Arrête de jouer le son de l'alarme actuelle.
* Afficher la boîte de dialogue Programmer des alarmes.

## Commandes séquentielles

Pour utiliser des commandes séquentielles, appuyez sur NVDA+Maj+F12 suivi de
l'une des touches suivantes :

* S: Démarre, réinitialise ou arrête le chronomètre;
* R: Réinitialise le chronomètre à 0 sans le démarrer;
* A: donne le temps écoulé et restant avant la prochaine alarme;
* T: Ouvre la boîte de dialogue Programmer des alarmes.
* C: Annule la prochaine alarme;
* Espace: Annonce le chronomètre actuel ou le compte à rebours de la
  minuterie;
* p: Si une alarme est trop longue, permet de l'arrêter;
* H: Répertorie toutes les commandes séquentielles (Aide).

## Configuration et utilisation

Pour configurer la fonctionnalité de l'horloge, ouvrez le menu NVDA,
Préférences, puis Paramètres et configurer les options suivantes à partir du
panneau Horloge:

* Format d'affichage de l'heure: Utilisez ces zones de liste déroulante pour
  configurer comment NVDA annoncera l'heure et la date lorsque vous appuyez
  une fois ou deux fois rapidement sur NVDA+F12, respectivement.
* Intervalle: Choisissez l'intervalle de l'annonce de l'heure de cette Zone
  de liste déroulante (désactivé, toutes les 10 minutes, 15 minutes, 30
  minutes ou toutes les heures).
* Annonce de l'heure (activée si l'intervalle n'est pas désactivée):
  Choisissez entre message et son, message seulement ou son seulement.
* Son de carillon d'horloge (activée si l'intervalle n'est pas désactivée):
  Sélectionnez le son de carillon d'horloge.
* Heures silencieuses (activée si l'intervalle n'est pas désactivée):
  Sélectionnez cette case à cocher pour configurer l'intervalle de temps
  dans laquelle l'annonce automatique ne doit pas se produire.
* Format des heures silencieuses (activée si les heures silencieuses est
  activée): Sélectionnez la manière dont les options des heures silencieuses
  sont présentées (au format 12 heures ou 24 heures).
* Début et fin de la durée des heures silencieuses: Sélectionnez
  l'intervalle d'heure ou minute pour les heures silencieuses à partir des
  zones de liste déroulante heures et minutes.

Pour planifier les alarmes, ouvrez le menu NVDA, Outils, puis sélectionnez
Planifier les alarmes. Le contenu de la boîte de dialogue comprend:

* Durée de l'alarme en: Sélectionnez la durée de l'alarme / minuterie entre
  heures, minutes et secondes.
* Durée: Entrez la durée de l'alarme dans l'unité spécifiée ci-dessus.
* Son de l'alarme: Sélectionnez le son de l'alarme à jouer.
* Les boutons Arrêter ou Pause: Arrête ou met en pause un son d'alarme long.

Cliquez sur OK, et un message vous informera de la durée de l'alarme
actuellement sélectionnée.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
