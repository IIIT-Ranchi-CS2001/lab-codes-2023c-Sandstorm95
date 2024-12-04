# Dictionary mapping English letters to hieroglyphic-like symbols (using random Unicode)
hieroglyphs = {
    'a': '𓀀', 'b': '𓃀', 'c': '𓂀', 'd': '𓄀', 'e': '𓂋',
    'f': '𓆑', 'g': '𓎼', 'h': '𓉔', 'i': '𓇋', 'j': '𓊃',
    'k': '𓎡', 'l': '𓃭', 'm': '𓅓', 'n': '𓈖', 'o': '𓅱',
    'p': '𓊪', 'q': '𓌤', 'r': '𓂋', 's': '𓈙', 't': '𓏏',
    'u': '𓅱', 'v': '𓆑', 'w': '𓅱', 'x': '𓐙', 'y': '𓇌', 'z': '𓊃'
}

# Function to translate English text to "hieroglyphs"
def translate_to_hieroglyphs(text):
    translated = ""
    text = text.lower()  # Convert the input to lowercase for uniformity
    for char in text:
        if char in hieroglyphs:
            translated += hieroglyphs[char] + " "
        else:
            translated += char + " "  # Preserve spaces and punctuation
    return translated
