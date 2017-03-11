def get_answer(question):
	a = str(question)
	answers = {'привет':'И тебе!',"?":"ничегO", "поКа":"пока!"}
	return answers.get(a.lower())

print(get_answer("?"))