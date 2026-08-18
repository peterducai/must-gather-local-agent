import asyncio
from ollama import Client
from pathlib import Path
import sys

definitions = None
testdata = None
data_path = sys.argv[1]
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)

def read_definitions():
    global definitions
    for path in Path(__file__).parent.glob('definitions/*.txt'):
        path_in_str = str(path)
        file = open(path_in_str, 'r')
        definitions = file.read()
        #print(content)
        file.close()

def collect_logs():
    for path in Path(__file__).parent.glob('logs/*.txt'):
        path_in_str = str(path)
        print(path_in_str)
        file = open(path_in_str, 'r', encoding='utf-8')
        testdata = file.read()
        # print(testdata)
        file.close()

def read_data_folder():
    global testdata
    global data_path
    print(data_path)
    for path in Path(__file__).parent.glob(data_path):
        path_in_str = str(path)
        print(path_in_str)
        file = open(path_in_str, 'r', encoding='utf-8')
        testdata = file.read()
        #print(testdata)
        file.close()

def chat():
  global testdata
  global definitions
  message = {'role': 'user', 'content': definitions }
  response = client.chat(model='granite4.1:3b', messages=[message])
  print(response)

def chat2():
  global testdata
  message = {'role': 'user', 'content': 'Check log for any errors or warnings. Content: '+ str(testdata) }
  response = client.chat(model='granite4.1:3b', messages=[message])
  print(response)

#read_definitions()
read_data_folder()
chat()
chat2()