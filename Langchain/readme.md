# LangChain Learning Summary

This repository contains learnings and experiments with the **LangChain** framework for building LLM-powered applications.

## Core Concepts & Components

### 1. Models
- Abstract interface for interacting with various types of language models (LLMs, chat models, embedding models).
- Enables model-agnostic development and easy swapping of different providers (OpenAI, Hugging Face, etc.).

### 2. Prompt
- Structured templates that dynamically generate input prompts for models.
- Supports role-based, few-shot, and chat prompt templates for flexible and reusable prompt design.

### 3. Structured Output
- Enforces LLM outputs to follow strict formats like JSON or Pydantic models.
- Improves downstream parsing, validation, and consistency.

### 4. Output Parser
- Converts raw LLM responses into structured formats to ensure your app can reliably interpret outputs.
- Examples include JSON parsers, regex-based parsers, and custom handlers.

### 5. Chains
- Chains connect multiple components (models, prompts, parsers) sequentially or conditionally.
- Enables building complex workflows like sequential chains, parallel chains, and conditional branching.

### 6. Runnables
- Reusable, composable primitives that represent steps in an AI pipeline.
- Examples include `RunnableSequence`, `RunnableParallel`, `RunnableBranch`.
- Provides fine-grained control over execution flow, logic branching, and concurrency.

### 7. Document Loaders
- Modules for loading different data sources (PDF, text files, web pages, CSV) into LangChain's document format.
- Enables feeding external knowledge into retrieval and generation chains.

### 8. Text Splitter
- Breaks large documents into manageable chunks to fit LLM input size constraints.
- Supports semantic splitting, length-based, and document-structure-based splitting.

### 9. Vector Stores
- Specialized databases optimized for storing and retrieving vector embeddings.
- Used to support semantic search and retrieval-based generation (RAG).
- LangChain supports multiple vector stores like FAISS, Pinecone, Chroma, Weaviate.

### 10. Retrievers
- Components that fetch relevant documents based on user queries, often backed by vector stores.
- Key to retrieval-augmented generation workflows.

## Summary

LangChain provides a **modular, extensible** ecosystem to build AI applications such as chatbots, summarizers, research assistants, and autonomous agents by combining LLMs with prompt engineering, structured output handling, and knowledge retrieval.

This framework simplifies complex AI app development with reusable components, consistent abstractions, and integrations with popular LLM providers and vector databases.

---

Explore each component in this repo with practical examples to deepen your understanding of building scalable LLM-powered applications using LangChain.
