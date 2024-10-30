import unittest
import tests_12_3

TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)
