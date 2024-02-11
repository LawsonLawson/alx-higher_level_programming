import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    """
    Contains multiple testing methods for the Base class.
    """

    def setUp(self):
        """
        Sets up necessary configurations before each test method runs.
        """
        Base._Base__nb_objects = 0

    def test_setValidId(self):
        """
        Test setting a valid integer id for Base object.
        """
        obj = Base(45)
        self.assertEqual(obj.id, 45)

    def test_setValidIdString(self):
        """
        Test setting a string id for Base object.
        """
        obj = Base("string")
        self.assertEqual(obj.id, "string")

    def test_setNoneId(self):
        """
        Test setting None as the id for Base object.
        """
        obj = Base(None)
        self.assertEqual(obj.id, 1)

    def test_setNoneIdMultiple(self):
        """
        Test setting None as the id for Base object multiple times.
        """
        obj1 = Base(None)
        self.assertEqual(obj1.id, 1)
        obj1.id = "bleh"
        self.assertEqual(obj1.id, "bleh")
        obj2 = Base(None)
        self.assertEqual(obj2.id, 2)

    def test_toJSONstrEmptyList(self):
        """
        Test to_json_string method with an empty list.
        """
        self.assertEqual(Base().to_json_string([]), "[]")

    def test_toJSONstrNone(self):
        """
        Test to_json_string method with None argument.
        """
        self.assertEqual(Base().to_json_string(None), "[]")

    def test_toJSONstrWithIntegers(self):
        """
        Test to_json_string method with a list containing integers.
        """
        self.assertEqual(Base().to_json_string([4, 6]), "[4, 6]")

    def test_fromJSONstrEmptyList(self):
        """
        Test from_json_string method with an empty list.
        """
        self.assertEqual(Base().from_json_string("[]"), [])

    def test_fromJSONstrNone(self):
        """
        Test from_json_string method with None argument.
        """
        self.assertEqual(Base().from_json_string(None), [])

    def test_fromJSONstrWithIntegers(self):
        """
        Test from_json_string method with a JSON-formatted list containing integers.
        """
        self.assertEqual(Base().from_json_string("[4, 6]"), [4, 6])

    def test_createWithRectangle(self):
        """
        Test create method with a normal rectangle.
        """
        rect1 = Rectangle(8, 2)
        rect1_dic = rect1.to_dictionary()
        rectA = rect1.create(**rect1_dic)
        self.assertEqual(str(rectA), "[Rectangle] (1) 0/0 - 8/2")

    def test_createWithSquare(self):
        """
        Test create method with a normal square.
        """
        sq1 = Square(4)
        sq1_dic = sq1.to_dictionary()
        sqA = sq1.create(**sq1_dic)
        self.assertEqual(str(sqA), "[Square] (1) 0/0 - 4")

    def test_createWithInvalidClass(self):
        """
        Test create method with an unsupported class.
        """
        with self.assertRaises(TypeError):
            Base().create(**{"name": "test", "value": 10})

if __name__ == '__main__':
    unittest.main()
