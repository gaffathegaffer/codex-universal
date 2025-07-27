import os
import google.generativeai as genai


def main():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY environment variable not set")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    print("Type 'exit' to quit.")
    while True:
        try:
            prompt = input("You> ")
        except EOFError:
            break
        if prompt.strip().lower() == "exit":
            break
        response = model.generate_content(prompt)
        print("Gemini>", response.text)


if __name__ == "__main__":
    main()
