# Clock: impostazioni avanzate per l'ora ed il calendario con NVDA #

* Authori: Hrvoje Katić, Abdel e altri collaboratori di NVDA.
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]
* Compatibilità con NVDA: 2019.3 e successive.

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

I seguenti comandi non sono assegnati per impostazione predefinita; se
desideri assegnarli, usa la finestra di dialogo Gesti e tasti di immissione
per aggiungere comandi personalizzati. Per farlo, apri il menu NVDA,
Preferenze, quindi Gesti e tasti di immissione. Espandi la categoria
Orologio, ed individua i comandi non assegnati dall'elenco sottostante e
seleziona "Aggiungi", quindi digita il gesto che desideri utilizzare.

* Tempo trascorso e tempo rimanente prima dell'allarme successivo. premendo
  questo comando  due volte rapidamente si annullerà l'allarme successivo.
* Interrompi la riproduzione del suono dell'allarme.

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

## Utilizzo

* Apre la finestra di dialogo di configurazione per questo componente
  aggiuntivo dalla finestra di dialogo Impostazioni NVDA.

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

## Formato per i valori della fascia oraria inattiva:

1. Per evitare errori, i valori vanno inseriti con un corretto formato.
2. Se attivate la casella "24-ore", il formato dovrà essere "HH:MM".
3. Se la casella "24-ore" è disattivata, il formato corretto sarà "HH:MM AM"
   o "HH:MM PM", il valore HH ammette numeri da 0 a 12, la dicitura "AM" o
   "PM" ammette sia minuscole che maiuscole.
4. Quando si attiva la casella "Fascia oraria inattiva", e si lasciano  i
   campi editazione "Inizio Fascia Oraria" o "Fine Fascia Oraria" vuoti o
   con valori errati, la casella "Fascia Oraria Inattiva" verrà disattivata
   automaticamente per evitare errori.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
