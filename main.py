import requests

API_KEY ="33dfa87af0ea5adb7ce00cba0e61a02b"
cidade = input('Digite a cidade desejada para saber como está a temperatura: ')
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
#&lang=pt_br = pra passar pra portugues

requisicao = requests.get(link)
#print(requisicao)#=200 -> funcionou, =404->nao funcionou, =500->servidor nao disponivel
requisicao_dic = requisicao.json()
descricao = requisicao_dic["weather"][0]['description']
temperatura = requisicao_dic["main"]['temp'] - 273.15
print(descricao, f"{temperatura}ºC")
