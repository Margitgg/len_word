from loguru import logger

logger.success('приложение запущено')


def len_word(data: list[str]):
    logger.info('функция запущена')
    word = data[0]
    for i in data:
        if len(i) > len(word):
            word = i
    logger.success('слово найдено')
    return word


words = ["смородина", "арбуз", "клавиатура", "мышь", "клавиатурa1"]
maks_word = len_word(words)
print(maks_word)
