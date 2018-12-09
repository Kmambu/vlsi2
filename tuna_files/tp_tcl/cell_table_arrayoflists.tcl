#!/bin/tclsh
set cells(and2)   [list "and2"   "AND"   [list "I0" "I1"]                [list "O"]       102 198]
set cells(andn3)  [list "andn3"  "AND"   [list "I0" "I1" "NI2"]          [list "O"]       251 430]
set cells(nand4)  [list "nand4"  "NAND"  [list "I0" "I1" "I1"]           [list "O"]       123 199]
set cells(or2)    [list "or2"    "OR"    [list "i0" "i1"]                [list "o"]       102 203]
set cells(or3)    [list "or3"    "OR"    [list "i0" "i1" "i2"]           [list "o"]       126 233]
set cells(xor2)   [list "xor2"   "XOR"   [list "i0" "i1"]                [list "x"]       213 359]
set cells(xor3)   [list "xor3"   "XOR"   [list "i0" "i1"]                [list "x"]       245 402]
set cells(bcell4) [list "bcell4" "BCELL" [list "a0" "a1" "b0" "b1"]      [list "O0" "O1"] 412 765]
set cells(bcell5) [list "bcell5" "BCELL" [list "a0" "a1" "b0" "b1" "b2"] [list "O0" "O1"] 498 876]

proc computeWC {path} {
	global cells
	set res 0
	foreach elem $path {
		puts "$elem"
		set res [expr {$res + [lindex $cells($elem) 5]}]
	}
	return $res
}

set val [computeWC [list and2 andn3]]
puts "WC_delay = $val"
