from django.test import TestCase
from .models import Blog, Author  # Adjust the import based on your app structure

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create an Author instance for testing
        cls.author = Author.objects.create(name='Test Author')

    def test_blog_creation(self):
        # Create a Blog instance
        blog = Blog.objects.create(
            author=self.author,
            title='Test Blog Title',
            body='This is the body of the test blog.'
        )
        # Check if the blog was created correctly
        self.assertEqual(blog.title, 'Test Blog Title')
        self.assertEqual(blog.body, 'This is the body of the test blog.')
        self.assertEqual(blog.author, self.author)
        self.assertEqual(blog.likes, 0)  # Default likes should be 0


    def test_blog_timestamps(self):
        # Create a Blog instance
        blog = Blog.objects.create(
            author=self.author,
            title='Test Blog Title',
            body='This is the body of the test blog.'
        )
        # Check if created_at and updated_at are set correctly
        self.assertIsNotNone(blog.created_at)
        self.assertIsNotNone(blog.updated_at)
        self.assertEqual(blog.created_at, blog.updated_at)  # They should be equal at creation

    def test_likes_increment(self):
        # Create a Blog instance
        blog = Blog.objects.create(
            author=self.author,
            title='Test Blog Title',
            body='This is the body of the test blog.'
        )
        # Increment likes
        blog.likes += 1
        blog.save()
        
        # Check if likes are incremented
        self.assertEqual(blog.likes, 2)