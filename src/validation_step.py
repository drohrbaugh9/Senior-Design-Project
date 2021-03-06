validation_step.py

import re
import argparse
import store
import regex

def return_id_and_time():
'''returns the ID and timestamp of the file.
 :param file: takes the file in which the data is stored
 :return: the parsed ID and time_stamp

'''
    with open('file.txt', 'r') as searchfile:
        #exchange file.txt with EXact location of file.
    for line in searchfile:
        info_list = line.split(" ")
        #split line of data into two and assign each value to a variable
        LID = info_list[1]
        #get the id from args
        time_stamp = info_list[2]
        #get the time stamp from args'
        return ID, time_stamp

def validate_returning_id(Leaving_ID, Returning_ID):
 '''returns true or false depending on whether or not the ID entered matches the ID in the file.
   :param ID: takes the ID parsed from the file in the return_id_and_time function.
   :return: returns true or false

   '''
           # check the args id
        if LEAVINGID == RETURNINGID:
           return true
           # compare ids
        else:
            return false
# print valdiate_returing_id()
def is_id_trash(ID):
   '''calls the appropriate script based on whether or not the ID passed from David is actually .
   :param ___: takes a
   :return: calls appropriate scrip based on the true/false options
   '''
   # use regex
    if len(ID) == 5 and ID.isdigit():
        return false
        #the string is not trash
    else: 
        return true
        #if the script that tests whether the IDs match returns false, this function will prompt the user to re enter ID
        #If it does return false, I think this is where it would call one of David's functions
        #prompting the user to re-enter their ID
def main(args):
    returningID = args['ID']
    LeaveID, timestamp = get_id_and_time()
    if is_id_trash(returningID)
        #call David with error message
        pass

    if validate_returning_id(LeaveID, returningID)
        pass

    #report to Arduino (depending on what David's script takes)
    #report to Haley (' ' ' ' ' Haley's ' ', may need to do argument formatting)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID must match the one in the file")
    args = vars(parser.parse_args())
    main(args)
