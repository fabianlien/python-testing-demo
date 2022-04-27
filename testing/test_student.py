import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.student = Student('Jackie', 'Chan')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('Test full name')
        self.assertEqual(self.student.full_name, 'Jackie Chan')

    def test_alert_santa(self):
        print('Test email')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email_output(self):
        print('Test alert_santa')
        self.assertEqual(self.student.email, 'jackie.chan@email.com')


if __name__ == '__main__':
    unittest.main()
