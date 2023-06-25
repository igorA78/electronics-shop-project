
class InstantiateCSVError(Exception):
    def __init__(self):
        self.msg = 'Файл items.csv поврежден'
    def __str__(self):
        return self.msg
