from openai import OpenAI
import streamlit as st  
import os 
from PIL import Image

# Set image path
image_path = "C:\\Users\\hapalakila\\Downloads\\AI_Building\\hr-aichatGPT\\images\\hr-aisolution_logo.jpg"  # Replace with your image path
image = Image.open(image_path)
st.set_page_config(page_title="HR-AISOLUTIONS-ChatGPT", page_icon=image, layout="wide")
st.sidebar.image(image, use_container_width=True)

# Give title to the app
st.title("HR-AISOLUTION ChatGPT-6.0-Beta-Version")
st.subheader("AI-Assistance - AI-Agent - AI-ChatGPT for HR-AISOLUTIONS Assistant")
st.write("Ask any HR-AISOLUTIONS questions and get instant answers!")
st.write("Developed by PALAKILA HARIKRISHNA")
st.write("Note: This HR-AISOLUTIONS-ChatGPT App uses HR-AISOLUTIONS. Please ensure you have access to YOUR account Should be Authenticate by hr-aisolutions.")
st.subheader("ChatGPT-6.0-Beta-Version - OpenAI’s most advanced AI model for deep reasoning, multimodal analysis, coding, content synthesis, and personalized planning. Delivers accurate, creative, and context-rich results across complex tasks with unmatched capability.")

#client = OpenAI(api_key="")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Initialize session variables at the start once
if 'model' not in st.session_state:
    st.session_state['model'] = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful HR assistant. Answer questions related to human resources, company policies, employee benefits, recruitment, and workplace culture."}
    ]


# Define a list of available model names
model_options = ["ChatGPT-6.0-Beta-Version","GPT-3.0","GPT-o3-mini","GPT-o3-nano","gpt-4.0-turbo","gpt-5.0","meta-laama""Linear Regression", "Decision Tree", "Random Forest"]

# Create the dropdown menu
st.header("Model Selection")
selected_model = st.selectbox(
    label="Choose a model:",
    options=model_options
)

# Display the user's selection
st.write(f"You have selected the **{selected_model}** model.")

# Use the selected_model variable to load or run the model
if selected_model == "Linear Regression":
    st.info("Loading Linear Regression model...")
    # Add your code here to load and use the Linear Regression model
elif selected_model == "Decision Tree":
    st.info("Loading Decision Tree model...")
    # Add your code here to load and use the Decision Tree model
elif selected_model == "Random Forest":
    st.info("Loading Random Forest model...")
    # Add your code here to load and use the Random Forest model

#ChatBot app
st.sidebar.title("HR-AISOLUTIONS  ChatBot App")



#Tools
st.sidebar.title("My Tools")
st.sidebar.markdown("HR-AISOLUTIONS-ChatGPT")
st.sidebar.markdown("ChatGPT")
st.sidebar.markdown("ChatGPT-4o")
st.sidebar.markdown("ChatGPT-5")
st.sidebar.markdown("ChatGPT-6.0-Beta-Version")
st.sidebar.markdown("Gemini")
st.sidebar.markdown("AI Chat")
st.sidebar.markdown("AI Search Engine")
st.sidebar.markdown("AI Image Generation")
st.sidebar.markdown("AI-Agent")


#Others
st.sidebar.title("Others")
st.sidebar.markdown("Mobile App")
st.sidebar.markdown("Desktop App")
st.sidebar.markdown("Pricing Plans")


#create sidebar for adjusting parameters
st.sidebar.title("AI Assistance - HR-AISOLUTIONS-ChatGPT")
st.sidebar.markdown("### AI Assistance Features")
st.sidebar.markdown("- **24/7 Availability**: Provide instant responses to HR-related queries anytime.")
st.sidebar.markdown("- **Comprehensive Knowledge**: Access a vast database of HR policies, procedures, and best practices.")
st.sidebar.markdown("- **Employee Support**: Assist employees with questions about benefits, leave policies, and payroll.")
st.sidebar.markdown("- **Recruitment Assistance**: Help with job descriptions, resume screening, and interview scheduling.")
st.sidebar.markdown("- **Performance Management**: Guide managers and employees through performance reviews and feedback.")
st.sidebar.markdown("- **Training and Development**: Suggest training programs and resources for skill enhancement.")
st.sidebar.markdown("- **Compliance Guidance**: Provide information on labor laws, workplace safety, and regulatory compliance.")
st.sidebar.markdown("- **Data Security**: Ensure confidentiality and security of sensitive HR information.") 
st.sidebar.markdown("- **Scalability**: Handle multiple queries simultaneously, ensuring prompt responses.")

