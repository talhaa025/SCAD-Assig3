class ImageClassifier:
    def classify(self, brightness):
        if brightness < 0 or brightness > 255:
            raise ValueError("Invalid brightness value")

        if brightness > 128:
            return "Bright"
        else:
            return "Dark"