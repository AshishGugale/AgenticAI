from langchain_core.messages import AIMessage, HumanMessage
from models.llm import llm
from typing import Dict
from datetime import datetime
from core.state import SupervisorState

def writer_agent(state: SupervisorState) -> Dict:
    """Writer uses Groq to create final report"""

    research_data = state.get("research_data", "")[:1000]
    analysis = state.get("analysis", "")[:1000]
    task = state.get("current_task", "")

    writing_prompt = f"""You are a professional technical writer.

Based on the following task and supporting information, write an executive report.

Task: {task}

Key Research Findings:
{research_data}

Key Analysis Insights:
{analysis}

Structure:
1. Executive Summary
2. Key Findings
3. Analysis & Insights
4. Recommendations
5. Conclusion

Keep it under 1000 words. Be clear and professional."""
    
    # Get report from LLM
    report_response = llm.invoke([HumanMessage(content=writing_prompt)])
    report = report_response.content
    
    # Create final formatted report
    final_report = f"""
📄 FINAL REPORT
{'='*50}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Topic: {task}
{'='*50}

{report}

{'='*50}
Report compiled by Multi-Agent AI System powered by Groq
"""
    
    return {
        "messages": [AIMessage(content=f"✍️ Writer: Report complete! See below for the full document.")],
        "final_report": final_report,
        "next_agent": "supervisor",
        "task_complete": True
    }