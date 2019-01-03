set_attribute library /users/enseig/tuna/ue_vlsi2/techno/cmos_120/cmos_120nm_core_Worst.lib
set rtl [list ./mips_32_1p_mul_div.vhd]
read_hdl -vhdl $rtl
elaborate MIPS_32_1P_MUL_DIV
check_design
synthesize -to_mapped
