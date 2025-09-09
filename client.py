from openai import OpenAI

# client = OpenAI()

client = OpenAI(
 api_key=os.environ.grt("CUSTOM_ENV_NAME"),
)
