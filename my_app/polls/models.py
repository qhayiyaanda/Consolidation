from django.db import models

class Question(models.Model):
    """
    A class representing a question.

    Attributes:
        question_text (CharField): The text of the question.
        pub_date (DateTimeField): The date the question was published.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns a string representation of the Question instance.

        Returns:
            str: The text of the question.
        """
        return self.question_text

class Choice(models.Model):
    """
    A class representing a choice for a question.

    Attributes:
        question (ForeignKey): The related Question for this choice.
        choice_text (CharField): The text of the choice.
        votes (IntegerField): The number of votes for this choice.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the Choice instance.

        Returns:
            str: The text of the choice.
        """
        return self.choice_text
