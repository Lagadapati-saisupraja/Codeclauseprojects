import time

def speed_typing_test():
    text = "This is Supraja Lagadapati."
    print("Type the following text:")
    print(text)

    input("Press Enter when you are ready to start...")
    start_time = time.time()

    typed_text = input("Start typing: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    words = text.split()
    typed_words = typed_text.split()

    correct_words = 0
    for word in typed_words:
        if word in words:
            correct_words += 1

    accuracy = (correct_words / len(words)) * 100
    words_per_minute = (len(typed_text.split()) / elapsed_time) * 60

    print("\nTime taken: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f}".format(words_per_minute))


if __name__ == "__main__":
    print("Welcome to the Speed Typing Test!")
    speed_typing_test()