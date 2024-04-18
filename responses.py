from random import choice, randint


def get_response(user_input: str) -> str:
	lowered: str = user_input.lower()
	if lowered == '':
		return 'Well, you\'re awfully silent...'
	elif 'hello' in lowered:
		return 'yo '
	elif 'how are you' in lowered:
		return 'not bad!'
	elif 'bye' in lowered:
		return 'pce btich!'
	elif 'who is king' in lowered:
		return 'NED is KING'
	elif 'roll dice' in lowered:
		return f'You rolled: {randint(1, 6)}'
	else:
		return choice(['I do not understand...',
			'What are you talking about?',
			'Do you mind rephrasing that?', 'tf you say to me?','idk bro', 'idk but zach is a bitch frfr','damn he thic','yeah','nah','sure','LMAOO??','stfu','bet lets do it','oh snap!','YIPEEREEEEE','I shit myself','REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE']
