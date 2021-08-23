#! /bin/bash

source condasetup.sh
echo ./getlatest.sh
./getlatest.sh

echo python counties.py -n -s Washington -c Snohomish
python counties.py -n -s Washington -c Snohomish
echo python counties.py -n -s Oregon -c Douglas
python counties.py -n -s Oregon -c Douglas
echo python counties.py -n -s Oregon -c Curry
python counties.py -n -s Oregon -c Curry
echo python counties.py -n -s Oregon -c Josephine
python counties.py -n -s Oregon -c Josephine
echo python counties.py -n -s Washington -c Spokane
python counties.py -n -s Washington -c Spokane
echo python counties.py -n -s Texas -c Harris
python counties.py -n -s Texas -c Harris
echo python counties.py -n -s California -c 'Los Angeles'
python counties.py -n -s California -c 'Los Angeles'
echo python counties.py -n -s 'South Carolina' -c Charleston
python counties.py -n -s 'South Carolina' -c Charleston

echo python states.py -n -s California
python states.py -n -s California
echo python states.py -n -s Washington
python states.py -n -s Washington
echo python states.py -n -s Oregon
python states.py -n -s Oregon



echo  python lastday.py -n -s  Washington
python lastday.py -n -s  Washington
echo  python lastday.py -n -s Oregon
python lastday.py -n -s Oregon
echo python lastday.py -n -s 'New Jersey'
python lastday.py -n -s 'New Jersey'
echo  python lastday.py -n -s California
python lastday.py -n -s California
echo python lastday.py -n -s 'South Carolina'
python lastday.py -n -s 'South Carolina' 
