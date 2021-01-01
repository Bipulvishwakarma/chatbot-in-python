import nltk 
from nltk.chat.util import Chat, reflections
import win32com.client
#speaker = win32com.client.Dispatch("SAPI.SpVoice")
#speaker.Speak("Welcome ")
training=[
	[
		"my name is(.*)",
		["Hello %1, How are you ?"]
	],
	 [
		"What is your name|what is ur name ?",
		["My name is Bipul vishwakarma","I am Bipul "]
		
	],
	 [
		"what is dbs ?",
		["Dbs is a Bank which is situated in Singapore"]
		
	],
	 [	
		"bye|tata",
		["ok bye"]
		
	],
	 [ 
		"I am a Boy",
		["oh thats great,Goodluck"]
		
	],
	 [
		"what is jbl ?",
		["speaker manufacturing comapny"]

	],
	 [
		"hello|hi",
		["Hi there How may I help you "]
		
	],
	 [
		"my account is block|account block|block",
		["follow the following step"]
],		
]

def fun():
	print("hello")
chat=Chat(training,reflections)
chat.converse()
if __name__=="__main__":
	fun()	
