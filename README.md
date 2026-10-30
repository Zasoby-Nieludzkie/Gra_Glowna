# One Hell of an Afterlife

Projekt zespołu **Zasoby Nieludzkie**, rozwijany na Cyberiadę 2026/2027 i w ramach przedmiotu **Inżynieria Oprogramowania**.

Do **6 listopada 2026** pracujemy nad pierwszym zaliczeniem IO. Materiały, zadania i instrukcje znajdują się poniżej.

## Gdzie co znaleźć?

| Miejsce | Do czego służy |
|---|---|
| [GitHub Project – Game Production – IO + Cyberiada](https://github.com/orgs/Zasoby-Nieludzkie/projects/2) | Tablica zadań, terminy, statusy, estymaty i godziny |
| [Issues dotyczące IO](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues?q=label%3Aio) | Konkretne zadania na zaliczenie |
| [Issue #1 – Efekt 1](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/1) | Technologie, narzędzia, harmonogram i przygotowanie eksportu |
| [Issue #2 – Efekt 2](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/2) | Analiza tematu i prezentacja |
| [Notatki i źródła do Efektu 2](docs/IO/01-efekt2-materialy.md) | Fabuła, mechaniki, porównanie gier, kwestie społeczne, prawne i organizacyjne |
| [Harmonogram](docs/IO/04-harmonogram.md) | Etapy do styczniowego zaliczenia IO i do Cyberiady |
| [Informacje o IO](docs/IO/README.md) | Terminy, podział pracy i sposób oddawania |
| [Projekt Unity](OneHellOfAnAfterlife/) | Pliki silnika, sceny, ustawienia i assety |

## IO – co robimy do 6 listopada?

**Termin obu zadań: piątek 6.11.2026, godz. 23:00.**

### Efekt 1 – dobór technologii i narzędzi

[Zadanie PZE](https://platforma.polsl.pl/rms/mod/assign/view.php?id=81404) · [Issue #1](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/1)

Do oddania: eksport zapisów z systemu zarządzania pracą, linki do zasobów oraz informacje o środowisku i wybranych narzędziach.

### Efekt 2 – analiza tematu projektu

[Zadanie PZE](https://platforma.polsl.pl/rms/mod/assign/view.php?id=81405) · [Issue #2](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/2)

Prezentację multimedialna: potrzebne informacje w [notatkach do Efektu 2](docs/IO/01-efekt2-materialy.md).

Pozostałe zadania do prezentacji: [#6 – porównanie gier](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/6) i [#7 – uwarunkowania projektu](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/7).

## Jak korzystać z Issues?

1. Wejdź w zakładkę **Issues** na górze repozytorium.
2. Wyszukaj numer zadania albo otwórz [listę zadań IO](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues?q=label%3Aio).
3. Kliknij tytuł zadania. Opis zawiera zakres i linki do materiałów; kratki `- [ ]` można odznaczać po wykonaniu odpowiedniej czynności.
4. Po prawej stronie w **Assignees** wybierz osobę odpowiedzialną. Jeśli nie możesz jej wybrać, osoba może potrzebować dostępu do repozytorium.
5. W komentarzu można podać wykonane czynności, dołączyć link do pliku lub Pull Request.
6. Gdy zadanie jest zakończone, kliknij **Close issue**. Zostaw otwarte zadania, nad którymi jeszcze pracujesz.

Zadania **#10–#15** dotyczą późniejszego tworzenia gry, nie obecnego zaliczenia.

## Jak korzystać z GitHub Projects?

1. Otwórz [GitHub Project #2](https://github.com/orgs/Zasoby-Nieludzkie/projects/2).
2. Przełącz widok na **Table** (tabela). W razie potrzeby utwórz nowy widok przez **New view → Table**.
3. Ustaw filtr `label:io`, aby zobaczyć zadania na IO.
4. Kliknij wiersz zadania albo jego tytuł, żeby otworzyć szczegóły.
5. Uzupełniaj pola: **Status**, **Priority**, **Target date**, **Estimated hours** i **Actual hours**. Wykonawcę ustaw w polu **Assignees** zgłoszenia.
6. **Estimated hours** to przewidywany czas zadania, a **Actual hours** to czas rzeczywiście przepracowany. Nie wpisujemy zmyślonych godzin.
7. Po zakończeniu pracy zmień **Status** na **Done**. Jeśli zadanie jest skończone całkowicie, zamknij również Issue.

Jeśli nie widać pola w tabeli, otwórz menu kolumn **Fields**, aby pokazać potrzebne kolumny.

### Zapis czasu pracy

Do zadania dodaj komentarz, np.:

```text
2026-11-02 – MP – 2 h
Porównanie gier referencyjnych i zebranie źródeł.
```

Następnie zaktualizuj łączną liczbę godzin w **Actual hours**. Przy pracy kilku osób każda zapisuje własny czas. Szczegóły: [ewidencja czasu](docs/IO/02-time-tracking.md).

## Gdzie umieścić prezentację?

W repozytorium otwórz folder [`docs/IO`](docs/IO/).

1. Kliknij **Add file → Upload files**.
2. Przeciągnij gotową prezentację, np. `IO_Efekt2_2026.pptx`.
3. Wpisz krótką wiadomość commita, np. `Dodanie prezentacji Efekt 2`.
4. Kliknij **Commit changes** (lub wybierz propozycję zmian na nowej gałęzi, jeśli nie masz prawa zapisu do `main`).
5. Skopiuj adres pliku z GitHuba i wklej go do [Issue #2](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/2).

Plik w repozytorium **nie zastępuje oddania na PZE**: gotową prezentację trzeba jeszcze przesłać w [zadaniu Efektu 2](https://platforma.polsl.pl/rms/mod/assign/view.php?id=81405).

## Jak wyeksportować zadania na IO?

1. Otwórz [GitHub Project #2](https://github.com/orgs/Zasoby-Nieludzkie/projects/2).
2. W widoku tabeli ustaw filtr `label:io`.
3. Pokaż kolumny wykonawców, terminów, statusów oraz godzin.
4. W menu widoku wybierz **Export view data**. GitHub pobierze plik TSV.
5. Otwórz go i sprawdź zawartość przed oddaniem. Gotowy eksport można dołączyć do materiałów Efektu 1.
6. Sprawdź też, czy sam **Project #2** jest widoczny dla prowadzących. Widoczność repozytorium i Projects ustawia się osobno.

Eksport i linki zbieramy w [Issue #9](https://github.com/Zasoby-Nieludzkie/Gra_Glowna/issues/9).

## Jak otworzyć projekt Unity?

1. Sklonuj repozytorium przez **Code → HTTPS**, GitHub Desktop albo `git clone`.
2. Otwórz **Unity Hub → Add project from disk**.
3. Wybierz folder **`OneHellOfAnAfterlife`** (a nie główny folder repozytorium).
4. Użyj wersji edytora zapisanej w [`ProjectVersion.txt`](OneHellOfAnAfterlife/ProjectSettings/ProjectVersion.txt): **Unity 6000.6.7f1**.

Docelowo gra wykorzystuje **HDRP**. Prace nad rozgrywką rozpoczniemy po pierwszym zaliczeniu IO.

## Kolejne terminy

| Termin | Cel |
|---|---|
| **6 listopada 2026** | Dwa zadania Obszaru 1 |
| **30 listopada – 4 grudnia 2026** | Harmonogram i ewidencja czasu, Obszar 2 |
| **18–22 stycznia 2027** | Grywalny fragment gry i materiały Obszarów 3–5 |
| **15 czerwca 2027** | Materiały finałowe na Cyberiadę |

Pełny plan: [docs/IO/04-harmonogram.md](docs/IO/04-harmonogram.md).
