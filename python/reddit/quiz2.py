import random

def ingest_questions():
    # csv read normally here
    answer_key = [
        {
            'q': 'Afghanistan',
            'a': ['Kabul', 'Mazari Sharif', 'Herat', 'Anar Dara']
        },
        {
            'q': 'Armenia',
            'a': ['Yerevan', 'Jermuk', 'Gyumri', 'Vanadzor']
        },
        {
            'q': 'Belarus',
            'a': ['Minsk', 'Barysaw', 'Viciebsk', 'Polatsk']
        },
        {
            'q': 'Croatia',
            'a': ['Zagreb', 'Sisak', 'Pozega', 'Osijek']
        },
        {
            'q': 'Ethiopia',
            'a': ['Addis Ababa', 'Dessie', 'Gondar', 'Jimma']
        },
        {
            'q': 'Iceland',
            'a': ['Reykjavik', 'Selfoss', 'Hof', 'Akureyri']
        },
        {
            'q': 'Niger',
            'a': ['Niamey', 'Agadez', 'Djado Plateau', 'Madama']
        },
        {
            'q': 'Qatar',
            'a': ['Doha', 'Dukhan', 'Salwa', 'Mesajeed']
        },
        {
            'q': 'Switzerland',
            'a': ['Bern', 'Zurich', 'Chur', 'Thun']
        },
    ]
    return answer_key

def ask_question(question):
    print(question)
    answer_letters = 'ABCD'
    answers = question.get('a')
    correct_answer = answers[0]
    random.shuffle(answers)
    answers = {
        answer_letters[i]: answer
        for i, answer in enumerate(answers)
    }
    print('Capital of {}?'.format(question.get('q')))
    for option in answer_letters:
        print('{}. {}'.format(option, answers[option]))
    response = input('Answer? ')
    if answers.get(response.upper()) == correct_answer:
        score = 1
    else:
        score = 0
    return score

def main():
    score = 0
    question_db = ingest_questions()
    for question in random.sample(question_db, 5):
        score += ask_question(question)
    print('Score: {}'.format(score))

if __name__ == '__main__':
    main()
