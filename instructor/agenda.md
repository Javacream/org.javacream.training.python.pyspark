# Schulungskonzept und Agenda – Python und PySpark

**Dauer:** 4 Tage, 16 Unterrichtseinheiten (UE) zu jeweils 90 Minuten. 8 UE Python-Grundlagen, anschließend 8 UE PySpark.

**Ziel:** Teilnehmende können grundlegende Python-Programme verstehen und schreiben sowie mit PySpark strukturierte Daten einlesen, transformieren, kombinieren, aggregieren und als Ergebnis speichern.

**Voraussetzungen:** Allgemeine IT-Kenntnisse; Programmiererfahrung hilfreich, aber nicht zwingend. Entwicklungsumgebung: Visual Studio Code mit Dev Container und lokaler Spark-Ausführung.

**Didaktik:** Demonstration, kurze Erklärungen und eigenständige Übungen. Übungen und Handout werden durch den Trainer separat erstellt. Ein durchgehender Fokus auf Datenverarbeitung verbindet Python und PySpark.

## Tag 1 – Entwicklungsumgebung und Python-Grundlagen

| UE | Thema | Inhalte |
|---|---|---|
| 1 | Einführung in die Programmierung | Visual Studio Code, Syntax Highlighting, Code Assist, Fehlererkennung, Git als Versionsverwaltungssystem, Commit und Push, Commit-Historie, Copilot und KI-Unterstützung |
| 2 | Einführung in Python | Erste Programme, Variablen, Datentypen, Strings, Ein- und Ausgabe |
| 3 | Kontrollstrukturen | Bedingungen, Schleifen, Einrückung |
| 4 | Collections und Objekte | Listen, Tupel, Dictionaries, Sets, Iteration, Objekte und objektorientierte Syntax |

## Tag 2 – Python und Datenverarbeitung

| UE | Thema | Inhalte |
|---|---|---|
| 5 | Dateiverarbeitung und Fehlerbehandlung | Textdateien lesen und schreiben, `with`, Exceptions |
| 6 | Funktionen und Module | Funktionen, Parameter, Rückgabewerte, lokale und globale Variablen, Module und Imports |
| 7 | Datenbankzugriff mit SQLite | Datenbanktreiber, Connection, Cursor, SQL-Abfragen, Verarbeitung der Ergebnisse |
| 8 | Strukturierte Datenverarbeitung | JSON, Datenbereinigung, Comprehensions, `map`, `filter`, Kombination von Datei- und Datenbankzugriff, praktische Übung; Lambdas nur optional demonstrieren |

## Tag 3 – PySpark-Grundlagen

| UE | Thema | Inhalte |
|---|---|---|
| 9 | Einführung in Apache Spark | Architektur, Driver, Executors, SparkSession, verteilte Datenverarbeitung |
| 10 | Daten einlesen und untersuchen | DataFrames, CSV, JSON, Schemas, Datentypen, erste Aktionen |
| 11 | DataFrame-Transformationen | `select`, `filter`, `withColumn`, `when`, fehlende Werte |
| 12 | Aggregationen | `groupBy`, Aggregatfunktionen, Sortierung, einfache Auswertungen |

## Tag 4 – PySpark-Datenverarbeitung

| UE | Thema | Inhalte |
|---|---|---|
| 13 | Daten kombinieren | Joins, Spark SQL, temporäre Views, JDBC-Datenquellen (Konzept und optionale Demonstration) |
| 14 | Ausführungsmodell von Spark | Lazy Evaluation, Transformations und Actions, DAG, Partitionierung |
| 15 | Weitere Verarbeitungskonzepte | Window Functions, Caching, Daten schreiben, Parquet |
| 16 | Abschlussübung | ETL-Pipeline mit mehreren Datenquellen, Transformationen, Aggregationen und Ausgabe |

## Abgrenzung

Keine eigene Klassenentwicklung, Vererbung, Dunder-Methoden, REST-Services oder Type Hints als Lernziele. Die objektorientierte Syntax wird am Punkt-Operator erklärt. Git ohne Branching oder Pull Requests. Keine externe Spark-Infrastruktur erforderlich; JDBC zu externen Datenbanken ist optional.
