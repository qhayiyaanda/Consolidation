from django.apps import AppConfig

class PollsConfig(AppConfig):
    """
    AppConfig for the 'polls' app.

    This class represents the configuration for the 'polls' app in Django.
    It sets the default_auto_field to 'django.db.models.BigAutoField'.

    Attributes:
    - default_auto_field (str): The default auto field used by the app.
    - name (str): The name of the app, in this case, 'polls'.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
