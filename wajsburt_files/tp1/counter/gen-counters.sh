declare -a arr=("a" "j" "m" "o" "r")
if [ ! -e "counter.pat" ]; then
	genpat counter_pat
fi
for i in "${arr[@]}"
do
	./gen-counter.sh $i &> counter"$i".log
done > counter"$i".log
