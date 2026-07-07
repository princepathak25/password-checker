# Password Strength Tester & Generator

import string
import random
import time

def check_strength(pwd):
    length = len(pwd)
    upper = any(c.isupper() for c in pwd)
    lower = any(c.islower() for c in pwd)
    digit = any(c.isdigit() for c in pwd)
    special = any(c in string.punctuation for c in pwd)

    score = sum([upper, lower, digit, special])
    
    print("\n🔍 Analyzing password strength...\n")
    time.sleep(1.5)  
    if length < 6:
        print("❌ Bro that’s shorter than a TikTok attention span.")
    elif score < 3:
        print("🧻 Weak af. Add some spice — caps, digits, symbols, bro!")
    elif score == 3 and length >= 8:
        print("👌 Not bad, but could still level up.")
    elif score == 4 and length >= 10:
        print("💪 Now that’s a strong password.")
    else:
        print("⚠️ Meh. You tryna get hacked or what?")

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print("🔐 Welcome to the Password Strength Tester & Generator!\n")
pwd = input("📝 Enter your password to check strength: ")
check_strength(pwd)
choice = input("\n🚀 Wanna generate a strong password? (y/n): ")
if choice.lower() == 'y':
    try:
        length = int(input("🔢 How long should it be? (min 8): "))
        if length < 8:
            print("😄 Too short. Giving you a solid 12-char one instead.")
            length = 12
        new_pwd = generate_password(length)
        time.sleep(1)
        print(f"\n✅ Here's your strong password:\n🔑 {new_pwd}")
    except ValueError:
        print("❌ Invalid input. Gave you a solid 12-char one anyway.")
        print(f"🔑 {generate_password()}")
else:
    print("👋 Alright, just don’t blame me if you get hacked 😭")

print("\n🙌 Thanks for using the Password Strength Tester & Generator!")
print("Stay safe out there! 🔒")
print("👑 Created by Prince - Your friendly neighborhood password guru!")
