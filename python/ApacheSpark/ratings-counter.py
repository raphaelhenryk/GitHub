#SparkContext lets you create a RDD. There must be a SparkConf to create a SparkContext
#SparkConf lets you to configure the SparkContext and defines where to run the program
from pyspark import SparkConf, SparkContext


import collections

#Where the program will run (local) and the program name to rastreability on the spark WebUI
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")

sc = SparkContext(conf = conf)

lines = sc.textFile("file:///C:/Users/RAPHAELHENRYKDASILVA/Documents/GitHub/GitHub/python/Dados/ml-100k/u.data")


ratings = lines.map(lambda x: x.split()[2])

#count(distinct ratings) 3,2 2,1 1,2
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))