
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User



class EmailAuthBackend(ModelBackend):
    def authenticate(self,request,username =None, password = None):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                success = user.check_password(password)
                if success:
                    return user
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None