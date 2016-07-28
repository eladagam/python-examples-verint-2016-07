"""
Elad Agam - Exceptions 
03 - Carete ImageFile Class that assert on wrong extension  
"""


class InvalidImageExt(Exception):
    def __init__(self, msg):
        super(InvalidImageExt, self).__init__(msg)



class ImageFile(object):
    def __init__(self, name):
        if not name.endswith(r'.png'):
            raise(InvalidImageExt("wrong type of file"))






import unittest

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()