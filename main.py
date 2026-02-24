import sys
import os

# Add the current directory to sys.path to allow imports from marketing_planner_agent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent import MarketingAgent

def main():
    print("\n--- Marketing Planning Assistant Agent ---")
    if len(sys.argv) > 1:
        goal = " ".join(sys.argv[1:])
    else:
        goal = input("Enter your high-level marketing goal: ")
    
    if not goal.strip():
        print("No goal provided. Exiting.")
        return

    print(f"\n[info] Planning for: '{goal}'...")
    
    try:
        agent = MarketingAgent()
        result = agent.run(goal)
        
        print("\n" + "="*50)
        print("FINAL EXECUTION PLAN")
        print("="*50)
        print(result["output"])
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n[error] An error occurred: {e}")
        print("\nNote: Ensure you have set your GOOGLE_API_KEY in the .env file.")

if __name__ == "__main__":
    main()
