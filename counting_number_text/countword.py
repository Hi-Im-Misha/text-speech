file_path = r"..\text.txt"


def countwords():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        
        total_chars = len(text)
        chars_without_spaces = len(text.replace(" ", ""))
        word_count = len(text.split())

        print(f"Total characters: {total_chars}")
        print(f"Without spaces: {chars_without_spaces}")
        print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print(f"ERROR: {e}")