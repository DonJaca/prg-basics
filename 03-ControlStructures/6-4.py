temperature = float(input('Enter temperature: '))
if temperature > 35:
    message = 'It is extremely hot'
elif temperature > 30:
    message = 'It is hot'
elif temperature >= 15:
    message = 'It is warm'
elif temperature >= 0:
    message = 'It is cold'
else:
    message = 'Warning, frost'
print(f'{temperature}°C: {message}')
