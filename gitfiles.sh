for file in $(ls *.md)
do
    cat ./.gitignore |  grep "$file" > /dev/null  || echo $file
done
