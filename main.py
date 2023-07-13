import openai
import requests

# Set up API key
weather_api_key = "2190d1677c98d6b411ac6044981f126f"
openai.api_key = "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"

# City
city = "Alhambra"
# API Call
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
response = requests.get(url)
weather_data = response.json()
print(weather_data)

prompt = f"Talk about the user's fortune based on the {weather_data['weather'][0]['main']} weather with a {weather_data['weather'][0]['description']} today."

print(prompt)

# Define the parameters to use in the generation
model = "text-davinci-003"
temperature = 0.5
max_tokens = 100
top_p = 1
n = 1
presence_penalty = 0
best_of = 1
stream = False
stop = None

# Make the API call
completions = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=top_p,
    n=n,
    presence_penalty=presence_penalty,
    best_of=best_of,
    stream=stream,
    stop=stop
)

# Get the first response from the API
message = completions.choices[0].text
print(message)
