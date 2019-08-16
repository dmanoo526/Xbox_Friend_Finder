"""
This file defines functions allowing us to return a list of all a user's friends from the Xbox Api based on their unique id
"""
from subprocess import PIPE, run
from user import User
import json

def get_friends(id):
	#NEXT LINE MUST HAVE REAL AUTH TOKEN INSERTED TO RUN!!!
    call_string = 'curl -H "X-AUTH: XXXXXXXXXXXXXXXXXXXX" https://xboxapi.com/v2/' + id +"/friends" #change XXXXXXXXXX to the real token to run
    result = run(call_string, stdout=PIPE, stderr=PIPE, universal_newlines=True) #run as subprocess
    data_list = result.stdout #receive result(json) from subprocess execution
    #print(data_list)
    user_object_list = []
    if data_list == '{"success":false,"error_code":403,"error_message":"API Rate Limit Exceeded"}':
        print("Api call limit exceeded")
        return
    if data_list != '{"code":1029,"source":"PeopleFd","description":"This request is not allowed for this title.","traceInformation":null}':
        json_data = json.loads(data_list)
        for user in json_data:
            temp = User(user["Gamertag"],user["id"],user["hostId"])
            user_object_list.append(temp)
            #print("Gamertag: {}, Id: {}, HostId: {}".format(temp.gamertag,temp.id,temp.hostid))
    #else:
        #print("error")
    #print(user_object_list[0].gamertag)
    return user_object_list


if __name__ == "__main__":
    get_friends("")