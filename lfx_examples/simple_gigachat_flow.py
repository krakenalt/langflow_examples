"""A simple agent flow example for Langflow.

This script demonstrates how to set up a conversational agent using Langflow's
Agent component with web search capabilities.

Features:
- Uses the new flattened component access (cp.AgentComponent instead of deep imports)
- Configures logging to 'langflow.log' at INFO level
- Creates an agent with OpenAI GPT model
- Connects ChatInput → Agent → ChatOutput

Usage:
    uv run lfx run simple_gigachat_flow.py "How are you?"
"""
"""
Простой пример агента для Langflow.

Этот скрипт демонстрирует, как настроить диалогового агента с использованием компонента Agent из Langflow.

Особенности:
- Использует новый упрощенный доступ к компонентам (cp.AgentComponent вместо глубоких импортов)
- Настраивает логирование в файл 'langflow.log' на уровне INFO
- Создает агента с моделью GigaChat
- Соединяет компоненты ChatInput → Agent → ChatOutput

Использование:
    uv run lfx run simple_gigachat_flow.py "Как дела?"
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from lfx import components as cp
from gigachat_components_lfx import GigaChatModelComponent
from lfx.graph import Graph
from lfx.log.logger import LogConfig

load_dotenv()
log_config = LogConfig(
    log_level="INFO",
    log_file=Path("../langflow.log"),
)

chat_input = cp.ChatInput()
llm = GigaChatModelComponent()
llm.set(
    model="GigaChat-2-Max",
    credentials=os.getenv("GIGACHAT_CREDENTIALS"),
    scope="GIGACHAT_API_CORP",
    input_value=chat_input.message_response,
)
chat_output = cp.ChatOutput().set(input_value=llm.message_response)

graph = Graph(chat_input, chat_output, log_config=log_config)