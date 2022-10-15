from statistics import mean
import unittest

string = "lorem ipsum dolor sit amet consectetur lorem ipsum et mihi quoniam et adipiscing elit.sed quoniam et advesperascit et mihi ad villam revertendum est nunc quidem hactenus ex rebus enim timiditas non ex vocabulis nascitur.nummus in croesi divitiis obscuratur pars est tamen divitiarum.nam quibus rebus efficiuntur voluptates eae non sunt in potestate sapientis.hoc mihi cum tuo fratre convenit.qui ita affectus beatum esse numquam probabis duo reges constructio interrete.de hominibus dici non necesse est.eam si varietatem diceres intellegerem ut etiam non dicente te intellego parvi enim primo ortu sic iacent tamquam omnino sine animo sint.ea possunt paria non esse.quamquam tu hanc copiosiorem etiam soles dicere.de quibus cupio scire quid sentias.universa enim illorum ratione cum tota vestra confligendum puto.ut nemo dubitet eorum omnia officia quo spectare quid sequi quid fugere debeant nunc vero a primo quidem mirabiliter occulta natura est nec perspici nec cognosci potest.videmusne ut pueri ne verberibus quidem a contemplandis rebus perquirendisque deterreantur sunt enim prima elementa naturae quibus auctis virtutis quasi germen efficitur.nam ut sint illa vendibiliora haec uberiora certe sunt.cur deinde metrodori liberos commendas.mihi inquam qui te id ipsum rogavi nam adhuc meo fortasse vitio quid ego quaeram non perspicis.quibus ego vehementer assentior.cur iustitia laudatur mihi enim satis est ipsis non satis.quid est enim aliud esse versutum nobis heracleotes ille dionysius flagitiose descivisse videtur a stoicis propter oculorum dolorem.diodorus eius auditor adiungit ad honestatem vacuitatem doloris.nos quidem virtutes sic natae sumus ut tibi serviremus aliud negotii nihil habemus."


def string_to_words(string):
    string_rep = string.replace(".", " ")
    string_arr = string_rep.split()
    return string_arr


def string_to_sentences(string):
    if string:
        while True:
            if string and string[-1] == ".":
                string = string[:-1]
            else:
                break
        sentences = string.split(".")
    else:
        sentences = ""
    return sentences


def words_counter(string):
    return len(string_to_words(string))


def sentences_count(string):
    if string_to_sentences(string) == [""]:
        result = 0
    else:
        result = len(string_to_sentences(string))
    return result


def longest_word_length(string):
    words_arr = string_to_words(string)
    words_arr = sorted(words_arr, key=len)
    if len(words_arr) == 0:
        result = 0
    else:
        result = len(words_arr[-1])
    return result


def create_asc_dict(string):
    words_arr = string_to_words(string)

    word_dict = dict()
    for word in words_arr:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    word_dict = dict(sorted(word_dict.items(), key=lambda x: -(x[1])))
    return word_dict


def popular_words(string, words=6):
    word_dict = create_asc_dict(string)

    result = [k for (k, v) in word_dict.items()][:words:]
    return result


def percentage_of_words_counted_once(string):
    word_dict = create_asc_dict(string)
    count_single_word = len([k for (k, v) in word_dict.items() if v == 1])
    if words_counter(string) == 0:
        return 0
    return count_single_word / words_counter(string) * 100


def avg_words_per_sentence(string):
    sentences_arr = string_to_sentences(string)
    sentences_length = [len(el.split()) for el in sentences_arr]
    if not sentences_length:
        return 0
    return mean(sentences_length)


def three_two_word_phrases(string, words=3):
    sentences_arr = string_to_sentences(string)
    sentences_by_word = [el.split() for el in sentences_arr]
    result_dict = dict()
    for x in range(len(sentences_by_word)):
        for y in range(len(sentences_by_word[x]) - 1):
            # if sentences_by_word[x][y] == sentences_by_word[x][y+1]:
            if sentences_by_word[x][y] + " " + sentences_by_word[x][y + 1] not in result_dict:
                result_dict[sentences_by_word[x][y] + " " + sentences_by_word[x][y + 1]] = 0
            result_dict[sentences_by_word[x][y] + " " + sentences_by_word[x][y + 1]] += 1

    result_dict = dict(sorted(result_dict.items(), key=lambda x: -(x[1])))
    final_result = [k for (k, v) in result_dict.items()][:words:]
    return final_result


