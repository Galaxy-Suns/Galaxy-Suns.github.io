rmdir tmp
mkdir tmp
for file in $@  
do 
    cat $file | sed -E 's/(.*)(D:\\code\\md\\|C:\\code\\md\\)(.*)/\1\3/' > tmp/$file 
done
