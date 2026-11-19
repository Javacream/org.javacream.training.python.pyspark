# Trainerleitfaden – Python und PySpark

Dieser Leitfaden ergänzt die [Agenda](agenda.md). Jede UE umfasst 90 Minuten. Die Zeitanteile sind Vorschläge für Demonstration, Einordnung und Übungszeit; die konkreten Übungen und das Handout erstellt der Trainer selbst.

## Rahmen und Vorbereitung

- Vor dem Seminar Docker/Dev Containers und VS Code prüfen; im Branch `training-pyspark` den Container starten.
- `python pyspark-environment/smoke_test.py` ausführen und lokale SparkSession verifizieren.
- Für die Python-Tage Beispiele aus dem bestehenden Repository gezielt auswählen; nicht die komplette frühere Commit-Historie durcharbeiten.
- PySpark-Beispiele liegen unter `resources/<blockname>/src/`, pro Block mit einer README.
- Git-Zugriff und gegebenenfalls Copilot-Zugang vorab klären; KI-generierten Code immer fachlich prüfen.
- Bei knapper Zeit priorisieren: DataFrames, Transformationen, Aggregationen, Joins, Spark-Ausführung und ETL. JDBC und Window Functions können als Demonstration behandelt werden.

## Tag 1 – Python-Grundlagen

### UE 1 – Einführung in die Programmierung

**Ziel:** Arbeitsablauf mit Editor, Fehlerrückmeldung, Versionsverwaltung und KI-Unterstützung verstehen.

**Ablauf:** 20 Min VS Code und Projektstruktur; 20 Min Syntax Highlighting, Code Assist und Fehlererkennung; 25 Min Git (Änderung, Commit, Push, Historie und Diff); 15 Min Copilot/KI demonstrieren; 10 Min Fragen.

**Trainerhinweise:** Nur elementaren Git-Workflow zeigen, keine Branches oder Pull Requests. KI-Vorschläge bewusst überprüfen. Falls Push-Zugriff fehlt, lokal committen und die Historie zeigen.

### UE 2 – Einführung in Python

**Ziel:** Einfache Programme lesen und schreiben, Datentypen und String-Verarbeitung verstehen.

**Ablauf:** 20 Min Syntax und Ausführung; 25 Min Variablen, Typen, Strings; 20 Min Ein-/Ausgabe; 25 Min Vertiefung.

**Trainerhinweise:** Dynamische Typisierung hervorheben. Keine Type Hints behandeln.

### UE 3 – Kontrollstrukturen

**Ziel:** Verzweigungen und Schleifen korrekt anwenden.

**Ablauf:** 20 Min Bedingungen; 25 Min Schleifen; 20 Min Einrückung und typische Fehler; 25 Min Vertiefung.

**Trainerhinweise:** Indentation als Syntaxbestandteil und Debugging im Editor aufgreifen.

### UE 4 – Collections und Objekte

**Ziel:** Grundlegende Collections nutzen und objektorientierte Aufrufsyntax lesen.

**Ablauf:** 35 Min Listen/Tupel; 20 Min Dictionaries/Sets; 20 Min Iteration; 15 Min Objekte, Punkt-Operator, Attribute, Methoden, Methodenverkettung.

**Trainerhinweise:** Keine eigenen Klassen erstellen. Die Aussage „vor dem Punkt steht ein Objekt“ als Einstieg verwenden; auch Rückgabewerte von Methoden können Objekte sein.

## Tag 2 – Python und Datenverarbeitung

### UE 5 – Dateiverarbeitung und Fehlerbehandlung

**Ziel:** Textdateien sicher verarbeiten und typische Fehler erkennen.

**Ablauf:** 30 Min Lesen/Schreiben; 20 Min `with` und Ressourcenverwaltung; 20 Min `try`/`except`; 20 Min Vertiefung.

**Trainerhinweise:** Textkodierung, Dateipfade und Fehlerfälle demonstrieren.

### UE 6 – Funktionen und Module

**Ziel:** Programme mit Funktionen strukturieren und Module verwenden.

**Ablauf:** 30 Min Funktionen, Parameter, Rückgaben; 20 Min Gültigkeitsbereiche; 20 Min Imports/Module; 20 Min Vertiefung.

**Trainerhinweise:** Funktionsaufruf und Methodenaufruf gegenüberstellen. Type Hints entfallen.

### UE 7 – Datenbankzugriff mit SQLite

**Ziel:** Treiber, Connection, Cursor, SQL-Ausführung und Ergebnisverarbeitung unterscheiden.

**Ablauf:** 20 Min Datenbank und Treiber; 25 Min Connection/Cursor; 25 Min SQL-Abfragen und Resultate; 20 Min Vertiefung.

**Trainerhinweise:** Ressourcenschließung, parametrisierte SQL-Abfragen und Unterschied zwischen lokalem SQLite-Zugriff und späterem Spark-JDBC erläutern. SQLite-Connection ist nicht gleich SparkSession.

### UE 8 – Strukturierte Datenverarbeitung

**Ziel:** Daten aus JSON, Dateien und Datenbanken einlesen, bereinigen und kombinieren.

**Ablauf:** 20 Min JSON; 20 Min Bereinigung; 20 Min Comprehensions/`map`/`filter`; 30 Min zusammenhängende Verarbeitung.

