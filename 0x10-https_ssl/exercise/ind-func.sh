#!/bin/bash
echo_var ()
{
    echo "$1"
}

message=Hello
Hello=Goodbye

echo_var "$message"
echo_var "${!message}"

Hello="Goodbye again!"

echo ---------------------------
echo_var "$message"
echo_var "${!message}"
