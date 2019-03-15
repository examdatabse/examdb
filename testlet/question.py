class Question(object):
    _id = 0
    _serial_code = ''
    _tags = []
    _question = ''
    _image = ''
    _answer = ''
    _ans_images = {}
    _ans_choices = {}
    _time_stamp = 0

    def __init__(self, id, serial, tags, question, img, ans, ans_imgs, ans_choices, time):
        self._id = id
        self._serial_code = serial
        self._tags = tags
        self._question = question
        self._image = img
        self._answer = ans
        self._ans_images = ans_imgs
        self._ans_choices = ans_choices
        self._time_stamp = time

    def get_info(self):
        return {
            'id': self._id,
            'serial': self._serial_code,
            'tags': self._tags,
            'question': self._question,
            'image': self._image,
            'answer': self._answer,
            'ans_images': self._ans_images,
            'ans_choices': self._ans_choices,
            'time': self._time_stamp
        }
