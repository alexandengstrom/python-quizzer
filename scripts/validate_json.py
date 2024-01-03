import json


def validate_json(file_path):
    question_count = {}

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            assert len(data) == 4

            for category, questions in data.items():
                question_count[category] = 0

                for question in questions:
                    question_count[category] += 1

                    try:
                        assert category == question["difficulty"]
                        assert "question" in question
                        assert "codeSnippet" in question
                        assert "explanation" in question
                        assert "correctAnswer" in question
                        assert "incorrectAnswers" in question
                        assert question["correctAnswer"] not in question["incorrectAnswers"]

                    except AssertionError as err:
                        raise Exception(
                            f"Invalid question data: {err}\n{question}")

        print("JSON is valid!")
        total_questions = 0
        for category, count in question_count.items():
            print(f"{category.title()}: {count} questions.")
            total_questions += count

        print(f"Total: {total_questions} questions")

    except json.JSONDecodeError as err:
        raise Exception(f"JSON file is invalid: {err}")


if __name__ == "__main__":
    validate_json("data/questions.json")