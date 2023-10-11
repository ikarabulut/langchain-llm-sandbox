from langchain.llms import HuggingFaceHub
# Allows us to create the template that can have inputs passsed
from langchain.prompts import PromptTemplate
# Allows us to put individual components together. LLM and prompt tempalte in this case
from langchain.chains import LLMChain
from huggingface_hub import HfApi, ModelFilter
from dotenv import load_dotenv

load_dotenv()


def list_hub_repositories(task, author):
    api = HfApi()
    models = api.list_models(filter=ModelFilter(task=task, author=author))
    for model in models:
        print(model)


def generate_pet_name(animal_type):
    repo_id = "google/pegasus-xsum"
    llm = HuggingFaceHub(repo_id=repo_id)

    template = "I have a pet {animal_type} and I want a cool name for it. Suggest me five cool names for my pet"
    prompt = PromptTemplate(template=template, input_variables=['animal_type'])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run({'animal_type': animal_type}))


# generate_pet_name("dog")

list_hub_repositories("question-answering", "google")
