"""
Stuff to know,  like where things are
"""




NYT = "/Users/jimt/work/covid/nyt"
DBOX = "/Users/jimt/Dropbox/work/covid"
AWSHOME = "/home/bitnami"

HTML = NYT + "/html"
IMAGES = NYT + "/images"
DSETS = NYT + "/datasets"
WEB = NYT + "/web"
DBIMG = DBOX + "/html/images"
AWSIMG = AWSHOME + "/htdocs/apps/covid/images"

## States that are too lazy to report on weekends This execise is all about
## keeping the generated files around if it's a weekend.
lazyStates = ["Washington", "Oregon", "South Carolina"]



#### Test below:
def main():
    print(IMAGES)

if __name__ == "__main__":
    main()
