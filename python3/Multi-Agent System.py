from dataclasses import dataclass


@dataclass
class AgentResult:
    agent: str
    result: str


class ResearchAgent:

    def run(self, task):
        return AgentResult(
            "Research Agent",
            f"Research completed for: {task}"
        )


class CodingAgent:

    def run(self, task):
        return AgentResult(
            "Coding Agent",
            f"Code plan created for: {task}"
        )


class ReviewerAgent:

    def run(self, task, results):
        summary = "\n".join(
            f"- {result.agent}: "
            f"{result.result}"
            for result in results
        )

        return AgentResult(
            "Reviewer Agent",
            (
                f"Review of task: {task}\n"
                f"{summary}\n"
                "Everything is ready."
            )
        )


class ManagerAgent:

    def __init__(self):

        self.research_agent = (
            ResearchAgent()
        )

        self.coding_agent = (
            CodingAgent()
        )

        self.reviewer_agent = (
            ReviewerAgent()
        )

    def run(self, task):

        results = []

        research = (
            self.research_agent
            .run(task)
        )

        results.append(research)

        coding = (
            self.coding_agent
            .run(task)
        )

        results.append(coding)

        review = (
            self.reviewer_agent
            .run(
                task,
                results
            )
        )

        results.append(review)

        return results


manager = ManagerAgent()


print("===== MULTI-AGENT SYSTEM =====")

task = input(
    "Give the agents a task: "
)


results = manager.run(task)


print("\n===== RESULTS =====")

for result in results:

    print(
        f"\n[{result.agent}]"
    )

    print(result.result)