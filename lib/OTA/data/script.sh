find . -name "*csv" -exec sed -i -e 's/^ //g'   {} \;
find . -name "*csv" -exec sed -i -e 's/  / /g' {} \;
find . -name "*csv" -exec sed -i -e 's/ /,/g'  {} \;
