from .TaggedImage import *

def get_new_uuid():
    return str(uuid.uuid4())

class IDataSet(object):

    def __init__(self, destination_path):
        self.destination_path = destination_path

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError( "next not implemented" )
