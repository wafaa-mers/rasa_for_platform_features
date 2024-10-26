# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionAddExpense(Action):
#     def name(self) -> str:
#         return "action_add_expense"

#     def run(self, dispatcher, tracker, domain):
#         amount = tracker.get_slot('amount')
#         category = tracker.get_slot('category')
#         date = tracker.get_slot('date')

#         # Process the expense addition logic here
#         response_message = f"Your expense of {amount} for {category} on {date} has been successfully added."
        
#         dispatcher.utter_message(text=response_message)
#         return []



# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet
# from typing import Any, Text, Dict, List

# class ActionAddExpense(Action):
#     def name(self) -> Text:
#         return "action_add_expense"

#     def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
#         # Retrieve slot values for expense details
#         amount = tracker.get_slot("amount")
#         category = tracker.get_slot("category")
#         date = tracker.get_slot("date")

#         # Assuming you have a function `add_expense_to_db` to add to the database
#         if amount and category and date:
#             # Call a function to add the expense to your database
#             success = add_expense_to_db(amount, category, date)

#             if success:
#                 dispatcher.utter_message(response="utter_confirm_expense_added", amount=amount, category=category, date=date)
#             else:
#                 dispatcher.utter_message(text="There was an error adding your expense. Please try again.")
#         else:
#             dispatcher.utter_message(text="I need more information to add the expense. Please specify the amount, category, and date.")

#         # Return an empty list of events
#         return []

# # Example of a helper function to add expense data to a database (to be implemented)
# def add_expense_to_db(amount, category, date):
#     # This function would contain code to add the expense to your database
#     # For example, you could use SQLAlchemy or another ORM
#     try:
#         # Example of adding to a database
#         # db.session.add(Expense(amount=amount, category=category, date=date))
#         # db.session.commit()
#         print(f"Expense added: {amount} for {category} on {date}")
#         return True
#     except Exception as e:
#         print(f"Error adding expense: {e}")
#         return False
