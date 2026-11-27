# Machine Learning Konzepte und Anwendungsgebiete

**Supervised Learning** (überwachtes Lernen) findet in der Praxis mit Abstand die verbreitetste Anwendung.

## 1. Branchen und Anwendungsgebiete der ML-Konzepte

| ML-Konzept | Funktionsweise | Typische Branchen & Anwendungsfälle |
| :--- | :--- | :--- |
| **Supervised Learning** | Lernt aus gelabelten Daten (bekannte Ein- und Ausgaben) für Vorhersagen und Klassifikationen. | **Finanzwesen:** Kreditwürdigkeitsprüfung und Betrugserkennung.<br>**Medizin:** Diagnoseunterstützung anhand von Röntgenbildern.<br>**Industrie & Handel:** Qualitätskontrolle und Umsatzprognosen. |
| **Unsupervised Learning** | Erkennt eigenständig Muster und Gruppen in ungelabelten Daten. | **Marketing & E-Commerce:** Kundensegmentierung für gezielte Werbung.<br>**IT-Sicherheit:** Erkennung von Anomalien und Cyberangriffen im Netzwerkverkehr.<br>**Streaming-Dienste:** Empfehlungssysteme. |
| **Reinforcement Learning** | Ein Agent lernt durch Interaktion mit der Umgebung und Belohnungssysteme (Trial-and-Error). | **Robotik & Fertigung:** Steuerung von Industrierobotern.<br>**Automobilindustrie:** Autonomes Fahren und Routenplanung.<br>**Energiewirtschaft:** Optimierung von Stromnetzen und Kühlung in Rechenzentren. |
| **Semi-Supervised Learning** | Kombiniert wenige gelabelte Daten mit vielen ungelabelten Daten. | **Gesundheitswesen:** Auswertung medizinischer Scans (da manuelles Labeln durch Ärzte teuer ist).<br>**Sprach- & Textverarbeitung:** Klassifikation großer Dokumentenmengen.<br>**Cybersicherheit:** Betrugsidentifikation bei wenigen bekannten Betrugsfällen. |
| **Self-Supervised Learning** | Erzeugt eigene Labels aus der Struktur der ungelabelten Rohdaten selbst. | **Tech & Software (Generative KI):** Training großer Sprachmodelle (wie ChatGPT) und Bildgeneratoren.<br>**Automobilindustrie:** Objekterkennung in Kameradaten ohne manuelle Vorarbeit. |

---

## 2. Verbreitung in der Praxis

* **Marktführer im Alltag (Supervised Learning):** In klassischen Unternehmen (Banken, Versicherungen, Handel, Produktion) macht Supervised Learning den Großteil aller produktiven Anwendungen aus. Die Ergebnisse sind gut messbar, zuverlässig und für Geschäftsprozesse wie Preisgestaltung oder Risikoanalyse direkt nutzbar.
* **Wachstumstreiber bei KI-Modellen (Self-Supervised Learning):** Durch den Boom von generativer KI (Text-, Bild- und Videogenerierung) ist Self-Supervised Learning heute die wichtigste Grundlage für große Basismodelle (Foundation Models).
* **Nischen- und Spezialanwendungen (Unsupervised, Semi-Supervised & Reinforcement):** Unsupervised und Semi-Supervised Learning dienen oft als Vorstufe, um Daten zu strukturieren. Reinforcement Learning bleibt trotz beeindruckender Erfolge in der Robotik und bei Spielen im klassischen Unternehmensalltag noch eine Nische, da das Training in realen Umgebungen oft teuer oder riskant ist.
