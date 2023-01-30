from tui import *

"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""
import csv

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""
# private function for reading the data file
def reading_data_file():
    reviews = []
    with open('data/hotel_reviews.csv', 'r') as file:
        dataset = csv.reader(file, delimiter =',', quotechar='"')
        next(dataset)  # removes the header
       # data_lines = list(dataset)
        for row in dataset:
            reviews.append(row)
           # print(row[1])
    return reviews

#print(reading_data_file())

#all_reviews_for_test = reading_data_file()

#Retrieve the reviews for a hotel where the hotel name is specified by the user
def number_of_all_reviews(all_reviews):
    total_reviews(all_reviews)

#number_of_all_reviews(all_reviews_for_test)

def retrive_reviews_for_hotel_name(list_of_reviews, hotelname=None):
    hotel_reviews = list()
    #print("hi")
    for review in list_of_reviews:
        #print(review)
       # print(hotelname)
       # cols = review.split(",")
      #  print(review[1])
        if review[1] == hotelname:
            hotel_reviews.append(review)
           # print(review)
    return hotel_reviews
#retrive_reviews_for_hotel_name(all_reviews_for_test, "Apex Temple Court Hotel")


#Retrieve the reviews for the dates specified by the user
def retrive_reviews_for_the_date(list_of_reviews, review_date=None):
    hotel_reviews = list()
    #print("hi")
    for review in list_of_reviews:
        #print(review)
       # print(hotelname)
       # cols = review.split(",")
      #  print(review[0])
        if review[0] == review_date:
            hotel_reviews.append(review)
           # print(review)
    return hotel_reviews
#retrive_reviews_for_the_date()


#Retrieve all the reviews grouped by the reviewer’s nationality
def retrive_reviews_user_nationality(list_of_reviews, nationality=None):
    hotel_reviews = list()
    #print("hi")
    for review in list_of_reviews:
        #print(review)
       # print(hotelname)
       # cols = review.split(",")
      #  print(review[2])
        if review[2] == nationality:
            hotel_reviews.append(review)
           # print(review)
    return hotel_reviews
#retrive_reviews_user_nationality()

#the total number of negative reviews on that date
def total_number_of_negative_reviews(list_of_reviews, negative_review = None):
    hotel_reviews = list()
    for review in list_of_reviews:
        if review[3] == negative_review:
            hotel_reviews.append(review_dates())
    return hotel_reviews
total_number_of_negative_reviews(review_dates, "05/03/2016")
