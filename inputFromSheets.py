"""
This file is comprised of functions that handle input from the Xbox_API_DATA sheet in the project.
All this does is pull in the 9984 ids and gamertags of Xbox users and return them to the calling file.
@Input: None
@Return Type: String Array (of the original xbox user ids from which we find all friends)
"""

#must run "pip install gspread oauth2client" in cmd local project file to allow interaction with sheets api
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

project = client.open("Cocal_Xbox_Users_Dhanvin_Project") #open the google sheets file with specified title(copy of original)

sheet = project.worksheet("Xbox_API_DATA") #open specific sheet in google sheets file

def get_ids():

    cell_list = sheet.range("I2:I9985") #pull all user id records from specific sheet to put into list in gamertags.py to iterate through

    return_data = []

    for cell in cell_list: #iterate through specified cells and store in gamertags.py
        return_data.append(cell.value)

    #print(len(return_data))

    return return_data

def get_gamertags():
    cell_list = sheet.range("H2:H9985") # pull all gamertag records from specific sheet to put into list in gamertags.py

    return_data = []

    for cell in cell_list: # iterate through specified cells and store in gamertags.py
        return_data.append(cell.value)

    #print(len(return_data))

    return return_data

if __name__ == "__main__":
    get_ids()
    print()
    get_gamertags()







