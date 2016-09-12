#!c:/Anaconda3/python
# coding: UTF-8

import http.cookies
import uuid
import os


__author__ = 'pedro'


class CookieManager(object):
    """
    Used to manage cookies
    """
    def __init__(self):
        # When we start we get the cookie string
        self.cookstr = None

        # We set the cookie to be empty
        self.cookie = None

        # Open cookie
        self.selected = False

        # Get the cookie
        self.get_cookie()

    def get_cookie(self):
        """
        Get cookie
        :return:
        """
        if not self.selected:
            self.cookstr = os.environ.get("HTTP_COOKIE")

            # If the cookie string is empty we create a new cookie
            if not self.cookstr:
                self.create_new_cookie()
            else:
                self.cookie = http.cookies.SimpleCookie(self.cookstr)

            self.selected = True

    def create_new_cookie(self):
        """
        Create a new cookie
        :return:
        """
        # We create a new cookie
        self.cookie = http.cookies.SimpleCookie()

        # We set its id
        self.cookie['session'] = str(uuid.uuid4())

        # Set the cookie session expiration time to 1 hour
        self.cookie["session"]["expires"] = 1 * 60 * 60

        # Set the session path
        self.cookie["session"]["path"] = "/"

        print(self.cookie)

    def set(self, key, value):
        """
        Set the cookie value
        :param var:
        :param value:
        :return:
        """
        # Then we set the variable in the cookie
        self.cookie['session'][key] = value

        # then we print the cookie
        print(self.cookie)

    def get(self, item):
        """
        Get the value of a cookie variable
        :param var:
        :return:
        """
        # Then we set the variable in the cookie
        return self.cookie['session'][item]

    def save(self):
        # Refresh expiration date
        # self.cookie["session"]["expires"] = 1 * 60 * 60

        # Print the cookie again
        print(self.cookie)

    def destroy(self):
        self.cookie["session"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"
