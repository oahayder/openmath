import os

import openai

def train_model():
    '''
    Ask the user a set of questions. write a JSONL file with format:

    {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
    {"prompt": "<prompt text>", "completion": "<ideal generated text>"}

    :return:
    '''

    return null

def generate_assignment(age="16", interest="sports"):
    return """Write a math question for a {} year old that likes {}:""".format(age, interest)

def call_prompt(prompt, temperature=0.7, max_tokens=4000):
    # Call OpenAPI for result
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response

def grade_assignment(assigment):
    response = call_prompt("Grade the answers below:\n{}".format(assigment))

    return response

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prompt for age
    age = input("Hello! Please enter your age: ")
    interest = input("What's your favourite thing? ")


    assignment_prompt = call_prompt(generate_assignment(age, interest))

    assignment_completed = ""
    '''
    for line in assignment_prompt.splitlines():
        answer = input(line + "\n")
        assignment_completed+=line + "\n{}".format(answer)
    '''
    question = assignment_prompt.choices[0].text
    answer = input("{}\n".format(question))
    assignment_completed+=question + "\n{}".format(answer)

    # Grade paper
    results = grade_assignment(assignment_completed)

    # Print grade on assignemnt
    #print(results)
    print(results.choices[0].text)
