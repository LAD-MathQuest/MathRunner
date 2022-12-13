#------------------------------------------------------------------------------#
# ./fvelgame/ui/Makefile

# Qt designer ui files 
PY_FILES=$(shell find -maxdepth 1 -name '*.py' -type f)
PK_FILES=$(PY_FILES:.py=.pkl)

# List of all subdirectories
# SUBDIRS=$(shell find -mindepth 1 -maxdepth 1 -type d -not -name __pycache__)

# Files to be removed from this directory at cleaning
CLEAN_FILES= *~ 

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__ ${PK_FILES}

#------------------------------------------------------------------------------#

default: $(PK_FILES)
#	@ for D in ${SUBDIRS} ; do \
#	  make -C $$D ;            \
#	done

%.pkl: %.py ../../world/meta_world.py
	python $<

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
