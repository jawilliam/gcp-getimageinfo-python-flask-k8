import web_detect
import argparse

import unittest

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:/Zenta/Projects/nexus-poc-mi-fraude-dev01-7fa6fcccceae.json"

class TestStringMethods(unittest.TestCase):

    def test_old_vw_bug_and_van(self):
        annotations = web_detect.annotate("http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg")
        self.assertTrue(True in (entity.description == "Volkswagen" for entity in annotations.web_entities))
        self.assertTrue(True in (entity.description == "Car" for entity in annotations.web_entities))
        self.assertTrue(True in (entity.description == "Van" for entity in annotations.web_entities))

#def get_annotations(path):
    #web_detect.report(web_detect.annotate(path))

if __name__ == '__main__':
    unittest.main()
    #print('Web URI')
    #get_annotations("http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg")
    #print('Local File')
    #get_annotations('D:/Zenta/Projects/Falabella/GetImageInfo/GetImageInfo/img/cluster.gif')