#!/bin/bash
latexmk -xelatex -output-directory=.latex-cache tc.tex tc.bib
cp .latex-cache/tc.pdf /Users/rdube/Tmp/tc.pdf
