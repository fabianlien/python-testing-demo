import unittest
from student import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('Jackie', 'Chan')

    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'Jackie Chan')

    def test_alert_santa(self):

        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email_output(self):
        self.assertEqual(self.student.email, 'jackie.chan@email.com')

    def test_apply_extension(self):
        before = self.student._end_date
        self.student.apply_extension(10)
        self.assertNotEqual(self.student._end_date, before)

    def test_schedule_success(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_schedule_fail(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong!")


if __name__ == '__main__':
    unittest.main()
