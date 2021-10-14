accents, non_accents = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
accent_translation = str.maketrans(accents, non_accents)

def clean_string(s: str) -> str:
    return s.lower().strip().replace(".", "").translate(accent_translation)