#!/bin/bash
latexmk -xelatex -output-directory=.latex-cache cmd.tex cmd.bib
cp .latex-cache/cmd.pdf /Users/rdube/Tmp/cmd.pdf
