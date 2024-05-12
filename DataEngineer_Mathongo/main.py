import json

def extract_questions(text):
    questions = []
    question_id = None
    question_text = None
    options = []
    correct_option = None
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
                correct_option = None
                solution_text = None

            question_id = line.split(': ')[1].strip('{}')  # Ensure no curly braces in question_id


        elif question_id and question_text is None and lines[line_index - 1] == '':
            question_text = line

        elif line.startswith('Sol.') and solution_text is None:
            solution_text = line.split('Sol. ')[1].strip()

        elif line.startswith('(A)') or line.startswith('(B)') or line.startswith('(C)') or line.startswith('(D)'):    
            option_number = line[1]
            option_text = line[4:].strip()
            is_correct = option_number == correct_option or correct_option in ['A', 'B', 'C', 'D'] and option_number == correct_option
            options.append({
                "optionNumber": option_number,
                "optionText": option_text,
                "isCorrect": is_correct
            })

        elif line.startswith('\\section*{Answer'):
            correct_option = line.split('Answer ')[1].strip()[1:-1]

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
