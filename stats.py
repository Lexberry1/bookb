def count(book_text):
        text = book_text.split()
        num_words = len(text)
        return num_words

def character_count(book_text):
	char_count = {}
	lower_text = book_text.lower()
	for char in lower_text:
		if char not in char_count:
			char_count[char] = 1
		else:
			char_count[char] += 1
	return char_count

def sort_on(characters):
	return characters['num']

def character_sort(characters):
	items = []
	for char in characters:
		items.append({"char": char, "num": characters[char]})
	items.sort(key=sort_on, reverse=True)
	return items
