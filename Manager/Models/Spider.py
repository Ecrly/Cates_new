
class SpiderObject(object):
    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._status = kwargs['status']
        self._file = kwargs['file']

    def get_name(self):
        return self._name

    def get_status(self):
        return self._status

    def get_file(self):
        return self._file

    def set_status(self, status):
        self._status = status