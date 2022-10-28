find . -name "inv_gm*csv" -exec sed -i -e 's/^ //g'   {} \;
find . -name "inv_gm*csv" -exec sed -i -e 's/  / /g' {} \;
find . -name "inv_gm*csv" -exec sed -i -e 's/ /,/g'  {} \;
