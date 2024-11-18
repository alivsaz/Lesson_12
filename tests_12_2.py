# Методы Юнит-тестирования

import runner_and_tournament as RaT
import unittest
from unittest import TestCase

class TurnamentTest(TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.r1 = RaT.Runner('Усэйн', 10)
        self.r2 = RaT.Runner('Андрей', 9)
        self.r3 = RaT.Runner('Ник', 3)

    def test_runner1(self):
        t1 = RaT.Tournament(90, self.r1, self.r3)
        self.all_results[0] = t1.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    def test_runner2(self):
        t2 = RaT.Tournament(90, self.r2, self.r3)
        self.all_results[1] = t2.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    def test_runner3(self):
        t3 = RaT.Tournament(90, self.r1, self.r2, self.r3)
        self.all_results[2] = t3.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    @classmethod
    def tearDownClass(self):
        for i in self.all_results:
            print(self.all_results[i])


if __name__ == '__main__':
    unittest.main()