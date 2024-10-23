import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = runner.Runner('Pygirl')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = runner.Runner('Pygirl')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r_1 = runner.Runner('Pygirl')
        r_2 = runner.Runner('Pyman')
        for i in range(10):
            r_1.run()
            r_2.walk()
        self.assertNotEqual(r_1.distance, r_2.distance)


if __name__ == '__main__':
    unittest.main()
