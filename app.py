import os
from chains.summarizer import summarize_notes
from chains.qa_chain import create_qa

def main():
    print("🔑 Please set your OpenAI API key first as an environment variable:")
    print("   export OPENAI_API_KEY=your_key_here\n")

    notes_path = input("📄 Enter the path to your notes file (default: data/sample_notes.txt): ") or "data/sample_notes.txt"
    if not os.path.exists(notes_path):
        print(f"❌ File not found: {notes_path}")
        return

    with open(notes_path, "r", encoding="utf-8") as f:
        notes = f.read()

    print("\n📌 SUMMARY:")
    print(summarize_notes(notes))

    qa = create_qa(notes)
    print("\n💬 Ask questions about your notes. Type 'exit' to quit.")
    while True:
        query = input("\n❓ Your question: ")
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break
        answer = qa.run(query)
        print(f"🤖 {answer}")

if __name__ == "__main__":
    main()
