# Заморозка кейсов

import logging
import rt_with_exceptions as RaT
import unittest
from unittest import TestCase

class RunnerTest(TestCase):

    def test_walk(self):
        try:
            r1 = RaT.Runner('Игорь', -5)            # отрицательное значение в 'speed'
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r2 = RaT.Runner(56, 5)          # неверный тип в 'name'
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        r3 = RaT.Runner('Наталья')
        r4 = RaT.Runner('Алекс')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)

class TurnamentTest(TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.r1 = RaT.Runner('Усэйн', 10)
        self.r2 = RaT.Runner('Андрей', 9)
        self.r3 = RaT.Runner('Ник', 3)

    def test_first_tournament(self):
        t1 = RaT.Tournament(90, self.r1, self.r3)
        self.all_results[0] = t1.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    def test_second_tournament(self):
        t2 = RaT.Tournament(90, self.r2, self.r3)
        self.all_results[1] = t2.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    def test_third_tournament(self):
        t3 = RaT.Tournament(90, self.r1, self.r2, self.r3)
        self.all_results[2] = t3.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    @classmethod
    def tearDownClass(self):
        for i in self.all_results:
            print(self.all_results[i])

logging.basicConfig(level=logging.INFO,
                        filename='runner_tests.log',
                        filemode='w',
                        encoding='utf-8',
                        format='%(asctime)s : %(levelname)s - %(message)s')

if __name__ == '__main__':
    unittest.main()