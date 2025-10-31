from prompt_generator import generate_prompt
from task_executor import execute_task


def process_user_input(user_input: str) -> str:
    prompt = generate_prompt(user_input)
    return execute_task(prompt)


if __name__ == "__main__":
    demo = "Please analyse the sentiment of this short paragraph about AI innovation."
    print(process_user_input(demo))
