def get_count(char):
    return combined_name.count(char)


print('Welcome to the Love Calculator!')
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')

combined_name = name1.lower() + name2.lower()

true_count = get_count('t') + get_count('r') + get_count('u') + get_count('e')
love_count = get_count('l') + get_count('o') + get_count('v') + get_count('e')

love_score = int(str(true_count) + str(love_count))

if (love_score < 10) or (love_score > 90):
    print(
        f'Your Love Score is {love_score}, you go together like coke and mentos.')
elif (love_score >= 40) and (love_score <= 50):
    print(f'Your Love Score is {love_score}, you are alright together.')
else:
    print(f'Your Love Score is {love_score}.')
