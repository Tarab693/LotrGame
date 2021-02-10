print('Hello, and welcome to dont wake Smaug!')
print('Answer correct and live, answer wrong and you will see..')

ans = input('Are you ready? (yes/no): ')
score = 0
total_q = 4
if ans.lower() == 'yes':
    ans = input('1. Where do hobbits live? ')
    if ans.lower() == 'the shire' or ans.lower() == 'hobbit hole':
        score += 1
        print('Phew! you pass two feet by Smaug')
    else:
        print('You woke Smaug!, all that remains is a pile of ash')

    
    ans = input('2. Who wears a grey hat and has a long beard? ')
    if ans.lower() == 'gandalf' or 'Gandalf the Grey':
        score += 1
        print('Phew! you pass 6 feet by Smaug')
    else:
        print('You woke Smaug!, he looks at you and takes a bite!')

    ans = input('3. Do Elves rule? ')
    if ans.lower() == 'yes':
        score += 1
        print('Phew! you pass 10 feet by Smaug, you are at the treasure!')
    else:
        print('Should have said yes! Smaug looks at you and takes a bite!')

        ans = input('4. What is Smaug? ')
    if ans.lower() == 'dragon':
        score += 1
        print('Yay, you grab all the gold you can carry, now run!')
    else:
        print('Silly thief, Smaug burns you to a crisp.. R.I.P')

        print('Enjoy your loot, you got', score, "questions correct.")
        mark = (score/total_q) * 100

        print("Mark: ", str(mark) + '%')
print('Goodbye adventurer!')
  

