import hashlib

def main():
    try:
        with open("list.txt", "r") as file:
            nice = file.read().splitlines()
            file.close()
            vide = []
            for i in nice:
                vide.append(i + ":" + hashlib.sha512(i.encode('utf-8')).hexdigest() + "\n")

            listToStr = ' '.join([str(elem) for elem in vide]) #cast array to string
            final = open("result.txt", "w")
            final.write(listToStr)
    except:
        pass

main()
