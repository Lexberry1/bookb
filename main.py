import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
from stats import count, character_count, sort_on, character_sort

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents


def main():
	book_text = get_book_text(sys.argv[1])
	num_words = count(book_text)
	char_num = character_count(book_text)
	char_order = character_sort(char_num)
	print('============ BOOKBOT ============')
	print(f'Analyzing book found at {sys.argv[1]}...')
	print('----------- Word Count ----------')
	print(f'Found {num_words} total words')
	print('--------- Character Count -------')
	for item in char_order:
		if item["char"].isalpha():
			print(f'{item["char"]}: {item["num"]}')
	print('============= END ===============')
main()
