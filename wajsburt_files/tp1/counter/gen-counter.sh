#!/bin/sh

flag=$1
syf -$1 -CEV counter counter$1
asimut -b counter"$1" counter counter"$1"
boom -V counter"$1" counter"$1"_boom
asimut -b counter"$1"_boom counter counter"$1"_boom
boog counter"$1"_boom counter"$1"_boog
asimut counter"$1"_boog counter counter"$1"_boog
loon counter"$1"_boog counter"$1"_loon
asimut counter"$1"_loon counter counter"$1"_loon
flatbeh counter"$1"_loon counter"$1"_loon
proof -d counter"$1" counter"$1"_loon
#xsch -I vst -l counter"$1"_boog
