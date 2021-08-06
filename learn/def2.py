def ask_ok(prompt,retries=4,reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('ye',"y","yes"):
            return True
        if ok in ('n','no','nop'):
            return False
        retries = retries -1
        if retries<0:
            raise ValueError('invaild use response')
        print(reminder)
        
        ask_ok('Do you really want to quit?')