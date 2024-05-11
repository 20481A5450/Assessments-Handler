import json

def extract_questions(text):
    questions = []
    question_id = None
    question_text = None
    options = []
    correct_option = None
    solution_text = None

    lines = text.split('\n')
    print(lines)

    for line_index, line in enumerate(lines):
        if line.startswith('Question ID:') or line.startswith('\section*{Question ID:'):
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


        elif line.startswith('(A)'):
            correct_option = line[1]
            options.append({
                "optionNumber": line[1],
                "optionText": line[4:].strip(),
                "isCorrect": True
            })
        elif line.startswith('(B)') or line.startswith('(C)') or line.startswith('(D)'):
            options.append({
                "optionNumber": line[1],
                "optionText": line[4:].strip(),
                "isCorrect": False
            })
        elif line.startswith('\\section*{Answer'):
            if line_index + 1 < len(lines):
                next_line = lines[line_index + 1]
                if next_line.startswith('Sol.'):
                    solution_text = next_line.split('. ')[1].strip()

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