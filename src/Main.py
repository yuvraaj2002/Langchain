from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == "__main__":
    print("Starting")

    # let's create a simple template
    template = """
    Given the linkedin information {input} of a person
    1. Give me short summary
    2. Two interesting facts about the person
    """

    # Now we will create a prompt template
    prompt_template = PromptTemplate.from_template(template=template)

    # Initializing the model
    model = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

    # Let's chain together everything using LLM Chain
    chain = LLMChain(llm=model, prompt=prompt_template)
    print(chain.run(input="Hari Singh Nalwa"))
