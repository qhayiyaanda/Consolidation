from django.apps import AppConfig

class UserAuthConfig(AppConfig):
    """
    AppConfig class for managing the 'user_auth' Django app.

    Attributes:
    - default_auto_field (str): Specifies the default auto-generated primary key field type
        for models in this app. Defaults to 'django.db.models.BigAutoField'.
    - name (str): The name of the Django app, which is set to 'user_auth'.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'

