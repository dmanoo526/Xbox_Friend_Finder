## Dhanvin Manoo Xbox API Challenge: All New Unique Friends of List of Users

### How it works:

This solution aims to find all unique friends of users from Xbox_API_DATA tab in Cocal_Xbox_Users_Dhanvin_Project and push them to Friends_Of_Gamertags_in_Xbox_API_DATA_Dhanvin tab
It takes all 9984 users in the original tab and appends unique friends of all of them to the second tab
If a friend of one user is already listed as a friend of another, it keeps track of this using the popularity attribute

_________________________________________________________________

1. Pull in all original user gamertags and ids from Xbox_API_DATA tab(first tab) in Cocal_Xbox_Users_Dhanvin_Project

2. Store original user ids in a normal array store original users gamertags in a dictionary structure(hashmap) so that lookup time is O(1)

3. Create a master dictionary(hashmap for O(1) lookup) to store only new unique friends as user objects defined in the user.py file which contain their id, gamertags, and popularity

Note: the point of the two hashmaps is one only stores new unique friends the other stores the original users and both are checked when attempting to determine uniqueness
of a new friend as one original user may have another original user listed as a friend. We can't only check the master dictionary as that only contains new friends not original users
so we must have a separate dictionary for original users themselves. The original user's ids are stored in an array to simply iterate through all of them as the xbox api works
off of ids not gamertags.

3. For each id in the array, call the xbox api to get a json list of all of their friends and their ids

4. Sort the json file and for each friend and their corresponding id, determine if this friend is already listed in the original gamertag dictionary as well as the master dictionary.
If it is not in either, then we add it to the master dictionary. If it is already in the master dictionary, we increment its popularity.

5. At the very end once we have populated the master dictionary of all the user's new unique friends, we push all of the new friends and their corresponding data to Friends_Of_Gamertags_in_Xbox_API_DATA_Dhanvin

_________________________________________________________________

### Issues/Bottlenecks:

Note: There are some missing files. The creds.json to access the google sheets api has not been pushed to github for obvious reason. The authentication token for the xbox api file
(in xboxApi.py) has also been censored and must be changed from "XXXXXXXXXX" to the real token. File creds.json and the authentication token must be added for this to run.

1. The xbox api has a limit to the number of calls made hourly. It is between 50 and 100(only around 75 of 9984 original users actually get looked up in the xbox api)

2. The google sheets api has an even smaller limit of calls to push data.(only around 60 new friends and their data can be pushed to google sheets)

In total only the first few original users have their unique friends pushed to sheets due to api limits on both sides.

3. Google sheets automatically formats to scientific notation and all entries from the input sheet in this format must be and are skipped and unfortunately outputs are also formatted this way.
There is no way around aside from manually inserting an apostrophe at the beginning of every entry. Formatting it any other way causes the least significant digit to be rounded which obviously doesn't work for an id.

When the xbox api limit is reached, the program automatically stops making calls to the xbox api and checks the remaining potential unique friends then attempt to push all of them to the sheets api.
Whenever the sheets api sends the api limit reached error, the program prints how many new friends were actually pushed and exits.
If the database wasn't google sheets, we could print all the friends of atleast the first 75 original users(a few thousand entries).
Next steps are to potentially automatically run the xbox api lookups every hour so the limit refreshes, consolidate current master dict with a long term storage dict, then also automate pushing each hour to 
sheets to bypass api limits of both sides and get all data for the full set of 9984 users(run in batches and consolidate dictionaries).
