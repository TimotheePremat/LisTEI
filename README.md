# What is LisTEI
This is a local, python and JS-based web-app for annotating lists in XML TEI documents. The goal is simply to make such tagging faster.

It has been developped by Timothée Premat, postdoctoral researcher for the ArchivU project <https://archivu.hypotheses.org>. It is distributed under GNU GPL v3 licence, without any guarantee as to the result or as to its stability.

# How to use
1. Open a terminal to the LisTEI folder, and run ```python app.py```.
2. The terminal displays a local URL, copy-paste it into the web browser of your choice. Do not close the terminal, it would crash the app!
3. In the web browser, upload (so to speak: this is purely local) a text or resume annotation of a previously annotated text

# Folders structure
- ```annotated``` : contains texts that have been tagged
- ```PDFs``` (optional) : might contains the PDF sources used for controlling the tagging
- ```templates``` : contains de ```.html``` files responsible for the program
- ```uploads``` : contains texts that have been load for tagging, preserved in their pre-tagging stage
- ```app.py``` : python script using Flask to emulate web-app.