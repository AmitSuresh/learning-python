#Writing clear prompts

name=input("please enter your name:")
print(f"\nHello, {name}!")

prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat is your first name?"
name=input(prompt)
print(f'\nHello, {name}!')