## install langchain[llms]
```shell
pip install langchain[llms]
```

## install library in requirements.txt
```shell
pip install -r requirements.txt
```

## Workflow upload file
> input parameters: profile_id, files
```mermaid
graph TD
   A[Upload document] --> B[Hash content]
   B --> C[Save profile map file name and file hash]
   B --> D[Save file to hashed folder]
   C --> E[Return profile files]
   D --> E
```

## Workflow embedding document
> input parameters: profile_id
```mermaid
graph TD
   A[Get list of profile files] --> B[Convert to Document]
   B --> C[Split text content to chunks] 
   C --> F[Embedding chunks to ChromaDB]
```

## Workflow query document
> input parameters: profile_id, query
```mermaid
graph TD
   A[Create retriever from chromaDB] --> D[Create retrieval question-answer]
   B[Create prompt] --> D
   C[Create large language model] --> D
   D --> E[Return result]
```
## Reference
- [LocalGPT] [https://github.com/PromtEngineer/localGPT