
from openai import OpenAI
from IPython.display import Markdown, display

def printmd(string):
    display(Markdown(string))

class ChatBot:
    def __init__(self, system="Du bist bitte eine hilfreiche KI!", model="gpt-4o"):
        self.client = OpenAI()
        self.system = system
        self.model = model
        self.conversation = []

    def ask(self, q, seed=1337, temperature=0.5):
        response = self.client.chat.completions.create(
        model=self.model,
        temperature=temperature,
        seed=seed,
        messages=[{"role": "system", "content": self.system}] \
                +[{"role": "user" if i%2 == 0 else "assistant", "content": e} \
                  for i, e in enumerate(self.conversation)]
                +[{"role": "user", "content": q}]
         )
        res = response.choices[0].message.content
        self.conversation += [q, res] 
        return res
