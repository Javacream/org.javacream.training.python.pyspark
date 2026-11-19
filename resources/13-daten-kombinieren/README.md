# UE 13 – Daten kombinieren

## Lernabsicht

Joins, temporäre Views, Spark SQL und Einordnung von JDBC.

## Beispiele

- `joins_and_sql.py`
- `jdbc_optional.py`

Die Programme verwenden jeweils eine `main()`-Funktion und sind eigenständig startbar. Sie dienen als Demonstrationen; Übungen und Handout werden separat erstellt.

## Ausführung

Im Dev Container vom Repository-Wurzelverzeichnis aus:

```bash
python resources/13-daten-kombinieren/src/joins_and_sql.py
```

```bash
python resources/13-daten-kombinieren/src/jdbc_optional.py
```

**JDBC-Hinweis:** `jdbc_optional.py` ist bewusst optional. Ein JDBC-Treiber und eine erreichbare relationale Datenbank sind nicht Bestandteil des Containers. Das Skript erklärt beim Start die benötigten Umgebungsvariablen. SQLite aus dem Python-Teil lässt sich nicht ohne passenden JDBC-Treiber und zusätzliche Konfiguration als Spark-JDBC-Quelle verwenden.
