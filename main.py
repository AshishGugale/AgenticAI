from rich.console import Console
from rich.markdown import Markdown
from core.workflow import graph
from langchain_core.messages import HumanMessage

# Sample task input
task = "How is generative AI transforming finance?"

inputs = {
    "messages": [HumanMessage(content=task)],
    "current_task": task
}

final_state = graph.invoke(inputs)

report = final_state.get("final_report", "")
console = Console()
console.print(Markdown(report))