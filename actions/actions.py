# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Action

from googletrans import Translator

class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):

        translator = Translator()

        translated_text = translator.translate("Hey! How are you?", dest='fr')
        dispatcher.utter_message(translated_text.text)

        return []

class ActionHappy(Action):
    def name(self):
        return 'action_happy'

    def run(self, dispatcher, tracker, domain):

        translator = Translator()

        translated_text = translator.translate("Great, carry on!", dest='fr')
        dispatcher.utter_message(translated_text.text)

        return []

class ActionCheerUp(Action):
    def name(self):
        return 'action_cheer_up'

    def run(self, dispatcher, tracker, domain):

        translator = Translator()

        translated_text = translator.translate("Here is something to cheer you up:", dest='fr')
        dispatcher.utter_message(text=translated_text.text, image="https://i.imgur.com/nGF1K8f.jpg")

        return []

class ActionDidThatHelp(Action):
    def name(self):
        return 'action_did_that_help'

    def run(self, dispatcher, tracker, domain):

        translator = Translator()

        translated_text = translator.translate("Did that help?", dest='fr')
        dispatcher.utter_message(translated_text.text)

        return []

    