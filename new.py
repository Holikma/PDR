import random

def main():
    percent = 90
    with open("picture.pgm", "r") as f:
        f.readline()
        width, height = map(int, f.readline().split())
        picture = [[int(f.readline()) for _ in range(int(width))] for _ in range(int(height))]
    display_matrix = [[1 for _ in range(int(width))] for _ in range(int(height))]
    counter = 0
    while counter < int(width)* int(height)/100 * percent:
        random_x = random.randint(1, int(width)-2)
        random_y = random.randint(1, int(height)-2)
        if display_matrix[random_y][random_x] == 0:
            continue
        else:  
            counter += 1
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
