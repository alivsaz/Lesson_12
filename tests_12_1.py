# Проверка на выносливость
import runner
import unittest
from unittest import TestCase

class RunnerTest(TestCase):

    def test_walk(self):
        r1 = runner.Runner('Игорь')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = runner.Runner('Петр')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = runner.Runner('Наталья')
        r4 = runner.Runner('Алекс')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


if __name__ == '__main__':
    unittest.main()