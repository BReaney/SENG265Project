#should contain a PostTest class with post unit tests i.e. initialisation test, repre test, eq test

from unittest import TestCase
from unittest import main
import time
from blogging.post import Post


class PostTest(TestCase):

    def setUp(self):
        self.post = Post(999, "Test", "This is a test post", time.time(), time.time() )

    def test_EqIni(self):
        expected1 = Post(999, "Test","This is a test post", time.time(), time.time() )
        expected2 = Post(888, "Test2", "This is a test post that isnt the same as test 1", time.time(), time.time() )
        expected3 = Post(777, "Test3", "This is a test post that isnt the same as test 1 or 2", time.time(), time.time() )

        self.assertEqual(expected1, expected1)
        self.assertNotEqual(expected1, expected2)
        self.assertNotEqual(expected2, expected3)

    def test_repre(self):
        Post1 = Post(555, "Test", "This is a test post", time.time(), time.time() )
        Post2 = Post(444, "Test2", "This is a test post that isnt the same as test 1", time.time(), time.time() )
        Post3= Post(333, "Test3", "This is a test post that isnt the same as test 1 or 2", time.time(), time.time() )

        expectedS1 = "Post(555, 'Test', 'This is a test post')"
        expectedS2 = "Post(444, 'Test2', 'This is a test post that isnt the same as test 1')"
        expectedS3 = "Post(333, 'Test3', 'This is a test post that isnt the same as test 1 or 2')"

        self.assertEqual(Post1.__repr__(), expectedS1)

        self.assertEqual(Post2.__repr__(), expectedS2)

        self.assertEqual(Post3.__repr__(), expectedS3)
if __name__ == '__main__':
	unittest.main()