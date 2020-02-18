import unittest
import main as a


class MyTestCase(unittest.TestCase):

    def testUserA(self):
        d = a.get_info('richkempinski')
        self.assertIn('hellogitworld', d)
        self.assertIn('helloworld', d)
        self.assertIn('Mocks', d)
        self.assertIn('Project1', d)
        self.assertIn('threads-of-life', d)
        self.assertEqual(d['hellogitworld'], 30)

    def testUserB(self):
        d = a.get_info('qdmfeng')
        self.assertIn('a3', d)
        self.assertIn('CSC343_Assignment_3', d)
        self.assertIn('Developing-with-the-Perspective-of-the-Tester-in-mind', d)
        self.assertIn('gameserver', d)
        self.assertIn('gitignore', d)
        self.assertIn('KeFa', d)
        self.assertIn('simplemessaging', d)
        self.assertIn('SSW567', d)
        self.assertIn('SSW810', d)
        self.assertIn('startupfinder', d)
        self.assertIn('start_up', d)
        self.assertIn('Triangle567', d)
        self.assertEqual(d['a3'], 22)
        #self.assertEqual(d['CSC343_Assignment_3'], 4)
        self.assertEqual(d['KeFa'], 15)
        self.assertEqual(d['simplemessaging'], 6)
        self.assertEqual(d['gameserver'], 2)

    def testEmpty(self):
        self.assertEqual(a.get_info(''), "Error, empty input.")


if __name__ == '__main__':
    unittest.main()
