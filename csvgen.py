"""
Just a simple script to randomly generate a lot of rows
"""
import random

f = open('ci_stats.csv', 'w')
it = 10000
statelist = ["success","failure","NULL","pending","opened","closed"]
contextlist = ["i","really","do","not","know","what","goes","in","here"]
a = []
for i in range(1000):
    #generate 1000 unique shas so we have some colliding
    a.append(hex(random.getrandbits(256)))

for i in range(it):
    state = statelist[random.randint(0,len(statelist)-1)] + ","
    sha = str(a[random.randint(0,len(a)-1)]) + ","
    repository_id = str(random.randint(1,100000)) + ","
    pull_request_id = str(random.randint(1,100000)) + ","
    context = contextlist[random.randint(0,len(contextlist)-1)] + ","
    f.write("NULL," + state + sha + repository_id + "NULL,NULL" + pull_request_id + context+"\n");

f.close()

f = open('repo.csv','w')
for i in range(it*10):
    f.write("NULL," + "this is some comment but does not matter since we only care about id anyway\n")

f.close()
