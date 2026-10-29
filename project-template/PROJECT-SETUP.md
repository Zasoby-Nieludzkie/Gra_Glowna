# Konfiguracja GitHub Projects

**Nazwa:** `One Hell of an Afterlife – Production` (zmień, jeśli finalny tytuł jest inny)

**Opis:** `Wspólny backlog i harmonogram dziesięcioosobowej produkcji gry; wydzielona, indywidualnie rozliczana praca IO: Alicja Janeczko, Miłosz Pakura, Sebastian Biksa.`

## Pola

| Pole | Typ | Wartości / użycie |
|---|---|---|
| Status | wbudowane single select | Todo, In Progress, Done; opcjonalnie dodaj Ready i In Review przez UI |
| Priority | single select | P0, P1, P2, P3 |
| Workstream | single select | Engineering, Game Design, Art, Audio, QA, Documentation, Production |
| Estimated hours | number | **Estymata przed pracą**, bez dopisywania godzin z pamięci jako faktycznych |
| Actual hours | number | Suma faktycznych sesji wykonawców z komentarzy |
| Target date | date | Termin ukończenia zadania |
| Iteration | iteration | Dodaj ręcznie w UI; proponowana długość: 1 tydzień |

Pola `Assignees` i `Labels` istnieją po stronie GitHub Issues; w Projects pokazuj je jako kolumny.

## Etykiety repozytorium
- `io` – prace studentów rozliczane na IO (techniczne i dokumentacyjne).
- `io-deliverable` – oddania i dokumentacja do PZE; **również `io`**.
- `engineering`, `game-design`, `art`, `audio`, `qa`, `documentation`, `production`, `bug` – rodzaj pracy.

**Nie oznaczaj `io` całej pracy dziesięcioosobowego zespołu.** Jeśli w zadaniu uczestniczą osoby spoza IO, zapisuj ich wkład osobno, a do raportów IO filtruj rzeczywiste wpisy trójki studentów.

## Widoki (w GitHub Projects: `New view`, a następnie zapisz filtr)

| Nazwa | Układ | Filtr | Sens |
|---|---|---|---|
| `🎮 Game Development` | Board by Status | `-label:io-deliverable` | cała produkcja gry, bez oddań na PZE |
| `🎓 IO – Work & Hours` | Table | `label:io` | tylko prace zaliczane do IO, w tym kod i dokumentacja |
| `📄 IO – Deliverables` | Table | `label:io-deliverable` | wyłącznie materiały do PZE |
| `🗓 Roadmap` | Roadmap | brak | cała produkcja, od dziś do finału |

W `IO – Work & Hours` pokaż kolumny: Assignees, Status, Estimated hours, Actual hours, Target date, Priority. Zmień ustawienie `Sum` dla pól liczbowych, jeśli jest dostępne w danym widoku.

## Automatyzacja
- Włącz workflow automatycznego dodawania Issues z właściwego repozytorium do Projects (jeśli nie korzystasz ze skryptu do seedowania).
- Zdecyduj, czy PR po zmergowaniu zamyka Issue przez `Closes #numer`.
- Nie włączaj na starcie złożonych automatyzacji godzin i raportowania: najpierw wypracujcie stabilny zwyczaj rejestrowania sesji.

## Pierwsze oddanie IO

**Zadanie 1 – Dobór technologii i narzędzi (10 pkt, do 06.11.2026 23:00):** eksport z systemu zarządzania, wstępne testy i uzasadnienie technologii, linki do zasobów, miejsce danych offline (jeśli dotyczy).

**Zadanie 2 – Analiza tematyki i uwarunkowań (10 pkt, do 06.11.2026 23:00):** prezentacja multimedialna: koncepcja, uwarunkowania społeczne/prawne/organizacyjne, podobne gry, analiza źródeł.

Nie zakładamy, że Cyberiada zastępuje dokumentację IO: oba zestawy mają własne kryteria.
