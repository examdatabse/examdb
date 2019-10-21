import app
import docs
import cache
import token_manager
import query
import time


TOKEN_LIFESPAN = 432000


class Server:
    __search_cache = cache.Cache()
    __login_info = dict()
    __token_pool = dict()
    __file_offset = 0

    def __init__(self):
        self.__initialize()
        pass

    def __initialize(self):
        self.__login_info = app.DatabaseManager.load_info()

    # authenticate a login request with provided password and username
    # returns a unique token for the user
    def login_password(self, username, password):
        if username not in self.__login_info.keys():
            return 1, ''
        else:
            if self.__login_info[username]['password'] == password:
                seed, token = token_manager.TokenManager.generate_token()
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

    def get_permission(self, token):
        return self.__login_info[self.__token_pool[token]['username']]['permission']

    def __update_token(self, old_token):
        seed, token = token_manager.TokenManager.generate_token()
        username = self.__token_pool[old_token]['username']
        password = self.__token_pool[old_token]['password']
        self.__token_pool[token] = {'username': username, 'password': password, 'start_time': seed}
        self.__token_pool.pop(old_token, None)
        return token

    def logout(self, token):
        self.__token_pool.pop(token)
        pass

    def change_password(self, old_password, new_password):
        pass

    def change_name(self, first_name, last_name):
        pass

    def add_question(self, form, files):
        app.DatabaseManager.add_questions(form, files)
        pass

    def bulk_upload(self, files):
        file_name = 'uploads/upload_{}.docx'.format(self.__file_offset)
        files.save(file_name)
        questions = docs.parse_doc(file_name, self.__file_offset)
        app.DatabaseManager.bulk_add(questions)
        self.__file_offset += 1

    def bulk_upload_unformatted(self, doc, attr_xml, attr_csv):
        doc_name = 'uploads/upload_{}.docx'.format(self.__file_offset)
        xml_name = 'uploads/upload_{}.xml'.format(self.__file_offset)
        csv_name = 'uploads/upload_{}.csv'.format(self.__file_offset)
        doc.save(doc_name)
        attr_xml.save(attr_xml)
        attr_csv.save(attr_csv)
        questions = docs.parse_doc_unformatted(doc_name, self.__file_offset, xml_name, csv_name)
        app.DatabaseManager.bulk_add(questions)

    def search_by_keyword(self, key_word):
        pass

    def search_by_tags(self, tag):
        pass

    def search_by_serial_number(self, serial_number):
        result, question = query.Query.query_by_id(serial_number)
        return [question]
        pass
