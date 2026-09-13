class Message:
    def __init__(self, content):
        self.content = content
        self.role = "assistant"

class Choice:
    def __init__(self, content):
        self.message = Message(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [Choice(content)]
        self.model = "gpt-4o-mini"
        self.usage = {"prompt_tokens": 45, "completion_tokens": 82, "total_tokens": 127}

# Simulated response as if the API returned it
sim_response = SimulatedResponse(
    "Sleep was the limiting factor today. James hit 7,800 steps but 6 hours is below optimal. "
    "Tomorrow: prioritize 8+ hours tonight. Keep the step target at 9,000, not 10,000, "
    "since recovery is still incomplete. Add a 20-minute walk after lunch to hit it without needing a long session."
)

# Extract the reply (same code you use with the live API)
reply = sim_response.choices[0].message.content
print("AI Coach Response:")
print(reply)
print(f"\nTokens used: {sim_response.usage['total_tokens']}")






import json

# Different system prompts produce different outputs for the same user message
system_prompts = {
    "SMP Coach": (
        "You are a strict SMP fitness coach. Be direct, no fluff. "
        "Give one actionable recommendation per response. Max 3 sentences."
    ),
    "Data Analyst": (
        "You are a fitness data analyst. Focus on numbers and trends. "
        "Output structured observations, not advice."
    ),
    "Nutritionist": (
        "You are a nutritionist specializing in intermittent fasting protocols. "
        "Focus only on eating patterns and timing."
    )
}

user_message = "James: steps=7800, sleep=6hr, protocol=OMAD, water=5 glasses, day 3 of deficit."

# Simulated responses for each system prompt
simulated_responses = {
    "SMP Coach": (
        "Six hours of sleep on day 3 of a deficit is why the steps are low. "
        "Tonight, sleep must be 8+ hours. Tomorrow target 9,000 steps only."
    ),
    "Data Analyst": (
        "Observation: Steps 22% below 10k goal. Sleep deficit likely compounding protocol fatigue. "
        "Water intake at 5/8 target. Recommend tracking energy levels as a leading indicator."
    ),
    "Nutritionist": (
        "Day 3 of OMAD with sleep deficit suggests cortisol is elevated. "
        "Consider shifting to 2MAD tomorrow to reduce stress load and support recovery."
    )
}

for role, prompt in system_prompts.items():
    print(f"[{role}]")
    print(f"  System: {prompt[:60]}...")
    print(f"  Response: {simulated_responses[role]}")
    print()





import json

# System prompt requesting JSON output
system = """You are a fitness data extractor.
Parse the user's daily log and return ONLY valid JSON with these keys:
steps (int), sleep_hours (float), protocol (str), cold_shower (bool), water_glasses (int).
No other text."""

# What the AI would return for this input
raw_log = "Today I did 9,200 steps, slept for 7.5 hours, followed OMAD, took a cold shower and drank 8 glasses of water."

# Simulated AI JSON response
simulated_json_response = '{"steps": 9200, "sleep_hours": 7.5, "protocol": "OMAD", "cold_shower": true, "water_glasses": 8}'

# Parse it
try:
    parsed = json.loads(simulated_json_response)
    print("Parsed structured data:")
    for key, value in parsed.items():
        print(f"  {key}: {value}")

    # Use it programmatically
    print()
    if parsed["steps"] >= 10000:
        print("Step goal: HIT")
    else:
        print(f"Step goal: {parsed['steps']:,}/10,000 ({10000 - parsed['steps']:,} short)")
    print(f"Sleep rating: {'Good' if parsed['sleep_hours'] >= 7.5 else 'Low'}")

except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")






import json

# System prompt requesting JSON output
system = """You are a fitness data extractor.
Parse the user's daily log and return ONLY valid JSON with these keys:
steps (int), sleep_hours (float), protocol (str), cold_shower (bool), water_glasses (int).
No other text."""

# Your own daily description
raw_log = "Woke up after 6 hours of sleep, managed only 9,900 steps, stuck to OMAD, skipped the cold shower, and only got through 5 glasses of water."

# Simulated AI JSON response (what the model would extract)
simulated_json_response = '{"steps": 9900, "sleep_hours": 6.0, "protocol": "OMAD", "cold_shower": false, "water_glasses": 5}'

# Parse it
try:
    parsed = json.loads(simulated_json_response)
    print("Parsed structured data:")
    for key, value in parsed.items():
        print(f"  {key}: {value}")

    print()
    if parsed["steps"] >= 10000:
        print("Step goal: HIT")
    else:
        print(f"Step goal: {parsed['steps']:,}/10,000 ({10000 - parsed['steps']:,} short)")
    
    print(f"Sleep rating: {'Good' if parsed['sleep_hours'] >= 7.5 else 'Low'}")
    print(f"Cold shower: {'Yes' if parsed['cold_shower'] else 'No'}")

except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")





import json

# VS Code version would add two lines:
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Then replace the simulated_responses below with a real client.chat.completions.create() call

workshop_system = """You are a Jua Kali workshop assistant for Kamau Metalworks, Gikomba.
When a client describes a job, return ONLY valid JSON with these keys:
  item (str), material (str), est_kes (int), days_to_complete (int), deposit_kes (int).
No other text."""

job_requests = [
    "I need a sliding gate, about 10 feet wide, mild steel.",
    "Window grills for three windows, 3x4 feet each, angle iron.",
    "A steel door frame for a standard door, hollow tube.",
]

# Simulated AI JSON responses
simulated_responses = [
    '{"item": "sliding gate", "material": "mild steel", "est_kes": 32000, "days_to_complete": 5, "deposit_kes": 16000}',
    '{"item": "window grills x3", "material": "angle iron", "est_kes": 21000, "days_to_complete": 3, "deposit_kes": 10500}',
    '{"item": "door frame", "material": "hollow tube", "est_kes": 9800, "days_to_complete": 2, "deposit_kes": 4900}',
]

print("Kamau Metalworks: AI Quotation Assistant\n")
for request, response_json in zip(job_requests, simulated_responses):
    print(f"Client: {request}")
    quote = json.loads(response_json)
    print(f"  Item:      {quote['item']}")
    print(f"  Material:  {quote['material']}")
    print(f"  Quote:     KES {quote['est_kes']:,}")
    print(f"  Deposit:   KES {quote['deposit_kes']:,}")
    print(f"  Ready in:  {quote['days_to_complete']} days")
    print()




import json

# VS Code version would add two lines:
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Then replace the simulated_responses below with a real client.chat.completions.create() call

workshop_system = """You are a Jua Kali workshop assistant for Kamau Metalworks, Gikomba.
When a client describes a job, return ONLY valid JSON with these keys:
  item (str), material (str), est_kes (int), days_to_complete (int), deposit_kes (int).
No other text."""

job_requests = [
    "I need a sliding gate, about 10 feet wide, mild steel.",
    "Window grills for three windows, 3x4 feet each, angle iron.",
    "A steel door frame for a standard door, hollow tube.",
]

# Simulated AI JSON responses
simulated_responses = [
    '{"item": "sliding gate", "material": "mild steel", "est_kes": 35000, "days_to_complete": 7, "deposit_kes": 26000}',
    '{"item": "window grills x3", "material": "angle iron", "est_kes": 90000, "days_to_complete":4, "deposit_kes": 45500}',
    '{"item": "door frame", "material": "hollow tube", "est_kes": 9800, "days_to_complete": 5, "deposit_kes": 8900}',
]

print("Kamau Metalworks: AI Quotation Assistant\n")
for request, response_json in zip(job_requests, simulated_responses):
    print(f"Client: {request}")
    quote = json.loads(response_json)
    print(f"  Item:      {quote['item']}")
    print(f"  Material:  {quote['material']}")
    print(f"  Quote:     KES {quote['est_kes']:,}")
    print(f"  Deposit:   KES {quote['deposit_kes']:,}")
    print(f"  Ready in:  {quote['days_to_complete']} days")
    print()