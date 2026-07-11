import asyncio
from ollama import AsyncClient
from pathlib import Path

testdata = ""

def read_definitions():
    for path in Path(__file__).parent.glob('definitions/*.txt'):
        path_in_str = str(path)
        file = open(path_in_str, 'r')
        content = file.read()
        #print(content)
        file.close()

def read_test_data():
    global testdata
    for path in Path(__file__).parent.glob('TEST_DATA/*.txt'):
        path_in_str = str(path)
        print(path_in_str)
        file = open(path_in_str, 'r', encoding='utf-8')
        testdata = file.read()
        #print(testdata)
        file.close()

async def chat():
  global testdata
  message = {'role': 'user', 'content': 'Read following content and tell me summary in 5 short points. Do not explain what you do just print summary points. Content: '+ str(testdata) }
  response = await AsyncClient().chat(model='granite4.1:3b', messages=[message])
  print(response)

#read_definitions()
read_test_data()
asyncio.run(chat())