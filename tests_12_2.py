from runner_and_tournament import Runner, Tournament
from unittest import TestCase, main


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

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
