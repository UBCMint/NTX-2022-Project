cd Data/Raw Data/Color
rm *.csv
for FILE in *.txt; do 
    tail -n +5 "$FILE" > "../csv_data/${FILE%.*}.csv";
done