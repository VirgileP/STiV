import datetime

now = datetime.datetime.now()

class horaire(object):

    def breakfast(self):
        today7am = now.replace(hour=7, minute=1, second=0, microsecond=0)
        today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
        if (self >= today7am) and (self <= today9am):
            print (True)
            print('breakfast')
        else:
            print (False)
            print('breakfast')

    def morning(self):
        today9am = now.replace(hour=9, minute=1, second=0, microsecond=0)
        today11am = now.replace(hour=11, minute=30, second=0, microsecond=0)
        if (self >= today9am) and (self <= today11am):
            print (True)
            print('morning')
        else:
            print (False)

    def lunch(self):
        today11am = now.replace(hour=11, minute=31, second=0, microsecond=0)
        today14am = now.replace(hour=14, minute=0, second=0, microsecond=0)
        if (self >= today11am) and (self <= today14am):
            print (True)
            print('lunch')
        else:
            print (False)
            print('lunch')

    def shopping(self):
        today14am = now.replace(hour=14, minute=1, second=0, microsecond=0)
        today19am = now.replace(hour=19, minute=0, second=0, microsecond=0)
        if (self >= today14am) and (self <= today19am):
            print (True)
            print('shopping')
        else:
            print (False)
            print('shopping')

    def diner(self):
        today19am = now.replace(hour=19, minute=1, second=0, microsecond=0)
        today22am = now.replace(hour=22, minute=0, second=0, microsecond=0)
        if (self >= today19am) and (self <= today22am):
            print (True)
            print('diner')
        else:
            print (False)
            print('diner')

    def night(self):
        today22am = now.replace(hour=22, minute=1, second=0, microsecond=0)
        today7am = now.replace(hour=7, minute=0, second=0, microsecond=0)
        if (self >= today22am) and (self <= today7am):
            print (True)
            print('night')
        else:
            print (False)
            print('night')

print(horaire.breakfast(now))
print(horaire.diner(now))
print(horaire.lunch(now))
print(horaire.morning(now))
print(horaire.night(now))
print(horaire.shopping(now))
