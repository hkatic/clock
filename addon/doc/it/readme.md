# Componente aggiuntivo Orologio e calendario per NVDA #

* Autori: Hrvoje Katić, Abdel e collaboratori NVDA
* Compatibilità NVDA: 2019.3 e successive

Questo componente aggiuntivo abilita funzionalità avanzate di orologio, timer di allarme e calendario per NVDA.

È possibile configurare NVDA per annunciare l’ora e la data in formati diversi da quelli forniti di default da Windows. Inoltre, è possibile ottenere il giorno corrente, il numero della settimana, nonché i giorni rimanenti fino alla fine dell’anno in corso, e impostare l’annuncio automatico dell’ora a intervalli specificati. Il componente include anche funzionalità di cronometro e timer di allarme che consentono di misurare il tempo delle proprie attività, come copiare file, installare programmi o cucinare pasti.

## Note:

* se si installa il componente aggiuntivo come aggiornamento, durante il processo di installazione la procedura guidata rileva se la vecchia configurazione è compatibile con la nuova e offre di correggerla prima dell’installazione, quindi sarà sufficiente confermare il pulsante OK.
* In Windows 10 e versioni successive, è possibile utilizzare l’app Sveglie e orologio per gestire cronometri e timer.

## Comandi da tastiera

* NVDA+F12: ottieni l’ora corrente
* NVDA+F12 premuto due volte rapidamente: ottieni la data corrente
* NVDA+F12 premuto tre volte rapidamente: annuncia il giorno corrente, il numero della settimana, l’anno corrente e i giorni rimanenti fino alla fine dell’anno
* NVDA+Shift+F12: entra nel livello orologio

## Comandi non assegnati

I seguenti comandi non sono assegnati per impostazione predefinita; se si desidera assegnarli, utilizzare la finestra Gesti di input per aggiungere comandi personalizzati. Per farlo, aprire il menu NVDA, Preferenze, poi Gesti di input. Espandere la categoria Orologio, individuare i comandi non assegnati nell’elenco seguente e selezionare "Aggiungi", quindi inserire il gesto desiderato.

* Tempo trascorso e rimanente prima del prossimo allarme. premendo questo gesto due volte rapidamente si annulla il prossimo allarme.
* Interrompere il suono dell’allarme attualmente in riproduzione.
* Mostra finestra di dialogo pianificazione allarmi.
* Mostra comandi a livelli (tasti da premere dopo NVDA+Shift+F12).

## Comandi a livelli

Per utilizzare i comandi a livelli, premere NVDA+Shift+F12 seguito da uno dei seguenti tasti:

* S: avvia, reimposta o arresta il cronometro
* R: reimposta il cronometro a 0 senza riavviarlo
* A: comunica il tempo trascorso e rimanente fino al prossimo allarme
* T: apre la finestra di pianificazione allarmi
* C: annulla il prossimo allarme
* Spazio: annuncia il cronometro o il conto alla rovescia corrente
* P: se un allarme è troppo lungo, consente di interromperlo
* H: elenca tutti i comandi a livelli (Aiuto)

## Configurazione e utilizzo

Per configurare le funzionalità dell’orologio, aprire il menu NVDA, Preferenze, poi Impostazioni, e configurare le seguenti opzioni nel pannello Orologio:

* Formato di visualizzazione di ora e data: utilizzare queste caselle combinate per configurare come NVDA annuncerà ora e data quando si preme NVDA+F12 una o due volte rapidamente.
* Intervallo: scegliere l’intervallo di annuncio dell’ora da questa casella combinata (disattivato, ogni 10 minuti, 15 minuti, 30 minuti o ogni ora).
* Annuncio dell’ora (attivato se l’intervallo non è disattivato): scegliere tra voce e suono, solo suono o solo voce.
* Suono del segnale orario (attivato se l’intervallo non è disattivato): selezionare il suono predefinito del segnale orario.
* Segnali separati per ore e minuti intermedi (attivato se l’intervallo non è disattivato, disattivato per impostazione predefinita): attivare questa casella per personalizzare i segnali dei minuti intermedi separatamente da quelli orari.
  * Suono dei minuti intermedi (attivato se “segnali separati per ore e minuti intermedi” è selezionato): selezionare il suono per i minuti intermedi.
* Ore silenziose (attivato se l’intervallo non è disattivato): selezionare questa casella per configurare il periodo di ore silenziose.
* Formato ore silenziose (attivato se le ore silenziose sono attivate): scegliere il formato (12 ore o 24 ore).
* Orario di inizio e fine ore silenziose: selezionare l’intervallo di ore e minuti per le ore silenziose dalle caselle combinate.

Per pianificare gli allarmi, aprire il menu NVDA, Strumenti, quindi selezionare Pianifica allarmi. La finestra include:

* Durata dell’allarme: selezionare la durata dell’allarme/timer in ore, minuti e secondi.
* Durata: inserire la durata dell’allarme nell’unità sopra indicata.
* Suono dell’allarme: selezionare il suono dell’allarme.
* Pulsanti arresta e pausa: arrestare o mettere in pausa un allarme lungo.

Fare clic su OK e verrà mostrato un messaggio con la durata dell’allarme selezionata.
