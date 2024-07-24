# 📚 Hierarchical Multi-Document RAG System for Textbook Q&A
This repository contains the implementation of a hierarchical multi-document Retrieval-Augmented Generation (RAG) system for question answering on textbooks.

## 🔍 Overview
This project implements an advanced question-answering system designed to work with multiple textbooks. It uses a combination of natural language processing techniques and large language models to extract, index, retrieve, and generate answers from textbook content.

Key features of the system include:
1. 📄 Content extraction from PDF textbooks
2. 🌳 Hierarchical tree-based indexing of the extracted content
3. 🔎 Hybrid retrieval using multiple techniques
4. 🏆 Reranking of retrieved results
5. 💡 Answer generation using a state-of-the-art language model

## 🛠️ System Components

### 1. Content Extraction 📄
- Utilizes PyMuPDF to extract text content from PDF files
- Processes multiple textbooks simultaneously

### 2. Hierarchical Indexing 🌳
- Implements a custom tree-like structure to represent the hierarchical nature of textbook content
- Allows for efficient navigation and retrieval of specific sections or chapters

### 3. Hybrid Retrieval 🔎
- Combines three different retrieval methods for comprehensive results:
  a. 🧠 Dense Passage Retrieval (DPR) using FAISS for semantic search
  b. 🔤 BM25 algorithm for traditional keyword-based retrieval
  c. 🔍 Whoosh for full-text indexing and search
- Integrates results from all three methods to improve retrieval accuracy

### 4. Query Expansion 🔀
- Implements synonym expansion and stemming to enhance query understanding
- Improves the system's ability to match relevant content

### 5. Reranking 🏆
- Uses a cross-encoder model to rerank the initially retrieved results
- Enhances the relevance of the top results used for answer generation

### 6. Answer Generation 💡
- Employs a T5 model for conditional generation of answers
- Utilizes the reranked top results as context for generating accurate and relevant answers

## 📚 Textbooks Used

The system was developed and tested using the following textbooks:
1. "Never Split the Difference"
2. "How to Talk to Anyone"
3. "What to Say When You Talk to Yourself"

## 🚀 Setup and Usage

Detailed instructions for setting up and using the system are provided in the NOTEBOOKS. This includes information on:
- Required dependencies
- Steps for content extraction and indexing
- How to run queries and generate answers

##🚀 Future Development
🔮 The app version of this tool is currently in progress. 
I'm working on creating a user-friendly application that will make this tool even easier to use.

## 📝 Note

This system is designed to run in a Kaggle notebook environment with GPU support. Modifications may be necessary to run it in other environments.

For any questions or issues, please open an issue in this repository. 🙋‍♂️🙋‍♀️





