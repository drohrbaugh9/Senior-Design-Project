#connect to mongo database
#connect to mongo collection
#create new document in collection
#adjust script so it takes ID and Timestamp as args
import argparse
import collections
import datetime
from datetime import date
import mongodb
import pymongo
from pymongo import MongoClient


def main(args):
    end_date_time = datetime.datetime.now()
    ID = args["ID"]
    beginning_timestamp = args["beginning_timestamp"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)
