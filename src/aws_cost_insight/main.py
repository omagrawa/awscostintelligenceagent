import sys
import os
from dotenv import load_dotenv

# Add the 'src' directory to the Python path dynamically
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'src')))

# Import the ask_question function from rag_engine after modifying sys.path
from aws_cost_insight.rag_engine import ask_question

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    query = "Why did EC2 cost increase last month?"
    answer = ask_question(query)
    print(answer)
