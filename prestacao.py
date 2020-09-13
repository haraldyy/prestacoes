def prestacao(preco):
    for w in range(1,25):
        prest=preco/w
        print(f'{w}x de R$ {prest:.2f}')
def main():
    preco=int(input(''))
    prestacao(preco)
if __name__=='__main__':
    main()
