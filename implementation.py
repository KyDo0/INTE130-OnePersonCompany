class Task:
    def __init__(self, title, data):
        self.title = title
        self.data = data

class Recommendation:
    def __init__(self, agent_name, advice):
        self.agent_name = agent_name
        self.advice = advice

class Agent:
    def __init__(self, name):
        self.name = name

    def process_task(self, task):
        raise NotImplementedError("Subclasses must implement logic.")

class FinanceAgent(Agent):
    def process_task(self, task):
        return Recommendation(self.name, f"Fee Analysis: ${task.data} per session.")

class MarketingAgent(Agent):
    def process_task(self, task):
        return Recommendation(self.name, f"Marketing Strategy: Focus on {task.data}.")

class OperationsAgent(Agent):
    def process_task(self, task):
        return Recommendation(self.name, f"Ops Update: Slot confirmed for {task.data}.")

class Founder:
    def __init__(self, name):
        self.name = name

    def review_and_decide(self, recommendations):
        print(f"\n>>> Founder {self.name} reviewing recommendations...")
        for rec in recommendations:
            print(f"- [{rec.agent_name}]: {rec.advice}")
        print("\nDecision: Approved. Smart Study is operational!")

class AiAgent:
    def AI(self):
        print("\n--- SYSTEM LOGIC OVERVIEW ---")
        print("This operation uses three primary agents for tutoring services:")
        print("\nFinance Agent: Manages financial health and session pricing.")
        print("\nMarketing Agent: Builds strategies to increase service visibility.")
        print("\nOperations Agent: Manages scheduling and session organization.")
        print("\nConclusion: Agents merge outputs for AI review and final data storage.")

def main():
    founder = Founder("Omran")
    finance = FinanceAgent("Finance-Bot")
    marketing = MarketingAgent("Marketing-Bot")
    operations = OperationsAgent("Ops-Bot")
    task_list = [
        (finance, Task("Course Fee", 45)),
        (marketing, Task("Social Media", "Instagram")),
        (operations, Task("Math Session", "10:00 AM"))
    ]

    final_reports = []
    for agent, task in task_list:
        report = agent.process_task(task)
        final_reports.append(report)
        print(f"Task '{task.title}' processed by {agent.name}.")

    founder.review_and_decide(final_reports)
    logic_summary = AiAgent()
    logic_summary.AI()
if __name__ == "__main__":
    main()
