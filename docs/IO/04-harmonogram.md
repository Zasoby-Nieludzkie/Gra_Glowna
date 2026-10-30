# Harmonogram projektu – IO 2026/2027 i Cyberiada

## Terminy

| Data | Wydarzenie | Rezultat |
|---|---|---|
| **6.11.2026, 23:00** | IO – Obszar 1 | Dobór technologii i narzędzi, środowisko pracy, eksport GitHub Projects oraz prezentacja analityczna |
| **30.11–4.12.2026** | IO – Obszar 2 | Aktualny harmonogram, zadania z wykonawcami, estymaty i rzeczywisty czas pracy, raport z odchyleń |
| **18–22.01.2027** | IO – Obszary 3–5 | Grywalny fragment gry, architektura i testy, pięciominutowy film, demonstracja wyróżniającej mechaniki |
| **8.06.2027** | Cyberiada | Koniec grywalizacji konkursowej |
| **15.06.2027** | Cyberiada | Przekazanie materiałów finałowych, w tym grywalnego buildu |
| **10.07.2027** | Cyberiada | Gala finałowa |

## Etapy pracy

| Okres | Etap | Plan prac | Co powinno działać na koniec |
|---|---|---|---|
| **30.10–6.11** | IO – przygotowanie projektu | Wybór technologii, konfiguracja repozytorium i GitHub Projects, testy współpracy, harmonogram i prezentacja. | Gotowe materiały Obszaru 1. **Nie rozpoczynamy jeszcze implementacji gry.** |
| **9–22.11** | M0 – fundament techniczny | Ustalenie zakresu pierwszej sceny, podstawowa struktura projektu, kamera 3/4, ruch postaci, kontrakt systemu rzeczywistości. | Prosta scena testowa z ruchem i zmianą rzeczywistości. |
| **23.11–4.12** | M0/M1 – pierwsza integracja + IO | Interakcje z obiektami, podstawy przedmiotów i walizki, pierwszy wspólny build; aktualizacja planu i raport godzin na IO. | Krótka sekwencja interakcji, poprawne przechodzenie przez proces budowania i testowania gry. |
| **7–20.12** | M1 – mechaniki gry | Przełączanie Czyśćca/Nieba/Piekła, zachowanie stanów przedmiotów, walizka z rozmieszczaniem i obrotem przedmiotów, podstawowy interfejs. | Mechaniki da się sprawdzić razem w jednym pomieszczeniu, nie tylko osobno. |
| **21.12–3.01** | Integracja i bufor | Łączenie komponentów, testy, poprawki i ograniczenie zakresu, jeśli pojawią się opóźnienia. | Stabilny punkt wyjścia do przygotowania styczniowego fragmentu. |
| **4–17.01** | M1/M2 – wersja na IO | Jedna krótka sytuacja wykorzystująca kilka głównych mechanik; podstawowe UI, czytelne informacje zwrotne, testy automatyczne i rozgrywkowe. | **5–10 minut grywalnego fragmentu** pokazującego kierunek projektu. Nie jest to pełna gra. |
| **18–22.01** | IO – prezentacja wyników | Testy, diagram i opis architektury, raport błędów, pięciominutowe wideo oraz demonstracja mechaniki „wow!”. | Build i komplet materiałów do Obszarów 3–5 na PZE. |
| **25.01–28.02** | Rozbudowa po IO | Rozszerzanie zawartości i systemów na podstawie wyników testów styczniowej wersji. | Spójny plan kolejnych poziomów i rozbudowany grywalny fragment. |
| **1.03–30.04** | Produkcja i testowanie | Kolejne sytuacje, poziomy, dialogi, przeciwnicy i zawartość wizualna; integracja oraz testy. W tym czasie odbywają się wyprawy edukacyjne Cyberiady. | Coraz pełniejsza wersja gry. |
| **1.05–7.06** | Stabilizacja wersji konkursowej | Kończenie zaplanowanej zawartości, optymalizacja, testy zewnętrzne, naprawa błędów i przygotowanie materiałów. | Kandydat do wersji finałowej. |
| **8–15.06** | Oddanie na Cyberiadę | Zamknięcie grywalizacji, weryfikacja buildu i przekazanie wymaganych materiałów do 15 czerwca. | Materiały finałowe przekazane organizatorowi. |

## Zakres grywalnej wersji na styczeń

Na zaliczenie IO przygotowujemy **krótki, działający fragment**, a nie pełną grę. Powinien pokazać:

- sterowanie postacią i kamerę 3/4;
- zmianę pomiędzy trzema rzeczywistościami w jednej przestrzeni;
- interakcję z przynajmniej kilkoma przedmiotami;
- walizkę z ograniczoną przestrzenią, układaniem i obrotem przedmiotów;
- zachowanie stanu przedmiotu po podniesieniu oraz jego reakcję na upuszczenie w innej rzeczywistości;
- jedną prostą sytuację do rozwiązania z wykorzystaniem tych reguł;
- podstawowy interfejs, informację zwrotną i możliwość przetestowania mechanik bez odgrywania całej gry.

**Kandydat na element „wow!”:** zastosowanie walizki do przeniesienia przedmiotu w zachowanym stanie pomiędzy rzeczywistościami, tak aby rozwiązać problem w świecie gry.

**Poza zakresem stycznia:** cała fabuła, wszystkie poziomy, pełna oprawa, wszystkie dialogi i przeciwnicy, kompletne nagrania głosowe oraz dopracowanie wszystkich mechanik. Rozbudowa tych elementów należy do późniejszej produkcji.

## Ewidencja czasu i aktualizacja planu

- Każde zadanie wykonawcze otrzyma wykonawcę, termin i estymatę godzin w GitHub Projects.
- Po pracy wpisujemy rzeczywisty czas w `Actual hours`. W komentarzach do Issues zapisujemy datę, osobę, liczbę godzin i krótki opis wykonanych czynności.
- Zadania wielodniowe rozbijamy na mniejsze, możliwe do sprawdzenia etapy. Raport na grudzień pokaże różnice pomiędzy estymatą a wykonaniem.
- Harmonogram aktualizujemy, gdy zmienia się zakres lub terminy. Szczegółowe estymaty zadań programistycznych uzupełnimy przed rozpoczęciem ich realizacji po 6 listopada.

[GitHub Project #2](https://github.com/orgs/Zasoby-Nieludzkie/projects/2) · [Zadania IO](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues?q=label%3Aio)
