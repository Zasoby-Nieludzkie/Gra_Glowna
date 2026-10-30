# Ewidencja pracy – zasady dla IO

## Jak to robimy w GitHub
1. Przed wykonaniem zadania podaj `Estimated hours` w GitHub Projects. Estymata ma być rzeczywistym przewidywaniem, nie wartością dobraną do oceny.
2. Każdy wykonawca zapisuje sesje w komentarzach pod Issue, **regularnie, z dokładnością wymaganą na PZE (minimum jeden wpis na każde 3 h pracy)**.
3. Każdy wpis zawiera datę, wykonawcę, czas i wykonane czynności. Unikamy wielogodzinnych uogólnień typu „pracowałem nad grą”.
4. Pole `Actual hours` aktualizujemy jako **sumę godzin wszystkich wykonawców tego Issue**. Jeśli trzeba rozliczyć oddzielnie dwie osoby, każdy ma własne wpisy. Na raport IO uwzględniamy tylko AJ, MP i SB.
5. Każdy wpis ma powiązany artefakt, jeśli możliwy: PR, commit, plik dokumentacji, test, build, screen.
6. Podczas grudniowego raportu porównujemy estymaty i wykonanie i **opisujemy przyczyny rozbieżności**, nie tylko procent odchylenia.

## Szablon komentarza (kopiuj do Issue)

```md
**Work log (IO)**
- Data: RRRR-MM-DD
- Wykonawca: [imię i nazwisko]
- Czas: [np. 1.5 h]
- Wykonane: [konkretne działanie]
- Dowód: [link do PR, commita, dokumentu albo wyniku testu]
```

## Raport Obszaru 2 (30.11–04.12.2026)

| Zadanie/Issue | Wykonawca | Estymata (h) | Faktyczne (h) | Różnica | Dlaczego? | Dowód |
|---|---|---:|---:|---:|---|---|
| … | … | … | … | … | … | … |

**Ważne:** GitHub Projects przechowuje zagregowany czas; komentarze pozostają źródłem wpisów szczegółowych. Eksport widoku tabeli zwykle **nie zawiera automatycznie treści komentarzy**. Do raportu godzin potrzebne będzie dodatkowe zestawienie lub skrypt generujący raport z Issues i komentarzy. Nie obiecujcie na PZE pełnego time-tracking reportu z samego CSV Projects.
