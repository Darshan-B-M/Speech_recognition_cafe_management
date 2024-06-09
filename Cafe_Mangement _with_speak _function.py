import os
import speech_recognition as sr

def text_to_speech(text):
    text = text.replace("'", "''")
    command = (f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; "
               f"$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
               f"$speak.Rate = 0; "
               f"$speak.Speak('{text}');\"")
    os.system(command)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Error Occurred; {0}".format(e))
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    query = str(query).lower()
    return query

menu = {
    "PIZZA": 199,
    "VEG BURGER": 59,
    "FRENCH FRIES": 70,
    "SAMOSA": 20,
    "PUFF": 20
}

print("------------------------------Welcome to Darshan's --------------------------------")
menu_text = "\n".join([f"{i + 1}. {item} = {price}rs" for i, (item, price) in enumerate(menu.items())])
print(menu_text)

s
text_to_speech("Welcome to Darshan's cafe and today's special menu items are.")
for item in menu.keys():
    text_to_speech(f"{item}")

order_total = 0
ordered_items = []

while True:
    print("You can either type your order or say it.")
    text_to_speech("You can either type your order or say it.")
    choice = input("Do you want to type (T) or speak (S) your order? ").upper()

    if choice == "T":
        item = input("Can I have your order, please? ").upper()
    elif choice == "S":
        item = listen().upper()
        if item:
            text_to_speech(f"You ordered {item}")
    else:
        print("Invalid choice. Please select either 'T' for type or 'S' for speak.")
        text_to_speech("Invalid choice. Please select either 'T' for type or 'S' for speak.")
        continue

    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"Your item {item} will be ready in 10 mins.")
        text_to_speech(f"Your item {item} will be ready in 10 mins.")
    else:
        print(f"The ordered item {item} is not available.")
        text_to_speech(f"The ordered item {item} is not available.")

    another_order = input("Do you want to order more? (YES/NO) ").upper()
    text_to_speech("Do you want to order more?")
    if another_order != "YES":
        break

order_summary = f"Your order details are: {', '.join(ordered_items)}. The total bill is {order_total} rupees."
text_to_speech(order_summary)

print("Your order details are:", ', '.join(ordered_items))
print(f"The total bill of ordered items = {order_total}rs")
text_to_speech("Thank you! Visit again!")
print("\t\tThank you! Visit again!")
