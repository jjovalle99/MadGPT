# MadGPT 😡🤖

Welcome to MadGPT, the (rude yet) helpful assistant! I'm designed to offer assistance with a bit of attitude. If you're ready for a unique interaction, I'm here to help. Check me out [live in action](https://huggingface.co/spaces/jjovalle99/mad-gpt)!

## About MadGPT

MadGPT is a conversational AI that combines helpfulness with a hint of sass. Built using OpenAI's powerful GPT 3.5 Turbo model, I'm capable of assisting with a wide range of queries while keeping the interaction lively and engaging.

### Features
- Interactive and engaging conversation style.
- Built using the latest in AI technology.
- Easily deployable through Docker.

## Getting Started

### Prerequisites
To get started with MadGPT, ensure you have the following installed:
- Docker
- OpenAI Api Key

### Installation and Deployment

```bash
# Build the Docker image
docker build -t madgpt .

# Run the container
docker run --rm -it -p 7860:7860 -e OPENAI_API_KEY=<your-api-key> madgpt
```

Visit http://localhost:7860/ to interact with MadGPT after successful deployment.

### Acknowledgments
A special thanks to the following for their support and resources:

- [AI Maker Space](https://www.linkedin.com/company/ai-maker-space/)
- [AI Maker Space GitHub](https://github.com/AI-Maker-Space)
