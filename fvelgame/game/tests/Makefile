#------------------------------------------------------------------------------#
# ./fvelgame/game/tests/Makefile

# Qt designer ui files 
TEST_FILES=$(shell find -maxdepth 1 -name 'test_*.py' -type f)





# Files to be removed from this directory at cleaning
CLEAN_FILES= *~

# Files to be removed from this directory at distribution cleaning
DISTCLEAN_FILES= __pycache__

#------------------------------------------------------------------------------#

run: 
	@ for T in $(TEST_FILES) ; do   \
	  python $$T ;                \
	done


all:




#------------------------------------------------------------------------------#

clean:
	-@ rm -vf ${CLEAN_FILES}




distclean: 
	-@ rm -vf ${DISTCLEAN_FILES}




.PHONY: run all clean distclean

#------------------------------------------------------------------------------#
