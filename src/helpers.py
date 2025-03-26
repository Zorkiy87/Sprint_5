import random

class Helpers:
    EMAIL = 'Mike_Kozulin_19_709@yandex.ru'
    PASSWORD = 'qwerty'
    INC_PASSWORD = 'qwert'
    NAME = 'Mike'



    def get_random_email():
        email_name = 'Mike_Kozuiln_19_'
        domain = '@yandex.ru'
        rad = random.randint(100,999)
        random_email = email_name + str(rad) + domain
        return random_email

    def get_random_password():
        random_password = random.randint(100000, 999999)
        return random_password