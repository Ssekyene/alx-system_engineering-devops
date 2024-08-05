#!/bin/bash
# dereference.sh
# Dereferencing parameter passed to a function.
# Script by Bruce W. Clare.

dereference ()
{
     y=\$"$1"   # Name of variable (not value!).
     echo $y    # $Junk
    
     expr $y    # $Junk
     echo ----------------------
     x=`eval "expr \"$y\" "`  # x = $Junk
     echo "x = $x"            # x = Some Text
     echo ----------------------
     echo $1=$x
     eval "$1=\"Some Different Text \""  # Assign new value.
}

Junk="Some Text"
echo $Junk "before"    # Some Text before

dereference Junk
echo $Junk "after"     # Some Different Text after

exit 0
