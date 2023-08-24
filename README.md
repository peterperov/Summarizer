# Summarizer

Calls Azure ChatGPT to summarise the content of a given recording. 

## inputs 

Currently supported inputs: 

* mp4 video - extracts audio wav, uses Azure Speech service for Speech2Text
* .vtt subtitle files 
* .doc subtitle files from MS Teams


# Installation

## libraries 
```
pip install -r requirements.txt
```
## Settings files

.env file hosts key for ChatGPT and Speech API 

Chunker uses different local.settings.json format, and Ada model for embeddings. 

Make sure that .env and local.settings.json are in your .gitignore file so that credentials are not leaked through the git repo.

### Azure Service keys .env file 
```
AZURE_OPENAI_DEPLOYMENT_NAME="davinci"
AZURE_OPENAI_ENDPOINT="https://xxx.openai.azure.com/"
AZURE_OPENAI_API_KEY="..."

AZURE_SPEECH_API_KEY="..."
AZURE_SPEECH_REGION="northeurope"
```

### local.settings.json 
```
{
    "IsEncrypted": false,
    "Values": {
      "FUNCTIONS_WORKER_RUNTIME": "python",
      "AzureWebJobsStorage": "UseDevelopmentStorage=true",
      "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
      "AZURE_OPENAI_API_KEY": "...",
      "AZURE_OPENAI_API_VERSION": "2023-05-15",
      "AZURE_OPENAI_EMBEDDING_DEPLOYMENT": "adaembedding",
      "AZURE_OPENAI_SERVICE_NAME": "xxx",
      "AZURE_OPENAI_EMBEDDING_SLEEP_INTERVAL_SECONDS": "30"
    }
  }
```

# Running


# References 

## ChatGPT token limits

Azure OpenAI has token limits on each model. For simplicity: 1 token - 4 letters. 

|gpt-35-turbo | 4K tokens |
|gpt-35-turbo-16k | 16k tokens |

To process large inputs I'm using chunker solution to break the text into chunks in a meaningful way: not in mid word/mid sentence, etc. 

[EmbeddingsGenerator from Azure Samples]
(https://github.com/Azure-Samples/azure-search-power-skills/tree/main/Vector/EmbeddingGenerator)

