from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    pass

if __name__ == "__main__":
    main()
