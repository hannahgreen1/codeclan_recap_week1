import unittest
from src.recap import *

class TestRecap(unittest.TestCase):

    def setUp(self):
        self.instructors = [
            {
                "name": "Colin",
                "cohort": "E10",
                "favourite_langauges": {
                    "1st": "React",
                    "2nd": "Spring",
                    "3rd": "Python"
                    }
            },
            {
                "name": "Hannah",
                "cohort": "E21",
                "favourite_langauges": {
                    "1st": "Python",
                    "2nd": "Java",
                    "3rd": "Vue"
                    }
            }
        ]

        self.new_lesson = {
            "name": "Multiple Classes",
            "langauge": "Python",
            "date": "Tuesday"
        }

        self.cc_cohort = {
            "students": [
                {
                    "name": "Amy",
                    "favourite_language": "Python",
                    "age": 28
                },
                 {
                    "name": "Dave",
                    "favourite_language": "JavaScript",
                    "age": 32
                },
                 {
                    "name": "James",
                    "favourite_language": "Java",
                    "age": 40
                },
                 {
                    "name": "Mary",
                    "favourite_language": "Ruby",
                    "age": 25
                }
            ],
            "staff": {
                "total_staff": 52,
                "instructors": "Colin, Hannah",
            },
            "cohort_name": "CodeClan E51"
        }

        self.cc_cohort2 = {
            "students": [
                {
                    "name": "Amy",
                    "favourite_language": "Python",
                    "age": 28
                },
                 {
                    "name": "Dave",
                    "favourite_language": "JavaScript",
                    "age": 32
                },
                 {
                    "name": "James",
                    "favourite_language": "Java",
                    "age": 40
                },
                 {
                    "name": "Mary",
                    "favourite_language": "Ruby",
                    "age": 25
                }
            ],
            "staff": {
                "total_staff": 52,
                "instructors": "Colin, Hannah",
            },
            "cohort_name": "CodeClan E52"
        }

    def test_cohort_name(self):
        name = get_cohort_name(self.cc_cohort)
        self.assertEqual("CodeClan E51", name)

    def test_cohort_name(self):
        name = get_cohort_name(self.cc_cohort2)
        self.assertEqual("CodeClan E52", name)

    # @unittest.skip("delete this line to run the test")
    def test_total_staff(self):
        sum = get_total_staff(self.cc_cohort)
        self.assertEqual(52, sum)


    @unittest.skip("delete this line to run the test")
    def test_list_of_student_names(self):
        students = get_student_names(self.cc_cohort)
        self.assertEqual(["Amy", "Dave", "James", "Mary"], students)

    @unittest.skip("delete this line to run the test")
    def test_get_Colins_second_fav_language(self):
        language = get_favourite_langauge(self.instructors)
        self.assertEqual("Spring", language)