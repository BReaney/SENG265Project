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

         time1 = time.time()
         time2 = time.time()
         time3 = time.time()

         Post1 = Post(555, "Test", "This is a test post", time1, time1)
         Post2 = Post(444, "Test2", "This is a test post that isnt the same as test 1", time2, time2 )
         Post3= Post(333, "Test3", "This is a test post that isnt the same as test 1 or 2", time3, time3 )

         expected2 = "Blog(888, 'TestBlog2', 'Test_Blog2', 'TestBlog2@gmail.com', 0)"
         expected3 = "Blog(777, 'TestBlog3', 'Test_Blog3', 'TestBlog3@gmail.com', 0)" 
        
         self.assertEqual(Blog2.__repr__(), expected2)
         self.assertEqual(Blog3.__repr__(), expected3)
         self.assertNotEqual(Blog2.__repr__(), Blog3.__repr__())

         expected2a = "Blog(888, 'TestBlog2', 'Test_Blog2', 'TestBlog2@gmail.com', 1)"
         
         self.assertNotEqual(Blog2.__repr__(), expected2a)

         Blog2.create_post('Post1', "This is a test post")

         self.assertEqual(Blog2.__repr__(), expected2a)
    
    def test_delete_blog(self):
         Blog2 = Blog(888, "TestBlog2", "Test_Blog2", "TestBlog2@gmail.com")

         Blog2.create_post("Test", "This is a test post")
         Blog2.create_post("Test 2", "This is a 2nd test post")
         
         ###deletes post
         self.assertIsNotNone(Blog2.search_post(1))
         self.assertTrue(Blog2.delete_post(1))
         self.assertIsNone(Blog2.search_post(1))

         ###post deletion not affected by earlier post deleted
         self.assertIsNotNone(Blog2.search_post(2))
         self.assertTrue(Blog2.delete_post(2))
         self.assertIsNone(Blog2.search_post(2))

    def test_post_and_blog_id_incrementation(self):
         Blog2 = Blog(888, "TestBlog2", "Test_Blog2", "TestBlog2@gmail.com")
         Blog3 = Blog(777, "TestBlog3", "Test_Blog3", "TestBlog3@gmail.com")

         time1 = time.time()
         time2 = time.time()
         time3 = time.time()

        #  Post1 = Post(555, "Test", "This is a test post", time1, time1)
        #  Post2 = Post(444, "Test2", "This is a test post that isnt the same as test 1", time2, time2 )
        #  Post3= Post(333, "Test3", "This is a test post that isnt the same as test 1 or 2", time3, time3 )

         expected2 = "Blog(888, 'TestBlog2', 'Test_Blog2', 'TestBlog2@gmail.com', 0)"
         expected3 = "Blog(777, 'TestBlog3', 'Test_Blog3', 'TestBlog3@gmail.com', 0)" 

         self.assertEqual(0, Blog2.code)
         Blog2.create_post("Test", "This is a test post")
         self.assertEqual(1, Blog2.code)
         Blog2.create_post("Test 2", "This is a 2nd test post")
         self.assertEqual(2, Blog2.code)

         Post1 = Blog2.search_post(1)
         Post2 = Blog2.search_post(2)
         self.assertEqual(Post1.code, 1)
         self.assertEqual(Post2.code, 2)

         self.assertIsNotNone(Blog2.search_post(2))
         self.assertTrue(Blog2.delete_post(2))
         self.assertIsNone(Blog2.search_post(2))

         ###deletion does not affect incrementation
         self.assertEqual(2, Blog2.code)

         ###posts continue to increment correctly
         Blog2.create_post("Test 3", "The code of this test should be unaffected by the prior test deletion")
         self.assertEqual(3, Blog2.code)
         self.assertEqual(Blog2.search_post(3).code, 3)


    
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