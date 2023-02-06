# multilingual_moodbot

This is a PoC multilingual chatbot made in Rasa inspired by [this post](https://forum.rasa.com/t/multilingual-chatbot/46102) on the Rasa forum. 

The bot uses Google translate API in custom actions to send replies translated in French. (check the **actions.py** file)

The bot is understands user messages in English and in French but replies only in French. This can be easily customised by having a slot indicating in what language the bot should reply. 
