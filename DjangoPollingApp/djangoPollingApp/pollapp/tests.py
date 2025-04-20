from django.test import TestCase
from pollapp.models import Register

#use command: <python manage.py test> === for run the test file

class RegisterTestCase(TestCase):
    def setUp(self):
        Register.objects.create(emailid="manimeraj123@gmail.com", firstname="mani",lastname='meraj',username='manimeraj123',mobile='8877887788',password='123')

    def test_register(self):
        obj = Register.objects.get(emailid="manimeraj123@gmail.com", firstname="mani",lastname='meraj',username='manimeraj123',mobile='8877887788',password='123')
        self.assertEqual(obj.emailid, 'manimeraj123@gmail.com')
        self.assertEqual(obj.username, 'manimeraj123')
        self.assertEqual(obj.mobile, '8877887788')


    def create_user(self,emailid="amman123@gmail.com", firstname="amman",lastname='surf',username='ammansurf123',mobile='7898998877',password='321'):
        return Register.objects.create(emailid="amman123@gmail.com", firstname="amman",lastname='surf',username='ammansurf123',mobile='7898998877',password='321')
    
    def test_crete_user(self):
        emailid = 'ammanmeraj123@gmail.com'
        username = 'ammansurf123'
        object1 = self.create_user(emailid=emailid)
        object2 = self.create_user(username=username)
        # object2 = self.create_user(username=username)
        qs = Register.objects.filter(username=username)
        self.assertEqual(qs.count(), 2)           #qs.count(), 3)=== for 3 no. of objects  
