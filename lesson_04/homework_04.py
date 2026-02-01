adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace(" .... ", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
temp_str = ""
for word in adventures_of_tom_sawer.split():
    temp_str += word + " "
temp_str = temp_str.strip()
adventures_of_tom_sawer = temp_str


# task 04
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""
print(f"Літера \"h\" зустрічається в тексті {adventures_of_tom_sawer.lower().count("h")} разів")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitalized_words_counter = 0
for word in adventures_of_tom_sawer.split():
    if word[0].isupper():
        capitalized_words_counter += 1
print(f"{capitalized_words_counter} слів у тексті починаються з Великої літери")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index = adventures_of_tom_sawer.find("Tom")
print(f"Слово \"Tom\" зустрічається вдруге на {adventures_of_tom_sawer.find("Tom", index+1)} позції")


# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(". ")


# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adventures_of_tom_sawer_sentences[3].lower())


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
testBool = False
for sentence in adventures_of_tom_sawer_sentences:
    if sentence.lower().count("By the time") > 0:
        testBool = True
print("Одне з речень починається з \"By the time\"") if testBool else print ("Жодне речення не починається з \"By the time\"")


# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
word_counter = 0
for word in adventures_of_tom_sawer_sentences[-1].split():
    word_counter += 1
print(f"Останнє речення складається з {word_counter} слів")