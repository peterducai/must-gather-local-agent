#!/bin/bash

ollama pull ibm/granite4.1:3b
ollama pull gemma4
OLLAMA_CONTEXT_LENGTH=64000 ollama serve &