def prominence(string, words=5):
    word_arr = string_to_words(string)
    word_arr.insert(0, None)

    five_pop_words = popular_words(string, words)
    total_words = words_counter(string)

    prom_dict = dict()
    for w in five_pop_words:
        position_sum = sum([i for i, el in enumerate(word_arr) if el == w])
        positions_num = word_arr.count(w)
        prom_dict[w] = (total_words - ((position_sum - 1) / positions_num)) * (100 / total_words)

    return prom_dict


print(words_counter(string))
print(sentences_count(string))
print(longest_word_length(string))
print(popular_words(string))
print(percentage_of_words_counted_once(string))
print(avg_words_per_sentence(string))
print(three_two_word_phrases(string))
print(prominence(string))


class TestingWordsCounter(unittest.TestCase):
    def test_words_counter(self):
        self.assertEqual(words_counter("some test"), 2, "Should be 2")
        self.assertNotEqual(words_counter("some test"), 1, "different than 1")
        self.assertEqual(words_counter(""), 0, "should be 0")
        self.assertEqual(words_counter("some.test"), 2, "should be 2")

    def test_sentences_count(self):
        self.assertEqual(sentences_count("some text.another text"), 2, "should be 2")
        self.assertEqual(sentences_count("some text.another text."), 2, "should be 2")
        self.assertEqual(sentences_count(""), 0, "should be 0")
        self.assertEqual(sentences_count("."), 0, "should be 0")
        self.assertEqual(sentences_count("..."), 0, "should be 0")

    def test_longest_word_length(self):
        self.assertEqual(longest_word_length("test test2"), 5, "should be 5")
        self.assertEqual(longest_word_length("test. test2"), 5, "should be 5")
        self.assertEqual(longest_word_length("test. test2."), 5, "should be 5")
        self.assertEqual(longest_word_length(".."), 0, "should be 0")
        self.assertEqual(longest_word_length(""), 0, "should be 0")

    def test_popular_words(self):
        self.assertListEqual(popular_words("some text. some", 1), ["some"], "should be some")
        self.assertListEqual(popular_words("some text. some. text some other", 2), ["some", "text"],
                             "should be some and text")
        self.assertListEqual(popular_words("", 2), [], "should be empty list")

    def test_percentage_of_words_counted_once(self):
        self.assertEqual(percentage_of_words_counted_once("test test. one two"), 50, "should be 50")
        self.assertEqual(percentage_of_words_counted_once(""), 0, "should be 0")
        self.assertEqual(percentage_of_words_counted_once("..."), 0, "should be 0")

    def test_avg_words_per_sentence(self):
        self.assertEqual(avg_words_per_sentence("test. other test"), 1.5, "should be 1.5")
        self.assertEqual(avg_words_per_sentence("other test"), 2, "should be 2")
        self.assertEqual(avg_words_per_sentence("other"), 1, "should be 1")
        self.assertEqual(avg_words_per_sentence(""), 0, "should be 0")
        self.assertEqual(avg_words_per_sentence("."), 0, "should be 0")

    def test_three_two_word_phrases(self):
        self.assertListEqual(three_two_word_phrases("some test. presented here. some test", 1), ["some test"],
                             "should be ['some test']")
        self.assertListEqual(three_two_word_phrases("some test. presented here. some test"),
                             ["some test", "presented here"], "should be ['some test', 'presented here']")
        self.assertListEqual(three_two_word_phrases("s t. p e. s t p t"), ["s t", "p e", "t p"],
                             "should be ['s t', 'p e', 't p']")

    def test_prominence(self):
        self.assertDictEqual(prominence(""), {}, "should be empty dict")
        self.assertDictEqual(prominence("test data"), {'data': 50.0, 'test': 100.0},
                             "should be {'data': 50.0, 'test': 100.0}")


if __name__ == '__main__':
    unittest.main()
