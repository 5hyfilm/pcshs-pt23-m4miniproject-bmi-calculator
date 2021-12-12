#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Information():
    print('')
    print('ถ้าต้องการดูข้อมููลเกี่ยวกับ BMI กด 1 ถ้าไม่ต้องการกด 0')
    print('')
    press = int(input('เลืือกหมายเลข: '))
    if press == 1:
        f = open('Information.txt')
        reader = f.read()
        print('')
        print(reader)
        print('-'*117)
        f.close()
    elif press == 0:
        print('')

