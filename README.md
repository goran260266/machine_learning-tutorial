# langchain-project

## 1. Projekt erstellen (PowerShell)

### 1.1 Verzeichnis anlegen und hineinwechseln

```powershell
mkdir C:\Artificial Intelligence\machine_learning-tutorial
cd C:\Artificial Intelligence\machine_learning-tutorial
```

### 1.2 Projektverzeichnis bereinigen und initialisieren

Löschen Sie alte Restdateien, um Konflikte zu vermeiden, und initialisieren Sie die Library-Struktur:

```bash
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .venv, src, tests, pyproject.toml, uv.lock, README.md, .python-version
uv init --lib
```

### 1.3 Testverzeichnis anlegen

Erstellen Sie manuell den Ordner für Unit-Tests und eine erste leere Testdatei:

```bash
New-Item -ItemType Directory -Path "tests"
New-Item -ItemType File -Path "tests\test_ml.py"
```

### 1.4 Abhängigkeiten hinzufügen

```bash
uv add langchain langchain-openai langchain-community langchain-openrouter python-dotenv
```

### 1.5 Dev-Abhängigkeiten hinzufügen

```bash
uv add --dev pytest ipykernel
```

## 2. Verwendung

### 2.1 uv installieren (einmalig, z. B. auf einem anderen Rechner)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2.2 Projekt klonen und ausführen

```powershell
git clone <URL-des-GitHub-Repos>
cd machine_learning-tutorial

# Umgebung aus pyproject.toml/uv.lock herstellen
uv sync

# Tests ausführen
uv run pytest
```

### 2.3 VS-Code-Extensions übernehmen

Die empfohlenen Extensions stehen in `.vscode/extensions.json` und werden mit dem Repository versioniert. Nach dem `git clone` und dem Öffnen des Ordners in VS Code erscheint ein Hinweis, diese Extensions zu installieren.

Alternativ per Terminal installieren:

```powershell
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.debugpy
code --install-extension ms-python.vscode-python-envs
code --install-extension charliermarsh.ruff
code --install-extension ms-toolsai.jupyter
code --install-extension tamasfe.even-better-toml
code --install-extension ms-vscode.powershell
code --install-extension davidanson.vscode-markdownlint
```

Alle Extensions des eigenen Rechners (unabhängig vom Projekt) lassen sich mit `Settings Sync` (`Ctrl+Shift+P`, dann `Settings Sync: Turn On`) oder per Export übertragen:

```powershell
# Auf dem alten Rechner exportieren
code --list-extensions > extensions.txt

# Auf dem neuen Rechner installieren
Get-Content extensions.txt | ForEach-Object { code --install-extension $_ }
```

## 3. Funktionstest

Sie können überprüfen, ob das Projekt korrekt importiert werden kann und die virtuelle Umgebung aktiv ist, indem Sie die Standardfunktion `hello()` aus dem Terminal heraus aufrufen:

```bash
uv run python -c "import machine_learning_tutorial; print(machine_learning_tutorial.hello())"
```

**Erwartete Ausgabe:**

```text
Hello from machine_learning-tutorial!
```

## 4. Codeprüfungen

Ruff prüft den Python-Code auf Stil- und Fehlerregeln, einschließlich ungenutzter Imports.
Mypy prüft statisch, ob die Typen im Code zu den Annotationen und Verwendungen passen.

```powershell
# Lint- und Fehlerregeln prüfen
uv run ruff check .

# Automatisch korrigierbare Befunde beheben
uv run ruff check --fix .

# Typen im Python-Paket prüfen
uv run mypy src/langchain_project
```

### 4.1 Testabdeckung (Coverage) messen

Um zu sehen, wie viel Prozent Ihres Codes durch Tests abgedeckt sind, fügen Sie das Tool hinzu und starten den Report:

```bash
uv add --dev pytest-cov
uv run pytest --cov=machine_learning_tutorial --cov-report=term-missing
```

## 5. Aufräumen & Git-Vorbereitung

Sollten durch das Coverage-Tool oder Ihre IDE temporäre Dateien (wie `coverage.json`) erzeugt werden, können Sie diese löschen und eine `.gitignore`-Datei anlegen, damit temporäre Python-Dateien und Umgebungsvariablen nicht im Projekt stören:

```bash
# Temporäre JSON-Berichte löschen
Remove-Item "coverage.json" -ErrorAction SilentlyContinue
```

API-Schlüssel in einer `.env`-Datei im Projektverzeichnis ablegen:

## 6. Git-Repository initialisieren

### 6.1 `.gitignore` anlegen

Legen Sie die Datei `.gitignore` im Projektverzeichnis an, damit virtuelle Umgebung, Caches, Coverage-Berichte und die `.env`-Datei mit den API-Schlüsseln nicht versioniert werden:

```powershell
@"
# Virtuelle Umgebung
.venv/

# Python-Artefakte
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Test-, Lint- und Typ-Caches
.pytest_cache/
.ruff_cache/
.mypy_cache/

# Coverage-Berichte
.coverage
coverage.json
htmlcov/

# Umgebungsvariablen und Geheimnisse
.env
"@ | Set-Content -Encoding utf8 .gitignore
```

`uv.lock` und `.python-version` sollten dagegen versioniert werden, damit die Umgebung reproduzierbar bleibt.

### 6.2 Repository initialisieren und ersten Commit erstellen

```powershell
git init
git add .
git status
git commit -m "Initial commit"
```

Prüfen Sie mit `git status` vor dem Commit, dass `.venv/` und `.env` nicht in der Liste der hinzugefügten Dateien erscheinen.