#AI -chatgpt tools
st.sidebar.title("AI Chat")
st.sidebar.markdown("### AI Chat Features")
st.sidebar.markdown("- **Natural Language Processing (NLP)**: Understand and respond to human language queries effectively.")
st.sidebar.markdown("- **Machine Learning (ML)**: Continuously learn from interactions to improve response accuracy.")
st.sidebar.markdown("- **Contextual Understanding**: Grasp the context of HR-related queries to provide accurate responses.")
st.sidebar.markdown("- **Personalized Responses**: Tailor answers based on company policies and culture.")
st.sidebar.markdown("- **Multimodal Input**: Process text and document uploads for comprehensive analysis.")    

#AI Search Engine
st.sidebar.title("AI Search Engine")
st.sidebar.markdown("### AI Search Engine Features")
st.sidebar.markdown("- **Advanced Search Algorithms**: Utilize cutting-edge algorithms to deliver precise search results.")
st.sidebar.markdown("- **Natural Language Queries**: Allow users to search using everyday language for ease of use.")
st.sidebar.markdown("- **Contextual Relevance**: Understand the context of queries to provide more accurate results.")
st.sidebar.markdown("- **Personalized Search Results**: Tailor search results based on user preferences and history.")
st.sidebar.markdown("- **Multimodal Search**: Support searches across text, images, and documents for comprehensive results.")
st.sidebar.markdown("- **Real-Time Indexing**: Ensure the search index is always up-to-date with the latest information.")
st.sidebar.markdown("- **Scalability**: Handle large volumes of search queries efficiently.")

#Image Generation
st.sidebar.title("AI Image Generation")
st.sidebar.markdown("### AI Image Generation Features")
st.sidebar.markdown("- **High-Quality Images**: Generate visually appealing and high-resolution images.")
st.sidebar.markdown("- **Customizable Styles**: Offer various artistic styles and themes for image generation.")
st.sidebar.markdown("- **Text-to-Image**: Create images based on textual descriptions for   versatile use cases.")
st.sidebar.markdown("- **Image Enhancement**: Improve the quality of existing images through AI-driven enhancements.")
st.sidebar.markdown("- **Creative Tools**: Provide tools for users to customize and modify generated images.")
st.sidebar.markdown("- **Fast Processing**: Deliver quick image generation to meet user demands.")  

#create sidebar for adjusting parameters
st.sidebar.title("Tools")    
st.sidebar.markdown("### Available Tools")
st.sidebar.markdown("- **Document Analysis**: Upload and analyze HR documents such as policies, handbooks, and contracts.")
st.sidebar.markdown("- **Employee Query Handling**: Answer common employee questions regarding benefits, leave policies, and payroll.")
st.sidebar.markdown("- **Recruitment Assistance**: Help with drafting job descriptions, screening resumes, and scheduling interviews.")
st.sidebar.markdown("- **Performance Management**: Provide guidance on performance reviews, feedback, and goal setting.")
st.sidebar.markdown("- **Training and Development**: Suggest training programs and resources for employee skill enhancement.")
st.sidebar.markdown("- **Compliance and Legal Guidance**: Offer information on labor laws, workplace    safety, and regulatory compliance.")
st.sidebar.markdown("- **HR Analytics**: Generate reports and insights on employee turnover, engagement, and satisfaction.")
st.sidebar.markdown("- **Onboarding Support**: Assist with creating onboarding plans and materials for new hires.")


