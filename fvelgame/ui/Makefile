#------------------------------------------------------------------------------#
# ./fvelgame/ui/Makefile

# Qt designer ui files 
UI_FILES=$(shell find -maxdepth 1 -name 'form_*.ui' -type f)
PY_FILES=$(UI_FILES:.ui=.py)

# List of all subdirectories
SUBDIRS=$(shell find -mindepth 1 -maxdepth 1 -type d -not -name __pycache__)

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~ 

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__

#------------------------------------------------------------------------------#

default: $(PY_FILES)
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D ;            \
	done

%.py: %.ui
	pyside6-uic --g python $< -o $@

#------------------------------------------------------------------------------#

clean:
	-@ rm -vf ${CLEAN_FILES}
	@ for D in ${SUBDIRS} ; do   \
	  make -C $$D clean ;      \
	done

distclean: 
	-@ rm -vf ${DISTCLEAN_FILES}
	@ for D in ${SUBDIRS}; do        \
	  make -C $$D distclean ;      \
	done

.PHONY: clean distclean

#------------------------------------------------------------------------------#
