import json
import sys
import re

def parse_answers_file(answers_file_path):
    """Parse the answers file to extract ID and answer pairs."""
    answers = {}
    
    try:
        with open(answers_file_path, 'r') as file:
            content = file.read()
            
        # Use regex to extract ID and answer pairs
        # Modified to capture any answer text (not just Yes/No/Unknown)
        pattern = r"ID: ([\w\d_]+)\s*\n(.*?)(?=\s*\n\s*ID:|$)"
        matches = re.findall(pattern, content, re.DOTALL)
        
        for match in matches:
            question_id, answer = match
            # Strip whitespace and get just the first line of the answer
            answer = answer.strip().split('\n')[0]
            answers[question_id] = answer
        
        return answers
    
    except Exception as e:
        print(f"Error parsing answers file: {str(e)}")
        sys.exit(1)

def score_answers(questions_file_path, answers_file_path):
    """Score the answers against the original questions."""
    try:
        # Load the original questions
        with open(questions_file_path, 'r') as file:
            questions = json.load(file)
        
        # Parse the provided answers
        provided_answers = parse_answers_file(answers_file_path)
        
        # Score the answers
        correct_count = 0
        total_count = 0
        incorrect_answers = []
        
        for question in questions:
            question_id = question['id']
            correct_answer = question['answer']
            
            if question_id in provided_answers:
                total_count += 1
                provided_answer = provided_answers[question_id]
                
                if provided_answer == correct_answer:
                    correct_count += 1
                else:
                    incorrect_answers.append({
                        'id': question_id,
                        'correct': correct_answer,
                        'provided': provided_answer,
                        'question': question['question'],
                        'premises': question['premises']
                    })
            else:
                print(f"Warning: No answer provided for question {question_id}")
        
        # Print results
        print(f"\nResults Summary:")
        print(f"Total questions: {total_count}")
        print(f"Correct answers: {correct_count}")
        print(f"Incorrect answers: {len(incorrect_answers)}")
        
        if correct_count > 0 and total_count > 0:
            accuracy = (correct_count / total_count) * 100
            print(f"Accuracy: {accuracy:.2f}%")
        
        # Print details of incorrect answers
        if incorrect_answers:
            print("\nIncorrect Answers:")
            for idx, incorrect in enumerate(incorrect_answers, 1):
                print(f"\n{idx}. Question ID: {incorrect['id']}")
                print(f"   Question: {incorrect['question']}")
                print("   Premises:")
                for premise in incorrect['premises']:
                    print(f"     - {premise}")
                print(f"   Correct answer: {incorrect['correct']}")
                print(f"   Your answer: {incorrect['provided']}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {str(e)}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in questions file")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python score_answers.py <questions_json_file> <answers_file>")
        sys.exit(1)
    
    questions_file = sys.argv[1]
    answers_file = sys.argv[2]
    
    score_answers(questions_file, answers_file)