# digitalhistory-uebungen

## usage

- python zusaetzliche-uebungen.py -t [tasknumber] -i input

## tasks

### zusätzliche zusaetzliche

Hier die versprochenen Übungen in aufsteigender Schwierigkeit: 

1) Gib alle Zahlen von 1 - 100 aus: Die while-Schleife

2) Ersetze in dieser Schleife alle Zahlen die durch drei teilbar sind durch den String "Digital" 
Beispielausgabe:
```
1 
2
Digital
4
5
```
3) Ersetze in einer Schleife, die Zahlen die durch fünf teilbar sind durch "History"
Beispielausgabe:
```
1
2
3
4
History
6
7
8
9
History
```
4) Kombiniere die Schritte 2 und 3 mit einem Elif, sodass du nicht doppelt ausgibst 
Beispielausgabe:
```
1
2
Digital
4
History
```
5) Ersetze Zahlen die durch 3 Teilbar sind durch den String "Digital", Zahlen die durch 5 teilbar sind durch den String "History" und Zahlen, die durch beides teilbar sind durch den String "Digital History"
Beispielausgabe:
```
1
2
Digital
4
History
6
....
11
Digital
13
14
Digital History
16
```
Achtung: Nicht alle Methoden haben wir in der Übung besprochen:
1) Ein IF-Statement kann mehrere Bedingungen enthalten: 
Syntax-Beispiel:
```python
If(Bedingung1 and Bedingung2):
    # Code der ausgefuehrt werden soll
```

2) Der Operator zum Vergleichen ob etwas "ohne Rest" durch 0 teilbar ist heißt Modulo-Operator und wird mit dem %-Zeichen gebildet. Um zu überprüfen ob eine Zahl ohne Rest durch eine andere Zahl durch etwas geteilt werden kann:
```python
N = 3
If(N % 3 ==0):
    Code der ausgeführt werden soll
```
