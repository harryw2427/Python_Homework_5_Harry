#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input('Please tell me a number: '))
if a%2==0:
    print('That number is even')
else:
    print('That number is odd')


# In[51]:


Windy=input('Is it Windy today? Please enter True or False: ')
Cold=input('Is it Cold today? Please enter True or False: ')
if (Cold=='True' and Windy=='True'):
    print('I brought my jacket ')
elif (Cold=='True' and Windy=='False'):
    print('I guess I should go get my coldproof jacket')
elif (Windy=='True' and Cold=='False'):
    print('I guess I should go get my windproof jacket')
elif (Windy=='False' and Cold=='False'):
    print('I donnot need jacket')
else:
    print('That is not an option please choose a different answer')

