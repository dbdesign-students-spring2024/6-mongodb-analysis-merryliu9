import pymongo

try:
    # Connect to the MongoDB database
    connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                     username="ql2453",
                                     password="JKCqZpsy",
                                     authSource="ql2453")
    print("Connected to MongoDB")
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e)
    exit()

try:
    db = connection["ql2453"]
    collection = db["listings"]
    print("Database and collection accessed")

    # Find the first 3 unique host names
    unique_host_names = collection.distinct("host_name")
    print("First three unique host names:", unique_host_names[:3])

    # Debugging: Print the number of unique host names found
    print("Total unique host names found:", len(unique_host_names))
except Exception as e:
    print("An unexpected error occurred:", e)

