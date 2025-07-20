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
        self.tools = [
            PlaceSearchTool(),
            WeatherInfoTool(),
            ExpenseCalculatorTool(),
            CurrencyConversionTool(),
        ]
       
        self.system_prompt = SYSTEM_PROMPT
        self.model_loader = ModelLoader()
        llm  = self.model_loader.load_llm()
        self.llm_with_tools = llm.bind(tools=self.tools)
        self.graph = None



    def agent_function(self,state: MessagesState):
        """ Main Agent Function """
        user_question = state['messages']
        input_quest = [self.system_prompt] + user_question
        res  = self.llm_with_tools.invoke(input_quest)
        return {"messages": [res]}


    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node('agent',self.agent_function)
        graph_builder.add_node("tools",ToolNode(self.tools))


        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)

        self.graph = graph_builder.compile()
        return self.graph


    def __call__(self):
        return self.build_graph()

