def print_message_box(message):
    """Imprime a mensagem em uma caixa de mensagem"""

    lines = message.splitlines()

    longer = 0
    for line in lines:
        if(len(line) > longer):
            longer = len(line)


    count = longer + 2

    horizontal_bar = "-" * count
    print()
    print(f"+{horizontal_bar}+")
    for line in lines:
        print(f"| {line.ljust(longer)} |")
    print(f"+{horizontal_bar}+")
    print()

SANITIZER = {
    "A": ["Á", "À", "Ã", "Â", "Ä", "Ả", "ª"],
    "E": ["É", "È", "Ẽ", "Ê", "Ë", "Ẻ"],
    "I": ["Í", "Ì", "Ĩ", "Î", "Ï", "Ỉ"],
    "O": ["Ó", "Ò", "Õ", "Ô", "Ö", "Ỏ", "º"],
    "U": ["Ú", "Ù", "Ũ", "Û", "Ü", "Ủ"],
    "C": ["Ç"],
}

def sanitize(string):
    """Sanitiza textos… Daquele jeito"""
    for target in SANITIZER:
        for destin in SANITIZER[target]:
            string = string.replace(destin, target)
    return (string)
