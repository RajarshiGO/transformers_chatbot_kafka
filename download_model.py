#! /usr/bin/python
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id = "microsoft/DialoGPT-medium", filename = "pytorch_model.bin")