# Defone latex and bash commands
LATEX       = pdflatex
BASH        = bash -c
ECHO        = echo
RM          = rm -rf

# Define temporary file suffixes to be removed
TMP_SUFFS   = aux bbl blg log dvi ps eps out
# Define the command to remove temporary files
RM_TMP      = ${RM} $(foreach suff, ${TMP_SUFFS}, *.${suff})

# Check if a LaTeX file needs to be rerun based on the log file
CHECK_RERUN = grep Rerun $*.log

# Define the list of all target files to be generated
ALL_FILES = cv.pdf pubs.pdf cv_pubs.pdf biosketch.pdf

# Rule to build all target files
all: ${ALL_FILES}

# Rule to build PDF files from corresponding LaTeX files
%.pdf: %.tex cvstyle.tex pubs_ref.tex pubs_unref.tex ../data/pubs.json ../data/other_pubs.json
	${LATEX} $<
	${LATEX} $<

# Rule to build a specific PDF file with publications
cv_pubs.pdf: cv.tex pubs_*.tex cvstyle.tex ../data/pubs.json ../data/other_pubs.json
	${LATEX} -jobname=cv_pubs "\def\withpubs{}\input{cv}"
	${LATEX} -jobname=cv_pubs "\def\withpubs{}\input{cv}"

# Rule to clean up temporary files and target files
clean:
	${RM_TMP} ${ALL_FILES}