def time_string(es,m,format):
    h = int(es)
    if format == "24":
        return f'{h}:{m}'
    elif format == "12":
        if h>=12:
            return f'{h-12}:{m}:pm'
        else:
            return f'{h}:{m}:am'

hour = input("Hours")
minuta = input("minuta")
Format = input("Format")
print(time_string(hour,minuta,Format))