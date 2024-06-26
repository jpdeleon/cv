# [Curriculum Vitae](https://raw.githubusercontent.com/jpdeleon/cv/main-pdf/tex/cv_pubs.pdf) | [resume](https://raw.githubusercontent.com/jpdeleon/cv/main-pdf/tex/resume.pdf)

[![Auto update](https://github.com/jpdeleon/cv/workflows/Auto%20update/badge.svg)](https://github.com/jpdeleon/cv/actions?query=workflow%3A%22Auto+update%22) [![Latest PDF](https://img.shields.io/badge/pdf-latest-orange.svg)](https://raw.githubusercontent.com/jpdeleon/cv/main-pdf/tex/cv_pubs.pdf)

This repo contains the python, tex, and shell scripts to periodically update and auto-generate the author's CV using github actions. The pdf files are published in the [main-pdf](https://github.com/jpdeleon/cv/tree/main-pdf/tex) branch.

Licensed under [Creative Commons Attribution](http://creativecommons.org/licenses/by/4.0/)

<hr>

$if(titleblock)$
$titleblock$

$endif$
$for(header-includes)$
$header-includes$

$endfor$
$for(include-before)$
$include-before$

$endfor$
$if(toc)$
$table-of-contents$

$endif$
$body$
$for(include-after)$

$include-after$
$endfor$
