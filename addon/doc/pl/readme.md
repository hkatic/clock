# Clock and calendar Add-on for NVDA #

* Autorzy: Hrvoje Katić, Abdel i NVDA współtwórcy;
* Pobierz [Wersja stabilna][1];
* Pobierz [Wersja rozwojowa][2].


Ten dodatek włącza rozbudowany zegar, licznik z alarmem i i funkcjonalność
kalendarza dla NVDA.

Zamiast dostarczać datę i czas z systemu, można dostosować ich odczytywanie
i wyświetlanie w brajlu przez NVDA

Oprócz tego można sprawdzić bieżący dzień tygodnia, numer tygodnia w roku
oraz liczbę dni pozostałych do końca bieżącego roku, a także ustawić
ogłaszanie czasu co konkretny okres

Wbudowane funkcje stopera i timera pomagają organizować zadania,
np. kopiowanie plików, instalowanie programów, czy gotowanie posiłków.

## Uwaga:

Podczas instalowania aktualizacji dodatku, kreator sprawdza, czy poprzednia
konfiguracja jest zgodna z nową i proponuje jej poprawę przed
instalacją. Aby to potwierdzić, wystarczy nacisnąć przycisk OK.

## Użycie

* Wybierz okno dialogowe ustawień dodatku z menu narzędzia NVDA, lub z
  panelu ustawień, w zależności od posiadanej wersji NVDA;

    * Dwie pierwsze listy rozwijane w oknie ustawień Clock służą do
      wybierania preferowanego formatu wyświetlania daty i czasu;
    * Lista rozwijana "Okres" służy do ustawiania okresu automatycznego
      ogłaszania czasu (co 10 minut, co 15 minut, co 30 minut, co godzinę,
      lub wyłączone);
    * Lista rozwijana "Ogłaszanie czasu" (widoczna tylko wtedy, gdy opcja
      "Wyłączone" na liście rozwijanej Okres nie jest zaznaczona), pozwala
      wybrać sposób ogłaszania czasu: mowa i dźwięk, tylko mowa, lub tylko
      dźwięk, gdy automatyczne ogłaszanie czasu jest włączone;
    * Lista rozwijana "Dźwięk dzwonka" (widoczna tylko wtedy, gdy opcja
      "Wyłączone" na liście rozwijanej Okres nie jest zaznaczona) umożliwia
      wybranie spośród różnych dostępnych dźwięków tego, który będzie
      odtwarzany, gdy automatyczne ogłaszanie czasu jest włączone i czas
      jest ogłaszany dźwiękiem;
    * Pole wyboru "Ciche godziny" (widoczne tylko wtedy, gdy opcja
      "Wyłączone" na liście rozwijanej Okres nie jest zaznaczona) służy do
      ustawiania przedziału czasu, w którym automatyczne ogłaszanie czasu ma
      być nieaktywne;
    * Pole wyboru "Wejście w formacie 24-godzinnym" (Widoczne tylko wtedy,
      gdy ciche godziny są włączone) służy do ustawiania formatu czasu
      wejścia dla cichych godzin na 12-godzidny, lub europejski 24-godzinny;
    * Pola edycji czasu początkowego i końcowego (widoczne tylko wtedy, gdy
      ciche godziny są włączone) służą do ustawiania zakresu czasu dla
      cichych godzin. Czas powinien być wprowadzony w formacie HH:MM, gdy
      pole wyboru "wejście w formacie 24-godzinnym" jest zaznaczone. W
      przeciwnym razie trzeba będzie używać formatu 12-godzinnego, jak
      poniżej;
    * Aby zapisać ustawienia, przejdź tabem do przycisku OK i aktywuj go
      naciskając enter;
    * Pierwsza lista rozwijana w oknie dialogowym Ustawianie Alarmu służy do
      wybierania preferowanego odliczania do dźwięku alarmu;
    * W polu edycji należy wpisać czas oczekiwania na dźwięk alarmu. Czas
      musi być wpisany za pomocą jednej lub więcej cyfr, bez liczb
      dziesiętnych;
    * Lista rozwijana "Dźwięk alarmu" służy do wybierania dźwięku, który
      będzie odtwarzany gdy nadejdzie czas alarmu;
    * Przycisk pauza służy do wstrzymywania/wznawiania zbyt długich alarmów;
    * Przycisk Zatrzymaj służy do zatrzymywania zbyt długich alarmów;
    * Aby zapisać ustawienia, przejdź tabem do przycisku OK i aktywuj go
      naciskając Enter. Powinna wyświetlić się wiadomość z przypomnieniem
      ile czasu pozostało do alarmu;

* NVDA+F12 naciśnięte raz - aktualny czas, naciśnięte dwukrotnie - bieżąca
  data, naciśnięte trzykrotnie - numer dnia i tygodnia w bieżącym roku, oraz
  liczba dni pozostałych do końca bieżącego roku

## Skróty klawiszowe

* NVDA+F12, odczytaj aktualny czas;
* NVDA+F12 dwukrotnie szybko naciśnięte, odczytaj aktualną datę;
* NVDA+F12 naciśnięte szybko trzy razy, odczytuje bieżący dzień, numer
  tygodnia w roku, bieżący rok oraz liczbę dni pozostałych do końca roku.
* Czas, który upłynął i pozostał do następnego alarmu jest podawany za
  pomocą skryptu.
* Żadne polecenie nie jest przypisane do tego skryptu. Należy przypisać
  własne polecenie w oknie dialogowym "Zdarzenia wejścia" w kategorii
  "Clock" ;
* To polecenie dwukrotnie szybko naciśnięte, anuluj następny alarm;
* Kolejny skrypt zatrzymuje aktualnie odtwarzany dźwięk. Do niego również
  nie jest przypisane żadne polecenie;
* Ten skrypt można też wywołać za pomocą poleceń warstwowych Clock opisanych
  poniżej.

## Polecenia warstwowe

Aby używać poleceń warstwowych, naciśnij NVDA+Shift+F12, a następnie 1 z
poniższych klawiszy:

* S: uruchamia, resetuje, lub zatrzymuje stoper;
* R: Zeruje stoper, ale go nie restartuje;
* A: Podaje czas, który upłynął i pozostał do następnego alarmu;
* C: Anuluje następny alarm;
* Spacja: Wymawia aktualną wartość stopera lub odliczanie;
* p: Zatrzymuje zbyt długi alarm;
* H: Pokaż wykaz poleceń warstwowych (Pomoc).

## Składnia dla cichych godzin 

* Należy konsekwentnie używać precyzyjnej składni dla cichych godzin, aby
  uniknąć błędów;
* Jeśli pole wyboru "Wejście w formacie 24-godzinnym" jest zaznaczone,
  należy wpisywać czas w formacie "HH:MM";
* Gdy pole wyboru "Wejście w formacie 24-godzinnym" jest odznaczone, należy
  wpisywać czas w formacie "HH:MM AM" lub "HH:MM PM". HH musi zawierać
  format 12-godzinny od 0 do 12, a przyrostek "AM"|"PM" można wpisać małymi
  lub wielkimi literami
* Może się zdarzyć, że pole wyboru ciche godziny" jest zaznaczone, ale pole
  edycji "Czas początkowy cichych godzin" czy "Czas końcowy cichych godzin"
  jest puste, lub jest tam wpisana błędna wartość. W takiej sytuacji pole
  wyboru "Ciche godziny" automatycznie się odznacza, co zapobiega błędom;
* Powinna wyświetlić się wiadomość informująca o błędzie.

## Zgodność

* Ten dodatek jest zgodny z wersjami NVDA od 2014.3 do 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

