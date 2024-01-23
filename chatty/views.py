

from django.shortcuts import render
from django.http import JsonResponse

import openai 

openai.api_key = "paste your own api key here"
def ask_openai(message):
 response = openai.chat.completions.create(
 model="gpt-3.5-turbo-1106",
 response_format={ "type": "json_object" },
 messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": message}
  ]
)
#  print(response.choices[0].message.content)
 return response.choices[0].message.content

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response_content = ask_openai(message)
        return JsonResponse({'message': message, 'response': response_content})
    return render(request, 'chatbot.html')
