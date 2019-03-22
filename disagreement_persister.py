from data_loader import get_task2
from relation_disagreement_finder import RelationDisagreementFinder

if __name__ == '__main__':
    reviews1, reviews2 = get_task2()
    disagreement_finder = RelationDisagreementFinder(reviews1, reviews2)

    attack_disagreements = disagreement_finder.find_disagreements_in_attack()
    support_disagreements = disagreement_finder.find_disagreements_in_attack()

    for key, disagreements in support_disagreements.items():
        with open('output/disagreement/{}'.format(key), 'w') as file:
            file.write("## Support:\n")
            for disagreement in disagreements:
                file.write(disagreement + "\n")

            file.write("\n")

    for key, disagreements in attack_disagreements.items():
        with open('output/disagreement/{}'.format(key), 'a') as file:
            file.write("## Attack:\n")
            for disagreement in disagreements:
                file.write(disagreement + "\n")
