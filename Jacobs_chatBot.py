# -*- coding: utf-8 -*-
from nltk.chat.util import Chat, reflections
import webbrowser
import sys

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
	[
        r"(.*)(good|great)",
        ["Glad to hear that",]
    ],
     [
        r"(.*)your name ?",
        ["My name is Chatty and I'm a chatbot",]
    ],
	[
        r"(why|how)(.*)name ?",
        ["Because I love to chat :)",]
    ],
	[
        r"(.*)reason(.*)name ?",
        ["Because I love to chat :)",]
    ],
	[
        r"(.*)(help|assist)(.*)",
        ["I can help you with various things such as finding key contacts in Jacobs finance and an overview of Jacobs. Please submit your query",]
    ],
    [
        r"(.*)how are you(.*) ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Vid created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city|located|place) ?",
        ['64 Allara stret, Canberra','Jacobs Australia, Canberra']
    ],
	[
        r"(.*)HR (email|contact)",
        ['Roma.Devi@jacobs.com']
    ],
	[
        r"(.*)hr (email|contact)",
        ['Roma.Devi@jacobs.com']
    ],
	[
        r"(.*)payroll (email|contact)",
        ['Please email your query to Payroll.JA@jacobs.com']
    ],
	[
        r"(how|what|where)(.*)(payslip|payslips|payg|payg summary)",
        ['Jacobs uses ADP payroll system. You can access payslips and payg summaries by logging into ADP payroll using the URL https://secure.adppayroll.com.au/ Please use S121764 as the client id and use your employee/oracle id as the user ID']
    ],
	[
        r"(.*) travel insurance",
        ['You can find information about Corporate Travel Insurance in https://jacobsconnect.jacobs.com/docs/DOC-240775']
    ],
	[
        r"(.*) (travel policy|official travel|company travel|business travel|corporate travel)",
        ['You can find information about travel policy on https://jax.jacobs.com.au/Download.asp?file=General/Travel/JA%20Travel%20Policy%202015-04.pdf Please note that you need to be logged on to Jacobs Extranet (https://jax.jacobs.com.au/) before accessing the travel policy link']
    ],
	[
        r"(.*) payroll",
        ['Please email your query to Payroll.JA@jacobs.com']
    ],
	[
        r"(.*) extranet",
        ['Please use the link: https://jax.jacobs.com.au/Login.asp']
    ],
	[
        r"(.*)timecard(.*)",
        ['Please use the link: https://ejamis.jacobstechnology.com/jaus/login.aspx']
    ],
		[
        r"(.*)(jacobs connect|jacobsconnect)(.*)",
        ['Please use the link: https://jacobsconnect.jacobs.com/welcome']
    ],
	[
        r"(what|who|do|does) (.*) jacobs (.*)",
        ['Please use the link: https://jacobsconnect.jacobs.com/welcome']
    ],
	[
        r"(what|who|do|does) jacobs (.*)",
        ['Please use the link: https://jacobsconnect.jacobs.com/welcome']
    ],
	
	[
        r"(.*)(leave balance|leave|leave balances)(.*)",
        ['Please use the link: http://ets.jacobs.com']
    ],
	
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining (in|at) (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %3"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) moviestar?",
        ["Brad Pitt"]
],
[
        r"who (.*) actor",
        ["Brad Pitt"]
],
    [
        r"Do you (want|need) (.*)?",
        ["Yes, please"]
],

    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
[
        r"(.*)",
        ["Sorry, i don't have an answer for that"]
],
]
def chatty():
	print(sys.getdefaultencoding())
	print("\n\nHi, I'm Chatty and I can help you with general information on Jacobs Australia :)\nPlease type lowercase English language to start a conversation. Type quit to leave\n\n")
	chat = Chat(pairs, reflections)
	chat.converse()
	
if __name__ == "__main__":
    chatty()
	