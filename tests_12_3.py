from runner import Runner
import unittest
from runner_and_tournament import Runner, Tournament
from unittest import TestCase, main


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = Runner('Pygirl')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runner('Pygirl')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r_1 = Runner('Pygirl')
        r_2 = Runner('Pyman')
        for i in range(10):
            r_1.run()
            r_2.walk()
        self.assertNotEqual(r_1.distance, r_2.distance)


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', speed=10)
        self.runner_2 = Runner('Андрей', speed=9)
        self.runner_3 = Runner('Ник', speed=3)

    def tearDown(self):
        print(self.all_results)

    def test_1(self):
        self.all_results = Tournament(90, self.runner_1, self.runner_3).start()
        for key, value in self.all_results.items():
            self.all_results[key] = value.name
        last_key = list(self.all_results.keys())[-1]
        self.assertTrue(self.all_results[last_key], 'Ник')

    def test_2(self):
        self.all_results = Tournament(90, self.runner_2, self.runner_3).start()
        for key, value in self.all_results.items():
            self.all_results[key] = value.name
        last_key = list(self.all_results.keys())[-1]
        self.assertTrue(self.all_results[last_key], 'Ник')

    def test_3(self):
        self.all_results = Tournament(90, self.runner_1, self.runner_2, self.runner_3).start()
        for key, value in self.all_results.items():
            self.all_results[key] = value.name
        last_key = list(self.all_results.keys())[-1]
        self.assertTrue(self.all_results[last_key], 'Ник')


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    unittest.main()
