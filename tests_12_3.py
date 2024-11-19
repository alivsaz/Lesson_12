# Заморозка кейсов

import runner
import runner_and_tournament as RaT
import unittest
from unittest import TestCase

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = runner.Runner('Игорь')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = runner.Runner('Петр')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = runner.Runner('Наталья')
        r4 = runner.Runner('Алекс')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)

class TurnamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.r1 = RaT.Runner('Усэйн', 10)
        self.r2 = RaT.Runner('Андрей', 9)
        self.r3 = RaT.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        t1 = RaT.Tournament(90, self.r1, self.r3)
        self.all_results[0] = t1.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        t2 = RaT.Tournament(90, self.r2, self.r3)
        self.all_results[1] = t2.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        t3 = RaT.Tournament(90, self.r1, self.r2, self.r3)
        self.all_results[2] = t3.start()
        self.assertTrue(self.all_results[0][len(self.all_results[0])] == 'Ник')

    @classmethod
    def tearDownClass(self):
        for i in self.all_results:
            print(self.all_results[i])


if __name__ == '__main__':
    unittest.main()