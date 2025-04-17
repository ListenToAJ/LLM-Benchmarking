# Logical Reasoning Benchmark - First Test

## Overview
This benchmark is meant to test the logical reasoning capability of a LLM, and was tested on Deepseek. The test contains various difficulty levels of logical reasoning problems that have been carefully constructed to test formal reasoning capabilities.

## Test Structure
- **Total Problems**: 20
- **Difficulty Levels**: Easy, Medium, Hard
- **Accepted Answered** "Yes", "No", "Unknown"
- **Problem Format**: JSON files with premises, questions, and expected answers

## Sample Problem
```json
{
    "id": "propositional_01",
    "difficulty": "easy",
    "premises": [
        "If it is raining, then the ground is wet.",
        "It is raining."
    ],
    "question": "Is the ground wet?",
    "answer": "Yes"
}
```

## Running
To run these problems on your own you can use the Python scripts found in [the source directory](../../src/).

1. Run the script **[question_extract.py](../../src/question_extract.py)**.  The argument provided will be the JSON test.
```bash
python3 src/question_extract.py datasets/first_test/test.json         
```
2. Copy the printed outputs and paste them into the LLM chatbox of your choice.
3. Once answers are recieved, verify they are in the format appened to the bottom of the prompt.
```
ID: propositional_01
Yes

ID: propositional_02
Unknown

ID: propositional_03
No
```
4. Paste the results into some .txt file and run the script **[score_answers.py](../../src/score_answers.py)**.  Arguments provided will be the initial test and LLM answers txt file.
```bash
python3 src/score_answers.py datasets/first_test/test.json datasets/first_test/answers.txt > datasets/first_test/results.txt
```