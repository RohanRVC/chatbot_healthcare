# chatbot_healthcare
chatbot link-: https://chatbot-for-fitness.onrender.com

# Step-by-Step Guide to Run the Health-Related Chatbot Application
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.6 or higher 
pip (Python package installer)
Virtual environment (recommended)
Setting Up Your Environment
Clone the Repository


Navigate to the directory where the repository is cloned and install the required Python packages using pip:
Copy code 
pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory of your project.
Add your GOOGLE_API_KEY to the .env file:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Running the Application
Starting the Streamlit Server

Run the Streamlit application with the following command:
arduino
Copy code
streamlit run app.py
A web page should automatically open in your default browser. If it doesn't, you can manually open the link provided in the terminal output.
Interacting with the Chatbot

Use the text input field to type in your health-related questions.
Click the "Ask the question" button to submit your query.
View the chatbot's response displayed below the input field.
Using the Chatbot to Extract Information from PDFs

The application is set up to scrape and extract text from predefined PDF URLs listed in the pdf_for_health_related_chatbot array.
The extract_text_from_pdf function will be called to process each URL and extract the text content from the PDFs.
Note: This functionality is dependent on having the necessary permissions to access and download content from the provided URLs.
Viewing Chat History

Your chat history with the bot is displayed on the webpage, allowing you to scroll through past interactions.
Shutting Down the Server

When you're done using the app, go back to the terminal and press Ctrl + C to stop the Streamlit server.
Troubleshooting
If you encounter any issues:

Ensure all environment variables are correctly set.
Check that all dependencies are installed and compatible with each other.
Verify that the PDF URLs are accessible and the server has proper internet access to download them.
Additional Notes
The code uses google.generativeai with trained on pdf text content library to handle the chat functionality with Gemini LLM API.
The application saves chat history to a local text file q_a_questions.txt for record-keeping.
