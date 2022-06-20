def read_file(filename):
    """
    Читает двумерный массив из файла по имени или полному пути к нему
    """
    with open(filename) as file:
        array2d = [[float(digit) for digit in line.split()] for line in file]
        
    return array2d

def plot_image(array2d):
    """
    Отрисовывает цветовую карту инвертируя изображение (фон - белый, источники - черные)
    """
        
    import matplotlib.pyplot as plt
    
    color_map = plt.cm.get_cmap('gray')
    reversed_color_map = color_map.reversed()

    plt.figure(figsize=(20, 20))
    plt.imshow(array2d, cmap=reversed_color_map)
    plt.show()
    
    return None