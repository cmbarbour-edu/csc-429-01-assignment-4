from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"
TEST_PATH = "tests/README.txt"

def collect_initial_facts():
    facts = []
    # List of questions to ask the user (important for invalid input handling)
    questions = {"Is portability important? (y/n) : " : ['y', 'n'],
                 "Do you need long battery life? (y/n): " : ['y', 'n'],
                 "Is your budget high, medium, or low? (h/m/l): " : ['h', 'm', 'l'],
                 "Is gaming a priority? (y/n): " : ['y', 'n'],
                 "Are you going to use the laptop for creative work? (y/n): " : ['y', 'n'],
                 "Is the laptop primarily going to be used for office work? (y/n): " : ['y', 'n'],
                 "Is your preferred OS Windows, MacOS, or Linux? (w/m/l): " : ['w', 'm', 'l'],
                 "Do you need AI training capabilities? (y/n): " : ['y', 'n'],
                 "Do you need a large screen? (y/n): " : ['y', 'n'],
                 "Do you travel often with your laptop? (y/n): " : ['y', 'n']}
    # Ask the user each question and collect their answer, ensuring that the answer is valid
    # Instead of using a tree to determine the next question to ask based on the user's previous answers, 
    #   iterate through all of them. This way, the user can have a recommendation that fits their needs,
    #   as well as specification information that is also relevant.
    for question in questions:
        while True:
            try:
                answer = input(question).lower()
                if answer not in questions[question]: # If the answer is not in the list of valid answers, raise an error
                    raise ValueError("Please enter a valid answer.") 
                else: # Otherwise, process the answer and add the corresponding fact to the list of facts if it is 'y'
                    if questions[question] == ['y', 'n'] and answer == 'y': # If the question is a yes or no question and the answer is 'y', add the corresponding fact based on the answer
                        if "portability" in question:
                            facts.append("portable")
                        elif "battery" in question:
                            facts.append("long_battery")
                        elif "gaming" in question:
                            facts.append("gaming")
                        elif "creative" in question:
                            facts.append("creative_work")
                        elif "office" in question:
                            facts.append("office_only")
                        elif "AI training" in question:
                            facts.append("needs_ai_accel")
                        elif "large screen" in question:
                            facts.append("large_screen")
                        elif "travel" in question:
                            facts.append("travel_often")
                    elif questions[question] == ['h', 'm', 'l']: # If the question is about budget, add the corresponding fact based on the answer
                        if answer == 'h':
                            facts.append("budget_high")
                        elif answer == 'm':
                            facts.append("budget_medium")
                        elif answer == 'l':
                            facts.append("budget_low")
                    elif questions[question] == ['w', 'm', 'l']: # If the question is about OS, add the corresponding fact based on the answer
                        if answer == 'w':
                            facts.append("pref_os_windows")
                        elif answer == 'm':
                            facts.append("pref_os_macos")
                        elif answer == 'l':
                            facts.append("pref_os_linux")
                    break
            except ValueError: # Catch the error and prompt the user to enter a valid answer; repeat the question until a valid answer is given
                print("Invalid input. Please enter 'y' or 'n'.")
    return facts

def main():
    # Load the rules, create the engine, collect the initial facts, assert them into the engine, and run the engine
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    facts = collect_initial_facts()
    engine.assert_facts(facts)
    print("\nInitial Facts:")
    for fact in facts:
        print(f"- {fact}")
    print("\nRunning the forward chaining engine...")
    engine.run()
    try: # Get the conclusions and print the recommendation information; if there are no recommendations, catch the error and print the respective error message
        conclusions = engine.conclusions()
        print("\nRecommendations:")
        for rec in conclusions.get("recommendations", []):
            print(f"{rec}")
        print("\nSpecifications:")
        for spec in conclusions.get("specs", []):
            print(f"{spec}")
        print("\nOther Facts:")
        for fact in conclusions.get("other facts", []):
            print(f"{fact}")
    except ValueError as e:
        print(f"Error: {e}")
        return
    

if __name__ == "__main__":
    main()
