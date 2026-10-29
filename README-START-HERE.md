# GitHub Projects – starter kit dla IO i Cyberiady

Pakiet jest **dodatkiem do istniejącego repozytorium Unity**. Nie zawiera i nie nadpisuje projektu gry (`Assets`, `Packages`, `ProjectSettings`, `.gitignore` itp.).

## Co dostajesz
- 4 szablony tworzenia GitHub Issues i szablon Pull Request.
- 15 propozycji pierwszych zadań (CSV) z rozróżnieniem `io` / `io-deliverable` / produkcja gry.
- Dokumentację planu oceny na IO, prowadzenia godzin i zakresu prac trzech studentów.
- Opcjonalny skrypt Python oparty na oficjalnym `gh`, który tworzy **nowy** GitHub Project, etykiety, pola i (na życzenie) Issues.

## Uruchomienie w 5 krokach
1. Rozpakuj ZIP. **Skopiuj zawartość folderu**, a nie folder nadrzędny, do katalogu głównego istniejącego repozytorium Unity. Nie nadpisuj istniejących plików bez ich obejrzenia.
2. Zacommituj `.github/` i `docs/` (oraz katalog `project-template/` i `scripts/`, jeśli chcecie trzymać je w repo).
3. W `Settings → General → Features` upewnij się, że **Issues** są włączone.
4. Utwórz projekt GitHub Projects, jego pola, etykiety i pierwsze Issues ręcznie, posiłkując się `project-template/PROJECT-SETUP.md`, **lub** uruchom skrypt poniżej.
5. W GitHub Projects dodaj cztery **zapisane widoki** ręcznie zgodnie z `PROJECT-SETUP.md` i sprawdź, czy obszar IO jest dobrze filtrowany.

### Wariant automatyczny (opcjonalnie)
Potrzebujesz Pythona 3.10+ i [GitHub CLI (`gh`)](https://cli.github.com/). Nie musisz podawać żadnego tokenu w plikach.

```bash
gh auth login
gh auth refresh -s project
python scripts/setup_github.py --repo OWNER/REPO --project-owner OWNER
```
Powyższe polecenie jest **podglądem**. Nic nie zapisuje na GitHubie. Gdy sprawdzisz ustawienia:

```bash
python scripts/setup_github.py --repo OWNER/REPO --project-owner OWNER --apply --seed-issues
```
Skrypt tworzy **nowy** GitHub Project; uruchom go jednokrotnie dla konkretnego repo. Jeśli masz już Project, przekaż `--project-number NUMER`, aby użył go zamiast zakładać kolejny.

**Uwaga:** skrypt nie tworzy automatycznie widoków (brak prostego odpowiednika `gh project view-create`). Ustaw je w interfejsie GitHub według instrukcji. Nie ustawia też personalnych przypisań ani estymat w godzinach: to świadome decyzje Waszej trójki.

## Najważniejsze daty IO
- **06.11.2026, 23:00** – Obszar 1, dwa zadania PZE, łącznie 20 punktów.
- **30.11–04.12.2026** – Obszar 2, harmonogramowanie i rozliczanie czasu.
- **18–22.01.2027** – Obszary 3–5: architektura/testy, użyteczność, element wyróżniający.

## Zasada kluczowa
`io` oznacza pracę zaliczaną do IO wykonywaną przez **Alicję, Miłosza lub Sebastiana**; `io-deliverable` oznacza materiały oddawane na PZE. Jedno zadanie może być zarówno zadaniem produkcyjnym gry, jak i częścią IO. Nie powielajcie Issues.

W całym repo i komunikacji o zaliczeniu używajcie konsekwentnego identyfikatora, np. `[IO NAZWA_KODOWA_GRY]`, zgodnego z wymaganiami prowadzącego.

## Dostępy
PZE wymaga dostępu odczytu do zasobów. **Prywatnego** GitHub Projects i repozytorium nie można przeglądać anonimowo na podstawie samego linku. Przed oddaniem uzgodnijcie z prowadzącym dostęp przez konto GitHub lub zaakceptowaną formę eksportu. Nie publikujcie kodu ani materiałów członków zespołu tylko po to, by dostarczyć link.
