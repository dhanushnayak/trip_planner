from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from prompt_library.prompt import SYSTEM_PROMPT
from tools.currency_conversion_tool import CurrencyConversionTool
from tools.expense_calculator_tool import ExpenseCalculatorTool
from tools.place_search_tool import PlaceSearchTool
from tools.weather_info_tool import WeatherInfoTool
from utils.config_loader import ConfigLoader
from utils.model_loader import ModelLoader


class GraphBuilder:
    def __init__(self):
        pass

    def agent_func(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass
