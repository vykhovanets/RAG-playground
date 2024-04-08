from enum import Enum

from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama


class LLMType(str, Enum):
    GPT3 = "gpt-3.5-turbo"
    MISTRAL = "mistral"

    @property
    def is_openai(self):
        return self.value in [LLMType.GPT3]

    @property
    def is_ollama(self):
        return self.value in [LLMType.MISTRAL]

    def from_type(self, temperature=0):
        if self.is_openai:
            return ChatOpenAI(model=self.value, temperature=temperature)
        if self.is_ollama:
            return Ollama(model=self.value, temperature=temperature)
        return ChatOpenAI(model=self.value, temperature=temperature)
