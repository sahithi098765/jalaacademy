try:
    t=open('text1.txt','r')
    print(t.read())
except Exception as e:
    print(f'error:{e}')