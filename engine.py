from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        # Check if all the antecedents of the rule are in the facts, and that the consequent is not already in the facts
        if all(ant in self.facts for ant in rule.antecedents) and rule.consequent not in self.facts:
            return True
        return False

    def run(self) -> None:
        if self.facts == []: # If there are no facts, raise an error
            raise ValueError("There are no facts to infer from")
        # Order the rules by priority (highest first)
        ordered_rules = sorted(self.rules, key = lambda r: r.priority)
        while True:
            fired_any = False
            # Iterate through the ordered rules and fire the first one that can be fired
            for rule in ordered_rules:
                if self.can_fire(rule):
                    self.facts.add(rule.consequent)
                    self.trace.append({
                        "rule": rule.name,
                        "antecedents": rule.antecedents,
                        "consequent": rule.consequent
                    })
                    print(f"Fired rule: {rule.name}, added fact: {rule.consequent}")
                    fired_any = True
                    break
            # If no rules were fired, break the loop
            if not fired_any:
                break

    def conclusions(self) -> Dict[str, List[str]]:
        recommendation_info = {
             "recommendations": [],
             "specs": [],
             "other facts": []
        }
        # If no rules were fired, raise an error
        if self.trace == []:
            raise ValueError("There are no suitable laptop recommendations based on the provided facts")
        # Otherwise, process the facts and return the valid information
        else:
            for fact in self.facts:
                if fact.startswith("recommend:"):
                    info = "- " + " ".join(fact.split("recommend:")[1].split("_"))
                    recommendation_info["recommendations"].append(info)
                    rule = next((r for r in self.rules if r.consequent == fact), None)
                    recommendation_info["recommendations"].append(f"    - (Derived from rule: {rule.name})")
                elif fact.startswith("spec:"):
                    info = "- " + " ".join(fact.split("spec:")[1].split("_"))
                    recommendation_info["specs"].append(info)
                    rule = next((r for r in self.rules if r.consequent == fact), None)
                    recommendation_info["specs"].append(f"    - (Derived from rule: {rule.name})")
                # If the fact contains similar formatting but does not start with recommend or spec, add it to the other facts section
                elif fact.__contains__(":") and not fact.startswith("recommend:") and not fact.startswith("spec:"):
                    info = "- " +" ".join(fact.split(":")[1].split("_"))
                    recommendation_info["other facts"].append(info)
                    rule = next((r for r in self.rules if r.consequent == fact), None)
                    recommendation_info["other facts"].append(f"    - (Derived from rule: {rule.name})")
            # If there are no facts in the recommendations section, add a default message to indicate that there are no specific recommended laptops
            if recommendation_info["recommendations"] == []:
                recommendation_info["recommendations"].append("- No specific laptop recommendations based on the provided facts")
            # If there are multiple recommendations, add a message to the other facts section to indicate that there is not a single laptop that meets all of the user's needs, but there are multiple laptops that meet some of the needs
            elif len(recommendation_info["recommendations"]) > 1:
                recommendation_info["other facts"].append("- There are no laptop recommendations that fit all of the provided facts, but these recommendations fit some of the facts provided\n")
            return recommendation_info