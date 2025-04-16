class noun(word, singular_translation, plural_translation):
    def __init__(self, word, singular_translation, plural_translation):
        self.word = word
        self.singular_translation = singular_translation
        self.plural_translation = plural_translation

    def get_word():
        return self.word

    def get_singular():
        return self.singular_translation

    def get_plural():
        return self.plural_translation

class verb(word, i, you, he_she_it, we, you_formal, they):
    def __init__(self, word, i, you, he_she_it, we, you_formal, they):
        self.word = word
        self.i = i
        self.you = you
        self.he_she_it = he_she_it
        self.we = we
        self.you_formal = you_formal
        self.they = they
