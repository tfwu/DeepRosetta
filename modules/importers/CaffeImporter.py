from core.BaseImporter import BaseImporter

class CaffeImporter(BaseImporter):
    """ Class modeling a Caffe importer

    """
    def __init__(self):
        pass

    def load(self, file_path):
        print 'Loading Caffe model: %s' % file_path
        return {}

    def loadFromObject(self, frameworkObj):
        return NotImplementedError
