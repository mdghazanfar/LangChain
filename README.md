````markdown
# 🚀 LangChain Demo Repository

This repository contains **hands-on demos and notes** to help you learn and experiment with **LangChain**, a powerful framework for building applications powered by **Large Language Models (LLMs)**. LangChain simplifies creating **context-aware, data-connected applications** by bridging raw LLM APIs (e.g., OpenAI, Hugging Face, Anthropic, Gemini) with real-world use cases.

![LangChain Architecture](https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/static/img/langchain_architecture.png)

---

## 📌 What is LangChain?

**LangChain** is a framework for developing applications that leverage LLMs with structured workflows, external data, memory, and dynamic reasoning. It’s ideal for building **chatbots**, **document Q&A systems**, **autonomous agents**, and **AI copilots**.

Key features:

- **Structured workflows**: Combine prompts, API calls, and logic.
- **External data integration**: Connect to databases, documents, or APIs.
- **Conversation memory**: Maintain context across interactions.
- **Dynamic agents**: Enable LLMs to choose tools like search engines or calculators.

---

## 🔑 Key Concepts in LangChain

### 1️⃣ Prompts & Templates

- Core building block: defines **what you ask the LLM**.
- `PromptTemplate` lets you create **reusable and parameterized prompts**.
- Example:  
  `"Translate the following text to French: {input_text}"`

---

### 2️⃣ Chains

- Chains are **sequences of steps**: prompt → LLM → parser → output.
- They let you **combine multiple components** into a workflow.
- Example:  
  User question → Retrieval → Summarization → Answer.

---

### 3️⃣ Memory

- By default, LLMs are stateless (they forget everything between calls).
- **LangChain Memory** allows you to **store past interactions**.
- Types:
  - **ConversationBufferMemory** → Keeps entire chat history.
  - **ConversationSummaryMemory** → Summarizes past interactions.
  - **VectorStoreRetrieverMemory** → Embedding-based memory for semantic recall.

---

### 4️⃣ Retrieval-Augmented Generation (RAG)

- Lets you **ground LLM answers in external knowledge**.
- Flow:  
  Convert documents into **embeddings** → store in a **vector database**.  
  When user asks a question → retrieve relevant chunks → pass to LLM.
- Solves problems like **hallucination** and **knowledge cutoff**.

---

### 5️⃣ Agents & Tools

- **Agents** use LLMs to decide **what actions to take next**.
- They can call:
  - APIs (weather, news, finance, etc.)
  - Python functions
  - Databases / Search engines
- Example: A math agent uses the LLM to decide _when to call a calculator tool_.

---

### 6️⃣ LangChain Expression Language (LCEL)

- A new way to **compose chains declaratively**.
- Makes workflows **cleaner, faster, and easier to debug**.
- Example:

```python
chain = prompt | llm | parser
result = chain.invoke({"input": "Hello"})
```
````

---

### 7️⃣ Embeddings & Vector Stores

- **Embeddings**: Numerical representations of text that capture meaning.
- Used for **semantic search, clustering, and similarity comparison**.
- Stored in vector databases like **FAISS, Pinecone, Weaviate, Chroma**.

---

## 📁 Project Structure

```
LangChain-Demo/
│
├── demos/
│   ├── basic_chat.py         # Simple chatbot with memory
│   ├── rag_document_qa.py    # Document Q&A with RAG
│   ├── agent_with_tools.py   # Agent with tool usage
│   └── streamlit_app.py      # Streamlit web interface
│
├── data/
│   └── sample_documents/     # Sample documents for RAG
│
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/LangChain-Demo.git
   cd LangChain-Demo
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_optional
GOOGLE_API_KEY=your_google_api_key_optional
```

> **Note**: Most demos use **OpenAI** as the default LLM provider.

---

## 🚀 Quick Start

Run a demo:

- **Basic Chat**: `python demos/basic_chat.py`
- **Document Q\&A**: `python demos/rag_document_qa.py`
- **Web Interface**: `streamlit run demos/streamlit_app.py`

---

## 💡 Demo Examples

### 1. Basic Chat with Memory

```python
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI()
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

response = conversation.predict(input="Hi, I'm learning LangChain!")
print(response)
```

---

### 2. Document Q\&A with RAG

```python
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load documents
loader = TextLoader("data/sample_documents/article.txt")
documents = loader.load()

# Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

# Create Q&A chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

answer = qa_chain.run("What is the main topic of the document?")
print(answer)
```

---

## 📚 Learning Path

1. **Beginner**: Explore prompts and chains (`basic_chat.py`).
2. **Intermediate**: Add memory for conversations (`basic_chat.py`).
3. **Advanced**: Build RAG systems (`rag_document_qa.py`).
4. **Expert**: Create agents with tools (`agent_with_tools.py`).
5. **Production**: Deploy apps with Streamlit (`streamlit_app.py`).

---

## 🛠️ Dependencies

Key packages in `requirements.txt`:

- `langchain` → Core framework
- `openai` → OpenAI API integration
- `chromadb` → Vector database
- `streamlit` → Web app framework
- `python-dotenv` → Environment variables
- `tiktoken` → Token counting

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Add new demos or improve existing ones.
2. Enhance documentation or fix bugs.
3. Suggest ideas via issues.

See our [Contributing Guidelines](CONTRIBUTING.md) for details.

---

## 📖 Resources

- [LangChain Documentation](https://python.langchain.com)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain-cookbook)
- [Awesome LangChain](https://github.com/kyrolabs/awesome-langchain)

---

## 🐛 Troubleshooting

- **API Key Errors**: Verify keys in `.env`.
- **Module Not Found**: Run `pip install -r requirements.txt`.
- **Version Conflicts**: Use a virtual environment.
- **Rate Limiting**: Add retry logic in code.

---

**Happy Building!** 🚀

```

---
```
