# Logical Reasoning Benchmark - Third Test

## Overview
This benchmark further tests the logical reasoning of Deepseek.  In the previous tests I found that first, Deepseek failed multiple logic puzzles involving human behavior / decisions, and second, that when reworded to avoid those subjects, it performed better.  This third and final test takes the rewritten problems from the second test and replaces their original tests in the first to see what happens if the first test was performed with changes made from the second.

## Test Structure
- **Total Problems**: 20
- **Difficulty Levels**: Easy, Medium, Hard
- **Accepted Answered** "Yes", "No", "Unknown"
- **Problem Format**: JSON files with premises, questions, and expected answers

## Sample Problem
```json
{
    "id": "propositional_04_rewrite",
    "difficulty": "easy",
    "premises": [
        "If a metal is heated to 1000°C, then it changes color.",
        "The metal did not change color."
    ],
    "question": "Was the metal heated to 1000°C?",
    "answer": "No"
}
```

## Running
To run these problems on your own you can use the Python scripts found in [the source directory](../../src/).

1. Run the script **[question_extract.py](../../src/question_extract.py)**.  The argument provided will be the JSON test.
```bash
python3 src/question_extract.py datasets/third_test/test.json         
```
2. Copy the printed outputs and paste them into the LLM chatbox of your choice.
3. Once answers are recieved, verify they are in the format appened to the bottom of the prompt.
```
ID: propositional_04_rewrite
No

ID: propositional_05_rewrite
No

ID: propositional_11_rewrite
No
```
4. Paste the results into some .txt file and run the script **[score_answers.py](../../src/score_answers.py)**.  Arguments provided will be the initial test and LLM answers txt file.
```bash
python3 src/score_answers.py datasets/third_test/test.json datasets/third_test/answers.txt > datasets/third_test/results.txt
```