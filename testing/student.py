from datetime import date, timedelta
import requests


class Student:
    """A class for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self._end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name}.{self._last_name}@email.com".lower()

    def apply_extension(self, num_days):
        self._end_date = self._end_date + timedelta(num_days)

    def course_schedule(self):
        response = requests.get(f"https://mocksite.com/schedule/{self._first_name + self._last_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong!"


if __name__ == '__main__':
    pass
