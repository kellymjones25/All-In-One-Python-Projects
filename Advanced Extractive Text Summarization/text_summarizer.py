def summarize_text(text):
    """
    Simple summarization: return first and last sentences.
    """
    sentences = [s.strip() for s in text.split(".") if s]
    if len(sentences) <= 2:
        return text
    return sentences[0] + ". " + sentences[-1] + "."


def run_summarizer():
    print("=== Simple Text Summarizer ===")
    while True:
        text = input("Enter paragraph (or 'exit' to quit): ")
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break
        summary = summarize_text(text)
        print(f"Summary: {summary}")


if __name__ == "__main__":
    run_summarizer()
