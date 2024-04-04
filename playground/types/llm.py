from enum import Enum


class LLMType(str, Enum):
    GPT3 = "gpt-3.5-turbo"

    @property
    def is_openai(self):
        return self.value in [LLMType.GPT3]
