# MUST GATHER troubleshooting agent (CONCEPT)




```
sudo dnf install python3-pip -y
pip install uv
uv python install 3.12
uv venv --python 3.12 --seed --managed-python
source .venv/bin/activate
pip install llama-index-llms-ollama llama-index-embeddings-huggingface
 ```