from argument_parser import ArgumentParser
from data_loader import get_task2


class RelationDisagreementFinder:
    def __init__(self, review1, review2):
        assert review1.keys() == review2.keys()  # both should have the same keys
        self.argument_parser1 = ArgumentParser(review1)
        self.argument_parser2 = ArgumentParser(review2)

    def find_disagreements(self):
        supports1 = self.argument_parser1.get_supports()
        supports2 = self.argument_parser2.get_supports()

        attacks1 = self.argument_parser1.get_attacks()
        attacks2 = self.argument_parser2.get_attacks()

        for key in supports1.keys():
            support_one = supports1[key]
            support_two = supports2[key]

            if support_one != support_two:
                print(key)


if __name__ == '__main__':
    reviews1, reviews2 = get_task2()
    RelationDisagreementFinder(reviews1, reviews2).find_disagreements()
