def do_upper(text):
    """Возвращает всю строку заглавными буквами"""
    return text.upper()


def do_title_text(text):
    """возвращает заглавными первые буквы каждого слова в строке"""
    text_list = text.split()
    new_text = " ".join(text_list).title()
    return new_text
