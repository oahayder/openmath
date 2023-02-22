import os

import openai

def generate_assignment(age):
    return """Write a math question for a {} year old:""".format(age)

def grade_assignment(assigment):
    # Call OpenAPI for assignment
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Grade the answers below:\n{}".format(assigment),
        temperature=0.7,
        max_tokens=4000,
    )

    return response

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prompt for age
    age = input("Hello! Please enter your age: ")

    # Call OpenAPI for assignment
    assignment_prompt = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_assignment(age),
        temperature=0.7,
        max_tokens=4000,
    )

    #print(assignment_prompt)
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
