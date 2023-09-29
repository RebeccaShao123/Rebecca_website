mkdir -p hw_test
cd hw_test
for i in $(seq 1 256)
do
    time=`date +%s%6N`
    mkdir -p MSDM$i
    cd MSDM$i
    touch 'time_till_now.txt'
    echo microseconds since 1970-01-01 00:00:00 UTC: >> time_till_now.txt
    echo "<"$time">" >> time_till_now.txt
    cd ..
done