#should contain a BlogTest class containing unit test functions for blog functionalities/ stories i.e. init, eq, repr, create post, search post, 
from unittest import TestCase
from unittest import main
import time

from blogging.post import Post
from blogging.blog import Blog

class BlogTest(TestCase):

    def setUp(self):
        self.Blog = Blog(999, "TestBlog", "Test_Blog", "TestBlog@gmail.com")

    def test_eq(self):
         Blog2 = Blog(888, "TestBlog2", "Test_Blog2", "TestBlog2@gmail.com")
         Blog3 = Blog(777, "TestBlog3", "Test_Blog3", "TestBlog3@gmail.com")
         

         self.assertEqual(Blog2, Blog2)
         self.assertNotEqual(Blog2, Blog3)

    def test_repre(self):
         Blog2 = Blog(888, "TestBlog2", "Test_Blog2", "TestBlog2@gmail.com")
         Blog3 = Blog(777, "TestBlog3", "Test_Blog3", "TestBlog3@gmail.com")
         expected2 = "Blog(888, 'TestBlog2', 'Test_Blog2', 'TestBlog2@gmail.com')" 
         expected3 = "Blog(777, 'TestBlog3', 'Test_Blog3', 'TestBlog3@gmail.com')" 

         self.assertEqual(Blog2.__repr__(), expected2)
         self.assertEqual(Blog3.__repr__(), expected3)
         self.assertNotEqual(Blog2.__repr__(), Blog3.__repr__())
    
    def test_createorsearchPost(self):
        Blog2 = Blog(888, "TestBlog2", "Test_Blog2", "TestBlog2@gmail.com")
        Blog3 = Blog(777, "TestBlog3", "Test_Blog3", "TestBlog3@gmail.com")

        Blog2.create_post("Test1", "This is a test Post")
        Blog2.create_post("Test2", "This is a second test Post")
        #Now we should be able to search for these two posts....

        self.assertTrue(Blog2.search_post(1))
        self.assertTrue(Blog2.search_post(2))
        self.assertIsNone(Blog2.search_post(50))

if __name__ == '__main__':
	unittest.main()