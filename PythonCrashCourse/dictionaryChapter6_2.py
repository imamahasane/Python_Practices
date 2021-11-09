fe_lang = {'jen': 'c', 'imam': 'python', 'sara': 'ruby', 'samiul': 'java'}
friend = ['imam', 'samiul']
for name in fe_lang.keys():
    print(name.title())

    if name in friend:
        lang = fe_lang[name].title()
        print(f"\t{name.title()}, I see you love {lang}")