**Trainerhinweise:** Lambdas höchstens zeigen, nicht als Pflichtkompetenz voraussetzen. Die fachliche Aufgabenstellung kann später als Spark-DataFrame-Verarbeitung wiederkehren.

## Tag 3 – PySpark-Grundlagen

### UE 9 – Einführung in Apache Spark

**Ziel:** Lokale Spark-Ausführung, SparkSession, Driver und Executors einordnen.

**Ablauf:** 25 Min Architektur; 25 Min SparkSession und lokaler Modus; 20 Min DataFrame und erste Actions; 20 Min Auswertung.

**Demo:** `resources/09-spark-grundlagen/src/first_dataframe.py`.

**Trainerhinweise:** `local[2]` nutzt lokale Threads und ist kein echter Multi-Node-Cluster. Spark Driver und Datenbanktreiber sind verschiedene Begriffe.

### UE 10 – Daten einlesen und untersuchen

**Ziel:** CSV und JSON mit Schema lesen und Datenqualität beurteilen.

**Ablauf:** 20 Min Reader-API; 25 Min CSV/JSON; 20 Min Schema und Datentypen; 25 Min Vertiefung.

**Demo:** `resources/10-daten-einlesen-und-untersuchen/src/read_csv_json.py`.

**Trainerhinweise:** Explizite Schemas gegenüber automatischer Inferenz bevorzugen; Unterschied `show()` und `printSchema()` erklären.

### UE 11 – DataFrame-Transformationen

**Ziel:** Projektionen, Filter, berechnete Spalten und fehlende Werte behandeln.

**Ablauf:** 20 Min `select`/`filter`; 25 Min `withColumn`/`when`; 20 Min NULL; 25 Min Vertiefung.

**Demo:** `resources/11-dataframe-transformationen/src/transform_people.py`.

**Trainerhinweise:** Spark-Column-Ausdrücke sind keine gewöhnlichen Python-Booleschen Werte. Transformationen liefern neue DataFrames.

### UE 12 – Aggregationen

**Ziel:** Daten gruppieren und Kennzahlen berechnen.

**Ablauf:** 25 Min `groupBy`; 25 Min `agg`, `sum`, `count`; 20 Min Sortierung; 20 Min Vertiefung.

**Demo:** `resources/12-aggregationen/src/aggregate_sales.py`.

**Trainerhinweise:** Aggregation und Sortierung unterscheiden; NULL-Werte und Datentypen bei Summen beachten.

## Tag 4 – PySpark-Datenverarbeitung

### UE 13 – Daten kombinieren

**Ziel:** Joins und Spark SQL verwenden, JDBC als Datenquelle einordnen.

**Ablauf:** 30 Min Join-Typen; 25 Min Views und SQL; 15 Min JDBC-Konzept; 20 Min Vertiefung.

**Demos:** `resources/13-daten-kombinieren/src/joins_and_sql.py`; optional `jdbc_optional.py`.

**Trainerhinweise:** JDBC-Demo erfordert Datenbank und Treiber-JAR, die nicht im Standardcontainer enthalten sind. Nicht als lauffähige Pflichtübung darstellen.

### UE 14 – Ausführungsmodell von Spark

**Ziel:** Lazy Evaluation, Actions, Ausführungspläne und Partitionen verstehen.

**Ablauf:** 25 Min Transformations/Actions; 25 Min `explain` und DAG; 20 Min Partitionen; 20 Min Vertiefung.

**Demo:** `resources/14-spark-ausfuehrungsmodell/src/execution_plan.py`.

**Trainerhinweise:** `explain` zeigt einen Ausführungsplan, nicht die tatsächliche Laufzeit; Partitionen sind nicht automatisch gleich Knoten.

### UE 15 – Weitere Verarbeitungskonzepte

**Ziel:** Window Functions, Caching und Parquet-Ausgabe kennenlernen.

**Ablauf:** 30 Min Windows; 20 Min Cache; 20 Min Parquet; 20 Min Vertiefung.

**Demo:** `resources/15-weitere-verarbeitungskonzepte/src/window_cache_parquet.py`.

**Trainerhinweise:** Caching nicht pauschal als Optimierung empfehlen; materialisieren und `unpersist()` zeigen.

### UE 16 – Abschlussübung

**Ziel:** Einen vollständigen ETL-Ablauf von mehreren Quellen bis zur Ausgabe nachvollziehen und selbständig umsetzen.

**Ablauf:** 15 Min Aufgabenstellung; 50 Min selbständige Umsetzung; 15 Min gemeinsame Besprechung; 10 Min Rückblick.

**Demo/Referenz:** `resources/16-abschlussuebung/src/etl_pipeline.py`.

**Trainerhinweise:** Das Skript ist eine Referenzdemonstration, keine vorgefertigte Teilnehmerübung. Dateien werden temporär angelegt und wieder gelöscht.

## Abschluss und Grenzen

- Spark-Beispiele sind Anwendungen mit `main()`, keine Unit Tests.
- Das Schulungskonzept legt die fachliche Progression fest, ersetzt aber nicht die vom Trainer geplanten Übungen oder das Handout.
- Ein produktiver Clusterbetrieb, Tuning im Detail, Deployment und Security sind nicht Teil der 16 UE.
