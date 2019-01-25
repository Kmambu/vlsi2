declare -a arr=("a" "j" "m" "o" "r")
if [ ! -e "digicode.pat" ]; then
	genpat digicode_pat
fi
for i in "${arr[@]}"
do
	./gen-digicode.sh $i #&> digicode"$i".log
done
