# Dodatek Zegar i kalendarz dla NVDA #

* Autorzy: Hrvoje Katić, Abdel i współtwórcy NVDA
* Zgodność z NVDA: 2019.3 i nowsze

Ten dodatek umożliwia zaawansowane funkcje zegara, timera alarmowego i kalendarza dla NVDA.

Możesz skonfigurować NVDA tak, aby ogłaszała godzinę i datę w formatach innych niż domyślne w systemie Windows. Dodatkowo możesz uzyskać bieżący dzień, numer tygodnia, a także liczbę dni pozostałych do końca roku oraz ustawić automatyczne ogłaszanie czasu w określonym interwale. Dodatek zawiera również wbudowane funkcje stopera i timera alarmów, które pozwalają mierzyć czas zadań, takich jak kopiowanie plików, instalowanie programów czy przygotowywanie posiłków.

Uwagi:

* jeśli instalujesz dodatek jako aktualizację, podczas procesu instalacji kreator wykrywa, czy poprzednia konfiguracja jest zgodna z nową i proponuje jej korektę przed instalacją, a następnie wystarczy potwierdzić przyciskiem OK.
* W systemie Windows 10 i nowszych możesz używać aplikacji Alarmy i zegar do zarządzania stoperami i timerami.

## Klawisze poleceń

* NVDA+F12: pobierz aktualny czas
* NVDA+F12 naciśnięte dwa razy szybko: pobierz bieżącą datę
* NVDA+F12 naciśnięte trzy razy szybko: raportuje bieżący dzień, numer tygodnia, bieżący rok oraz liczbę dni pozostałych do końca roku
* NVDA+Shift+F12: wejście w warstwę zegara

## Nieprzypisane polecenia

Następujące polecenia nie są domyślnie przypisane; jeśli chcesz je przypisać, użyj okna dialogowego Gesty wprowadzania, aby dodać własne polecenia. Aby to zrobić, otwórz menu NVDA, Preferencje, a następnie Gesty wprowadzania. Rozwiń kategorię Zegar, znajdź nieprzypisane polecenia z poniższej listy i wybierz „Dodaj”, a następnie wprowadź gest, którego chcesz użyć.

* Upłynął i pozostały czas przed następnym alarmem. Dwukrotne szybkie naciśnięcie tego gestu anuluje następny alarm.
* Zatrzymaj aktualnie odtwarzany dźwięk alarmu.
* Wyświetl okno dialogowe planowania alarmów.
* Pokaż polecenia warstwowe (klawisze do naciśnięcia po NVDA+Shift+F12).

## Polecenia warstwowe

Aby używać poleceń warstwowych, naciśnij NVDA+Shift+F12, a następnie jeden z poniższych klawiszy:

* S: uruchamia, resetuje lub zatrzymuje stoper
* R: resetuje stoper do 0 bez ponownego uruchamiania
* A: podaje czas, który upłynął i pozostały do następnego alarmu
* T: otwiera okno dialogowe planowania alarmów
* C: anuluje następny alarm
* Spacja: odczytuje aktualny stoper lub minutnik
* p: jeśli alarm jest zbyt długi, pozwala go zatrzymać
* H: lista wszystkich poleceń warstwowych (pomoc)

## Konfiguracja i użytkowanie

Aby skonfigurować funkcje zegara, otwórz menu NVDA, Preferencje, a następnie Ustawienia i skonfiguruj opcje w panelu Zegar:

* Format wyświetlania godziny i daty: użyj tych pól kombi, aby określić sposób ogłaszania godziny i daty po naciśnięciu NVDA+F12 raz lub dwa razy.
* Interwał: wybierz interwał ogłaszania czasu (wyłączony, co 10 minut, 15 minut, 30 minut lub co godzinę).
* Ogłaszanie czasu (aktywne, jeśli interwał nie jest wyłączony): wybierz między mową i dźwiękiem, tylko dźwiękiem lub tylko mową.
* Dźwięk dzwonka zegara (aktywne, jeśli interwał nie jest wyłączony): wybierz domyślny dźwięk dzwonka.
* Oddzielne dzwonki godzin i minut pośrednich (aktywne, jeśli interwał nie jest wyłączony, domyślnie wyłączone): zaznacz, aby dostosować dźwięki osobno.
  * Dźwięk minut pośrednich (aktywne, jeśli włączono oddzielne dzwonki): wybierz dźwięk dla minut pośrednich.
* Godziny ciszy (aktywne, jeśli interwał nie jest wyłączony): ustaw zakres godzin, w których automatyczne ogłaszanie czasu jest wyłączone.
* Format godzin ciszy (aktywne, jeśli godziny ciszy są włączone): wybierz format 12- lub 24-godzinny.
* Godziny rozpoczęcia i zakończenia ciszy: wybierz zakres godzin i minut.

Aby zaplanować alarmy, otwórz menu NVDA, Narzędzia, a następnie wybierz „Zaplanuj alarmy”. Okno dialogowe zawiera:

* Czas trwania alarmu w: wybierz godziny, minuty i sekundy
* Czas trwania: wpisz czas trwania alarmu
* Dźwięk alarmu: wybierz dźwięk alarmu
* Przyciski zatrzymania i pauzy: zatrzymaj lub wstrzymaj długi alarm

Kliknij OK, a pojawi się komunikat informujący o wybranym czasie trwania alarmu.
