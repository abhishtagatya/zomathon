import os
import sys
import json
import requests

class ZomatoAPI(object):
    """
    Performs requests to the Zomato API service.
        Documentation : https://developers.zomato.com/documentation
    """

    def __init__(self, key, headers=None, debug_mode=False):
        """
        :params key: zomato API key. required and provided here
            https://developers.zomato.com/api
        :type key: string

        :params headers: custom HTTP headers. default is
            {
                "User-agent": "curl/7.43.0",
                "Content-type": "application/json",
                "X-Zomato-API-Key": api-key
            }
        :type headers: dict
        """

        self.key = key
        self.baseurl = 'https://developers.zomato.com/api/v2.1/'
        self.debug = debug_mode

        if (headers != None):
            self.headers = headers
        else :
            self.headers = {
                "User-agent": "curl/7.43.0",
                "Content-type": "application/json",
                "X-Zomato-API-Key": self.key
            }

    def category(self):
        """ Returns the list of available categories in Zomato. """
        category_url = self.baseurl + 'categories'
        response = requests.get(url=category_url, headers=self.headers).json()

        if(self.debug):
            print(category_url)

        return response

    def cities(self, count=5, **option):
        """ Returns the Zomato ID and details of a city.

        :params option

            :params q: query by city name.
            :type q: string

            :params coordinate: the latitude and longitude of the city or location.
                example : (latitude, longitude)
            :type coordinate: string, list or tuple

            :params city_ids: the id of the city or location.
            :type city_ids: interger or string*
                it can take more than one value, simply separate it using commas
                example : "74,75,76"

        :params count: the max number of list items. default is 5 items.
        :type count: interger
        """

        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']


        cities_url = self.baseurl + 'cities'
        response = requests.get(url=cities_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()

    def collections(self, count=5, **option):
        """ Returns Zomato's restaurant collection in a city or location.

        :params option

            :params city_id: the id of the city or location.
            :type city_id: interger or string*
                it can take more than one value, simply separate it using commas
                example : "74,75,76"

            :params coordinate: the latitude and longitude of the city or location.
                example : (latitude, longitude)
            :type coordinate: string, list or tuple

        :params count: the max number of list items. default is 5 items.
        :type count: interger
        """

        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']


        collection_url = self.baseurl + 'collections'
        response = requests.get(url=collection_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()

    def cuisines(self, **option):
        """ Returns Zomato's list of available cuisines in a city or location.

        :params option

            :params city_id: the id of the city or location.
            :type city_id: interger or string*
                it can take more than one value, simply separate it using commas
                example : "74,75,76"

            :params coordinate: the latitude and longitude of the city or location.
                example : (latitude, longitude)
            :type coordinate: string, list or tuple
        """


        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']


        cuisines_url = self.baseurl + 'cuisines'
        response = requests.get(url=cuisines_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()

    def establishments(self,**option):
        """ Returns Zomato's list of restaurant types in a city or location.

        :params option

            :params city_id: the id of the city or location.
            :type city_id: interger or string*
                it can take more than one value, simply separate it using commas
                example : "74,75,76"

            :params coordinate: the latitude and longitude of the city or location.
                example : (latitude, longitude)
            :type coordinate: string, list or tuple
        """

        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']


        establishment_url = self.baseurl + 'establishments'
        response = requests.get(url=establishment_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()


    def geocode(self, coordinate):
        """ Returns Zomato's list of restaurant index at a given coordinate.

        :params coordinate: the latitude and longitude of the city or location.
            example : (latitude, longitude)
        :type coordinate: string, list or tuple
        """

        if type(coordinate) is str:
            lat, lon = coordinate.split()
        else :
            lat, lon = coordinate

        option = {
            'lat' : lat,
            'lon' : lon
        }

        geocode_url = self.baseurl + 'geocode'
        response = requests.get(url=geocode_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()

    def location_details(self, entity_id, entity_type):
        """ Returns Zomato's list of index, cuisines and best
            rated restaurant in a city or location.

        :params entity_id: the id of a location (can be found in locations() function).
        :type entity_id: interger

        :params entity_type: the type of location the id represents
        (can be found in locations() function).
            types: city, zone, subzone, landmark, metro, group
        :type entity_type: string
        """

        option = {
            'entity_id' : entity_id,
            'entity_type' : entity_type
        }

        locdetails_url = self.baseurl + 'location_details'
        response = requests.get(url=locdetails_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()

    def locations(self, count=5, **option):
        """ Returns Location ID and details by query.

        :params option

            :params q: query by location name.
            :type q: string

            :params coordinate: the latitude and longitude of the city or location.
                example : (latitude, longitude)
            :type coordinates: string, list or tuple

        :params count: the max number of list items. default is 5 items.
        :type count: interger
        """

        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']


        location_url = self.baseurl + 'locations'
        response = requests.get(url=location_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()

    def dailymenu(self, res_id):
        """ Returns a list of Daily Menu at a restaurant.

        :params res_id: the id of a restaurant (can be found in restaurant() function).
        :type res_id: interger
        """

        dailymenu_url = self.baseurl + 'dailymenu'
        option = {
            'res_id' : res_id
        }

        response = requests.get(url=dailymenu_url, params=option, headers=self.headers)

        if (self.debug):
            print(response.url)

        return response.json()

    def restaurant(self, res_id):
        """ Returns detailed information of a restaurant.

        :params res_id: the id of a restaurant (can be found in restaurant() function).
        :type res_id: interger
        """

        restaurant_url = self.baseurl + 'restaurant'
        option = {
            'res_id' : res_id
        }

        response = requests.get(url=restaurant_url, params=option, headers=self.headers)

        if (self.debug):
            print(response.url)

        return response.json()

    def reviews(self, res_id, count=5):
        """ Returns a list of reviews at a restaurant.

        :params res_id: the id of a restaurant (can be found in restaurant() function).
        :type res_id: interger

        :params count: the max number of list items. default is 5 items.
        :type count: interger
        """

        reviews_url = self.baseurl + 'reviews'
        option = {
            'res_id' : res_id
        }

        response = requests.get(url=reviews_url, params=option, headers=self.headers)

        if (self.debug):
            print(response.url)

        return response.json()

    def search(self, count=5, **option):
        """ Returns restaurant search result by arguments passing in the function.
        To learn more on this feature, please read the implementation notes
        in the Zomato API documentation.

            https://developers.zomato.com/documentation#!/restaurant/search

        :params option

            :params q: query by city name.
            :type q: string

            :params entity_id: the id of a location (can be found in locations() function).
            :type entity_id: interger

            :params entity_type: the type of location the id represents
            (can be found in locations() function).
                types : city, zone, subzone, landmark, metro, group
            :type entity_type: string

            :params start: fetch results after this offset.
            :type start: interger

            :params coordinates: the latitude and longitude of the city or location.
                example : (latitude, longitude)
            :type coordinates: string, list or tuple

            :params radius: radius around (lat,lon)
                to define search area, defined in meters(M)
            :type radius: interger or float

            :params cuisines: list of cuisine id's
            :type cuisines: interger or string*
                it can take more than one value, simply separate it using commas
                example : "74,75,76"

            :params establishment_type: the id of an establishment
                (can be found in establishments() function)
            :type establishment_type: interger or string

            :params collection_id: the id of a collection.
                (can be found in collections() function)
            :type collection_id: interger or string

            :params category: the id of a category.
                (can be found in category() function)
            :type category: interger or string

            :params sort: sorting search result methods.
                methods: cost, rating, real_distance
            :type sort: string

            :params order: order of search result methods.
                methods: asc or desc
            :type order: string

        :params count: the max number of list items. default is 5 items.
        :type count: interger
        """

        if 'coordinate' in option:
            if type(option['coordinate']) is str:
                lat, lon = option['coordinate'].split()
            else :
                lat, lon = option['coordinate']

            option['lat'] = lat
            option['lon'] = lon
            del option['coordinate']


        search_url = self.baseurl + 'search'
        response = requests.get(url=search_url, params=option, headers=self.headers)

        if(self.debug):
            print(response.url)

        return response.json()
