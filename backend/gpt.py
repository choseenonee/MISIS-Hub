import os
from typing import List

import openai
from dotenv import load_dotenv


dotenv_relative_path = '../.env'
dotenv_path = os.path.abspath(dotenv_relative_path)
load_dotenv(dotenv_path=dotenv_path)

openai.api_key = os.getenv('GPT_API_KEY')


def send_prompt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=1300,
        n=1,
        stop=None
    )

    return response.choices[0].text.strip()


def validate_tag(tag: str) -> bool:
    prompt = f'''Ответь да, если {tag} может быть тегом в анкете для знакомств, или нет. Под тэгом я имею ввиду hard, soft skills, а так же чьи-то интересы, хобби, предпочтения. Отвечай только да или нет.'''

    answer = send_prompt(prompt)

    answer = answer.lower()
    if 'yes' in answer or 'да' in answer.lower():
        return True
    else:
        return False


def convert_to_tags(text: str) -> List[str]:
    prompt = f'''Проанализируй текст, разбей его на теги, которые могут означать hard, soft skills, интересы, хобби, предпочтения в анкете для знакомств: {text}. 
    В своём ответе укажи только теги с большой буквы через пробел, не используй никаких других дополнительных слов.'''

    answer = send_prompt(prompt)
    maybe_tags = answer.split(' ')
    validated_tags = [tag for tag in maybe_tags if validate_tag(tag)]
    return validated_tags


def get_questions():
    base_prompt = "генерируй по два вопроса на каждую тему: IT-технологии, цель на жизнь, тема для глубокого разговора, внимательные темы для разговоров, общие темы для разговоров. добавь ещё 3 случайных вопроса. отвечай строго по русски и не создавай никаких заголовков. предоставь мне строго вопросы"
    answer = send_prompt(base_prompt)
    answer = answer[answer.find('IT')::]
    return answer
