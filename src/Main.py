from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from Tools.Scrape_linkedin import scrape_linkedin_data_profile
from Agent.Find_Profile_URL import find_url_agent


def main(username: str) -> str:
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

    linkedin_profile_url = find_url_agent(name=username)
    """
        From find_url_agent will give us ->  The LinkedIn profile URL for
        Harrison Chase is https://www.linkedin.com/in/harrison-chase-961287118, so we need to extract the URL
    """
    start_index_of_url = linkedin_profile_url.find("https://www.linkedin.com/in/")
    linkedin_profile_url = linkedin_profile_url[start_index_of_url:]

    # Now we will pass linkedin_profile_url as an argument to extract all the data from the profile
    person_linkedin_data = scrape_linkedin_data_profile(url=linkedin_profile_url)
    result = chain.run(input=person_linkedin_data)

    return result


if __name__ == "__main__":
    print("Process Started")
    print(main(username="Harison Chase"))
