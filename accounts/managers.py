from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, password=None, email=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError("User must have a username.")

        if email is None:
            raise TypeError("User must have an email address.")

        user = self.model(username=username, email=email, is_email_verified=False)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """

        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
