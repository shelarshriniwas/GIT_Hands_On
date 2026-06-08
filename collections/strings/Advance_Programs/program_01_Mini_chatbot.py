# program_01_Mini_chatbot.py

message = input("You : ")

if message == "hello":
    print("Bot : Hi")

elif message == "bye":
    print("Bot : Goodbye")

else:
    print("Bot : I don't understand")


responses = {
    "hello": "Hi",
    "how are you": "I am fine",
    "bye": "Goodbye"
}

message2 = input("You : ")

print(responses.get(message2, "Unknown Message"))