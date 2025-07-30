# Video Search and Summarization Developer Workshop

<img src="_static/robots/video.png" alt="VSS Robot Character" style="float:right; max-width:350px;margin:15px;" />

The [NVIDIA AI Blueprint for video search and summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization) helps you build video analytics AI agents that let industrial operators communicate with their infrastructure through search and summarization of live or archived video sensor data. It integrates vision language models (VLMs), large language models (LLMs), and NVIDIA NIM™ to deliver a whole new level of collaboration.

This workshop will help you get started integrating this Blueprint in your enterprise. At the end of this workshop, you will go home with:

 - access to NVIDIA cloud resources and documentation
 - a running copy of the VSS Blueprint
 - turn-key, portable, development environment
 - a custom integrated application

 The entire lab can take anywhere from 1 to 2 hours to complete.

## Learning Objectives

By the end of this workshop, you will be able to:

- **Deploy and Configure VSS**: Set up the NVIDIA VSS Blueprint using Docker Compose with different GPU configurations
- **Understand VSS Architecture**: Learn how the ingestion and retrieval pipelines work together to process video data
- **Interact with VSS APIs**: Use the REST API to upload videos, generate summaries, and chat with video content
- **Customize VSS Parameters**: Tune video chunking, model parameters, and prompts for optimal performance
- **Build Custom Applications**: Create a production-ready Python application that integrates VSS for specific use cases

## Prerequisites

### Hardware Requirements

- **GPU Configuration**: Choose one of the following setups:
  - **Single GPU**: Minimum 40GB VRAM
  - **Dual GPUs**: Minimum 40GB VRAM
  - **Quad GPUs**: Minimum 80GB VRAM
- **Storage**: At least 100GB available disk space for models and data

### NVIDIA Account and Access

- **NVIDIA NGC Account**: Active account on [build.nvidia.com](https://build.nvidia.com)
- **API Key**: Valid NVIDIA API key (starts with `nvapi-...`)
  - Generate at: [NVIDIA API Keys](https://build.nvidia.com/settings/api-keys)
- **NGC Registry Access**: Ability to pull containers from `nvcr.io`

### Knowledge Prerequisites

- **Basic Docker Knowledge**: Understanding of containers, images, and Docker Compose
- **Python Programming**: Familiarity with Python syntax and basic programming concepts
- **Command Line**: Comfort with terminal/command line operations
- **API Concepts**: Basic understanding of REST APIs and JSON data formats

> Head over to [Setting up Secrets](secrets) to get started!