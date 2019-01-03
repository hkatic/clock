# Clock: impostazioni avanzate per l'ora ed il calendario con NVDA #

* Authori: Hrvoje Katić, Abdel and NVDA contributors;
* Scarica [versione stabile][1];
* Scarica [versione in sviluppo][2].


Questo componente aggiuntivo presenta impostazioni avanzate per l'orologio,
il calendario e un timer per NVDA.

E' possibile personalizzare il modo in cui viene letta o mostrata nella
barra braille l'ora e la data con NVDA.

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

*	Aprire la finestra di configurazione per il componente aggiuntivo dal menu strumenti o dal pannello delle impostazioni, a Seconda della versione di NVDA;
	*	Nella finestra impostazioni orologio le prime due caselle di controllo consentono di impostare il formato di visualizzazione dell'ora e della data;
	*	ILa casella di controllo "Formato 24-ore" si riferisce alle impostazioni della fascia oraria inattiva. Permette di scegliere se inserire l'ora nel formato 12-ore (A.M. o  P.M.), oppure il formato europeo 24-ore ;
	*	La casella combinata "Segnale Orario" consente di controllare l'annuncio automatico dell'ora che può essere spento oppure a intervalli differenti (ogni 10 minuti,ogni 15 minuti, ogni 30 minuti o ogni ora);
	*	La casella combinata "Avviso segnale orario" consente di specificare in modo in cui viene segnalata l'ora, voce e suono, solo suono, solo voce;
	*	La casella combinata "Suono segnale orario" permette di scegliere il suono per il segnale orario;
	*	La casella di controllo "Fascia oraria inattiva" consente di disattivare l'annuncio automatico per un certo intervallo di tempo impostabile;
	*	Nei campi editazione Inizio fascia oraria e fine fascia oraria è possibile indicare l'inizio e la fine dell'intervallo di inattività dell'annuncio dell'orario automatico. Questi campi editazione verranno visualizzati solo se è attiva la casella di controllo per la fascia oraria inattiva. L'ora deve essere inserita nel formato HH:MM;
	*	Premere il pulsante Ok o Applica per salvare le impostazioni;
	*	nelle impostazioni Timer, la prima casella di controllo permette di scegliere l'unità di misura per il Timer;
	*	Nel campo editazione è possibile inserire il tempo di attesa prima del suono d'allarme. si possono inserire più cifre, i numeri digitali non son validi;
	*	nella casella di controllo "suono per il Timer" si può scegliere tra vari suoni che servirà come allarme allo scadere del tempo;
	*	Una volta impostato, premere il pulsante Ok per impostare. Verrà visualizzato un messaggio di conferma che riporta il tempo di attesa impostato per il timer;
	*	Premendo NVDA+F12 una volta leggerà l'ora, premendo due volte la data, premendo tre volte il numero del giorno, della settimana ed i giorni rimanenti rispetto all'anno in corso;

## Comandi rapidi

- NVDA+F12, annuncia l'ora corrente. - NVDA+F12 premuto  due volte
rapidamente, annuncia la data. - NVDA+F12 premuto tre volte rapidamente,
informa sul numero del giorno, della  settimana e i giorni restanti rispetto
all'anno in corso. 

- NVDA+F12 informa sul tempo restante e tempo trascorso nel timer. -
NVDA+F12 premuto due volte disattiva il timer.

## comandi a livello:

Per usare i comandi a livello, premere NVDA+Shift+F12 e poi uno dei seguenti
tasti:

- S: Avvia, interrompe o azzera per riavviare il cronometro. - R: Azzera il
cronometro senza ripartire. - A: Fornisce alcune informazioni sul Timer. -
C: Annulla il Timer impostato. - BarraSpaziatrice: Legge il tempo trascorso
nel cronometro. - H: Elenca i comandi a livello disponibili.

## Compatibilità:

- Questo componente aggiuntivo è compatibile con NVDA dalla versione 2014.3
fino alla versione 2019.1.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

