def get_answer(question):
	a = str(question)
	answers = {'привет':'И тебе!',"?":"ничегO", "поКа":"пока!"}
	return answers.get(a.lower())


if __name__ == '__main__':
    print(get_answer("?"))