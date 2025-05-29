from PIL import Image, ImageDraw

def create_image(filename, size, color, shape):
    img = Image.new("RGB", size, "white") # Start with white background
    draw = ImageDraw.Draw(img)
    if shape == "square":
        draw.rectangle([(0,0), (size[0]-1, size[1]-1)], fill=color)
    elif shape == "circle":
        draw.ellipse([(0,0), (size[0]-1, size[1]-1)], fill=color)
    elif shape == "triangle":
        # A simple equilateral-ish triangle
        points = [(size[0]//2, 0), (0, size[1]-1), (size[0]-1, size[1]-1)]
        draw.polygon(points, fill=color)
    img.save(filename)

if __name__ == "__main__":
    # This script assumes it's run from the root of the py_sikuli_like directory
    # or that the py_sikuli_like/examples/images/ path is valid from cwd.
    # For the agent, it's run from /app, so paths should be relative to that.
    output_dir = "py_sikuli_like/examples/images/"
    image_size = (50, 50)

    create_image(output_dir + "red_square.png", image_size, "red", "square")
    print(f"Created {output_dir}red_square.png")

    create_image(output_dir + "blue_circle.png", image_size, "blue", "circle")
    print(f"Created {output_dir}blue_circle.png")

    create_image(output_dir + "green_triangle.png", image_size, "green", "triangle")
    print(f"Created {output_dir}green_triangle.png")
