# Clock and calendar Add-on for NVDA #

* Autorzy: Hrvoje Katić, Abdel i NVDA współtwórcy;
* Pobierz [Wersja stabilna][1];
* Pobierz [Wersja rozwojowa][2].


Ten dodatek włącza rozbudowany zegar, licznik z alarmem i i funkcjonalność
kalendarza dla NVDA.

Zamiast dostarczać datę i czas z systemu Windows, można dostosować do swoich
potrzeb sposób w jaki NVDA odczytuje i wyświetla to w brajlu.

Dodatkowo można otrzymać aktualny dzień, numer tygodnia w ciągu roku oraz
liczbę dni pozostałych do końca aktualnego roku. Można tąż ustawić
automatyczny odczyt godziny co wybrany przedział czasu.

Dodatek posiada również wbudowane funkcje stopera, alarmu i timera. Mogą one
pomóc w planowaniu zadań, takich jak kopiowanie plików, instalowanie
programów, czy gotowanie posiłków.

## Uwaga!

Podczas aktualizowania dodatku, kreator instalacji sprawdza, czy
dotychczasowa konfiguracja jest zgodna z nową i proponuje poprawienie jej
przed zainstalowaniem aktualizacji. Aby potwierdzić wykonanie tej operacji,
wystarczy nacisnąć przycisk OK.

## Użycie

* Otwórz okno ustawień dodatku Clock w meni Narzędzia, lub w panelu ustawień
  NVDA, w zależności od zainstalowanej wersji NVDA;

    * Pierwsze dwie listy rozwijane w oknie konfiguracji Clock służą do
      wybierania preferowanego formatu wyświetlania daty i czasu;
    * Lista rozwijana "Interwał" pozwala określić, co ile czasu ma być
      ogłaszana aktualna godzina (co 10 minut, co 15 minut, co 30 minut, co
      godzinę, lub wyłączone);
    * Lista rozwijana "Ogłaszanie czasu" jest widoczna tylko wtedy, gdy
      opcja "wyłączone" z listy "Interwał" nie została zaznaczona. Można tu
      wskazać sposób ogłaszania aktualnego czasu (mowa i dźwięk, tylko mowa,
      lub tylko dźwięk) Automatyczne ogłaszanie czasu musi być włączone;
    * Lista rozwijana "Dźwięk zegara" jest widoczna tylko wtedy, gdy opcja
      "Wyłączone" z listy Interwał nie została zaznaczona. Spośród
      dostępnych dźwięków zegara można wybrać ten, który będzie odtwarzany
      gdy automatyczne ogłaszanie czasu jest włączone i ustawione na
      używanie dźwięku;
    * Pole wyboru "Ciche godziny" jest widoczne tylko wtedy, gdy opcja
      "Wyłączone" z listy Interwał nie została wybrana. Tu ustawia się
      liczbę godzin, w ciągu których ma być używane automatyczne ogłaszanie
      czasu;
    * Pole wyboru "Wejście w formacie 24-godzinnym" jest widoczne tylko
      wtedy, gdy Ciche godziny są włączone. Można tu określić, czy czas dla
      Cichych godzin ma być wyświetlany w formacie 12-godzinnym (A.M. lub
      P.M.), czy w europejskim formacie 24-godzinnym;
    * Pola edycji Początek i Koniec służą do wprowadzania czasu trwania
      Cichych godzin. Czas należy wpisywać w formacie HH:MM, jeśli pole
      wyboru "Wejście w formacie 24-godzinnym" jest zaznaczone. W przeciwnym
      razie, trzeba użyć formatu 12 godzinnego opisanego poniżej;
    * Po wprowadzeniu zmian przejdź klawiszem Tab do przycisku OK i
      uaktywnij go wciskając Enter. Zmiany ustawień zostaną zapisane;
    * Pierwsza lista rozwijana w oknie ustawiania alarmu umożliwia wybranie
      preferowanego odwrotnego odliczania do dźwięku alarmu;
    * Pole edycji służy do wprowadzania czasu oczekiwania na dźwięk
      alarmu. Czas musi być podawany za pomocą 1 lub kilku cyfr, bez części
      dziesiętnych;
    * Lista rozwijana "Dźwięk alarmu" pozwala wybrać dźwięki, które będą
      odtwarzane gdy nadejdzie czas alarmu;
    * Przycisk Pauza wstrzymuje/wznawia zbyt długie alarmy;
    * Przycisk Stop zatrzymuje zbyt długie alarmy;
    * Po wprowadzeniu zmian przejdź klawiszem Tab do przycisku OK i
      uaktywnij go wciskając Enter. Powinien pojawić się komunikat
      przypominający o czasie oczekiwania na alarm;

