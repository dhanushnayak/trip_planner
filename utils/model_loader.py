from pydantic import BaseModel, Field
from typing import Any, Optional
from typing_extensions import Literal,Any
from langchain_groq import ChatGroq
from utils.config_loader import load_config
import os


class ConfigLoader:
    def __init__(self):
        print(f"Loaded config")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]


class ModelLoader(BaseModel):
    model_provider: Literal['groq', 'openai'] = 'groq'
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self,__context: Any) -> None:
            self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True


    def __init__(self):
        pass

    def load_llm(self):
        print("""Loading LLM """)
        print(f"Model provider: {self.model_provider}")
        if self.model_provider == 'groq':
            print("Loading Groq LLM")
            groq_api_key =  os.getenv("GROQ_API_KEY")
            model_name = self.config['llm']['groq']['model_name']
            llm = ChatGroq(
                model_name=model_name,
                api_key=groq_api_key,
                verbose=True,
            )
            return llm



    def get_model(self):
        pass


