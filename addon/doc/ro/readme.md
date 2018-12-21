# Suplimentul Clock and calendar pentru NVDA #

* Autori: Hrvoje Katić, Abdel și contribuitorii NVDA;
* Descarcă [versiunea stabilă][1];
* Descarcă [versiunea în dezvoltare][2].


Acest supliment activează ceasul avansat, alarma și calendarul pentru NVDA.

În loc să obțineți mereu data și ora de la Windows, puteți personaliza cum
să fie spuse sau afișate în braille de NVDA.

În plus, puteți obține ziua curentă, numărul săptămânii, dar și câte zile au
mai rămas până la sfârșitul anului curent. Puteți să setați anunțarea
automată a orei într-un interval specificat.

De asemenea, sunt implementate în supliment caracteristicile cronometru și
alarmă, cu ajutorul cărora vă puteți programa activități precum copierea de
fișiere, instalarea de programe sau, de ce nu, luarea micului dejun, a
prânzului, a cinei, sau chiar a unei mici gustări.

## Notă:

Dacă instalați suplimentul ca actualizare, în timpul procesului de
instalare, vrăjitorul vede dacă configurația veche este compatibilă sau nu
cu cea nouă și se oferă să o corecteze înainte de instalare, apoi
dumneavoastră trebuie doar să apăsați butonul OK ca să confirmați această
acțiune.

## Folosire

*	Deschideți dialogul de configurare pentru acest supliment din meniul instrumentelor NVDA sau din panoul de setări, în funcție de versiunea de NVDA pe care o aveți;
	*	În dialogul de setare a ceasului, prima casetă combinată vă permite să alegeți formatele în care să fie afișate data și ora;
	*	Caseta de bifat etichetată „format de 24 de ore” vă permite să configurați dacă vreți ca timpul pentru orele de liniște să se afișeze în 12 ore (A.M. sau P.M.), ori în formatul european de 24 de ore;
	*	Caseta combinată etichetată „Interval” vă permite să setați intervalul pentru anunțarea automată a orei (Din sfert în sfert de oră, Din jumătate în jumătate de oră, Din oră în oră sau Dezactivat);
	*	Caseta combinată etichetată „Anunțare timp” Vă permite să configurați cum ar trebui să fie raportată anunțarea automată a timpului (Vorbire și sunet, Doar vorbire sau Doar sunet) atunci când această caracteristică este activă;
	*	Caseta combinată etichetată „cum să sune ceasul” vă permite să alegeți dintr-o varietate de sunete de ceas, care vor fi redate atunci când anunțarea automată a timpului este activă și raportată cu sunet;
	*	Caseta de bifat etichetată „Ore de liniște” vă permite să configurați timpul în care anunțarea automată a orei nu ar trebui să apară, nu contează dacă aceasta e activată sau nu;
	*	Caseta de editare pentru începutul și sfârșitul timpului (vizibilă doar dacă orele de liniște sunt activate) vă permite să configurați perioada acestora. Timpul ar trebui să fie introdus în formatul HH:MM;
	*	Când terminați, apăsați butonul OK pentru a vă salva setările;
	*	În dialogul de setare a alarmei, prima casetă combinată vă permite să alegeți cronometrul numărătorii inverse  înainte ca alarma să sune;
	*	Caseta de editare vă permite să tastați timpul de așteptare înainte ca alarma să sune. Această durată trebuie să fie specificată în una sau mai multe cifre, nu înytr-un număr zecimal;
	*	Caseta combinată etichetată „Sunet de alarmă” vă permite să alegeți dintr-o varietate de sunete de alarmă, care vor fi redate când e timpul ca alarma să sune;
	*	Când terminați, apăsați butonul OK. Va fi afișat un mesaj care să vă amintească de timpul de așteptare de dinaintea alarmei;
	*	Apăsați NVDA+F12 o dată pentru a obține ora curentă, de două ori pentru a obține data curentă, sau de trei ori pentru ziua curentă, numărul săptămânii, dar și câte zile mai sunt până la sfârșitul anului curent.

## Comenzi de tastatură

- NVDA+F12, spune ora curentă; - NVDA+F12 apăsat de două ori rapid, spune
data curentă; - NVDA+F12 apăsat rapid de trei ori, spune ziua curentă,
numărul sătpămânii dinn an și câte zile mai sunt până la sfârșitul anului.

- Control+F12, dă timpul scurs și timpul rămas până la alarma următoare; -
Control+F12 apăsat de două ori rapid, anulează alarma următoare.

## Comenzi stratificate

Pentru a folosi comenzile stratificate, apăsați NVDA+Shift+F12 urmat de una
din următoarele taste:

- S: Pornește, resetează sau oprește cronometrul; - R: Resetează cronometrul
la 0 fără să-l repornească; - A: Dă timpul scurs și timpul rămas până la
următoarea alarmă; - C: Anulează alarma următoare; - Bara de spațiu: Spune
cronometrul curent sau pe cel al numărătorii inverse; - H: Listează toate
comnzile stratificate (Ajutor).

## Compatibilitate

- Acest supliment este compatibil cu versiunile de NVDA pornind de la
versiunea 2014.3 până la versiunea 2019.1.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

