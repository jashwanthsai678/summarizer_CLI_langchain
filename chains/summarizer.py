from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def summarize_notes(notes: str) -> str:
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following notes in concise bullet points:\n\n{text}"
    )
    # Use a small open-source model hosted on Hugging Face Hub
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-small", 
        model_kwargs={"temperature": 0.5, "max_length": 200}
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(notes)
