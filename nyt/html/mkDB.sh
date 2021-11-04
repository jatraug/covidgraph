#!/bin/bash
## -*-sh-*-


### make a usable presence on Dropbox
export DB=/Users/jimt/Dropbox/work/covid
export CP=/bin/cp
export PY=python
export RM=/bin/rm

$RM $DB/html/images/*jpg
$CP ../images/*jpg $DB/html/images
