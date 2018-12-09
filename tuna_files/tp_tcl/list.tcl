#!/bin/tclsh
set coders [list "jack" "steve" "william" "franck" "edward"]
foreach coder $coders {
	puts $coder
}
set third_coder [lindex $coders 2]
puts " the third coder is $third_coder"
