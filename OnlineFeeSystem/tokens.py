from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, student_register, timestamp):
        return (
            six.text_type(student_register.enroll_id) + six.text_type(timestamp) +
            six.text_type(student_register.email)
        )

account_activation_token = AccountActivationTokenGenerator()