import pandas as pd

print(pd.__version__) # prind out the version of pandas

cities_names = pd.Series(["San Francisco", "San Jose", "Sacramento"])
cities_population = pd.Series([852000,101500,48500])

cities_dataFrame = pd.DataFrame({"City Name": cities_names, "Population": cities_population})
# saved the data frame obj to a cities_dataframe var
print(cities_dataFrame["City Name"])
print(cities_dataFrame["Population"])

#to access the specific element in a column
print(cities_dataFrame["City Name"][1] + " City's population is: " + str(cities_dataFrame["Population"][1]))
#in the meantime, just like the python list, you can access and display multiple
print(cities_dataFrame["City Name"][1:])

#to manipulate the value in the specific series
cities_dataFrame["City Name"][1] = "Chicago"; cities_dataFrame["Population"][1] = "2300000"
print(cities_dataFrame)

#we can also do some boolean operation
cities_population = cities_population.apply(lambda val: val > 1000000) # i dont think the lambda is working
print(cities_population)

#we can also know about how many elements are there in the df
print(cities_names.index)
print(cities_population.index)

#in the meantime, we can re-arrange the order fo the element, by manipulate the index
print(cities_dataFrame.reindex([2,0,1]))
#print(cities_dataFrame)



