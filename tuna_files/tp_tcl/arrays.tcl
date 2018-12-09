#!/bin/tclsh
set days(d1) Monday
set days(d2) Tuesday
set days(d3) Wednesday
set days(d4) Thursday
set days(d5) Friday
set days(d6) Saturday
set days(d7) Sunday

puts [array size days]

foreach k [array names days] {
	puts "key: $k val: $days($k)"
}
