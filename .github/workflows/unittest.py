import unittest

class TestImageClassifier(Mainclass.TestCase):

    def setUp(self):
        self.classifier = ImageClassifier()

    def test_bright(self):
        self.assertEqual(self.classifier.classify(200), "Bright")

    def test_dark(self):
        self.assertEqual(self.classifier.classify(100), "Dark")

    def test_boundary(self):
        self.assertEqual(self.classifier.classify(128), "Dark")

    def test_negative(self):
        with self.assertRaises(ValueError):
            self.classifier.classify(-10)

    def test_above_range(self):
        with self.assertRaises(ValueError):
            self.classifier.classify(300)