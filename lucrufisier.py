def main():
    f=open("fisiertest.txt","r")
    semnepunctuatie=['.',':','?','!',',','-']
    continut=f.read()
    continut_final=""
    for c in continut:
        if c not in semnepunctuatie:
            continut_final+=c

    f.close()
    f=open("fisiertest.txt","w")
    f.write(continut_final)


if __name__ == "__main__":
    main()