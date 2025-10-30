"""A simple agent flow example for Langflow.

This script demonstrates how to set up a conversational agent using Langflow's
Agent component with web search capabilities.

Features:
- Uses the new flattened component access (cp.AgentComponent instead of deep imports)
- Configures logging to 'langflow.log' at INFO level
- Creates an agent with OpenAI GPT model
- Connects ChatInput → Agent → ChatOutput

Usage:
    uv run lfx run simple_agent_openai.py "How are you?"
"""
"""
Простой пример агента для Langflow.

Этот скрипт демонстрирует, как настроить диалогового агента с использованием компонента Agent из Langflow.

Особенности:
- Использует новый упрощенный доступ к компонентам (cp.AgentComponent вместо глубоких импортов)
- Настраивает логирование в файл 'langflow.log' на уровне INFO
- Создает агента с моделью OpenAI GPT
- Соединяет компоненты ChatInput → Agent → ChatOutput

Использование:
    uv run lfx run simple_agent_openai.py "Как дела?"
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from lfx import components as cp
from lfx.graph import Graph
from lfx.log.logger import LogConfig

load_dotenv()
log_config = LogConfig(
    log_level="INFO",
    log_file=Path("../langflow.log"),
)

# Showcase the new flattened component access - no need for deep imports!
chat_input = cp.ChatInput()
agent = cp.AgentComponent()
url_component = cp.URLComponent()
#tools = url_component.to_toolkit()
agent.set(
    model="gpt-4.1-mini",
    agent_llm="OpenAI",
    api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    input_value=chat_input.message_response,
)
chat_output = cp.ChatOutput().set(input_value=agent.message_response)

graph = Graph(chat_input, chat_output, log_config=log_config)