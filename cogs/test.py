import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GSS_KEY
import random

def get_gss_worksheet(gss_name, gss_sheet_name):

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    c = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)

    gs = gspread.authorize(c)

    
    if gss_name == "prsk_songs":
        spreadsheet_key = GSS_KEY

    worksheet = gs.open_by_key(spreadsheet_key).worksheet(gss_sheet_name)

    return worksheet

def song():
    worksheet = get_gss_worksheet(gss_name='prsk_songs', gss_sheet_name='main')
    num = random.randint(0,300)

    value = worksheet.acell("B"+str(num)).value
    return value
    
    #value = int(value) + 1

    #worksheet.update_acell("A1", value)

