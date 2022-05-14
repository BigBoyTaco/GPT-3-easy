#imports
import os
#setup
try:
    import key
except:
    api_key = input('please input your api key: ')
    organization = input('please input your organization id: ')
    y_n = input('would you like to save this info?(WARNING NOT VERY SECURE)(y/n): ')
    if(y_n == 'y'):
        with open('key.py', 'w') as k:
            k.write('key = "' + api_key + '"' + '\norganization = "' + organization + '"')
try:
    import openai
except:
    input('some required packages are not installed press enter to install them')
    os.system('pip install openai')
    print('finished installing required packages please restart ai thingy')

#stuff
try:
    openai.organization = key.organization
    openai.api_key = key.key
    openai.Engine.list()
except:
    openai.organization = organization
    openai.api_key = api_key
    openai.Engine.list()

def main():
    prompt = input('what do you want this ai to write?: ')
    if(prompt == 'exit'):
        exit()
    print('working please wait...')
    response = openai.Completion.create(engine = 'text-davinci-002', prompt=prompt, temperature = 1, max_tokens = 1000, top_p = 1, frequency_penalty = 0, presence_penalty = 0)
    print(response['choices'][0]['text'])
    with open('result.txt', 'w') as f:
        f.write(response['choices'][0]['text'])
    print('completed, a result.txt file was also created')
    input()
main()
input()