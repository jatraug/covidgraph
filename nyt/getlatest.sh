## -*-sh-*-

mkdir -p datasets
mkdir -p images

    curl -o datasets/us-states.csv https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

curl -o datasets/us-counties.csv https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

curl -o datasets/us.csv https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv

curl -o datasets/us-counties-2020.csv https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2020.csv

