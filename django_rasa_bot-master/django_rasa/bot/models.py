from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def save_file(string, path):
    if default_storage.exists(path):
        default_storage.delete(path)
    default_storage.save(path, ContentFile(string))
    

def create_bot_files():
    nlu_file_path = 'rasa_files/data/nlu.yml'
    domain_file_path = 'rasa_files/domain.yml'
    stories_file_path = 'rasa_files/data/stories.yml'
    

    #nlu file
    nlu_string = "version: \"3.0\" \n \nnlu: \n"
    for category in Intent.objects.all():
        nlu_string += f"- intent: {category} \n     examples: \n"
        for question in Usermsg.objects.filter(example_of_intent=category):
            nlu_string += f"        - {question} \n"
        nlu_string += "\n \n"
    save_file(nlu_string, nlu_file_path)
    





    # domain file
    domain_string = "version: \"3.0\" \n \nintents: \n"
    for category in Intent.objects.all():
        domain_string += f" - {category} \n"  
    domain_string += "\n \nresponses: \n"

    for category in Action.objects.all():
        domain_string += f" utter_{category.title}: \n "

        for category in Answer.objects.filter(action=category):
            domain_string += f" - text: {category.answer_text} \n "  
        domain_string += "\n \n"
    save_file(domain_string, domain_file_path)




    # stories file
    stories_string = "version: \"3.0\" \n \nstories: \n"
    
    for story in Story.objects.all():
        stories_string += f"- story: {story.title}\n steps: \n"
        for intent in Intent.objects.filter(story=story):
            stories_string += f"    - intent: {intent.name} \n"
        for action in Action.objects.filter(story=story):
            stories_string += f"    - action:  utter_{action.title} \n"
        stories_string += "\n \n"
    save_file(stories_string, stories_file_path)
 

class Story(models.Model):
    title = models.CharField("Story Title", max_length=50)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"
        
   
class Intent(models.Model):
    name = models.CharField("Intent Name", max_length=50)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Intent"
        verbose_name_plural = "Intents"

class Usermsg(models.Model):
    user_msg_text = models.CharField("Text of User Massage (Example)", max_length=50)
    example_of_intent = models.ManyToManyField(
        Intent, related_name="Intents"
    )

    def __str__(self):
        return self.user_msg_text
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "User Massage (Example)"
        verbose_name_plural = "User Massages (Examples)"



        

class Action(models.Model):
    title = models.CharField("Action Title", max_length=50)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"



class Answer(models.Model):
    answer_text = models.CharField("Answer Text", max_length=50)
    action = models.ManyToManyField(Action, related_name="action_text")

    def __str__(self):
        return self.answer_text
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_bot_files()

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        
