print("hello AI")
#activity 1 "hello ai"
print("hello, I am a AI bot. What's your name?")
name = input()
print(f"Nice to meet you, {name}")
print("How are you feeling today? (good/bad):")
mood = input().lower() 

if mood == "good":
    print("I'm glad to hear that.")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see sometimes its hard to put feelings into words.")
    
