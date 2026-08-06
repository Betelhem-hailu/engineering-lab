# Introduction to AI

What is an embedding?
Is vector representation of information; can be video, audio, text, photo and more.
Index in vector represents numerical value floating between 0 & 1
dimensions of a vector describe the level of detail
What is a vector database?
A vector database indexes and stores vector embeddings for fast retrieval and similarity search, with capabilities like CRUD operations, metadata filtering, horizontal scaling, and serverless.
Why does RAG exist?
Retrieval-Augmented Generation (RAG) is an AI framework that integrates an information retrieval component into the generation process of Large Language Models (LLMs) to improve factuality and relevance.
LLM Limitations:LLMs are frozen snapshots. Once a model is trained, it only knows what was in its training data.
Cost of Retraining vs. Dynamic Retrieval
Dynamic retrieval (looking things up at query time) is vastly cheaper and always up-to-date.
RAG addresses all three challenges by decoupling knowledge from the model.
That's the whole RAG pipeline. Indexing → Retrieval → Augmentation → Generation.
