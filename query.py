from examdb.databse import Problems


class Query(object):
    def __init__(self):
        pass

    @staticmethod
    def query_by_id(serial):
        query = Problems.select().where(Problems.serial_code == serial)
        if len(query) == 0:
            return False, ''
        else:
            for q in query:
                return True, {
                    'id': q.id,
                    'serial': q.serial_code,
                    'tags': q.tags,
                    'permission': q.permission,
                    'testlet': q.question,
                    'answer': q.answer,
                    'choice1': q.choice_1,
                    'choice2': q.choice_2,
                    'choice3': q.choice_3,
                    'choice4': q.choice_4,
                    'choice5': q.choice_5,
                    'time': q.time_stamp
                }

    def query_by_tags(self, list_tags):
        pass