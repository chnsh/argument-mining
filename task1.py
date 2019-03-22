from argument_parser import ArgumentParser
from data_loader import get_task1


class InconsistentReviewFinder:
    def __init__(self, review1, review2):
        assert review1.keys() == review2.keys()  # both should have the same keys
        self.argument_parser1 = ArgumentParser(review1)
        self.argument_parser2 = ArgumentParser(review2)

    def find_inconsistent_files(self):
        arguments1 = self.argument_parser1.get_arguments()
        arguments2 = self.argument_parser2.get_arguments()

        labels1 = self.argument_parser1.get_labels()
        labels2 = self.argument_parser2.get_labels()

        inconsistent_files = set()

        for key in arguments1.keys():
            argument_one = arguments1[key]
            argument_two = arguments2[key]

            label_one = labels1[key]
            label_two = labels2[key]

            if argument_one != argument_two:
                inconsistent_files.add(key)

            if label_one != label_two:
                inconsistent_files.add(key)
        return inconsistent_files


if __name__ == '__main__':
    reviews1, reviews2 = get_task1()
    InconsistentReviewFinder(reviews1, reviews2).find_inconsistent_files()
