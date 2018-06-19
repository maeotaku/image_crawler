from .Base.IDataSet import *
from .Base.TaggedImage import *
import csv
import os
import urllib
import uuid
import datetime
import re
from xml.sax.saxutils import unescape

class Properties(dict):

    def get_uuid(self):
        return get_new_uuid()

    def __init__(self, image_data, search_query, catclass, *args, **kw):
        super(Properties,self).__init__(*args, **kw)
        super(Properties,self).__setitem__("Class", catclass)
        super(Properties,self).__setitem__("SearchQuery", search_query)
        super(Properties,self).__setitem__("URL", image_data["link"])
        super(Properties,self).__setitem__("Title", image_data["title"])
        super(Properties,self).__setitem__("Kind", image_data["kind"])
        super(Properties,self).__setitem__("DisplayLink", image_data["displayLink"])
        super(Properties,self).__setitem__("MIME", image_data["mime"])

class ClassDataSet(IDataSet):

    def __init__(self, destination_path, images_data, catclass, search_query):
        super(ClassDataSet, self).__init__(destination_path)

        self.search_query = search_query
        self.catclass = catclass
        self.images_data = images_data
        print("File loaded...", len(self.images_data))

        self.current = 0
        self.high = len(self.images_data)

    def create_new_img(self, img_name, url, properties):
        return TaggedImageURL(img_name, url=url, properties=properties)

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            while self.current < self.high:
                image_data = self.images_data[self.current]
                url = image_data["link"]
                props = Properties(image_data, self.search_query, self.catclass)
                uuid = props.get_uuid()
                self.current += 1
                return self.create_new_img(uuid, url, props)
            raise StopIteration
