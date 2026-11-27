# Roadmap: Expertenwissen für komplexe Lineare Regressions-Projekte

Um komplexe und praxistaugliche Machine-Learning-Projekte auf Basis von linearer Regression erfolgreich zu realisieren, müssen Sie die folgenden vier Kernbereiche beherrschen.

---

## 1. Datenvorbereitung & Pipeline-Architektur

Echte Datensätze sind selten sauber. Die fehlerfreie Aufbereitung ohne Informationsverlust ist das Fundament jedes Modells.

* **Umgang mit Datenlücken:** Sichere Anwendung von `SimpleImputer` (z. B. `median` bei Zahlen vs. `most_frequent` bei Text), um Systemabstürze durch fehlende Werte (`NaN`) zu verhindern.
* **Kategoriale Transformation:** Korrekter Einsatz von `OneHotEncoder` für nominale Daten ohne Reihenfolge (z. B. Städte, Farben) und `OrdinalEncoder` für logische Rangfolgen (z. B. Bildungsgrade, Kundenzufriedenheit).
* **Skalierungs-Strategien:** Auswahl des passenden Skalierers (`StandardScaler` als Standard, `MinMaxScaler` für feste Grenzen wie Bildpixel, `RobustScaler` bei extremen Ausreißern in den Daten).
* **Vermeidung von Data Leakage:** Striktes Kapseln aller Vorbereitungsschritte und des Modells in einer `Pipeline`, damit Testdaten niemals unbewusst das Training beeinflussen.

---

## 2. Regularisierung & Modellvarianten

Die Standard-Lineare-Regression scheitert oft an echtem Datenrauschen. Fortgeschrittene Varianten schützen das Modell vor Overfitting.

* **Ridge-Regression (L2):** Verstehen, wie Koeffizienten nahe an Null geschrumpft werden, um die Modellkomplexität bei verrauschten Daten stabil zu bremsen.
* **Lasso-Regression (L1):** Nutzen der automatischen Merkmalsauswahl (*Feature Selection*), bei der irrelevante Koeffizienten rigoros auf exakt `0` gesetzt und somit eliminiert werden.
* **ElasticNet-Regression:** Kombinieren von Ridge und Lasso, um das Problem zu lösen, dass Lasso bei stark korrelierten Variablen-Gruppen blind Daten löscht.
* **Hyperparameter-Tuning:** Systematisches Suchen nach der perfekten Kombination aus Bremsfaktor (`alpha`) und Linien-Verankerung (`fit_intercept`) mittels `GridSearchCV`.

---

## 3. Modell-Evaluierung & Validierung

Ein Modell ist nur so gut, wie seine Überprüfbarkeit auf ungesehenen Daten.

* **Kreuzvalidierung (Cross-Validation):** Daten mittels des `cv`-Parameters in mehrere Falten splitten, um eine ehrliche und stabile Generalisierungsfähigkeit des Modells zu berechnen.
* **Metriken-Kompetenz:** Sichere Interpretation und Unterscheidung von:
  * **R² (Bestimmtheitsmaß):** Wie viel Prozent der Datenvarianz kann das Modell erklären? (Skala 0 bis 1).
  * **MSE (Mean Squared Error):** Der mathematische, quadrierte Fehler für die Optimierung.
  * **RMSE (Root Mean Squared Error):** Der durchschnittliche Fehler in der echten Original-Einheit des Ziels (z. B. Abweichung in Euro, Metern oder Kilogramm).
* **Train-Test-Split:** Konsequente und saubere Trennung der Daten in Trainings- und Testsets vor jeglicher Optimierung, um Überanpassung aufzudecken.

---

## 4. Fortgeschrittene Konzepte (Komplexitäts-Erweiterung)

Komplexe reale Probleme erfordern mathematische Erweiterungen und den Schritt in die Produktion.

* **Nicht-lineare Zusammenhänge:** Einsatz von `PolynomialFeatures`, um Interaktionen und quadratische Beziehungen (x²) zu erzeugen. Dadurch lernt das lineare Modell hochflexible Kurven statt starrer Geraden.
* **Multikollinearität:** Erkennen und Entschärfen von Variablen, die stark voneinander abhängen (z. B. Wohnfläche in m² und Quadratfuß), da diese die mathematische Berechnung der Standard-Regression extrem instabil machen.
* **Modell-Deployment:** Speichern der gesamten trainierten Pipeline (inklusive Imputer, Scaler und Modell) mittels `joblib` oder `pickle`, um sie produktiv in Web-Anwendungen oder APIs für Live-Vorhersagen bereitzustellen.
