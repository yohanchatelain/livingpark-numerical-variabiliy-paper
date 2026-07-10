# LivingPark Numerical Variability Paper

LaTeX source for the manuscript on numerical variability in neuroimaging
analyses of Parkinson's disease.

[![PDF Download](https://img.shields.io/badge/PDF-paper--full.pdf-blue)](https://github.com/yohanchatelain/livingpark-numerical-variabiliy-paper/releases/latest/download/paper-full.pdf)

## Build

Build the main manuscript:

```sh
make
```

Build the full manuscript with appendix:

```sh
make full
```

Build a highlighted-diff PDF against the default review baseline:

```sh
make diff
```

Use another baseline commit for the diff with:

```sh
make diff BASE=<commit>
```

Clean generated LaTeX artifacts:

```sh
make clean
```

The diff build uses `latexdiff-vc`, `latexdiff`, and
`scripts/strip-latexdiff-structural-markup.py` to keep LaTeX-only reference and
math changes from being visually highlighted.

## Data and Analysis Code

Data processing and analysis code are maintained in:

https://github.com/yohanchatelain/livingpark-numerical-variability
