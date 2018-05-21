import sys;
reload(sys);
sys.setdefaultencoding("utf8")
import telegramMessaging

def matchInfo(match, complete):
    if complete==1 : telegramMessaging.sendMessage('OMG! Someone complete the QUIZ!!')
    if complete==0 : telegramMessaging.sendMessage('New match!')
    telegramMessaging.sendMessage('Name: ' + str(match.user.name))
    telegramMessaging.sendMessage('Age: ' + str(match.user.age))
    telegramMessaging.sendMessage('Bio: ' + str(match.user.bio))
    telegramMessaging.sendMessage('Jobs: ' + str(match.user.jobs))
    telegramMessaging.sendMessage('Schools: ' + str(match.user.schools))
    telegramMessaging.sendMessage('Tinder photos:')
    if match.user.photos:
        for p in match.user.photos: telegramMessaging.sendMessage(str(p))
    telegramMessaging.sendMessage('Instagram profile: ' + str(match.user.instagram_username))
    telegramMessaging.sendMessage('Instagram photos:')
    if match.user.instagram_photos:
        for t in match.user.instagram_photos: telegramMessaging.sendMessage(str(t))

