from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

information = """
Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] i; born 17 September 1950)[b] is an Indian politician who has served as the 14th prime minister of India since May 2014. Modi was the Chief Minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister from outside the Indian National Congress.

Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at the age of eight. His account of helping his father sell tea at the Vadnagar railway station has not been reliably corroborated. At age 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. The RSS assigned him to the BJP in 1985 and he held several positions within the party hierarchy until 2001, rising to the rank of general secretary.[c]

In 2001, Modi was appointed Chief Minister of Gujarat and elected to the legislative assembly soon after. His administration is considered complicit in the 2002 Gujarat riots,[d] and has been criticised for its management of the crisis. A little over 1,000 people were killed, according to official records, three-quarters of whom were Muslim; independent sources estimated 2,000 deaths, mostly Muslim.[10] A Special Investigation Team appointed by the Supreme Court of India in 2012 found no evidence to initiate prosecution proceedings against him.[e] While his policies as chief minister, which were credited for encouraging economic growth, were praised, Modi's administration was criticised for failing to significantly improve health, poverty and education indices in the state.[f] In the 2014 Indian general election, Modi led the BJP to a parliamentary majority, the first for a party since 1984. His administration increased direct foreign investment; it reduced spending on healthcare, education, and social-welfare programmes. Modi began a high-profile sanitation campaign, controversially initiated the 2016 demonetisation of high-denomination banknotes and introduced the Goods and Services Tax, and weakened or abolished environmental and labour laws.

Modi's administration launched the 2019 Balakot airstrike against an alleged terrorist training camp in Pakistan. The airstrike failed,[13][14] and the deaths of six Indian personnel to friendly fire was later revealed: but the action had nationalist appeal.[15] Modi's party comfortably won the 2019 general election which followed.[16] In its second term, his administration revoked the special status of Jammu and Kashmir, an Indian-administred portion of the disputed Kashmir region,[17][18] and introduced the Citizenship Amendment Act, prompting widespread protests, and spurring the 2020 Delhi riots in which Muslims were brutalized and killed by Hindu mobs,[19][20][21] sometimes with the complicity of police forces controlled by the Modi administration.[22][23] Three controversial farm laws, led to sit-ins by farmers across the country, eventually causing their formal repeal. Modi oversaw India's response to the COVID-19 pandemic, during which 4.7 million Indians died, according to the World Health Organization's estimates.[24][25]

Under Modi's tenure, India has experienced democratic backsliding, or the weakening of democratic institutions, individual rights, and freedom of expression.[26][27][g] As prime minister, he has received consistently high approval ratings.[33][34][35] Modi has been described as engineering a political realignment towards right-wing politics. He remains a controversial figure domestically and internationally, over his Hindu nationalist beliefs and handling of the 2002 Gujarat riots, which have been cited as evidence of a majoritarian and exclusionary social agenda.[h]
"""
if __name__ == "__main__":
    print("Hello LangChain!")
    summary_template = """
          given the information {information} about a person from I want you to create:
          1. a short summary of the person
          2. two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=information))
