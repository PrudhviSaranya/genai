from openai import OpenAI
client = OpenAI(
  api_key="",
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion)

# ChatCompletion(
#     id='chatcmpl-9otnFQxhwi4s0F5Vf3QE20UMBqjce', 
#     choices=[
#         Choice(
#             finish_reason='stop',
#             index=0, 
#             logprobs=None, 
#             message=ChatCompletionMessage(content="In the realm of code, where logic intertwines,\nLies a wondrous concept, like intricate vines,\nRecursion, a technique, both elegant and bold,\nA programming marvel, a tale to be told.\n\nLike a mirror reflecting its own reflection,\nRecursion calls upon its own direction,\nA function that invokes itself anew,\nA mystical loop, a cycle so true.\n\nThrough recursive calls, problems we dissect,\nIn a journey of depth, we find answers perfect,\nBreaking dilemmas into smaller parts,\nSolving recursively, with creative arts.\n\nLike a Russian doll, nested deep within,\nRecursion unwraps complexities, akin\nTo a dance of patterns, endlessly spun,\nA recursive melody, harmonious and one.\n\nSo embrace the power of recursion's embrace,\nA magical journey through time and space,\nIn the world of programming, let it be unfurled,\nRecursion, a poetic loop that shapes our world."
#   , role='assistant', function_call=None, tool_calls=None))], created=1721917897, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=186, prompt_tokens=39, total_tokens=225))