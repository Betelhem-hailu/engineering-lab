# Vector Similarity

1. Why does an embedding allow us to compare meaning?
Embeddings turn information into vectors where semantic relationships can be measured mathematically.
2. What is cosine similarity?
Cosine similarity is the measurement of the angle between the vectors on the vector space.
3. Why would semantic search find:
    "How do I reset my password?"
    when the document says:
    "Users can recover their account credentials through the account recovery page."
    even though the exact words aren't the same?
 The words in the document are stored in vector form and when the search is applied it changes in the vector form and applies the search based on the similarity. Here we are not making exact word by word search instead it compares the semantic and meaning of the information too
4. Where would this fit into your AI Document Assistant?
Embeddings are primarily used to retrieve relevant information. The LLM then uses the retrieved information to generate the answer.
