""" Parse a sentence into keywords by removing 'stopwords' and verbs """

import re
import io


class Parser:
    """
        Parse a sentence into a list of words
        by removing stopwords and verbs
    """

    @staticmethod
    def unicoding(word):
        """
            Remove accentuation of letters in a 'word'
            As input  : a 'word' where the accents must be removed
            In return : the 'word' without accented letter
        """
        substituts = {  
                    'a': ['à', 'â', 'ä'],
                    'e': ['é', 'è', 'ê', 'ë'],
                    'i':['ï', 'î'],
                    'o': ['ô', 'ö'],
                    'u': ['ù', 'û', 'ü'], 
                    'y': 'ÿ',
                    'c': 'ç'
                    }

        result = ""
        for letter in word:
            for (cle, valeur) in substituts.items():
                solution = False
                # if an accented letter is found...
                if letter in valeur:
                    result += cle
                    # ... then replace it with an unaccented one
                    solution = True
                    break
            if not solution:
                result += letter
        # returns the word without accented letter
        return result

    @staticmethod
    def sentence_parser (sentence):
        """
            Extract only words of the 'sentence'
            and remove single letters (d',l'...)
            As input  : a sentence as string
            In return : a list of words
        """
        # extract only the words of the 'sentence'
        words_list = re.findall(r"[\w]+", sentence)
        # remove words who are single letters
        for word in words_list:
            if len(word) == 1:
                del(words_list[words_list.index(word)])
        return words_list

    @staticmethod
    def delete_stopwords(list_of_words):
        """
            Remove the 'stopwords' in the 'list_of_words'
            As input  : a 'list_of_words' as list
            In return : a list of keywords
        """
        keywords = []
        # read all words of file 'stopwords.txt'...
        with open('ChatBot/static/stopwords.txt', "r", encoding="latin-1") as stopwords:
            lignes = stopwords.readlines()
            # transform the file 'stopwords.txt' into a list of words
            crible = lignes[0].split(',')
            # ... and compare with list_of_words of question
            for word in list_of_words:
                if not(word.lower() in crible):
                    keywords.append(word)
        # return the 'list_of_words' without stopwords
        return keywords

    @classmethod
    def verbs_file_name(cls, verb):
        """
            creates the name of the verbs file in which
            the presented word could be found
            As input  : the 'verb' as string
            In return : the name of the verbs file as string
            (the verb "attendre" is in the file "verbes_a.txt")
        """
        # the verb "trouver" is in the file "verbes_t.txt"
        nom_fichier_verbes = "verbes_" + cls.unicoding(verb[0].lower()) + ".txt"
        # return the name of the verb file
        return nom_fichier_verbes

    @classmethod
    def delete_verbs(cls, list_of_words):
        """
            Remove 'verbs' from 'list_of_words'
            and returns the list of remaining keywords
            As input  : the list_of_words of the question
            In return : a list of remaining keywords of the question
        """
        keywords = []
        for word in list_of_words:
            # search the good file of verbs to see if the 'word' is a verb
            file_path = 'ChatBot/static/Verbes_en_francais/' + cls.verbs_file_name(word)
            with open(file_path, "r", encoding="latin-1") as stop_verbs:
                lignes = stop_verbs.readlines()
                crible = lignes[0].split(',')
                if not(word.lower() in crible):
                    keywords.append(word)
        # return the original "list_of_words" without the verbs
        return keywords

    @classmethod
    def parsing(cls, question):
        """ Parse the 'question', remove the stopwords
            and the verbs and return a list of keywords
            As input  : the sentence as string
            In return : the list of keywords of the question
        """        
        return cls.delete_verbs(cls.delete_stopwords(cls.sentence_parser(question)))


if __name__=='__main__':
    # question = "Est-ce que tu sais où se trouve OpenClassrooms ?"
    question = "Quelle est l'adresse de la Tour Eiffel ?"
    print(question, " : ", Parser.parsing(question))
