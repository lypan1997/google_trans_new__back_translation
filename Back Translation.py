# 需要安装：pip install google_trans_new

from google_trans_new import google_translator

translator = google_translator()

sentence = ['stay hungry, stay foolish. -- spoken / said by Steve Jobs']

# 英 -> 中
translation_cn = translator.translate(sentence, lang_tgt='zh-cn')
print(translation_cn)

# 中 -> 英
translation_en = translator.translate(translation_cn, lang_tgt='en')
print(translation_en)

# 随机选择一种语言翻译
import random
import google_trans_new

languages = list(google_trans_new.LANGUAGES.keys())

print(len(languages))  # 可翻译的语言种类

object_lang = random.choice(languages)
print(object_lang)

# 正向翻译
translations = translator.translate(sentence, lang_tgt=object_lang)
print(translations)

# 反向翻译
back_trans = translator.translate(translations, lang_tgt='en')
print(back_trans)