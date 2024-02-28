from django.test import TestCase
from .models import User, Post
from django.urls import reverse
from .forms import PostCreateForm , RegisterForm


class TestBlog(TestCase):
    def setUp(self):
        user = User.objects.create(
            first_name  = "Ravshan",
            last_name   = "Shukurulloyev",
            username    = "slowdushe",
            email       = "slowdushe@gmail.com",
            avatar      = "avatars/ravwanceek.png")
        
        user.set_password('2005')
        user.save()
        self.user = user

        post = Post.objects.create(
            title           = "Unga bolgan mexrim",
            content         = 'contennt',
            publisher_at    = '2024-02-05',
            author          = user,
            is_active       = True
        )
        self.post = post

    def test_home(self):
        response = self.client.get( reverse('home') )
        self.assertEqual(response.status_code, 200)

    def test_About_page(self):
        response = self.client.get( reverse('about') )
        self.assertEqual(response.status_code, 200)

    def test_Login_page(self):
        response = self.client.get( reverse('login') )
        print(response.headers)

    def test_post_detil(self):
        response = self.client.get(reverse('post_detail', kwargs={  "id":self.post.id   }))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)
        self.assertContains(response, self.post.author.first_name)
        self.assertContains(response, self.post.author.last_name)
        self.assertTrue(self.post.is_active, 'True')
        
    
    def test_forms(self):
        form_data =  {
            "title"         :"postTietle1",
            "content"       :"postContent1",
            "publisher_at"  :"2024-02-05",
            "is_active"     :True,
            "author"        :self.user}
        
        form = PostCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_objects_firstname_and_lastname(self):
        author = User.objects.get(id=1)
        post_count = author.is_active
        object_name = f"{author.first_name}, {author.last_name}|Is active: {post_count}"

        print(object_name)

    def test_register_form(self):
        user_create_form_data = {
            "username"      :"slowdushe",
            "first_name"    :"Ravshan",
            "last_name"     :"Shukurulloyev",
            "password1"     :"ravshan",
            "password2"     :"ravshan",
            "email"         :"slowdushe@gmail.com",
            "avatar"        :"C:/Users/user/Pictures/Screenshots homevork/Снимок экрана 2024-02-08 193246.png"
        }
        form = RegisterForm(data=user_create_form_data)
        self.assertTrue(form.is_valid())
        
    def test_Users(self):
        users = User.objects.all()
        print(users)