# Regularisierte Lineare Regression: Ridge, Lasso und ElasticNet

Sowohl **Ridge**, **Lasso** als auch **ElasticNet** sind echte lineare Regressionsmodelle. Sie nutzen dieselbe mathematische Grundgleichung:
y = b + a · x₁ + d · x₂ + ...

Der Unterschied zur Standard-Lineare-Regression liegt in der **eingebauten Bremse (Regularisierung)**, die verhindert, dass das Modell zufälliges Rauschen auswendig lernt (Overfitting).

---

## Die zentralen Hyperparameter

Mit `GridSearchCV` sucht man systematisch nach der besten Kombination dieser Stellschrauben:

* **`alpha` (Die Gesamtbremse):** Steuert, wie stark das Modell insgesamt für große Koeffizienten bestraft wird.
* **`fit_intercept` (Der Startpunkt):**
  * `True`: Der Achsenabschnitt (b) wird frei berechnet (Linie verschiebt sich).
  * `False`: Der Achsenabschnitt wird starr auf b = 0 gesetzt (Linie geht durch den Ursprung).
* **`l1_ratio` (Nur bei ElasticNet):** Bestimmt das Mischungsverhältnis zwischen Lasso und Ridge (Wert zwischen 0 und 1).

---

## Ridge, Lasso und ElasticNet im direkten Vergleich

| Eigenschaft | Ridge-Regression (`L2`) | Lasso-Regression (`L1`) | ElasticNet-Regression |
| :--- | :--- | :--- | :--- |
| **Effekt auf Koeffizienten** | Schrumpft Koeffizienten nahe an die Null, aber **nie exakt auf 0**. | Setzt unwichtige Koeffizienten **exakt auf 0**. | Kombiniert beide Effekte: Schrumpft und setzt auf 0. |
| **Merkmalsauswahl** | Behält alle Variablen im Modell (Formel bleibt lang). | Führt eine **automatische Merkmalsauswahl** durch. | Führt eine **intelligente Merkmalsauswahl** durch. |
| **Umgang mit korrelierten Daten** | Teilt das Gewicht gleichmäßig auf ähnliche Features auf. | Wählt zufällig *ein* Feature aus und setzt die anderen auf 0. | Behält **Gruppen** von ähnlichen Features gemeinsam im Modell. |
| **Bester Einsatzbereich** | Wenn fast alle Features wichtig sind. | Wenn viele komplett irrelevante Features im Datensatz sind. | Wenn viele Features miteinander korrelieren (Gruppen-Effekt). |

---

## Was macht ElasticNet besonders?

ElasticNet ist die **Kombination aus Ridge und Lasso**. Es löst ein großes Problem von Lasso: Wenn zwei Merkmale stark miteinander zusammenhängen (z. B. *Zimmeranzahl* und *Wohnfläche*), filtert Lasso oft blind eines davon heraus. ElasticNet hingegen merkt, dass sie als Gruppe wichtig sind, behält beide bei (Ridge-Eigenschaft) und wirft trotzdem den echten Müll heraus (Lasso-Eigenschaft).

Das Mischungsverhältnis wird über den Hyperparameter **`l1_ratio`** gesteuert:
* `l1_ratio = 1.0` → Das Modell verhält sich zu 100% wie **Lasso**.
* `l1_ratio = 0.0` → Das Modell verhält sich zu 100% wie **Ridge**.
* `l1_ratio = 0.5` → Das Modell mischt beide Strafen zu gleichen Teilen (50/50).

---

## Praxis-Beispiel für `GridSearchCV` mit ElasticNet

```python
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV

# Modell definieren
model = ElasticNet()

# Such-Gitter (param_grid) inklusive dem Mischungsverhältnis l1_ratio
param_grid = {
    'alpha': [0.01, 0.1, 1.0, 10.0],
    'l1_ratio': [0.2, 0.5, 0.7, 0.9],  # Testet verschiedene Mischungen
    'fit_intercept': [True, False]
}

# GridSearchCV findet automatisch die beste Kombination aus allen drei Welten
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
```
