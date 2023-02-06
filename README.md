# multilingual_moodbot

## You need a working Rasa installation to run the bot

This is a PoC multilingual chatbot made in Rasa inspired by [this post](https://forum.rasa.com/t/multilingual-chatbot/46102) on the Rasa forum. 

The bot uses [Google Translate API](https://pypi.org/project/googletrans/) translate its replies to French. (check the **actions.py** file)

The bot is understands user messages in English and in French but replies only in French. This can be easily customised by having a slot indicating in what language the bot should reply. 
