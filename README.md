# COVID Graph

## Graph COVID-19 cases and deaths using data supplied by the New York Times

I started this project as a way to become familiar with Pandas and Matplotlib.
All the python files are in dreadful need of refctoring.

## Examples

Most of the actual running of the code occurs in dolatest.sh. Here's
some examples (taken from dolatest.sh):

### Produce graph of Covid cases and deaths by county:
python counties.py -n -s California -c 'Los Angeles'

### Produce graphs of Covid dases and deaths by state:
python states.py -n -s Washington

### Produce graphs of Covid cases and deaths by county on the last(most current) day:
python lastday.py -n -s 'New Jersey'

The options -s and -c are self-explanatory. 
The -n option prevents the formation of an interactive graph at runtime.
A static graph of the data is always produced.


## Setup
- symlink (or copy) makefile from nyt/accessory/makefile to wherever is
comfortable and edit to taste. I put this in my home diectory as a
tribute to my laziness.
- edit nyt/.env to match your system.
- ADD Avg and Census
