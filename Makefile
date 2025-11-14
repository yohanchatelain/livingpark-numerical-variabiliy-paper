all: pdf

pdf: paper.tex main.tex methods.tex appendix.tex paper.bib 
	pdflatex paper ; bibtex paper ; pdflatex paper ; pdflatex paper 

clean:
	\rm *.{out,aux,log,pdf,blg,bbl}