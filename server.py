import examdb.app
import examdb.docs
import examdb.cache
import examdb.token_manager
import time


TOKEN_LIFESPAN = 432000


class Server:
    __search_cache = examdb.cache.Cache()
    __login_info = dict()
    __token_pool = dict()

    def __init__(self):
        self.__initialize()
        pass

    def __initialize(self):
        self.__login_info = examdb.app.load_info()

    # authenticate a login request with provided password and username
    # returns a unique token for the user
    def login_password(self, username, password):
        if username not in self.__login_info.keys():
            return 1, ''
        else:
            if self.__login_info[username]['password'] == password:
                seed, token = examdb.token_manager.TokenManager.generate_token()
                self.__token_pool[token] = {'username': username, 'password': password, 'start_time': seed}
                return 0, token
            else:
                return 2, ''

    # authenticate a login request with provided token
    # returns true if token is valid
    def login_token(self, token):
        if token not in self.__token_pool.keys():
            return False, ''
        else:
            if time.time() - self.__token_pool[token]['start_time'] > TOKEN_LIFESPAN:
                return False, ''
            else:
                new_token = self.__update_token(token)
                return True, new_token

    def __update_token(self, old_token):
        seed, token = examdb.token_manager.TokenManager.generate_token()
        username = self.__token_pool[old_token]['username']
        password = self.__token_pool[old_token]['password']
        self.__token_pool[token] = {'username': username, 'password': password, 'start_time': seed}
        self.__token_pool.pop(old_token, None)
        return token

    def change_password(self, old_password, new_password):
        pass

    def change_name(self, first_name, last_name):
        pass

    def add_question(self, files, questions):
        pass

    def bulk_upload(self, files):
        pass

    def search_by_keyword(self, key_word):
        pass

    def search_by_tags(self, tag):
        pass

    def search_by_serial_number(self, serial_number):
        pass
