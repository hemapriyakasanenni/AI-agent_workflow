# agentic_workflow.py

class PlannerAgent:
    def plan(self, goal):
        print("🧠 Planner thinking...")
        return [
            "Collect data",
            "Analyze data",
            "Generate insights"
        ]


class ExecutorAgent:
    def execute(self, steps):
        print("⚙️ Executor working...")
        results = []
        for step in steps:
            results.append(f"✔ Completed: {step}")
        return results


class EvaluatorAgent:
    def evaluate(self, results):
        print("🔍 Evaluator reviewing...")
        if results:
            return "🎉 Workflow completed successfully"
        return "❌ Workflow failed"


class AgenticWorkflow:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.evaluator = EvaluatorAgent()

    def run(self, goal):
        print(f"\n🎯 Goal: {goal}")
        plan = self.planner.plan(goal)
        results = self.executor.execute(plan)
        evaluation = self.evaluator.evaluate(results)

        return evaluation


if __name__ == "__main__":
    workflow = AgenticWorkflow()
    output = workflow.run("Improve customer retention")
    print(output)
