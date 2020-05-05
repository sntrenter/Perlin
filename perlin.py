from PIL import Image
import time
import random



X = 1000
Y = 1000


L = []

def perlin_noise(x,y):
    

    


def main():
    L = [[0 for x in range(Y)] for y in range(X)]#columns x rows
    for i in range(X):
        for j in range(Y):
            L[i][j] = int(random.random()*255)

    #print(L)
    perlin = Image.new("RGB",(Y,X),255)
    data = perlin.load()
    for x in range(X):
        for y in range(Y):
            #p = int(L[x][y])
            p = perlin_noise(x,y)
            data[x,y] = (
                p,
                p,
                p
            )

    
    perlin.show()
    
            
            


main()


#random shit i thought would be helpful below


def open_Image():
    im = Image.open("Vihren_Pirin_IMG_8898.jpg")
    im.show()


#https://stackoverflow.com/questions/12062920/how-do-i-create-an-image-in-pil-using-a-list-of-rgb-tuples
