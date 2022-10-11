import random
from faker import Faker
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import datetime

fake=Faker()
nomes = []
numeros=[];
my_file = open('Nomes_notas.txt','w+')

for i in range(10):
  nom = str(fake.name())
  num = str(random.randint(1,10))
  numeros.append(num)
  nomes.append(nom)
for x, y in zip(nomes, numeros):
  print(x, y)   


for nom , num in zip(nomes, numeros):
  my_file.write(nom+ num+'\n')


my_file.close()

for num in open('Nomes_notas.txt'):
    print(numeros)

for line in open('Nomes_notas.txt'):
    print(line)

lista_notas = numeros

num_bins=15; plt.hist(lista_notas,num_bins,density=True,facecolor='green', alpha=0.75)

plt.xlabel('Valores')
plt.ylabel('Probabilidade')
plt.title('Histograma dos valores')
plt.grid(True)
plt.show()
