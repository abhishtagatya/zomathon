import os
import sys
import json
import requests

from zomathon import ZomatoAPI

API_KEY = os.environ.get('ZOMATO_API_KEY')

def example():
    """
    Here are some examples of using the Zomato API
    """

    # Setting up your authentication
    zom = ZomatoAPI(API_KEY)

    def getCategory():
        # Get the category
        get_category = zom.category()

        print('Here are all the available categories in Zomato')
        for num, category in enumerate(get_category['categories']):
            print("{number}. {name}".format(
                number=num + 1,
                name=category['categories']['name']
            ))

    def nearbyRestaurant():
        # Find the nearby restaurant
        print('Finding Nearby Restaurant\n')
        while True:
            print('Input your location using latitude and longitude :\n')
            latitude = input('latitude : ')
            longitude = input('longitude : ')

            coordinate = "{lat} {lon}".format(lat=latitude, lon=longitude)
            nearby = zom.geocode(coordinate=coordinate)

            try :
                for num, restaurant in enumerate(nearby['nearby_restaurants']):
                    print('{number}, {name} - {addr}'.format(
                        number= num+1,
                        name=restaurant['restaurant']['name'],
                        addr=restaurant['restaurant']['location']['address']
                        ))
            except :
                print('Something went wrong when fetching nearby restaurant...')

            print('\nTry Again?')
            confirmation = input('Yes/No :').lower()

            if 'y' in confirmation:
                continue
            else :
                break

    def readReviews():
        # Get the restaurant reviews
        print('Reading Peoples Reviews on Restaurants')

        while True:
            print('Example ID : 16782899')
            id = input('Enter Restaurant ID : ')
            review = zom.reviews(res_id=id)

            try :
                for num, comment in enumerate(review['user_reviews']):
                    username = comment['review']['user']['name']
                    foodie_level = comment['review']['user']['foodie_level']
                    comment_text = comment['review']['review_text']

                    print('{name} - {level}\nCommented : {text}'.format(
                        name=username,
                        level=foodie_level,
                        text=comment_text
                        ))
            except :
                print('Something went wrong when fetching the comment section...')

            print('\nTry Again?')
            confirmation = input('Yes/No :').lower()

            if 'y' in confirmation:
                continue
            else :
                break

    while True:

        print('\nWelcome to the API Example :')
        print(' 0. Category\n 1. Find Restaurant\n 2. Read Reviews\n 3. Quit\n')

        try :
            select = int(input())
            if (select == 0):
                getCategory()
            elif (select == 1):
                nearbyRestaurant()
            elif (select == 2):
                readReviews()
            elif (select == 3):
                sys.exit()
            else :
                print('No command found')

        except (KeyboardInterrupt, ValueError, EOFError):
            sys.exit()



if __name__ == '__main__':
    example()
