"""
This file is comprised of a function which takes a final master dictionary from gamertags.py and writes the data to the
Friends_Of_Gamertags sheet.
@Input: takes a dictionary and writes the new user values to google sheets api
@Return Type: None
"""

#must run "pip install gspread oauth2client" in cmd local project file to allow interaction with sheets api
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

project = client.open("Cocal_Xbox_Users_Dhanvin_Project") #open the google sheets file with specified title(copy of original)

sheet = project.worksheet("Friends_Of_Gamertags_in_Xbox_API_DATA_Dhanvin") #open specific sheet in google sheets file

def print_to_sheets(dict, counter):
    sheets_index = 2 #keep track of current index in google sheets
    try:
        for user in dict.values():
            row = [user.gamertag, user.id, user.hostid, user.popularity]
            sheet.insert_row(row, sheets_index)
            sheets_index+=1
        sheet.cell(1,5).value = "Total number of successful xbox api calls: {}".format(counter) #print number of api calls to google sheets
    except:
        print("Sheets api limit reached")
    rows_added = sheets_index - 2 #started at index 2 find how many total rows added
    print("Google sheets successfully updated with {} rows added and {} original users had their friends looked up in the api before the limit was exceeded".format(rows_added,counter))
