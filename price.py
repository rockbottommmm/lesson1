def get_summ(one,two,delimeter='&'):
    return (f'{one} {delimeter} {two}')

result = get_summ('learn','python')
for n in result.split():
    print(n.capitalize(), end = ' ')

print()

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

result = format_price(56.24)
print(result)