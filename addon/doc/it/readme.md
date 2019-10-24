# Clock: impostazioni avanzate per l'ora ed il calendario con NVDA #

* Authori: Hrvoje Katić, Abdel e altri collaboratori di NVDA.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]


Questo componente aggiuntivo presenta impostazioni avanzate per l'orologio,
il calendario e funzioni di timer e cronometro per NVDA.

E' possibile personalizzare il modo in cui viene letta l'ora e la data, sia
tramite sintesi che in braille.

In oltre, è possibile conoscere il numero del giorno, della settimana ed i
giorni rimanenti rispetto all'anno in corso, e impostare un intervallo per
l'avviso automatico dell'ora.

Il componente aggiuntivo dispone anche di un cronometro e un timer, utile
per controllare il tempo impiegato in varie facende personali come copiare
file, installare programmi o cucinare.

## Nota:

se si sta aggiornando il componente aggiuntivo, durante il processo di
installazione la procedura guidata rileva se la vecchia configurazione è
compatibile con la nuova e propone la correzione. Sarà sufficiente premere
il pulsante Ok per confermare.

## Utilizzo

* Aprire la finestra di configurazione per il componente aggiuntivo dal menu
  strumenti o dal pannello delle impostazioni, a Seconda della versione di
  NVDA;

    * Nella finestra impostazioni orologio le prime due caselle di controllo
      consentono di impostare il formato di visualizzazione dell'ora e della
      data;
    * La casella combinata "Segnale Orario" consente di controllare
      l'annuncio automatico dell'ora che può essere spento oppure a
      intervalli differenti (ogni 10 minuti,ogni 15 minuti, ogni 30 minuti o
      ogni ora);
    * La casella combinata "Avviso segnale orario" (visibile quando il
      "Segnale orario" è attivo) consente di specificare in modo in cui
      viene segnalata l'ora, voce e suono, solo suono, solo voce;
    * La casella combinata "Suono segnale orario" (visibile se la casella
      "Segnale orario" è attivo) permette di scegliere il suono per il
      segnale orario;
    * La casella di controllo "Fascia oraria inattiva" (visibile se il
      "Segnale Orario" è attivo) consente di disattivare l'annuncio
      automatico per un certo intervallo di tempo impostabile;
    * La casella di controllo "Formato 24-ore" si riferisce alle
      impostazioni della "Fascia Oraria Inattiva". Permette di scegliere se
      inserire l'ora nel formato 12-ore (A.M. o  P.M.), oppure il formato
      europeo 24-ore ;
    * Nei campi editazione Inizio fascia oraria e fine fascia oraria è
      possibile indicare l'inizio e la fine dell'intervallo di inattività
      dell'annuncio dell'orario automatico. Questi campi editazione verranno
      visualizzati solo se è attiva la casella di controllo per la fascia
      oraria inattiva. L'ora deve essere inserita nel formato HH:MM se si
      usa il formato "24-ore", in caso contrario, è necessario utilizzare il
      formato 12-ore, come descritto di seguito;
    * Premere il pulsante Ok o Applica per salvare le impostazioni;
    * nelle impostazioni Timer, la prima casella di controllo permette di
      scegliere l'unità di misura per il Timer;
    * Nel campo editazione è possibile inserire il tempo di attesa prima del
      suono d'allarme. Si possono inserire più cifre, i numeri decimali non
      son validi;
    * nella casella di controllo "suono per il Timer" si può scegliere tra
      vari suoni che servirà come suono di allarme allo scadere del tempo;
    * Il pulsante Pausa consente di sospendere o riprendere la riproduzione
      dei suoni, utile quando si sceglie tra i suoni troppo lunghi;
    * Il pulsante Stop permette di interrompere suoni troppo lunghi;
    * Una volta impostato, premere il pulsante Ok per salvare la
      configurazione. Verrà visualizzato un messaggio di conferma che
      riporta il tempo di attesa impostato per il timer;

* NVDA+F12, annuncia l'ora corrente. - NVDA+F12 premuto  due volte
  rapidamente, annuncia la data. - NVDA+F12 premuto tre volte rapidamente,
  informa sul numero del giorno, della  settimana e i giorni restanti
  rispetto all'anno in corso. 

## Comandi rapidi

* NVDA+F12, legge l'ora;
* NVDA+F12 premuto due volte, legge la data;
* NVDA+F12 premuto tre volte rapidamente, informa sul numero del giorno,
  della  settimana e i giorni restanti rispetto all'anno in corso. 
* Il componente aggiuntivo include uno script per controllare il tempo
  trascorso e rimanente del timer;
* Di default non è stato assegnato nessun comando per questo script, è
  possibile assegnare i comandi  dalla finestra "Gesti e Tasti di
  Immissione" nella categoria "Clock";
* Il comando premuto due volte permette di annullare il timer;
* Un altro script permette di interrompere il suono in riproduzione, anche
  questo script non ha un comando assegnato di default;
* Lo script può essere richiamato anche con i comandi a livello descritti di
  seguito:

## comandi a livello:

Per usare i comandi a livello, premere NVDA+Shift+F12 e poi uno dei seguenti
tasti:

* S: Avvia, interrompe o azzera per riavviare il cronometro.
* R: Azzera il cronometro senza ripartire.
* A: annuncia il tempo restante e trascorso per il timer;
* C: Annulla il Timer impostato.
* BarraSpaziatrice: Legge il tempo trascorso nel cronometro.
* P: interrompe il suono del timer;
* H: elenca i comandi a livello disponibili.

## Formato per i valori della fascia oraria inattiva:

* Per evitare errori, i valori vanno inseriti con un corretto formato.
* Se attivate la casella "24-ore", il formato dovrà essere "HH:MM".
* Se la casella "24-ore" è disattivata, il formato corretto sarà "HH:MM AM"
  o "HH:MM PM", il valore HH ammette numeri da 0 a 12, la dicitura "AM" o
  "PM" ammette sia minuscole che maiuscole.
* Quando si attiva la casella "Fascia oraria inattiva", e si lasciano  i
  campi editazione "Inizio Fascia Oraria" o "Fine Fascia Oraria" vuoti o con
  valori errati, la casella "Fascia Oraria Inattiva" verrà disattivata
  automaticamente per evitare errori.
* Un messaggio vi informerà dell'errore.

## Compatibilità:

* Questo componente aggiuntivo è compatibile con NVDA dalla versione 2014.3
  alla versione 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

