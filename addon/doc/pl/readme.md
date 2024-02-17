# Clock and calendar Add-on for NVDA #

* Authors: Hrvoje Katić, Abdel and NVDA contributors
* Pobierz [wersja stabilna][1]

* Zgodność z NVDA: 2019.3 i nowsze

Ten dodatek umożliwia zaawansowane funkcje zegara, timera alarmowego i
kalendarza dla NVDA.

NvDA można skonfigurować tak, aby ogłaszała godzinę i datę w formatach
innych niż domyślnie dostępne w systemie Windows. Dodatkowo można uzyskać
bieżący dzień, numer tygodnia, a także pozostałe dni przed końcem bieżącego
roku, a także ustawić automatyczne ogłaszanie czasu w określonym
interwale. W dodatku wbudowane są również funkcje stopera i timera alarmów,
które pozwalają zaplanować zadania, takie jak kopiowanie plików,
instalowanie programów lub gotowanie posiłków.

Uwagi:

* jeśli zainstalujesz dodatek jako aktualizację, podczas procesu instalacji
  kreator wykryje, czy stara konfiguracja jest zgodna z nową i zaoferuje jej
  poprawienie przed instalacją, musisz tylko sprawdzić poprawność przycisku
  OK, aby to potwierdzić.
* W systemie Windows 10 lub nowszym możesz używać aplikacji Alarmy i zegar
  do zarządzania stoperami i timerami.

## Skróty klawiszowe

* NVDA+F12: pobierz aktualny czas
* NVDA+F12 dwukrotnie szybko wciśnięty: pobierz bieżącą datę
* NVDA+F12 naciskana trzy razy szybko: raportuje bieżący dzień, numer
  tygodnia, bieżący rok i pozostałe dni przed końcem roku
* NVDA+Shift+F12: wejdź w warstwę zegara

## Nieprzypisane polecenia

Następujące polecenia nie są domyślnie przypisywane; Jeśli chcesz je
przypisać, użyj okna dialogowego Gesty wprowadzania, aby dodać
niestandardowe polecenia. Aby to zrobić, otwórz menu NVDA, Preferencje, a
następnie Gesty wprowadzania. Rozwiń kategorię Zegar, a następnie znajdź
nieprzypisane polecenia z poniższej listy i wybierz "Dodaj", a następnie
wprowadź gest, którego chcesz użyć.

* Upłynął i pozostały czas przed kolejnym alarmem. dwukrotne naciśnięcie
  tego gestu spowoduje anulowanie następnego alarmu.
* Zatrzymaj aktualnie odtwarzanie dźwięku alarmu.
* Wyświetl okno dialogowe Zaplanuj alarmy.

## Polecenia warstwowe

Aby używać poleceń warstwowych, naciśnij NVDA+Shift+F12, a następnie 1 z
poniższych klawiszy:

* S: Uruchamia, resetuje lub zatrzymuje stoper
* R: Resetuje stoper do 0 bez ponownego uruchamiania
* Odp .: podaje czas, który upłynął i pozostały do następnego alarmu
* T: otwiera okno dialogowe zaplanuj alarmy.
* C: Anuluj następny alarm
* Spacja: Wypowiada bieżący stoper lub minutnik
* p: Jeśli alarm jest zbyt długi, pozwala go zatrzymać
* H: Lista wszystkich poleceń warstwowych (Pomoc)

## Konfiguracja i użytkowanie

Aby skonfigurować funkcjonalność zegara, otwórz menu NvDA, Preferencje, a
następnie Ustawienia i skonfiguruj następujące opcje z panelu Zegar:

* Format wyświetlania godziny i daty: użyj tych pól kombi, aby skonfigurować
  sposób, w jaki NVDA będzie ogłaszać godzinę i datę po naciśnięciu NVDA +
  F12 odpowiednio raz lub dwa razy.
* Interwał: wybierz interwał ogłaszania czasu z tego pola kombi (wyłączone,
  co 10 minut, 15 minut, 30 minut lub co godzinę).
* Zapowiedź czasu (włączona, jeśli interwał nie jest wyłączony): wybierz
  między mową a dźwiękiem, tylko dźwiękiem lub tylko mową.
* Dźwięk dzwonka zegara (włączony, jeśli interwał nie jest wyłączony):
  wybierz dźwięk dzwonka zegara.
* Godziny ciszy (włączone, jeśli interwał nie jest wyłączony): zaznacz to
  pole wyboru, aby skonfigurować zakres godzin ciszy, w których automatyczne
  ogłaszanie czasu nie powinno mieć miejsca.
* Format czasu ciszy w godzinach pracy (włączony, jeśli włączone są godziny
  ciszy): wybierz sposób wyświetlania opcji godzin ciszy (format 12-godzinny
  lub 24-godzinny).
* Godziny ciszy rozpoczynają i kończą: wybierz zakres godzin i minut dla pól
  kombi godziny i minut ciszy z godzin i minut.

Aby zaplanować alarmy, otwórz menu NVDA, Narzędzia, a następnie wybierz
Zaplanuj alarmy. Zawartość okna dialogowego obejmuje:

* Czas trwania alarmu w: wybierz czas trwania alarmu/timera między
  godzinami, minutami i sekundami.
* Czas trwania: wprowadź czas trwania alarmu w urządzeniu określonym
  powyżej.
* Dźwięk alarmu: wybierz dźwięk alarmu, który ma być odtwarzany.
* Przyciski zatrzymania i wstrzymania: zatrzymaj lub wstrzymaj długi dźwięk
  alarmu.

Kliknij przycisk OK, a pojawi się komunikat informujący o wybranym czasie
trwania alarmu.

[[!tag stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=clock
