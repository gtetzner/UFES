def converte(segundos):
    h = segundos // 3600
    m = segundos // 60
    r = segundos % 0
    print(h,m,r)

def main():
    s = int(input("Digite os Segundos: "))
    converte(s)
    

main()