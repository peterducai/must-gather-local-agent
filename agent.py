import asyncio
from ollama import AsyncClient
from pathlib import Path

pathlist = Path('definitions').glob('**/*.txt')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)
    file = open(path_in_str, "r")

    # Read the entire content of the file
    content = file.read()
    print(content)


async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='ibm/granite4:latest', messages=[message])
  print(response)

#asyncio.run(chat())