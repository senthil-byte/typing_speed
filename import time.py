import time
import random

def generate_sentences():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python programming is fun and challenging.",
        "The world is full of opportunities.",
        "Effort is the key to success.",
        "Life is like a box of chocolates.",
        "Hard work pays off in the end.",
        "Coding opens doors to endless possibilities.",
        "Success comes to those who persevere.",
        "In every difficulty lies opportunity.",
        "Learning new things enriches the mind."
    ]
    return random.sample(sentences, k=10)  # Select 10 random sentences from the list

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    print("You'll be given 10 random sentences to type. Type each sentence as fast and accurately as you can.")

    sentences = generate_sentences()
    total_words = 0
    total_accuracy = 0

    for index, sentence in enumerate(sentences, start=1):
        print(f"\nSentence {index}:")
        print(sentence)

        input("Press Enter when you're ready to start typing...")
        start_time = time.time()
        user_text = input("Start typing: ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        words_per_minute = len(user_text.split()) / (elapsed_time / 60)
        accuracy = calculate_accuracy(user_text, sentence)

        print(f"\nYour typing speed for this sentence: {words_per_minute:.2f} words per minute")
        print(f"Accuracy for this sentence: {accuracy:.2f}%")

        total_words += words_per_minute
        total_accuracy += accuracy

    average_words_per_minute = total_words / 10
    average_accuracy = total_accuracy / 10

    print("\nTest complete!")
    print(f"Average typing speed: {average_words_per_minute:.2f} words per minute")
    print(f"Average accuracy: {average_accuracy:.2f}%")

def calculate_accuracy(user_text, original_text):
    correct_characters = sum(1 for x, y in zip(user_text, original_text) if x == y)
    total_characters = len(original_text)
    accuracy = (correct_characters / total_characters) * 100
    return accuracy

typing_speed_test()
