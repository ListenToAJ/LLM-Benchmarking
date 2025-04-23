# Deepseek Logic Problem-Solving Benchmark
**Anthony Simao - Spring 2025**

This repository contains the code, data, and analysis for benchmarking the Deepseek large language model's logic problem-solving capabilities, particularly focusing on how it handles problems involving human behavior and decision-making.

## Overview

This project explores how Deepseek handles propositional logic problems and reveals an interesting pattern: the model struggles significantly more with logically identical problems when framed in human behavioral contexts compared to abstract or mechanical contexts.

## Key Findings

- Overall accuracy of 70% on propositional logic problems
- Significant performance gap between human behavior (16.7% accuracy) and non-human contexts (66.7% accuracy after rewording)
- Deepseek tends to answer "Unknown" for problems with a correct answer of "No" when framed in human contexts
- Performance improves substantially when human behavior problems are reframed in non-human contexts

## Data Format

- `datasets`
    - `first_test` &emsp; (Folder for first test)
        - `test.json`  &emsp; (Testing dataset for first test)
        - `answers.txt`  &emsp; (Exact answers from DeepSeek)
        - `results.txt`  &emsp; (Scoring results answers.txt)
        - `readme.md`  &emsp; (Readme file explaining first test)
    - `second_test/`  &emsp; (Folder for second test)
        - `test.json`  &emsp; (Testing dataset for secondthird test)
        - `answers.txt`  &emsp; (Exact answers from DeepSeek)
        - `results.txt`  &emsp; (Scoring results answers.txt)
        - `readme.md`  &emsp; (Readme file explaining secondthird test)
    - `third_test/`  &emsp; (Folder for third test)
        - `test.json`  &emsp; (Testing dataset for third test)
        - `answers.txt`  &emsp; (Exact answers from DeepSeek)
        - `results.txt`  &emsp; (Scoring results answers.txt)
        - `readme.md`  &emsp; (Readme file explaining third test)

## Code

- `src/question_extract.py`: Converts JSON problems into standardized prompts
- `src/score_answers.py`: Processes model outputs and calculates accuracy metrics
