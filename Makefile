all: pdf

pdf: paper.tex main.tex methods.tex paper.bib 
	pdflatex "\def\includeappendix{false}\input{paper}"
	bibtex paper
	pdflatex "\def\includeappendix{false}\input{paper}"
	pdflatex "\def\includeappendix{false}\input{paper}"
	pdflatex "\def\includeappendix{false}\input{paper}"

full: paper.tex main.tex methods.tex appendix.tex paper.bib
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"
	bibtex paper-full
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"
	pdflatex -jobname=paper-full "\def\includeappendix{true}\input{paper}"

# Highlighted-changes ("track changes") PDF versus a base revision, using
# latexdiff. BASE defaults to the version submitted for first-round review
# (the commit just before "Answering first round reviews"). Override with:
#   make diff BASE=<commit>
# Requires: latexdiff, latexpand. Produces paper-diff.pdf.
#
# We flatten each revision into a single self-contained .tex before diffing
# (rather than letting latexdiff-vc flatten on the fly). The appendix is
# promoted out of its \ifthenelse guard first: latexdiff treats a
# command-argument brace group as one opaque block and can never word-diff it,
# so flattening alone is not enough -- the appendix must sit at the top level.
BASE ?= b488490
BUILDDIR := .diff-build
# PICTUREENV lists environments latexdiff must not inject markup into. We add
# the tabularray environments (tblr/longtblr): injecting \DIFadd... color
# markers inside them corrupts the alignment (Misplaced \noalign). Changed
# tables are instead marked as a whole. Keep the built-in defaults too.
LATEXDIFF_OPTS ?= --preamble=latexdiff-preamble.tex --ignore-warnings --disable-citation-markup --graphics-markup=none --math-markup=off --config MINWORDSBLOCK=1 --config 'PICTUREENV=picture[\w\d*@]*;tikzpicture[\w\d*@]*;DIFnomarkup[\w\d*@]*;tblr[\w\d*@]*;longtblr[\w\d*@]*'

diff: paper.tex main.tex methods.tex appendix.tex paper.bib
	\rm -f *.aux *.bbl *.blg paper-diff.out paper-diff$(BASE).tex
	\rm -rf $(BUILDDIR)
	mkdir -p $(BUILDDIR)/base
	git archive $(BASE) | tar -x -C $(BUILDDIR)/base
	python3 scripts/promote-appendix-guard.py $(BUILDDIR)/base/paper.tex
	cd $(BUILDDIR)/base && latexpand paper.tex > ../base-flat.tex
	cp paper.tex $(BUILDDIR)/new-paper.tex
	python3 scripts/promote-appendix-guard.py $(BUILDDIR)/new-paper.tex
	latexpand $(BUILDDIR)/new-paper.tex > $(BUILDDIR)/new-flat.tex
	latexdiff $(LATEXDIFF_OPTS) $(BUILDDIR)/base-flat.tex $(BUILDDIR)/new-flat.tex > paper-diff$(BASE).tex
	python3 scripts/strip-latexdiff-structural-markup.py paper-diff$(BASE).tex
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"
	bibtex paper-diff
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"
	pdflatex -interaction=nonstopmode -jobname=paper-diff "\def\includeappendix{true}\input{paper-diff$(BASE).tex}"

clean:
	\rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.synctex.gz paper.pdf paper-full.pdf paper-diff.pdf paper-diff*.tex
	\rm -rf $(BUILDDIR)
