for dir in $(ls | grep chap)
do
    cd $dir
    for file in $(ls | grep .py)
    do
	preName=$(echo $file | sed -E 's/^(.*).py$/\1/')
	output=$preName'.md'
	rename=$(echo $output | sed -E 's/^(.*)_(.*)$/\1\2/')
	. MDWriter $file
	mv $output $rename
    done
    cd ..
done
