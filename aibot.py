import streamlit as st
st.chat_message("AI",avatar="aibot.png").write("Hello! I am your AI chatbot.")
st.chat_message("AI",avatar="aibot.png").write("You can ask me about: hi, name, college, course, python, time, weather, thanks, help, bye")
command=st.chat_input("Enter your command")
if command:
	st.chat_message("User",avatar="user.png").write(command)
	if command.lower()=="hi":
		st.chat_message("AI",avatar="aibot.png").write("Hello! How are you?")
	elif command.lower()  == "name":
    		st.chat_message("AI",avatar="aibot.png").write(" My name is Python Bot.")

	elif command.lower()  == "college":
    		st.chat_message("AI",avatar="aibot.png").write(" I am a college assistant chatbot.")

	elif command.lower()  == "course":
    		st.chat_message("AI",avatar="aibot.png").write("We offer BCOM, BBA and BCA courses.")

	elif command.lower()  == "python":
    		st.chat_message("AI",avatar="aibot.png").write("Python is a high-level programming language.")

	elif command.lower()  == "time":
    		st.chat_message("AI",avatar="aibot.png").write(" You can check the current time on your device.")

	elif command.lower()  == "weather":
   		st.chat_message("AI",avatar="aibot.png").write(" I hope the weather is pleasant today!")

	elif command.lower()  == "thanks":
   		st.chat_message("AI",avatar="aibot.png").write(" You're welcome!")

	elif command.lower()  == "help":
   		 st.chat_message("AI",avatar="aibot.png").write(" Try commands like hello, name, college, course or python.")

	elif command.lower()  == "bye":
    		st.chat_message("AI",avatar="aibot.png").write(" Goodbye! Have a nice day.")
	else:
		 st.chat_message("AI",avatar="aibot.png").error("Please choose the options from the list")
