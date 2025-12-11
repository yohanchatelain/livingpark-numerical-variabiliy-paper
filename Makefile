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


clean:
	\rm -f *.{out,aux,log,pdf,blg,bbl}