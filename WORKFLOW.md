Workflow CI/CD
Repozytorium korzysta z GitHub Actions do automatyzacji procesu ciągłego wdrażania aplikacji. Workflow składa się z następujących etapów:

1. Build and Test
Uruchamiane przy pushu na branch main lub pull requestach.

Checkout kodu.

Instalacja Pythona (wersja 3.12).

Instalacja zależności z requirements.txt.

Uruchomienie testów jednostkowych za pomocą pytest w katalogu tests/.

Jeśli testy zakończą się pomyślnie, workflow przechodzi do kolejnego etapu.

2. Deploy na Render
Uruchamiany po udanym buildzie i testach na branchu main.

Checkout kodu.

Trigger deploymentu aplikacji na Render poprzez wywołanie API Render z użyciem sekretu RENDER_API_KEY.

Po wdrożeniu wykonywany jest health check endpointu /health.

Jeśli health check nie powiedzie się, deployment jest oznaczany jako nieudany i pipeline kończy się błędem.

3. Rollback (manualny)
Osobny workflow uruchamiany ręcznie z poziomu GitHub Actions.

Pozwala na wycofanie deploymentu do wskazanego commita poprzez wywołanie API Render z odpowiednim parametrem commitHash.

Umożliwia szybkie przywrócenie stabilnej wersji aplikacji w razie problemów.

Kluczowe elementy konfiguracji
Secrets: RENDER_API_KEY

Trigger: push na main, pull request, workflow_dispatch (dla manualnego uruchamiania rollback)

Health check: GET na /health endpoint

Automatyzacja wdrożeń: minimalizuje przestoje i ryzyko błędów w produkcji.