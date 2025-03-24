from PIL import Image
image1 = Image.open("british_shorthair.jpg")
gscale2 = "@%#*+=-:. "

def createAsciiPicture(image1,scale=30):
    image = image1.convert('L')
    width, height = image1.size[0], image.size[1]
    image = image.resize((width // scale, height // scale))
    width, height = image.size[0], image.size[1]
    pix = image.load()

    # creating a base for ascii picture based on resized picture
    grid = []
    for i in range(height):
        grid.append(["X"]*width)

    # changing our base according to brightness of each pixel
    # pixels have a brightness from 0 to 100
    # every 10 pixels - different ascii character
    for y in range(height):
        for x in range(width):
            if pix[x,y] < 10:
                grid[y][x] = gscale2[0]
            elif pix[x,y] == 100:
                grid[y][x] = gscale2[9]
            else:
                pixel = int(pix[x,y])
                pixel = int(str(pixel)[0])
                grid[y][x] = gscale2[pixel]

    # creating a new file in which there is an output
    art = open("jpg","w")
    for row in grid:
        art.write("".join(row)+"\n")
    art.close()
    print(art)

createAsciiPicture(image1)
