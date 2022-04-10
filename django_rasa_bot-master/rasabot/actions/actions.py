import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from api import loginApi, degreeApi, classInfoApi


logging.basicConfig(level=logging.DEBUG)
db_file="./actions/db.sqlite3"
class AuthenticatedAction(Action):
    def name(self) -> Text:
        return "action_authenticated"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
            username = tracker.get_slot("username")
            password = tracker.get_slot("password")
            # Api call
            user_id = loginApi(username, password)
            
            if user_id is not None:
                dispatcher.utter_message(template="utter_authenticated_successfully")
                return [SlotSet("is_authenticated", True), SlotSet("student_id",user_id)]
            
            else:
                dispatcher.utter_message(template="utter_authentication_failure")      
            return []

class CourseDegreeAction(Action):
    def name(self) -> Text:
        return "action_course_degree"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
        
        if tracker.slots.get("is_authenticated", False) == False:
            dispatcher.utter_message(template="utter_authentication_required")
            return []
            
        student_id = tracker.get_slot("student_id")
        course_name = tracker.get_slot("course_name")
        # Api call
        _, _, degree  = degreeApi(user_id=student_id, course_name=course_name)
        
        if student_id is not None:
            dispatcher.utter_message(text="Your degree in the {} course is: {}".format(course_name, degree))
            return [SlotSet("course_name", None)]
            
        else:
            dispatcher.utter_message(text="You are not in the class of there is no degree")        
        return []

class ClassInfoAction(Action):
    def name(self) -> Text:
        return "action_class_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
        
        if tracker.slots.get("is_authenticated", False) == False:
            dispatcher.utter_message(template="utter_authentication_required")
            return []    
        
        course_name = tracker.get_slot("course_name")    
        # Api call
        data = classInfoApi(course_name=course_name)
            
                    
        if data is not None or data is not []:
            for class_info in data:
                dispatcher.utter_message(text="The class {} for the {} course is on {} starting at {} - til {}, with Ms. {}".format(class_info['class_title'],
                                                                                                                               class_info['course_title'],
                                                                                                                               class_info['class_day'] ,
                                                                                                                               class_info['start_time'] ,
                                                                                                                               class_info['end_time'] ,
                                                                                                                               class_info['lecturer']))
            return [SlotSet("course_name", None)]

        else:
            dispatcher.utter_message(text="Sorry, but i didnt find and results!")         
        return []

class ComplaintAction(Action):
    def name(self) -> Text:
        return "action_complaint"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
        
        if tracker.slots.get("is_authenticated", False) == False:
            dispatcher.utter_message(template="utter_authentication_required")
            return []    
        
        username = tracker.get_slot("username")
        complaint = tracker.get_slot("complaint")    
        
        if complaint is not None:    
            dispatcher.utter_message(template="utter_complaint_send_successfully")
        
        else:
            dispatcher.utter_message(text="Sorry, didn't catchup your complaint")
            
        return [SlotSet("complaint", None)]
        