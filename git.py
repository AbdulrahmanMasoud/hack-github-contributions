import os , random

for i in range(200):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin master
#git rebase origin/master
