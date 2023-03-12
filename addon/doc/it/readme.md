# Clock: impostazioni avanzate per l'ora ed il calendario con NVDA #

* Authori: Hrvoje Katić, Abdel e altri collaboratori di NVDA.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* NVDA compatibility: 2019.3 and later

Questo componente aggiuntivo presenta impostazioni avanzate per l'orologio,
il calendario e funzioni di timer e cronometro per NVDA.

Permette a NVDA di gestire le funzionalità avanzate di orologio e
calendario. Invece di ottenere l'orario e la data sempre da Windows, è
possibile personalizzare la modalità con cui orario e data debbano essere
annunciate sia con la sintesi che in braille. Inoltre, è possibile sapere il
giorno corrente e il numero della settimana dell'anno in corso, ed è anche
possibile impostare degli annunci automatici ad un intervallo di tempo
specifico.

Nota:

* se si sta aggiornando il componente aggiuntivo, durante il processo di
  installazione la procedura guidata rileva se la vecchia configurazione è
  compatibile con la nuova e propone la correzione. Sarà sufficiente premere
  il pulsante Ok per confermare.
* Su Windows 10 e versioni successive, puoi utilizzare l'app Sveglie e
  Orologio per gestire cronometro e timer.

## Comandi rapidi

* NVDA+F12, legge l'ora;
* NVDA+F12 premuto due volte, legge la data;
* NVDA+F12 premuto tre volte rapidamente, informa sul numero del giorno,
  della  settimana e i giorni restanti rispetto all'anno in corso. 
* NVDA+Shift+F12: attiva i comandi a livello.

## Comandi non assegnati:

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, open NVDA
menu, Preferences, then Input Gestures. Expand Clock category, then locate
unassigned commands from the list below and select "Add", then enter the
gesture you wish to use.

* Tempo trascorso e tempo rimanente prima dell'allarme successivo. premendo
  questo comando  due volte rapidamente si annullerà l'allarme successivo.
* Interrompi la riproduzione del suono dell'allarme.
* Visualizza la finestra di dialogo degli allarmi programmati.

## comandi a livello:

Per usare i comandi a livello, premere NVDA+Shift+F12 e poi uno dei seguenti
tasti:

* S: Avvia, interrompe o azzera per riavviare il cronometro.
* R: Azzera il cronometro senza ripartire.
* A: annuncia il tempo restante e trascorso per il timer;
* T: apre la finestra di dialogo degli allarmi programmati.
* C: Annulla il Timer impostato.
* BarraSpaziatrice: Legge il tempo trascorso nel cronometro.
* P: interrompe il suono del timer;
* H: elenca i comandi a livello disponibili.

## Configurazione e utilizzo

Per configurare la funzionalità dell'orologio, apri il menu NvDA,
Preferenze, quindi Impostazioni e configura le seguenti opzioni dal pannello
Orologio:

* Formato di visualizzazione dell'ora e della data: usa queste caselle
  combinate per configurare come NVDA annuncerà l'ora e la data quando premi
  NVDA+F12 una o due volte velocemente, rispettivamente.
* Intervallo: scegli l'intervallo di tempo dell'annuncio da questa casella
  combinata (off, ogni 10 minuti, 15 minuti, 30 minuti o ogni ora).
* Time announcement (enabled if interval is not off): choose between speech
  and sound, sound only, or speech only.
* Clock chime sound (enabled if interval is not off): select the clock chime
  sound.
* Quiet hours (enabled if interval is not off): select this checkbox to
  configure quiet hours range when automatic time announcement should not
  occur.
* Quiet hours time format (enabled if quiet hours is enabled): select how
  quiet hours options are presented (12-hour or 24-hour format).
* Quiet hours start and end times: select hour and minute range for quiet
  hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The
dialog contents include:

* Alarm duration in: select alarm/timer duration between hours, minutes, and
  seconds.
* Duration: enter alarm duration in the unit specified above.
* Alarm sound: select the alarm sound to be played.
* Stop and pause buttons: stop or pause a long alarm sound.

Click OK, and a message will inform you the curretnly selected alarm
duration.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
