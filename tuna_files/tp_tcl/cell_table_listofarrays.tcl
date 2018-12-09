#!/bin/tclsh
#
################################################################################
#                             and2 cell instantiation                          #
################################################################################
set and2_cell(name) "and2"
set and2_cell(type) "AND"
set and2_cell(inputs) [list "I0" "I1"]
set and2_cell(outputs) [list "O"]
set and2_cell(bc_timing) 102
set and2_cell(wc_timing) 198

################################################################################
#                             andn3 cell instantiation                         #
################################################################################
set andn3_cell(name) "andn3"
set andn3_cell(type) "AND"
set andn3_cell(inputs) [list "I0" "I1" "NI2"]
set andn3_cell(outputs) [list "O"]
set andn3_cell(bc_timing) 251
set andn3_cell(wc_timing) 430

################################################################################
#                             nand4 cell instantiation                         #
################################################################################
set nand4_cell(name) "nand4"
set nand4_cell(type) "NAND"
set nand4_cell(inputs) [list "I0" "I1" "I1"]
set nand4_cell(outputs) [list "Z"]
set nand4_cell(bc_timing) 123
set nand4_cell(wc_timing) 199

################################################################################
#                             or2 cell instantiation                           #
################################################################################
set or2_cell(name) "or2"
set or2_cell(type) "OR"
set or2_cell(inputs) [list "i0" "i1"]
set or2_cell(outputs) [list "o"]
set or2_cell(bc_timing) 102
set or2_cell(wc_timing) 203

################################################################################
#                             or3 cell instantiation                           #
################################################################################
set or3_cell(name) "or3"
set or3_cell(type) "OR"
set or3_cell(inputs) [list "i0" "i1" "i2"]
set or3_cell(outputs) [list "o"]
set or3_cell(bc_timing) 126
set or3_cell(wc_timing) 233

################################################################################
#                             xor2 cell instantiation                          #
################################################################################
set xor2_cell(name) "xor2"
set xor2_cell(type) "XOR"
set xor2_cell(inputs) [list "i0" "i1"]
set xor2_cell(outputs) [list "x"]
set xor2_cell(bc_timing) 213
set xor2_cell(wc_timing) 359

################################################################################
#                             xor3 cell instantiation                          #
################################################################################
set xor3_cell(name) "xor3"
set xor3_cell(type) "XOR"
set xor3_cell(inputs) [list "i0" "i1"]
set xor3_cell(outputs) [list "x"]
set xor3_cell(bc_timing) 245
set xor3_cell(wc_timing) 402

################################################################################
#                             bcell4 cell instantiation                        #
################################################################################
set bcell4_cell(name) "bcell4"
set bcell4_cell(type) "BCELL"
set bcell4_cell(inputs) [list "a0" "a1" "b0" "b1"]
set bcell4_cell(outputs) [list "O0" "O1"]
set bcell4_cell(bc_timing) 412
set bcell4_cell(wc_timing) 765

################################################################################
#                             bcell5 cell instantiation                        #
################################################################################
set bcell5_cell(name) "bcell5"
set bcell5_cell(type) "BCELL"
set bcell5_cell(inputs) [list "a0" "a1" "b0" "b1" "b2"]
set bcell5_cell(outputs) [list "O0" "O1"]
set bcell5_cell(bc_timing) 498
set bcell5_cell(wc_timing) 876

set cells [list and2_cell andn3_cell nand4_cell]
