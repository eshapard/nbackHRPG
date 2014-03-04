#/usr/bin/python
import csv, sys, ConfigParser, urllib2
#location of stats file
statfile = './data/stats.txt'
#location of config file
config_file = 'nbackHRPG.conf'
config = ConfigParser.RawConfigParser()
config.read(config_file)
hrpg_user = config.get('HabitRPG', 'user_id')
hrpg_token = config.get('HabitRPG', 'api_token')
score = int(config.get('Nback', 'score'))
last_datetime = config.get('Nback', 'last_datetime')

def internet_on():
    try:
        response=urllib2.urlopen('http://habitrpg.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

#HabitRPG variables
habit_post = urllib2.Request('https://habitrpg.com/api/v1/user/task/NBack/up','')
habit_post.add_header('x-api-user', hrpg_user)
habit_post.add_header('x-api-key', hrpg_token)


#open stat file for reading
with open(statfile, 'rb') as f:
 reader = csv.reader(f)
 for row in reader:
   colnum = 0
   for col in row:
     #find and store date splitting of timestamp
     if colnum == 0:
       cur_datetime = col
     #find number of trials
     if colnum == 6:
       trials = int(col)
     #find n-back level
     if colnum == 4:
       nbacklevel = int(col)
     colnum += 1
   #if date = today, tally score
   if cur_datetime > last_datetime:
     #score += (nback level * trials) 
     score += (nbacklevel * trials)

print("%s trials unscored." % (score))
#Score HabitRPG
if internet_on:
 while score >= 100:
   print("Scoring 100 trials")
   #send habitrpg api signal
   urllib2.urlopen(habit_post)
   score -= 100

#Write new score to config_file
config.set('Nback', 'score', score)
config.set('Nback', 'last_datetime', cur_datetime)
with open(config_file, 'wb') as configfile:
   config.write(configfile)