* NVDA+F12 naciśnięte raz odczytuje aktualną godzinę, 2 razy bieżącą datę,
  naciśnięte 3 razy dzień tygodnia, numer tygodnia, a także liczbę dni
  pozostałych do końca bieżącego roku.

## Skróty klawiszowe

* NVDA+F12, Sprawdź aktualny czas;
* NVDA+F12 naciśnięte szybko dwa razy, Sprawdź aktualną datę;
* NVDA+F12 naciśnięte szybko 3 razy, odczytuje aktualny dzień, numer
  tygodnia, bieżący rok oraz liczbę dni pozostałych do końca roku.
* Jest to skrót klawiszowy, który oznajmia ile czasu już upłynęło i ile
  pozostało do następnego alarmu;
* Żadne polecenie klawiszowe nie jest przypisane do tego skrótu. Trzeba
  przypisać je samodzielnie w oknie dialogowym "Zdarzenia wejścia" w
  kategorii "Zegar";
* Ten skrót naciśnięty szybko dwa razy anuluje następny alarm;
* Kolejny skrót klawiszowy zatrzymuje aktualnie odtwarzany dźwięk. On
  również nie ma przypisanego polecenia;
* Można też wywołać ten skrót przy pomocy poleceń warstwowych zegara
  opisanych poniżej.

## Polecenia warstwowe

Aby użyć poleceń warstwowych, naciśnij NVDA+Shift+F12, a potem któryś z
następujących klawiszy:

* S: włącza, resetuje lub zatrzymuje stoper;
* R: zeruje stoper nie resetując go;
* A: Podaje ile czasu upłynęło i pozostało do następnego alarmu;
* C: anuluje następny alarm;
* Spacja: odczytuje aktualny czas stopera lub odliczania wstecz;
* p: zatrzymuje zbyt długi alarm;
* H: Wyświetl listę poleceń warstwowych (Pomoc).

## Składnia do wpisywania Cichych godzin

* Ciche godziny muszą być wpisywane precyzyjną składnią, w celu uniknięcia
  błędów;
* Jeśli zaznaczysz pole wyboru "Wejście w formacie 24-godzinnym" Ciche
  godziny muszą być wpisane w formacie "HH:MM";
* Jeśli odznaczysz pole wyboru "Wejście w formacie 24-godzinnym" Ciche
  godziny muszą być wpisane w formacie "HH:MM AM" lub "HH:MM PM". HH musi
  zawierać format 12-godzinny od 0 do 12 oraz przyrostek "AM"|"PM" może być
  wpisane małą lub wielką literą
* Gdy zaznaczysz pole wyboru Ciche godziny" ale zostawisz pole edycji
  "Początek Cichych godzin" lub "Koniec cichych godzin" puste albo z błędną
  wartością, pole wyboru "Ciche godziny" zostanie automatycznie odznaczone w
  celu uniknięcia błędów;
* Powinien pojawić się komunikat zgłaszający Twój błąd.

## Zgodność

* Ten dodatek jest zgodny z wersjami NVDA od 2014.3 do 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

