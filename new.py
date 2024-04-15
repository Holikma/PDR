import random

def main():
    percent = 10
    with open("picture.pgm", "r") as f:
        f.readline()
        width, height = map(int, f.readline().split())
        picture = [[int(f.readline()) for _ in range(int(width))] for _ in range(int(height))]
    display_matrix = [[1 for _ in range(int(width))] for _ in range(int(height))]
    for _ in range(int((height*width)/percent)):
        random_x = random.randint(0, int(width)-1)
        random_y = random.randint(0, int(height)-1)
        display_matrix[random_y][random_x] = 0
    with open("new_picture.pgm", "w") as f:
        f.write("P2\n")
        f.write(str(width) + " " + str(height) + "\n")
        f.write("255\n")
        for i in range(int(height)):
            for j in range(int(width)):
                f.write(str(picture[i][j] * display_matrix[i][j]) + "\n")   
        
    return 0


if __name__ == "__main__":
    main()
