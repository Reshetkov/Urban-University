from rt_with_exceptions import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r = Runner('Pygirl', -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            r = Runner(5)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        r_1 = Runner('Pygirl')
        r_2 = Runner('Pyman')
        for i in range(10):
            r_1.run()
            r_2.walk()
        self.assertNotEqual(r_1.distance, r_2.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format='%(asctime)s | %(levelname)s | %(message)s')
