import streamlit as st

# Define your function to generate responses
def get_response(message):
    # Your logic for generating responses goes here
    return "This is a generated response to: " + message

# Define your Streamlit app
def main():
    st.title("Capital Rent a Car Chatbot")
    
    # Get user input
    message = st.text_input("Enter your message here:")
    
    # Check if user submitted a message
    if message:
        # Generate response
        response = get_response(message)
        # Display response
        st.write("Response:", response)

# Run the Streamlit app
if __name__ == "__main__":
    main()
