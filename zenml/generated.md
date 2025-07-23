<div align="center">

  <a href="https://zenml.io">
    <img src="docs/book/.gitbook/assets/header.png" alt="ZenML Header">
  </a>

  <h3>Your unified toolkit for shipping everything from decision trees to complex AI agents—built on the MLOps principles you already trust.</h3>

  [![PyPi](https://img.shields.io/pypi/pyversions/zenml?color=281158)](https://pypi.org/project/zenml/)
  [![Version](https://img.shields.io/pypi/v/zenml?color=361776)](https://pypi.org/project/zenml/)
  [![Downloads](https://img.shields.io/pypi/dm/zenml?color=431D93)](https://pypi.org/project/zenml/)
  [![Contributors](https://img.shields.io/github/contributors/zenml-io/zenml?color=7A3EF4)](https://github.com/zenml-io/zenml/graphs/contributors)
  [![License](https://img.shields.io/github/license/zenml-io/zenml?color=9565F6)](https://github.com/zenml-io/zenml/blob/main/LICENSE)

  <p>
    <a href="https://zenml.io/features">Features</a> •
    <a href="https://zenml.io/roadmap">Roadmap</a> •
    <a href="https://github.com/zenml-io/zenml/issues">Report Bug</a> •
    <a href="https://zenml.io/pro">ZenML Pro</a> •
    <a href="https://www.zenml.io/blog">Blog</a> •
    <a href="https://zenml.io/podcast">Podcast</a>
  </p>

  🎉 See the latest updates in our <a href="https://github.com/zenml-io/zenml/releases">release notes</a>!

</div>

---

## 🧠 Overview

ZenML is an extensible MLOps framework built to streamline the development, evaluation, and deployment of classical ML models and modern AI agents in one unified platform.

- ✅ Apply CI/CD, reproducibility, versioning, and testing across your entire AI stack.
- 🔄 Avoid maintaining separate infrastructures for ML and LLM workflows.
- 📈 Integrate popular tools like LangGraph, LiteLLM, Langfuse, MLflow, and Weights & Biases.

---

## 🚨 The Problem: MLOps Works for Models, But What About AI?

You're a seasoned ML engineer. You’ve perfected deploying `scikit-learn` models and orchestrating PyTorch jobs. But now, you're building AI agents, and your stack is cracking.

- **The Adaptation Struggle:** How do you regression test a non-deterministic LLM? Version prompts?
- **The Divided Stack:** One set of tools for classical models, another for LLM agents.
- **The Broken Feedback Loop:** Long iteration cycles and shifting requirements make development frustrating.

---

## 💡 The Solution: One Framework for Your Entire AI Stack

ZenML lets you use the same principles and tools across both ML models and AI agents.

```python
# Morning: Train and deploy sklearn pipeline
train_and_deploy_classifier()

# Afternoon: Evaluate and deploy a new AI agent
evaluate_and_deploy_agent()

    ✅ Unified versioning for models and prompts

    🧪 Reproducible experiments

    🛠️ Full observability across tools

💻 Example: Compare Multi-Agent Architectures

Test multiple customer service agents on real-world data with ZenML’s reproducible pipelines and integrations like LangGraph, LiteLLM, and Langfuse.

👉 See full example →

@pipeline
def compare_agent_architectures():
    queries = load_real_conversations()
    prompts = load_prompts()
    classifier = train_intent_classifier(queries)
    results, viz = run_architecture_comparison(queries, classifier, prompts)
    report = evaluate_and_decide(queries, results)

🚀 Quickstart
🏗️ Architecture

ZenML uses a client-server architecture with an integrated web dashboard:

    Local: pip install "zenml[server]"

    Production: Install ZenML server separately, then connect with CLI.

pip install "zenml[server]"
pip install scikit-learn openai numpy
zenml init
zenml login
export OPENAI_API_KEY=sk-xxxx

📦 Your First Pipeline

@pipeline
def simple_ml_pipeline():
    X_train, X_test, y_train, y_test = create_dataset()
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    try:
        generate_summary(accuracy)
    except ImportError:
        print("OpenAI not installed.")

export OPENAI_API_KEY="your-api-key"
python simple_pipeline.py

💬 Talk to Your Pipelines with ZenML MCP Server

Use natural language to query, debug, and trigger your ZenML pipelines via the ZenML MCP Server:

    “Which pipeline runs failed this week?”

    “Trigger the fraud detection pipeline.”

    Install the .dxt plugin in Claude Desktop or Cursor to get started.

📚 Learn More
🖼️ Docs & Guides

    📘 Starter Guide

    🤖 LLMOps Guide

    🛠 SDK Reference

📺 Watch 11-minute intro on YouTube
🧪 Example Projects

    🧠 Agent Architecture Comparison

    📊 E2E Batch Inference

    🔎 LLM RAG Pipeline

    🧬 Fine-Tuning Pipeline

🏢 Deployment

    Self-hosted

    ZenML Pro (Free Trial)

Requirements:

    Docker or Kubernetes

    Object storage (S3, GCS, Azure)

    MySQL 8.0+ or MariaDB

🤝 Contributing

    🌟 Star ZenML on GitHub

    🛠 Contribution Guide

    🧩 Write Integrations

Join our community:

    🗺 Public Roadmap

    📰 Blog

    🎙 Slack Community

❓ FAQs

Q: Do I need to rewrite my models or agents?

A: No. Just wrap your code in a @step.

Q: How is this different from LangSmith/Langfuse?

A: LangSmith/Langfuse = observability. ZenML = full orchestration for the whole lifecycle.

Q: Can I still use MLflow or W&B?

A: Yes. ZenML integrates with MLflow and W&B.

Q: What about Kubernetes?

A: ZenML supports Kubeflow and K8s Orchestrator.

Q: How much does it cost?

A: Open-source forever. Use existing infrastructure.
🧩 VS Code Extension

Manage pipelines directly in your IDE.
<details> <summary>See it in action</summary> <img src="docs/book/.gitbook/assets/zenml-extension-shortened.gif" alt="ZenML Extension Demo" width="60%" /> </details>

👉 Install from Marketplace
📜 License

ZenML is licensed under the Apache License 2.0. See the LICENSE file for details.