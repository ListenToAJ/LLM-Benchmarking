import json
import sys

def print_id_and_answers(json_file_path):
    try:
        # Load the JSON data from the specified file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Iterate through each item and print only id and answer
        for item in data:
            print(f"ID: {item['id']}")
            print(f"{item['answer']}\n")
    
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{json_file_path}' contains invalid JSON.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script2.py <json_file_path>")
    else:
        json_file_path = sys.argv[1]
        print_id_and_answers(json_file_path)