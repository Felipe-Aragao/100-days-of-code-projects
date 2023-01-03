import colorgram

colors_extract = colorgram.extract('image.jpg', 40)
colors_list = []

for color in colors_extract:
    rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
    colors_list.append(rgb)

for i in range(2):
    colors_list.pop(0)
