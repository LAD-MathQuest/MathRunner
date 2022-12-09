#------------------------------------------------------------------------------#
# ./fvelgame/Makefile

# List of all subdirectories
SUBDIRS=$(shell find -mindepth 1 -maxdepth 1 -type d -not -name __pycache__ -not -name venv)

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__

#------------------------------------------------------------------------------#

default: 
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D ;            \
	done

#------------------------------------------------------------------------------#

clean:
	-@ rm -vf ${CLEAN_FILES}
	@ for D in ${SUBDIRS} ; do \
	  make -C $$D clean ;      \
	done

distclean: 
	-@ rm -vf ${DISTCLEAN_FILES}
	@ for D in ${SUBDIRS}; do \
	  make -C $$D distclean ; \
	done

.PHONY: clean distclean

#------------------------------------------------------------------------------#
