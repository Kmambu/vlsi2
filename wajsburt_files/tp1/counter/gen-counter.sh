#!/bin/sh

flag=$1
syf -$1 -CEV counter counter$1
asimut -b counter"$1" counter counter"$1"
