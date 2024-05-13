import json
import re

def extract_questions(text):
    questions = []
    question_id = None
    question_text = None
    options = []
    correct_option = None  # Moved outside the loop
    solution_text = None

    lines = text.split('\n')

    for line_index, line in enumerate(lines):
        if line.startswith('Question ID:') or line.startswith('\\section*{Question ID:'):
            # If we're already processing a question, save it before starting a new one
            if question_id:
                question = format_question(question_id, question_text, options, correct_option, solution_text, questions)
                questions.append(question)

                # Reset variables for the next question
                question_id = None
                question_text = None
                options = []
                solution_text = None

            question_id = line.split(': ')[1].strip('{}')  # Ensure no curly braces in question_id

        elif question_id and question_text is None and lines[line_index - 1] == '':
            question_text = line

        elif line.startswith('Sol.') and solution_text is None:
            solution_text = line.split('Sol. ')[1].strip()

        elif  line.startswith('\\section*{Answer') or line.startswith('Answer'):
            # Extract only the alphabet part from the answer section
            # correct_option = line.split('Answer')[1].strip()[1:].strip()[0]
            # print(correct_option)
            correct_option = re.search(r'\((.*?)\)', line).group(1)
            print("Correct option:", correct_option)

        elif line.startswith('(A)') or line.startswith('(B)') or line.startswith('(C)') or line.startswith('(D)'):
            option_number = line[1]
            option_text = line[4:].strip()
            print(correct_option)
            # is_correct = option_number in correct_option
            is_correct = option_number == correct_option
            print (option_number, correct_option, is_correct) 
            options.append({
                "optionNumber": option_number,
                "optionText": option_text,
                "isCorrect": is_correct
            })

    # Add the last question
    if question_id:
        question = format_question(question_id, question_text, options, correct_option, solution_text, questions)
        questions.append(question)

    return questions


def format_question(question_id, question_text, options, correct_option, solution_text, questions):
    return {
        "questionNumber": len(questions) + 1,
        "questionId": question_id,
        "questionText": question_text,
        "options": options,
        "correctOption": correct_option,
        "solutionText": solution_text
    }


# Read input text from file
with open('Task.txt', 'r') as file:
    text = file.read()

# Extract questions from the text
questions = extract_questions(text)

# Write questions to JSON file
with open('output.json', 'w') as json_file:
    json.dump(questions, json_file, indent=2)
    print('done')
