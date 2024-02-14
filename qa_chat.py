from dotenv import load_dotenv
load_dotenv()
import requests
import PyPDF2
import io
from distutils.log import error
from lib2to3.pgen2.token import NEWLINE
import csv , requests
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# now wee are writing function to load Gemini Pro mode land get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def extract_text_from_pdf(url):
    response = requests.get(url)
    with io.BytesIO(response.content) as open_pdf_file:
        reader = PyPDF2.PdfFileReader(open_pdf_file)
        text = ""
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        return text

# Pdf related to Helath , Fitness , Nutrients , so that chatbot can learn from it
pdf_for_health_related_chatbot=['https://www.uakron.edu/armyrotc/MS1/15.pdf',
                                'https://www.eolss.net/sample-chapters/c03/E1-12-89-11.pdf',
                                 'https://www.exerciseismedicine.org/assets/page_documents/Complete%20HCP%20Action%20Guide.pdf',
                                'https://yas.nic.in/sites/default/files/Fitness%20Protocols%20for%20Age%2018-65%20Years%20v1%20(English).pdf',
                                'https://www.acsm.org/docs/default-source/publications-files/acsms-complete-guide-fitness-health.pdf?sfvrsn=88c6fc17_0',
                                'https://oer.galileo.usg.edu/cgi/viewcontent.cgi?article=1005&context=health-textbooks',
                                'https://ncert.nic.in/textbook/pdf/kehe103.pdf',
                                'https://www.researchgate.net/publication/342916972_Importance_of_health_and_fitness_in_life',
                                'https://ncert.nic.in/pdf/publication/otherpublications/iehped101.pdf'
                                'https://exerciseismedicine.org/assets/page_documents/ExPro_Action_Guide.pdf',
                                'https://eatrightindia.gov.in/eatrightschool/assets/resource/file/introduction-to-nutrition.pdf',
                                'https://pdf.usaid.gov/pdf_docs/PA00TBCT.pdf',
                                'https://cns.ucdavis.edu/sites/g/files/dgvnsk416/files/inline-files/nutrition_3_nutrients.pdf',
                                'https://www.ars.usda.gov/is/np/NutritiveValueofFoods/NutritiveValueofFoods.pdf',
                                'https://www.nin.res.in/downloads/DietaryGuidelinesforNINwebsite.pdf',
                                'https://www.ctahr.hawaii.edu/oc/freepubs/pdf/pnm3.pdf',
                                'https://lpi.oregonstate.edu/sites/lpi.oregonstate.edu/files/pdf/mic/micronutrients_for_health.pdf',
                                'https://www.ncert.nic.in/ncerts/l/fesc102.pdf',
                                'https://ugcmoocs.inflibnet.ac.in/assets/uploads/1/132/4536/et/1%20Script200302090903033030.pdf',
                                'https://pietsanskritinfl.com/wp-content/uploads/2021/09/834_Food-nutrution-XI.pdf',
                                'https://alraziuni.edu.ye/uploads/pdf/fundamentals-of-foodnutrition-and-diet-therapy.pdf',
                                'https://health.gov/sites/default/files/2019-09/Appendix-E3-1-Table-A4.pdf',
                                'https://resources.saylor.org/wwwresources/archived/site/wp-content/uploads/2010/11/Nutrition.pdf',
                                'https://www.accessdata.fda.gov/scripts/InteractiveNutritionFactsLabel/assets/InteractiveNFL_Vitamins&MineralsChart_October2021.pdf',
                                'https://nios.ac.in/media/documents/SrSec314NewE/Lesson-28.pdf',
                                'https://www.fao.org/ag/humannutrition/32444-09f5545b8abe9a0c3baf01a4502ac36e4.pdf']


for url in pdf_for_health_related_chatbot:
    try:
        pdf_text = extract_text_from_pdf(url)
        print(f"Text from {url}:")
    except:
        pass

def get_answer():
    user_question = request.json['question']
    headers = {
  'x-api-key': 'sec_e9mLkHgnmPSCRAAIcbfT3KuIFTk38Jtk',
  'Content-Type': 'application/json'
    }
    data = {'url': 'https://pgcag.files.wordpress.com/2010/01/48lawsofpower.pdf'}
    headers = {
    'x-api-key': 'sec_e9mLkHgnmPSCRAAIcbfT3KuIFTk38Jtk',
    "Content-Type": "application/json",
    }
    response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-url', headers=headers, json=data)

    if response.status_code == 200:
        source_id= response.json()['sourceId']
    headers = {
    'x-api-key': 'sec_e9mLkHgnmPSCRAAIcbfT3KuIFTk38Jtk',
    "Content-Type": "application/json",
    }

    data = {
    'sourceId': source_id,
    'messages': [
        {
            'role': "user",
            'content': user_question,
            }
        ]
        }

    

    response = requests.post(
        pdf_text, headers=headers, json=data)

    answer=response.json()['content']

    if response.status_code == 200:
        return jsonify({'answer': answer})

    pass




def get_gemini_response(question):
    response=get_answer()
    for url in pdf_for_health_related_chatbot:
        try:
            pdf_text = extract_text_from_pdf(url)
            print(f"Text from {url}:")
        except:
            pass
    response=chat.send_message(question,stream=True) # as llm modelis giving u the output we will steam and show the output
    return response

# now we are gonna initialize our streamlit app
st.set_page_config(page_title='qna_on_chatbot_development')

st.header("ChatBot For Fitness")
st.subheader("Scroll down for Chat History")

# Initialize session state for chat history if it does'nt exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input('Input:',key='input')  
submit=st.button("Ask the question") 

if submit and input:
    response=get_gemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(('You',input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
    print(f'\nYou-:{input} \nAI BOT-:{response.text} \n')

    with open('q_a_questions.txt','a') as f:
        f.write(f'You-: {input}\n AI BOT-:{response.text}\n')  
        f.write('------------------------------------------------------------------------------------\n')  

st.subheader("The Chat history is")
for role,text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')
