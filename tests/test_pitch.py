from unicodedata import category
import unittest
from app.models import Pitch, User

class PitchTest(unittest.TestCase):
    #Pitches - id,pitch,upvote,downvote,user,category
    def setUp(self):
        self.user_John = User(username='John',password='Kenya123',email='john@example.com')
        self.new_pitch = Pitch(pitch='Lorem Ipsum',user=self.user_John,category='Tech')

    def tearDown(self):
            Pitch.query.delete()
            User.query.delete()

    def test_check_instance(self):
        self.assertEqual(self.new_pitch.pitch,'Lorem Ipsum')
        self.assertEqual(self.new_pitch.user,self.user_John)
        self.assertEqual(self.new_pitch.category,'Tech')

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitches(self):
        self.new_pitch.save_pitch()
        all_pitches = Pitch.get_pitches(1)
        self.assertTrue(len(all_pitches)==1)

    def test_get_pitches_user(self):
        self.new_pitch.save_pitch()
        self.test_pitch=Pitch(pitch='This is us',user=self.user_John,category='Sales')
        self.test_pitch.save_pitch()
        user_pitches = Pitch.get_all_pitches_user(1)
        self.assertTrue(user_pitches)

    def test_get_pitches_category(self):
        self.new_pitch.save_pitch()
        user_pitches = Pitch.get_all_pitches_category('Sales')
        self.assertTrue(user_pitches)