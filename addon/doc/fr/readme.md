# Extension Horloge et calendrier pour NVDA #

* Auteurs : Hrvoje Katić, Abdel et les contributeurs NVDA
* Compatibilité NVDA : 2019.3 et versions ultérieures

Cette extension permet les fonctionnalités avancées d’horloge, de minuteur d’alarme et de calendrier pour NVDA.

Vous pouvez configurer NVDA pour annoncer l’heure et la date dans des formats différents de ceux fournis par Windows par défaut. De plus, vous pouvez obtenir le jour actuel, le numéro de semaine, ainsi que le nombre de jours restants avant la fin de l’année en cours, et vous pouvez également définir une annonce automatique de l’heure à un intervalle spécifié. Il y a également un chronomètre et des fonctions de minuteur d’alarme intégrées dans l’extension qui permettent de chronométrer vos tâches, comme la copie de fichiers, l’installation de programmes ou la préparation de repas.

Remarques :

* si vous installez l’extension comme mise à jour, durant le processus d’installation, l’assistant détecte si l’ancienne configuration est compatible avec la nouvelle et propose de la corriger avant l’installation, puis vous n’aurez qu’à valider le bouton OK pour confirmer cela.
* Sous Windows 10 et versions ultérieures, vous pouvez utiliser l’application Alarmes et horloge pour gérer le chronomètre et les minuteurs.

## Commandes principales

* NVDA+F12 : obtenir l’heure actuelle
* NVDA+F12 appuyé deux fois rapidement : obtenir la date actuelle
* NVDA+F12 appuyé trois fois rapidement : annonce le jour actuel, le numéro de semaine, l’année en cours et le nombre de jours restants avant la fin de l’année
* NVDA+Shift+F12 : entrer dans la couche horloge

## Commandes non assignées

Les commandes suivantes ne sont pas assignées par défaut ; si vous souhaitez les assigner, utilisez le dialogue Gestes de commande pour ajouter des commandes personnalisées. Pour cela, ouvrez le menu NVDA, Préférences, puis Gestes de commande. Développez la catégorie Horloge, puis repérez les commandes non assignées dans la liste ci-dessous et sélectionnez « Ajouter », puis entrez le geste que vous souhaitez utiliser.

* Temps écoulé et restant avant la prochaine alarme. Un double appui rapide sur ce geste annulera la prochaine alarme.
* Arrêter le son de l’alarme en cours de lecture.
* Afficher la boîte de dialogue des alarmes programmées.
* Afficher les commandes en couche (touches à presser après NVDA+Shift+F12).

## Commandes en couche

Pour utiliser les commandes en couche, appuyez sur NVDA+Shift+F12 puis sur l’une des touches suivantes :

* S : démarre, réinitialise ou arrête le chronomètre
* R : réinitialise le chronomètre à 0 sans le redémarrer
* A : annonce le temps écoulé et restant avant la prochaine alarme
* T : ouvre le dialogue de programmation des alarmes
* C : annule la prochaine alarme
* Espace : annonce le chronomètre ou le compte à rebours actuel
* p : si une alarme est trop longue, permet de l’arrêter
* H : liste toutes les commandes en couche (aide)

## Configuration et utilisation

Pour configurer les fonctionnalités de l’horloge, ouvrez le menu NVDA, Préférences, puis Paramètres, et configurez les options suivantes dans le panneau Horloge :

* Format d’affichage de l’heure et de la date : utilisez ces listes déroulantes pour configurer la manière dont NVDA annoncera l’heure et la date lorsque vous appuyez sur NVDA+F12 une ou deux fois rapidement, respectivement.
* Intervalle : choisissez l’intervalle d’annonce de l’heure dans cette liste (désactivé, toutes les 10 minutes, 15 minutes, 30 minutes ou chaque heure).
* Annonce de l’heure (activée si l’intervalle n’est pas désactivé) : choisissez entre voix et son, son uniquement ou voix uniquement.
* Son du carillon de l’horloge (activé si l’intervalle n’est pas désactivé) : sélectionnez le son du carillon par défaut pour les minutes intermédiaires et les heures pleines.
* Carillons séparés pour les heures et les minutes intermédiaires (activé si l’intervalle n’est pas désactivé, désactivé par défaut) : activez cette case à cocher pour personnaliser séparément les carillons des minutes intermédiaires et des heures.
  * Son des minutes intermédiaires (activé si « Carillons séparés pour les heures et les minutes intermédiaires » est coché) : sélectionnez le son du carillon spécifiquement pour les minutes intermédiaires.
* Heures calmes (activé si l’intervalle n’est pas désactivé) : cochez cette case pour configurer une plage d’heures calmes durant laquelle l’annonce automatique de l’heure ne doit pas se produire.
* Format des heures calmes (activé si les heures calmes sont activées) : choisissez la manière dont les options d’heures calmes sont présentées (format 12 heures ou 24 heures).
* Heures de début et de fin des heures calmes : choisissez la plage horaire dans les listes déroulantes d’heures et de minutes.

Pour programmer des alarmes, ouvrez le menu NVDA, Outils, puis sélectionnez Programmer des alarmes. Le contenu du dialogue comprend :

* Durée de l’alarme en : choisissez la durée entre heures, minutes et secondes.
* Durée : saisissez la durée de l’alarme dans l’unité indiquée ci-dessus.
* Son de l’alarme : sélectionnez le son à jouer.
* Boutons arrêt et pause : arrêt ou pause d’une alarme longue.

Cliquez sur OK, et un message vous indiquera la durée de l’alarme actuellement sélectionnée.
