# import azure.functions as func

import os
import re  
import logging
import json
import jsonschema
from EmbeddingGenerator.chunker.text_chunker import TextChunker
from EmbeddingGenerator.chunker.chunk_metadata_helper import ChunkEmbeddingHelper
from EmbeddingGenerator.embedder import text_embedder
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion, AzureTextCompletion

# local utils and shortcuts
from utils import *

import sys
sys.path.append('')

# removes timings and empty strings from vtt files
def cleanUpVTT(filename):
    output = filename + '.cleaned.txt'  
    
    regexArray = [  
        r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}',  
        r'\d{2}:\d{2}:\d{2}.\d{3} -->',   
        r'^\s*$'  
    ]  
    
    matchPattern = '|'.join(map(re.escape, regexArray))  
    
    try:    
        streamWriter = open(output, 'w', encoding='utf-8')    
        
        with open(filename, 'r') as reader:  
            for line in reader:  
                found = False  
                for regex in regexArray:  
                    if re.search(regex, line):  
                        found = True  
                        break  
                
                if found:  
                    continue  
    
                # print(line, end='')  
                streamWriter.write(line)  
    
    finally:    
        streamWriter.close()  

    return output


def split_chunks(filepath):
    TEXT_CHUNKER = TextChunker()

    sleep_interval_seconds = int(os.getenv("AZURE_OPENAI_EMBEDDING_SLEEP_INTERVAL_SECONDS", "1"))
    num_tokens = int(os.getenv("NUM_TOKENS", "2500"))
    min_chunk_size = int(os.getenv("MIN_CHUNK_SIZE", "10"))
    token_overlap = int(os.getenv("TOKEN_OVERLAP", "0"))

    text = read_all(filepath)

    chunking_result = TEXT_CHUNKER.chunk_content(text, file_path=filepath, num_tokens=num_tokens, min_chunk_size=min_chunk_size, token_overlap=token_overlap)

    # TODO: embeddings, vector search later 
    #CHUNK_METADATA_HELPER = ChunkEmbeddingHelper()
    #content_chunk_metadata = CHUNK_METADATA_HELPER.generate_chunks_with_embedding(document_id, [c.content for c in chunking_result.chunks], fieldname, sleep_interval_seconds)
    #for document_chunk, embedding_metadata in zip(chunking_result.chunks, content_chunk_metadata):
    #    document_chunk.embedding_metadata = embedding_metadata

    return chunking_result


#prepare chunks

startingFile = "C:/Recordings/01/Azure SQL High Availability and Disaster Recovery.txt"

file = cleanUpVTT(startingFile)
chunking_result = split_chunks(file)

# init kernel
kernel = sk.Kernel()
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service("dv", AzureTextCompletion(deployment, endpoint, api_key))

all_summary = ""

cnt = 0
for chunk in chunking_result.chunks:
    cnt += 1
    print("******************************************")
    print("chunk " + str(cnt))
    print("******************************************")
    # print(chunk.content)

    chunkFile = startingFile + ".chunk" + str(cnt) + ".txt"
    #write the chunk to a file
    write_file(chunkFile, chunk.content)

    summaryFile = startingFile + ".summary" + str(cnt) + ".txt"

    context = kernel.create_new_context()

    prompt_text = chunk.content + "\n\n identify key points"
    # ask for summary 
    prompt = kernel.create_semantic_function( prompt_text )

    # answer = await prompt.invoke_async(context)
    # answer = await prompt.invoke_async(context)
    # answer = await kernel.run_on_vars_async(context, prompt)
    
    res = prompt()
    write_file(summaryFile, res.result)

    all_summary += chunkFile + "\n\n" + res.result + "\n\n"

write_file(startingFile + ".summary_all.txt", all_summary)  