#create sidebar for adjusting parameters
st.sidebar.title("AI-Agent")
st.sidebar.markdown("### AI-Agent Features")
st.sidebar.markdown("- **Contextual Understanding**: Grasp the context of HR-related queries to provide accurate responses.")
st.sidebar.markdown("- **Multimodal Input**: Process text and document uploads for comprehensive    analysis.")
st.sidebar.markdown("- **Personalized Responses**: Tailor answers based on company policies and culture.")
st.sidebar.markdown("- **Continuous Learning**: Improve over time with feedback and new HR trends.")
st.sidebar.markdown("- **Integration Capabilities**: Connect with HRIS and other enterprise systems for seamless operations.")
st.sidebar.markdown("- **Scalability**: Handle multiple queries simultaneously, ensuring prompt responses.")
st.sidebar.markdown("- **Security and Privacy**: Ensure data protection and confidentiality in all interactions.")

#create sidebar for adjusting parameters
st.sidebar.title("AI-Agent Tools")
st.sidebar.markdown("### AI-Agent Tools")
st.sidebar.markdown("- **Natural Language Processing (NLP)**: Understand and respond to human language queries effectively.")
st.sidebar.markdown("- **Machine Learning (ML)**: Continuously learn from interactions to improve response accuracy.")
st.sidebar.markdown("- **Document Parsing**: Extract relevant information from uploaded HR documents.")
st.sidebar.markdown("- **Sentiment Analysis**: Gauge employee sentiment from feedback and communications.")
st.sidebar.markdown("- **Knowledge Base Integration**: Access and utilize company-specific HR knowledge bases.")
st.sidebar.markdown("- **Workflow Automation**: Streamline HR processes such as leave approvals and onboarding.")
st.sidebar.markdown("- **Data Analytics**: Provide insights and reports on HR metrics and trends.")



#create sidebar for adjusting parameters
st.sidebar.title("Settings/Modle Parameters")    
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
max_tokens = st.sidebar.slider("Max Tokens", min_value=1, max_value=4096, value=256)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 1.0, 0.1)
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.1)
st.sidebar.markdown("Adjust the parameters to fine-tune the AI's responses.")





#update the interface with previous messages
for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.markdown(f"**You:** {msg['content']}")
    elif msg['role'] == 'assistant':
        st.markdown(f"**HR-AISOLUTIONS-ChatGPT:** {msg['content']}")

#create the chat interface
if prompt := st.chat_input("Type your message here..."):
    # Append user message to the session state
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message('user'):
        st.markdown(prompt)  
    
    # get response from the model
    with st.chat_message('assistant'):
        client = st.session_state['model']
        stream = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": message["role"], "content": message["content"]} for message in st.session_state['messages']
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True
        )

        response = st.write_stream(stream)
    st.session_state['messages'].append({"role": "assistant", "content": response})


######## login and signup page ############
def main():
    st.title("Login and Signup Page")

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the HR-AISOLUTIONS-ChatGPT App")
        st.write("This is the home page. Please login or sign up to continue.")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            # Here you can add your authentication logic
            if username == "admin" and password == "admin":
                st.success(f"Logged In as {username}")
                st.info("Go to the Chat section to start chatting.")
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        if st.button("Signup"):
            # Here you can add your signup logic
            st.success(f"Account created for {new_user}")
            st.info("Go to the Login section to log in.")   

#########login and signup page2 ############
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Implement your authentication logic here (e.g., check against a database)
        if username == "user" and password == "password": # Example credentials
            st.success("Logged in successfully!")
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password.")

def signup_page():
    st.title("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Sign Up"):
        if new_password == confirm_password:
            # Implement your user creation logic here (e.g., save to a database)
            st.success("Account created successfully!")
            st.session_state["logged_in"] = True # Automatically log in after signup
        else:
            st.error("Passwords do not match.")

# Main app logic
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    col1, col2 = st.columns(2)
    with col1:
        login_page()
    with col2:
        signup_page()
else:
    st.write("Welcome! You are logged in.")
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

    # handle message overflow based on the model size
