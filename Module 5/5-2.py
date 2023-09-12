import json

class Model:
    title = 213
    content = 'Brunoyam'
    date_posted = '2023.09.12'
    author = 'Владимир Лобес'
    def save(self):
        dct = {k: str(v) for k, v in vars(Model).items()}
        with open('file.json', 'w', encoding='utf-8') as fout:
            json.dump(dct, fout)

obj = Model()
obj.save()

print(dir(Model))
print(list(filter(lambda x: not x.startswith('_'), dir(Model))))