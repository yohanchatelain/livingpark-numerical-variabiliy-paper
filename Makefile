all: pdf

pdf: paper.tex main.tex methods.tex paper.bib 
	pdflatex "\def\includeappendix{false}\input{paper}"
	bibtex paper
	pdflatex "\def\includeappendix{false}\input{paper}"
	pdflatex "\def\includeappendix{false}\input{paper}"

full: paper.tex main.tex methods.tex appendix.tex paper.bib
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"
	bibtex paper-full
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"

# Highlighted-changes ("track changes") PDF versus a base revision, using
# latexdiff. BASE defaults to the version submitted for first-round review
# (the commit just before "Answering first round reviews"). Override with:
#   make diff BASE=<commit>
# Requires: latexdiff, latexdiff-vc. Produces paper-diff.pdf.
BASE ?= b488490

diff: paper.tex main.tex methods.tex appendix.tex paper.bib
	\rm -f *.aux *.bbl *.blg paper-diff$(BASE).tex
	latexdiff-vc --git --flatten --force -r $(BASE) paper.tex
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"
	bibtex paper-diff
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"

clean:
	\rm -f *.{out,aux,log,pdf,blg,bbl} paper-diff*.tex