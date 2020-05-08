from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


class Converter:
    @staticmethod
    def convert(text):
        output = ""
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        tokenized = tokenizer.tokenize(text)
        words = word_tokenize(text)
        tagged = nltk.pos_tag(words)
        for i in range(0, len(words)):
            replacements = []

            # Only replace nouns with nouns, vowels with vowels etc.
            for syn in wordnet.synsets(words[i]):

                # Do not attempt to replace proper nouns or determiners
                if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT':
                    break

                # The tokenizer returns strings like NNP, VBP etc
                # but the wordnet synonyms has tags like .n.
                # So we extract the first character from NNP ie n
                # then we check if the dictionary word has a .n. or not
                word_type = tagged[i][1][0].lower()
                if syn.name().find("." + word_type + "."):
                    # extract the word only
                    r = syn.name()[0:syn.name().find(".")]
                    replacements.append(r)

            if len(replacements) > 0:
                # Choose a random replacement
                replacement = replacements[randint(0, len(replacements) - 1)]
                # replacement = replacements[0]
                output = output + " " + replacement
            else:
                # If no replacement could be found, then just use the
                # original word
                output = output + " " + words[i]

        return output
