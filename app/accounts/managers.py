from django.contrib.auth.base_user import BaseUserManager

# ----------------------
# All Users Manager ---
# ----------------------


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(username, password, **other_fields)

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have an username address")
        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user
