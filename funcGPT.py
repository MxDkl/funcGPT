import os
from dotenv import load_dotenv
import openai
from ast import literal_eval

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# A helper function that tries to convert a string to a python type
def simplest_type(s):
    try:
        return literal_eval(s)
    except:
        return s


# A decorator that uses GPT-3.5 to 'calculate' the output of a function
def funcGPT(function):
    def wrapper(*args, **kwargs):
        system_prompt = "You are a helpful assistant. Given the name of a python function and its arguments, you will return what you think is the expected output of the function. You will not explain your response. You will NEVER preface your response with anything. NDo notEVER end your response with a period."
        prompt = "What is the expected output of the following python function: " + function.__name__ + ", with the following arguments: " + str(args) + " and " + str(kwargs) + "?"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        response = response["choices"][0]["message"]["content"]
        return simplest_type(response)
    return wrapper


# a decorator that uses GPT-3.5 to print what it thinks the output of a function is
def printGPT(function):
    def wrapper(*args, **kwargs):
        system_prompt = "You are a helpful assistant. Given the name of a python function and its arguments, you will return what you think is the expected output of the function."
        prompt = "What is the expected output of the following python function: " + function.__name__ + ", with the following arguments: " + str(args) + " and " + str(kwargs) + "?"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        response = response["choices"][0]["message"]["content"]
        print(response)
        return function(*args, **kwargs)
    return wrapper