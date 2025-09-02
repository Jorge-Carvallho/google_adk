from google.adk.agents import Agent
from datetime import datetime



def get_time():
    """
    Retorna a hora atual do sistema.
    """
    return datetime.now().strftime("%H:%M:%S")


def get_weekday():
    """
    Retorna o dia da semana atual do sistema.
    """
    return datetime.now().strftime("%A")
    



root_agent  = Agent(

    name="my_tool_agent",
    model="gemini-2.0-flash",
    description="Você é um agente que retorna a hora atual e dia da semana  ",
    instruction="""
        Você é um agente que retorna a hora atual e dia da semana.
        Você deve usar a ferramenta get_time pra retorna a hora atual.
        você deve usar a ferramenta get_weelday para retorna o dia da semana
    """,
tools=[get_time, get_weekday],
)