#%%
from distutils.log import info


def about(name,age,likes):
    sentence="Meet {}! They are {} year old and they like {} ".format(name,age,likes)
    return sentence

info=about("AnsIlyas",19,"Games")
# about(likes="games",age=19,name="Ans")

print(info)

