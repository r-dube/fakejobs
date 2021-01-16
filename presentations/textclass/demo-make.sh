#!/bin/bash
latexmk -xelatex -output-directory=.latex-cache demo.tex demo.bib
cp .latex-cache/demo.pdf /Users/rdube/Tmp/demo.pdf
