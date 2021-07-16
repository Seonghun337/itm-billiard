from django.test import TestCase,Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_trump = User.objects.create_user(username='trump', password='somepassword')
        self.user_obama = User.objects.create_user(username='obama', password='somepassword')


    def navbar_test(self, soup):
        navbar = soup.nav
        self.assertIn('Home', navbar.text)
        self.assertIn('Forum', navbar.text)

        logo_btn = navbar.find('a', text='ITM-Billiard')
        self.assertEqual(logo_btn.attrs['href'], '/')

        home_btn = navbar.find('a', text='Home')
        self.assertEqual(home_btn.attrs['href'], '/')

        forum_btn = navbar.find('a', text='Forum')
        self.assertEqual(forum_btn.attrs['href'], '/forum/')


    def test_post_list(self):
        response = self.client.get('/forum/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Forum')

        # navbar = soup.nav

        # self.assertIn('Home', navbar.text)
        # self.assertIn('Forum', navbar.text)
        self.navbar_test(soup)

        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. we are the world',
            author=self.user_trump,
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='나는 두번째 랍니당ㅇㅇ',
            author=self.user_obama,
        )
        self.assertEqual(Post.objects.count(), 2)

        response = self.client.get('/forum/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

        self.assertIn(self.user_trump.username, main_area.text)
        self.assertIn(self.user_obama.username, main_area.text)
        

    def test_post_detail(self):
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. we are the world',
            author=self.user_trump,
        )

        self.assertEqual(post_001.get_absolute_url(), '/forum/1/')

        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # navbar = soup.nav
        # self.assertIn('Forum', navbar.text)
        # self.assertIn('Home', navbar.text)
        self.navbar_test(soup)

        self.assertIn(post_001.title, soup.title.text)

        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(post_001.title, post_area.text)

        self.assertIn(self.user_trump.username, post_area.text)

        self.assertIn(post_001.content, post_area.text)

    def test_create_post(self):
        response = self.client.get('/forum/create_post/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual('Create Post - Forum', soup.title.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Create New Post', main_area.text)
        
    # def test_update_post(self):
        # update_post_url = f'/forum/update_post/{self.post_003.pk}'

        # response = self.client.get()