FROM langflowai/langflow:latest

RUN uv pip install langchain-gigachat

COPY ../gigachat gigachat/

ENV LANGFLOW_HOST=0.0.0.0
ENV LANGFLOW_PORT=7860
ENV LANGFLOW_COMPONENTS_PATH=gigachat/

CMD ["langflow", "run"]