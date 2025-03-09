import google as genai
import google.generativeai as genai

# Set up the API key
genai.configure(api_key="GEMINI_API_KEY")

def generate_text(topic):
    model = genai.GenerativeModel("gemini-2.0-flash")  # Use "gemini-pro" for high-quality responses
    response = model.generate_content(f"Write a coherent paragraph about {topic}.")
    return response.text  # Corrected to fetch the generated text

def main():
    topic = input("Enter a topic: ")
    generated_text = generate_text(topic)
    print("\nGenerated Text:\n")
    print(generated_text)

if __name__ == "__main__":
    main()
