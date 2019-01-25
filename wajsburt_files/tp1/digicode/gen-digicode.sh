#!/bin/sh

flag=$1
syf -$1 -CEV digicode digicode$1
asimut -b digicode"$1" digicode digicode"$1"
boom -V digicode"$1" digicode"$1"_boom
asimut -b digicode"$1"_boom digicode digicode"$1"_boom
boog digicode"$1"_boom digicode"$1"_boog
asimut digicode"$1"_boog digicode digicode"$1"_boog
loon digicode"$1"_boog digicode"$1"_loon
asimut digicode"$1"_loon digicode digicode"$1"_loon
flatbeh digicode"$1"_loon digicode"$1"_loon
proof -d digicode"$1" digicode"$1"_loon
#xsch -I vst -l digicode"$1"_boog
