# digitalhistory-uebungen

Dieses Repository enthält meine Lösungen der Aufgaben im Rahmen der
Veranstaltung "Digital History - Update der Geschichtswissenschaften" im
Wintersemester 2024/2025 an der Universität Heidelberg.

Grundsätzlich ist jede Aufgabe als `.py`-Datei gelöst. Die
Aufgabenstellungen der einzelnen Aufgaben finden sich im Abschnitt
[Aufgabenstellung](#Aufgabenstellung). Das Aufrufen der Dateien benötigt meist
ein Schema, welches im Abschnitt ["Nutzung"](#Nutzung) angeführt wird.
Vereinzelt sind die Lösungen auch zusätzlich in einer `.ipynb`-Datei übertragen.
Diese Dateien tragen den gleichen Namen wie die zugrunde liegende `.py`-Datei

Alle zusammengehörenden Dateien liegen grundsätzlich in einem Ordner mit dem Namen des Aufgabentitel.

Bei Umfangreicheren Aufaben wie beispielsweise der Weihnachtsaufgabe werden
dependencies benötigt, die nicht standardmäßg bei python in der binary geshipped
werden. Diese Aufgaben lassen sich an der existenz einer "requirements.txt"
erkennen. Ich empfehle dabei die verwendung von Pythons virtual environments:
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r  [aufgabe]-requirements.txt
```

## Nutzung

### zusaetzliche uebungen
`python zusaetzliche-uebungen/zusaetzliche-uebungen.py <tasknumber>`

### weihnachtsaufgabe
> [!NOTE]
> dieses projekt hat externe dependencies!

`python weihnachtsaufgabe/weihnachtsaufgabe.py <inputfile> <outputfile> [-t (pdf || hocr || txt || alto) -l eng+deu -r 600]`

> [!WARNING]  
> die software benötigt, dass auf dem System [tesseract](https://tesseract-ocr.github.io/tessdoc/Downloads.html) installiert ist und über PATH abgerufen werden kann. 
> möglicherweise müssen auch erweiterte Sprach-Modelle installiert werden (siehe [tessdata](https://github.com/tesseract-ocr/tessdata))
## Aufgabenstellungen

### zusätzliche Uebungen
> [!NOTE] 
> Diese Übungen sind sowohl als Python Datei als auch als Python Notebook verfügbar

Hier die versprochenen Übungen in aufsteigender Schwierigkeit: 



1) Gib alle Zahlen von 1 - 100 aus: Die while-Schleife

2) Ersetze in dieser Schleife alle Zahlen die durch drei teilbar sind durch den String "Digital"
<details>
<summary> Beispielausgabe </summary>
<br>
1 
2
Digital
4
5
</details>
3) Ersetze in einer Schleife, die Zahlen die durch fünf teilbar sind durch "History"
<details>
<summary>Beispielasusgabe</summary>

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

</details>
4) Kombiniere die Schritte 2 und 3 mit einem Elif, sodass du nicht doppelt ausgibst 
<details>
<summary>Beispielasusgabe</summary>

1
2
Digital
4
History

</details>
5) Ersetze Zahlen die durch 3 Teilbar sind durch den String "Digital", Zahlen die durch 5 teilbar sind durch den String "History" und Zahlen, die durch beides teilbar sind durch den String "Digital History"
<details>
<summary>Beispielasusgabe</summary>

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

</details>

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
    # Code der ausgeführt werden soll
```

### Weihnachtsaufgabe
Es (Anm.: Git) ist in der Software-Entwicklung und der DH eines der wichtigsten Tools.
Sie haben ein hervorragendes Tutorial: [Link zum Tutorial](https://docs.github.com/de/get-started/start-your-journey/hello-world)

Bearbeitet bitte das Tutorial und fügt eine Datei ein, die alle Python-Grundlagen enthält, die ihr bisher gelernt habt.
Sendet uns den Link zum Repository bitte bis 03.01.2025.

#### Ausführung zum Projekt
**multipage-ocr using tesseract.**

Wenn ich schon was schreibe, dann auch gern etwas das ich tatsächlich verwende.

Ein zu häufiger Arbeitsablauf im Studium ist bei mir das jagen von Scans durch
OCR, um zumindest etwas durchsuchbarkeit zu haben. Dafür verwende ich meist
`tesseract` als cli-tool. Leider kann tesseract nicht mit mehrseitigen
textdokumenten umgehen, was zu folgendem mehrschrittigen Ablauf führt:
```sh
mkdir tmp
pdftoppm -tiff -r 300 input.pdf tmp/page
for f in tmp/*.tif; do
    tesseract $f $f -l eng+deu PDF
done
pdfunite tmp/*pdf out.pdf
rm -rf tmp
```

Um mich nicht immer erneut an dieses Bash-script zu erinnern, gibt mir diese
Aufgabe hier die Zeit ein Toolkit dafür zu schreiben :)



### *eigenständige Uebung*: versuche-mit-nlp
um mich an den Umgang mit NLP und v.a. staCy zu gewöhnen, ist hier auch meine Uebung dazu zu sehen. 
Als ursprünglicher Anlass von `versuche-mit-nlp/generator.py` diente die Analyse von den Wahlprogrammen 2025.

> [!NOTE]
> Da diese Datei intern verständlich dokumentiert ist, wurde vorerst auf einen Eintrag in der
> [ReadMe](#Nutzung) verzichtet!
