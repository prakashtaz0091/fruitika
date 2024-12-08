from django.db import models
from django.contrib.auth.models import AbstractUser







class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    email = models.EmailField(unique=True)
    # role = 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']









class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=100)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="blogs")


    def __str__(self):
        return self.title
    



"""
blog_id | tag_id
1       | 1
1       | 2
2       | 1
2       | 3


"""




class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.blog.title[:20]}'s image"




class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]
















class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    





class AppleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(brand__iexact='apple')



class SamsungManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(brand__iexact='samsung')



class ProductQuerySet(models.QuerySet):
    def affordable_products(self):
        return self.filter(price__lt=1000)
    

    def flexive_products(self):
        return self.filter(price__gt=1000)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    brand = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # objects = models.Manager()
    # apple = AppleManager()
    # apple = AppleManager()
    # samsung = SamsungManager()
    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return self.name
    











