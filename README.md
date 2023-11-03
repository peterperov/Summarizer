# Summarizer

Calls Azure ChatGPT to summarise the content of a given recording. 

## inputs 

Currently supported inputs: 

* mp4 video - extracts audio wav, uses Azure Speech service for Speech2Text
* .vtt subtitle files 
* .doc subtitle files from MS Teams

## Description

**audio_extractor.py** - extracts wav file from mp4, in fact from most of the video files supported by your system codecs. 
 
**subtitle_creator.py** - feeds extracted wav to Azure Cognitive Speech to Text, to extract text 
 
**process_vtt.py** - vtt format is a text file with timestamps. this core removes timestamps and other non-textual data, and creates a simple text file. Then it splits the text into chunks, and feeds it to ChatGPT for summary creation per chunk. 

**run_me.py** - runs the whole process, from mp4 to summary.

# Pre-requisites

Azure Subcription 
[Create Speech Resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices)
[Create OpenAI Resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

I used following models for text extraction: text-davinci-003, text-embedding-ada-002, gpt-35-turbo


## docs

[Quickstart: Recognize and convert speech to text](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-csharp)



# Python Installation and configuration

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

All .py files will have filename variable which specifies the input filename

## audio_extractor.py

Extracts audio wav from video file using ffmpeg to filename + ".audio_only.wav" in the same folder

## subtitle_creator.py 

Calls Azure Speech service to Speech to text conversion.


# References 

## ChatGPT token limits

Azure OpenAI has token limits on each model. For simplicity: 1 token - 4 letters. 

|gpt-35-turbo | 4K tokens |
|gpt-35-turbo-16k | 16k tokens |

To process large inputs I'm using chunker solution to break the text into chunks in a meaningful way: not in mid word/mid sentence, etc. 

[EmbeddingsGenerator from Azure Samples]
(https://github.com/Azure-Samples/azure-search-power-skills/tree/main/Vector/EmbeddingGenerator)

