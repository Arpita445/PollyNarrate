from deep_translator import GoogleTranslator


def split_text(text, max_length=4500):
    chunks = []

    while len(text) > max_length:
        split_index = text[:max_length].rfind(" ")

        if split_index == -1:
            split_index = max_length

        chunks.append(text[:split_index].strip())
        text = text[split_index:].strip()

    if text:
        chunks.append(text)

    return chunks


def translate_text(text, language):

    language_map = {
        "English": "en",
        "Hindi": "hi",
        "Spanish": "es",
        "French": "fr"
    }

    if language == "English":
        return text

    target = language_map.get(language, "en")

    translator = GoogleTranslator(
        source="auto",
        target=target
    )

    translated_chunks = []

    for chunk in split_text(text):
        translated_chunks.append(translator.translate(chunk))

    return "\n".join(translated_chunks)
    