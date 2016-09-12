import pickle
import os
import time
import CookieManager

__author__ = 'pedro'


class SessionManager(object):
    """
    Object to handle session operations
    """
    def __init__(self, **paramns):
        """
        Initialize Session
        :return:
        """
        # First we must get the cookie manager
        self.cookie_manager = CookieManager.CookieManager()

        # With the cookie manager we check to see if the session exists
        self.session_id = self.cookie_manager.cookie["session"].value

        current_path = os.getcwd()
        break_path = current_path.split(os.path.sep)
        if break_path[len(break_path) - 1] != "Novo":
            self.session_path = os.path.join("..", "_session", self.session_id)
        else:
            self.session_path = os.path.join("_session", self.session_id)

        if os.path.exists(self.session_path):
            self.session_file = open(self.session_path, 'rb')
            self.session_obj = pickle.load(self.session_file)
        else:
            self.session_file = open(self.session_path, 'wb')
            self.session_obj = {'start_time': time.time()}
            for key in paramns:
                self.session_obj[key] = paramns[key]
            pickle.dump(self.session_obj, self.session_file)

        # Close the session file
        self.session_file.close()

    def get(self, item):
        return self.session_obj[item]

    def set(self, key, value):
        self.session_obj[key] = value

    def unset(self, key):
        if key in self.session_obj:
            del self.session_obj[key]

    def isset(self, key):
        return key in self.session_obj

    def save(self):
        """
        Save the session
        :return:
        """
        self.session_file = open(self.session_path, 'wb')
        pickle.dump(self.session_obj, self.session_file)
        self.session_file.close()
        self.cookie_manager.save()

    def destroy(self):
        """
        Destroy session
        :return:
        """
        # Remove the file
        os.remove(self.session_path)

        # Set the dictionary to empty
        self.session_obj = {}

        # Destroy the cookie
        self.cookie_manager.destroy()