import tweepy
# Declarar tokens de autenticação
client = tweepy.Client(bearer_token='SEU BEARER_TOKEN')
client = tweepy.Client(consumer_key='CLIENT_ID',
                       consumer_secret='CLIENT_ID SECRET',
                       access_token='ACESS_TOKEN',
                       access_token_secret='ACESS_TOKEN SECRET')
clinte = tweepy

error = "<built-in function input>"

def CriarTweet():
    print("Digite o que você deseja tweetar: ")
    texto = input()
    tweet = client.create_tweet(text=texto)
    print("Tweet feito: ", texto)



def DarReTweet():
    print("Digite o ID que você deseja retweetar: ")
    texto = input()
    tweet = client.retweet(texto) #Colocar ID do tweet que quero dar RT
    print("ReTweet efetuado!")

def MandarMensagem():
    recipient_id = "v1ctorsales"  # ID of the user
    mensagem = "teste"
    client.send_direct_message(recipient_id, mensagem)
    print("Mensagem enviada: ", mensagem)

print("Digite qual opção você quer:\n 1- Criar Tweet || 2- Dar Retweet || 3- Mandar Mensagem")
resposta = input()


if resposta == "1": CriarTweet()
elif resposta == "2": DarReTweet()
elif resposta == "3": MandarMensagem()

#print(tweet)