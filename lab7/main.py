import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from string_package import (
    reverse_string, capitalize_words, remove_punctuation,
    count_characters, count_words, average_word_length
)

def analyze_string(text):
    if not text.strip():
        print("Error: Empty input")
        return
    
    print("\nString Analysis Results:")
    print("-" * 30)
    
    print(f"Original text: '{text}'")
    
    reversed_text = reverse_string(text)
    print(f"Reversed: '{reversed_text}'")
    
    capitalized_text = capitalize_words(text)
    print(f"Capitalized: '{capitalized_text}'")
    
    clean_text = remove_punctuation(text)
    print(f"Without punctuation: '{clean_text}'")
    
    char_count = count_characters(text)
    print(f"Character count (excluding spaces): {char_count}")
    
    word_count = count_words(text)
    print(f"Word count: {word_count}")
    
    avg_length = average_word_length(text)
    print(f"Average word length: {avg_length:.2f} characters")

def main():
    print("String Analyzer")
    print("=" * 30)
    text = input("Enter a sentence to analyze: ")
    analyze_string(text)

if __name__ == "__main__":
    main()