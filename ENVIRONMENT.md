Dokumentacja konfiguracji środowiska
Sekrety (Secrets)
W repozytorium GitHub zostały skonfigurowane następujące sekrety:

RENDER_API_KEY

Klucz API do autoryzacji wywołań do Render API (np. do triggerowania deployów i rollbacków).

Dodany w Settings > Secrets and variables > Actions repozytorium.

Zmienne środowiskowe (Environment Variables)
W panelu Render, w konfiguracji serwisu, ustawiono następujące zmienne środowiskowe:

DEBUG

Przykładowa zmienna typu boolean lub string (np. True lub False) decydująca o trybie debugowania aplikacji.

Ustawiana przez panel Render.

ENV

Zmienna opisująca środowisko (np. production, staging).

Ustawiana przez panel Render.

Inne ustawienia
Aplikacja odczytuje zmienne środowiskowe za pomocą os.environ (np. w Pythonie).

Sekrety i zmienne środowiskowe nie są commitowane do repozytorium dla bezpieczeństwa.

Aby zmodyfikować lub dodać nowe sekrety, należy wejść w ustawienia repozytorium na GitHubie.

Aby zmienić zmienne środowiskowe, należy zalogować się do dashboardu Render i edytować odpowiednią aplikację.