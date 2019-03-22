import logging

LABEL_UNIVERSE = {'value', 'fact', 'reference', 'policy', 'non-arg', 'testimony', 'quote'}


# can speed up the parser with pre-compiled regex for the future
class ArgumentParser:
    def __init__(self, reviews):
        """
        Parses reviews!
        :param reviews: map {file -> list of lines in review files}
        """
        self.labels_ix = None
        self.support_ix = None
        self.attack_ix = None
        self.reviews = reviews

    def get_arguments(self):
        """
        returns a map of file name to arguments
        :return: map {file_name : [arguments]}
        """
        arguments = {}
        for key, value in self.reviews.items():
            file_args = []
            for ix, line in enumerate(value):
                if not line.startswith("##"):
                    file_args.append(line.strip())
                else:
                    self.labels_ix = ix  # can refactor get labels to start from here
                    break
            arguments[key] = file_args
        return arguments

    def get_labels(self):
        """
        returns a map of file name ot labels
        :return: map {file_name : [labels]
        """
        labels = {}
        for key, value in self.reviews.items():
            file_labels = []
            ix = 0
            while not value[ix].startswith("## Labels"):
                ix += 1

            ix += 1  # skip line with ##labels

            while not value[ix].startswith("##"):
                parsed_label = value[ix].split()[
                    1].strip()  # format is 1. LABEL (take 2nd index value)
                if parsed_label not in LABEL_UNIVERSE:
                    logging.warning("{} not in label universe in file {}".format(parsed_label, key))
                    break
                file_labels.append(parsed_label)
                ix += 1
            self.support_ix = ix
            labels[key] = file_labels
        return labels

    def get_supports(self):
        """
        Returns a map of file name to supports
        :return: map file_name to supports
        """
        supports = {}
        for key, value in self.reviews.items():
            file_supports = []
            ix = 0
            while ix < len(value) and not value[ix].startswith("## Support"):
                ix += 1

            if ix + 1 < len(value):
                ix += 1  # skip line with ## support
                while not value[ix].startswith("##") and ix < len(value):
                    file_supports.append(value[ix].strip())
                    ix += 1
                self.attack_ix = ix
            supports[key] = file_supports
        return supports

    def get_attacks(self):
        """
        Returns a map of file name to attacks
        :return: map of file name to attacks
        """
        attacks = {}
        for key, value in self.reviews.items():
            file_attacks = []
            ix = 0
            while ix < len(value) and not value[ix].startswith("## Attack"):
                ix += 1

            if ix + 1 < len(value):
                ix += 1
                while ix < len(value):
                    file_attacks.append(value[ix].strip())
                    ix += 1
            attacks[key] = file_attacks
        return attacks
