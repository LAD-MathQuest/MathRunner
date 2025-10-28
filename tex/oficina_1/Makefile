#------------------------------------------------------------------------------#
.NOTPARALLEL:

TEX_FILES := Criando_um_jogo.tex
EXT_FILES := $(shell find -maxdepth 2 \
             -name '*.cls' -or \
             -name '*.sty' -or \
             -name '*.bib' -or \
             -name '*.asy')

PRES:=pres

HAND_PDF_FILES := $(TEX_FILES:.tex=.pdf)
PRES_PDF_FILES := $(foreach item, $(HAND_PDF_FILES), $(PRES)_$(item))

LATEX := >/dev/null 2>&1 latexmk -pdf -silent

BUILD_HAND = $(LATEX) -usepretex='\PassOptionsToClass{handout}{beamer}' $<
BUILD_PRES = $(LATEX) -jobname=$(PRES)_$(<:.tex=) $<

PRINT_LOG = texlogfilter --filename $(@:.pdf=.log)

ASY_DONE := ./asy/_all_done
MAKE = make --no-print-directory -C 

DEPENDENCIES := $(EXT_FILES) $(wildcard ./figs/*) $(ASY_DONE)

#------------------------------------------------------------------------------#

.PHONY: all pres hand
all: pres hand

pres: $(PRES_PDF_FILES)

hand: $(HAND_PDF_FILES)

$(PRES)_%.pdf: %.tex $(DEPENDENCIES)
	@ echo Compiling $@
	@ $(BUILD_PRES) || $(PRINT_LOG)

%.pdf: %.tex $(DEPENDENCIES)
	@ echo Compiling $@
	@ $(BUILD_HAND) || $(PRINT_LOG)

$(ASY_DONE):
	@ $(MAKE) asy

#------------------------------------------------------------------------------#

.PHONY: clean
clean:
	@ echo Cleaning $(notdir $(CURDIR))
	@ $(MAKE) asy clean
	@ rm -f ./ex/*.aux
	@ rm -f *~ .*~ *.bak                                    \
          *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc \
          *.bcf *.run.xml *.snm *.nav *.vrb .*.sw?        \
          *.psynctex.gz *.synctex.gz *.rubbercache *.pre  \
          *.fdb_latexmk *.fls *.dvi

.PHONY: distclean
distclean: clean
	@ echo Distcleaning $(notdir $(CURDIR))
	@ $(MAKE) asy distclean
	@ rm -f *.pdf

#------------------------------------------------------------------------------#
