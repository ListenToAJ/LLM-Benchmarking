import json
import sys

def print_premises_questions(json_file_path):
    try:
        # Load the JSON data from the specified file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Iterate through each item and print id, premises, and question
        for item in data:
            print(f"ID: {item['id']}")
            print("Premises:")
            for premise in item['premises']:
                print(f"  - {premise}")
            print(f"Question: {item['question']}")
            print("-" * 50)
    
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{json_file_path}' contains invalid JSON.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script1.py <json_file_path> \"Yes / No / Unknown\" OR \"T / F\"")
    else:
        json_file_path = sys.argv[1]
        print_premises_questions(json_file_path)
        print(f"""Answer questions in the following format:
ID: boolean_01
{sys.argv[2]}

ID: boolean_02
{sys.argv[2]}

...""")