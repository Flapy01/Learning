#this code need 2 images. exemplo1 and exemplo2 .jpeg
idade = int(input("Digite a sua idade:"))
idade = 2020 - idade
print("O ano do seu nascimento é:", idade)
if( idade <= 2002):
    import cv2
    print("Você é maior de idade")
    imagempositivo =  cv2.imread ("exemplo1.jpeg", 1)
    cv2.imshow (":)", imagempositivo)
    cv2.waitKey (0)
    cv2.destroyAllWindows ()
else:
    print("Você é menor de idade")
    import cv2
    imagemnegativo = cv2.imread("exemplo2.jpeg", 1)
    cv2.imshow(":(", imagemnegativo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()