# Заморозка кейсов

import tests_12_1, tests_12_2, tests_12_3
import unittest

# Часть 1. TestSuit.
RTsuite = unittest.TestSuite()
RTsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
RTsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TurnamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(RTsuite)

# Часть 2. Пропуск тестов.
RTnewsuite = unittest.TestSuite()
RTnewsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RTnewsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TurnamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(RTnewsuite)
