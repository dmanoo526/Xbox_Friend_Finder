"""
Main file which pulls original set of Xbox user ids and gamertags, iterates through all of them and for each makes a call to the
Xbox API to find all of their friends, then appends only new gamertags to the master_dict. At the very end all new unique ids
and their corresponding gamertags are added to the project under the Friends_Of_Gamertags sheet. This is all done with minimal
calls to the Xbox API.
"""

import inputFromSheets
import outputToSheets
from user import User
from xboxApi import get_friends

#temp = User("bob",1,1)
#print(temp.popularity)


#array of original user ids from Xbox API DATA tab in sheets(nothing is appended here it's solely used for iteration)
#dictionary of gamertags to quickly lookup new gamertags for uniqueness without appending originals to master_dict
original_ids = inputFromSheets.get_ids()
original_gamertags = inputFromSheets.get_gamertags()
original_gamertags_dict = {}
for gamertag in original_gamertags:
    original_gamertags_dict[gamertag] = 0



#Dictionary mapping gamertags(keys) to user objects(values). Create user objects for all original users from Xbox API DATA.
#After returning list of friends from the API for each user in original_users, if the key for the friend's username
#already exists in the dictionary, master_dict['gamertag'].popularity += 1(increment popularity.
#Otherwise, master_dict["gamertag"] = User("gamertag", "id", "hostid")
master_dict = {}
counter = 0 #keeps track of successful calls to the xbox api(aka lookups of original user ids)

for id in original_ids:
#for id in original_ids[0:48]: #dont want to exceed api max call limit
    #print(id)
    if "." in id: #if there is a formatting issue from google sheets for the given id, skip it and don't try to look it up in xbox api
        continue
    user_object_list = get_friends(id)
    if user_object_list is None:
        print("Limit exceeded, pushing current names to sheets")
        break
    for user_object in user_object_list:
        check_string = user_object.gamertag
        if check_string in original_gamertags_dict: #check if the new gamertag is actually in the original or already added from someone else's list
            continue
        elif check_string in master_dict:
            master_dict[check_string].popularity+=1
            continue
        else:
            master_dict[check_string] = user_object
    counter+=1

#for key in master_dict.keys():
    #print(key)

outputToSheets.print_to_sheets(master_dict, counter) #call output to sheets function

