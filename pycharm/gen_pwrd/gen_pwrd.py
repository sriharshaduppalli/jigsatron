#Random password generator

import random
import string

class gen_pwrd:
    def __init__(self,name):
        self.name = name

    def random_combo(self):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        ran1 = ''.join(random.sample(self.name,len(self.name)))
        #print("Random combo for the name is {}".format(self.name))
        print("The randomly generated string is 1st way: " + str(ran))
        print("The randomly generated string is 2nd way: " + str(ran1))

test1 = gen_pwrd("Harsha")

test1.random_combo()
