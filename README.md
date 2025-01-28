
# Overview

**BlogWok** is an AI-powered content aggregation and summarization tool that leverages **Agents & Crew AI** to parse and summarize internet content efficiently. It uses **Serper API** to fetch web content and **Gemini 1.5 Pro** for summarization. The summarized content is then formatted into an article, which can be downloaded as a Markdown file. The project is built with **Streamlit**, providing an interactive and user-friendly UI.

# Features

- Automated Web Parsing: Uses Serper API to retrieve relevant content from the internet.

- AI-Powered Summarization: Utilizes Google Gemini 1.5 Pro for summarizing parsed content into structured articles.

- Markdown Export: Allows users to download the summarized articles in Markdown format.

- Streamlit UI: Provides a clean and intuitive interface for users to interact with the tool.

# Crew AI Agents:

Web Parsing Agent: Fetches web content using Serper API.

Summarization Agent: Processes and formats content into a proper article using LLM.

# Tech Stack

- Python

- Streamlit (Frontend UI)

- Crew AI (Agent-based automation)

- Serper API (Web content retrieval)

- Google Gemini 1.5 Pro (LLM-powered summarization)

# Installation

### Clone the repository:

```bash
git clone https://github.com/bhartijoshi04/A-BlogWok
cd A-BlogWok 
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Set up API keys:

Serper API Key

Google Gemini API Key

### Create a .env file and add:

```bash
SERPER_API_KEY=your_serper_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### Run the Streamlit app:

```bash
streamlit run app.py
```
[Watch the demo video](https://github.com/bhartijoshi04/A-BlogWok/blob/main/file/DEMO.mp4)

# Usage

- Enter a search query in the Streamlit UI.

- The Web Parsing Agent fetches relevant content using Serper API.

- The Summarization Agent processes and formats the content into an article.

- View the generated article in the UI.

- Download the article in Markdown format.

