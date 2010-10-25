from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from tagging.models import TaggedItem
from wiki.models import Article
from ct_groups.models import CTGroup

TESTPASS='testpass'

class PageTest(TestCase):
    """test a few pages and public/private group access"""
    
    # TODO move stuff out of test.json into separate files and remove
    fixtures = ['test.json']
    
    def setUp(self):
        """docstring for setUp"""
        # fix up contenttypes
        ct_ids = { 
            14: ContentType.objects.get(app_label='blog', model='post'),
            16: ContentType.objects.get(app_label='ct_groups', model='CTGroup'),
            32: ContentType.objects.get(app_label='wiki', model='Article'),
            37: ContentType.objects.get(app_label='ct_groups', model='CTPost'),
            }
        obj_types = (Comment,  Article)
        for obj_type in obj_types:
            for obj in obj_type.objects.all():
                # print obj, obj.content_type.id
                obj.content_type = ct_ids[obj.content_type.id]
                obj.save()
    
    def _login(self, uname, next='/'):
        return self.client.post(
            '/accounts/login/?next=%s' % next,
            {'username': uname, 'password': TESTPASS})

    def test_main_pages(self):
        """test a few main pages"""
        pages = ('/', 
            '/groups/', '/catalogues/', '/mappings/', '/tags/', 
            '/contact/', '/about/', '/blog/', )
        for page in pages:
            r = self.client.get(page)
            self.failUnlessEqual(r.status_code, 200)

    def test_group_access(self):
        """unauthorised user, testing public and private group access"""
        #  public group ok for access
        r = self.client.get('/groups/group-one/')
        g = CTGroup.objects.get(name='Scottish Community Nursing Census')
        self.failUnlessEqual(r.context[-1]['object'], g)
        self.failUnlessEqual(r.status_code, 200)
        
        # private group returns permission denied
        r = self.client.get('/groups/group-two/')
        self.failUnlessEqual(r.status_code, 403)
        
    def test_non_member_access(self):
        """ log in as non-member and try again"""
        self.failUnlessEqual(self.client.login(username= 'jimmy', password= TESTPASS), True)
        r = self.client.get('/groups/group-two/')
        self.failUnlessEqual(r.status_code, 403)
        self.client.logout()
        
    def test_member_access(self):
        """log in as private group member and try again"""
        r = self._login('nick', next='/groups/group-two/')
        self.failUnlessEqual(r.status_code, 302)
        r = self.client.get('/groups/group-two/')
        self.failUnlessEqual(r.status_code, 200)

#    EXAMPLE FROM http://www.pocketuniverse.ca/archive/2008/december/11/testy/

# class ArchiveMonthTestCase(TestCase):
#     fixtures = ['test.json']
# 
#     def setUp(self):
#         self.client = client.Client()
# 
#     def testWithoutCategoryLoads(self):
#         response = self.client.get(reverse('blog_archive_month', None, (),
#                                            {'year': '2008', 'month': 'november'}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'blog/blogpost_archive_month.html')
#         self.failUnless('category' in response.context[-1])
#         self.assertEqual(response.context[-1]['category'], None)
#         self.failUnless('month' in response.context[-1])
#         self.assertEqual(response.context[-1]['month'].year, 2008)
#         self.assertEqual(response.context[-1]['month'].month, 11)
# 
#     def testWithCategoryLoads(self):
#         category = Category.objects.all()[0]
#         response = self.client.get(reverse('category_archive_month', None, (),
#                                            {'category_slug': category.slug,
#                                             'year': '2008',
#                                             'month': 'november'}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'blog/blogpost_archive_month.html')
#         self.failUnless('category' in response.context[-1])
#         self.assertEqual(response.context[-1]['category'], category)
#         self.failUnless('month' in response.context[-1])
#         self.assertEqual(response.context[-1]['month'].year, 2008)
#         self.assertEqual(response.context[-1]['month'].month, 11)        
        