print ("I love {0} {1} {2}".format("python","programming","!"))
# {0} , {1}, {2} refer first and second argument provided to the format.

# Mixing positional and named arguments
sentance = "{0} and {1} are {2} company in {city}."
print(sentance.format("Aktiv software","Icreative technologies","best",city="ahmedabad"))

# Format integers and floats with specified width and percision

print("Fav number:{0:1d}, Seconf fav number:{1:8.2f}".format(223,0.111123))

# Demonstrate order swapping and formatting precision

print("Second argument: {1:3d}, first one:{0:8.2f}".format(52.51,17))
