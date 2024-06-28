claudioNotas = [10, 7, 5, 6 ]
joaoNotas = [3, 5, 6 ,5]
thiagoNotas = [10, 7, 7, 9]
samuelNotas = [10, 9, 9, 8]

claudioMedia = sum(claudioNotas ) / 4
joaoMedia =   sum (joaoNotas) / 4
thiagoMedia = sum(thiagoNotas ) / 4
samuelMedia = sum (samuelNotas) / 4

if claudioMedia >= 5:
    claudioAprovaçao = 'Aprovado'
else:
    claudioAprovaçao = 'Reprovado'

if joaoMedia >= 5:
    joaoAprovaçao = 'Aprovado'
else:
    joaoAprovaçao = 'Reprovado'

if thiagoMedia >= 5:
    thiagoAprovaçao = 'Aprovado'
else:
  thiagoAprovaçao = 'Reprovado'

if samuelMedia>= 5:
    samuelAprovaçao = 'Aprovado'
else:
    samuelAprovaçao = 'Reprovado'


print('===\tNota média doa alunos\t===')
print(f'Claudia: {claudioMedia}\t {claudioAprovaçao}\nJoão: {joaoMedia}\t {joaoAprovaçao}\nThiago: {thiagoMedia}\t {thiagoAprovaçao}\nSamuel: {samuelMedia}\t {samuelAprovaçao} ')


