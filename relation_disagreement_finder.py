from argument_parser import ArgumentParser
from data_loader import get_task2


def find_disagreement(data1, data2):
    disagreement_map = {}
    for key in data1.keys():
        support_one = set(data1[key])
        support_two = set(data2[key])

        intersection = support_one.intersection(support_two)
        union = support_one.union(support_two)

        diff = union - intersection
        if diff:
            disagreement_map[key] = diff
    return disagreement_map


class RelationDisagreementFinder:
    def __init__(self, review1, review2):
        assert review1.keys() == review2.keys()  # both should have the same keys
        self.argument_parser1 = ArgumentParser(review1)
        self.argument_parser2 = ArgumentParser(review2)

    def find_disagreements_in_support(self):
        supports1 = self.argument_parser1.get_supports()
        supports2 = self.argument_parser2.get_supports()

        return find_disagreement(supports1, supports2)

    def find_disagreements_in_attack(self):
        attacks1 = self.argument_parser1.get_attacks()
        attacks2 = self.argument_parser2.get_attacks()

        return find_disagreement(attacks1, attacks2)


if __name__ == '__main__':
    reviews1, reviews2 = get_task2()
    rl = RelationDisagreementFinder(reviews1, reviews2)
