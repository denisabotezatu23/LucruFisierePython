def main():
    f=open("fisiertest.txt","r")
    semnepunctuatie=['.',':','?','!',',','-']
    continut=f.read()
    continut_final=""
    for c in continut:
        if c not in semnepunctuatie:
            continut_final+=c

    cuvinte=continut.split()
    rezultat=" ".join([c for c in cuvinte if len(c)>4])

    f.close()
    f=open("fisiertest.txt","w")


    f.write(rezultat)


if __name__ == "__main__":
    main()