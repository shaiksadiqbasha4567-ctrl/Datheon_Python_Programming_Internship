
import json
import string


def load_json():
    with open("sample_faq.json", "r") as json_file:
        data = json.load(json_file)

    return data


def get_response(question, data):

    question = question.lower().strip()
    question = question.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Check greetings
    greetings = data["greetings"]

    if question in greetings:
        return "Hello! Welcome to Datheon Chatbot. How can I help you?"

    # Check FAQs
    for faq in data["faqs"]:

        faq_question = faq["question"].lower().strip()

        faq_question = faq_question.translate(
            str.maketrans("", "", string.punctuation)
        )

        if question == faq_question:
            return faq["answer"]

    return "I don't understand you."


def main():

    data = load_json()

    print("Welcome to Datheon Chatbot")
    print("Type 'exit' to stop the chatbot")

    while True:

        question = input("\nYou: ").lower().strip()

        if question == "exit":
            print("Thank you for using Datheon Chatbot")
            break

        response = get_response(question, data)

        print("Bot:", response)


main()
