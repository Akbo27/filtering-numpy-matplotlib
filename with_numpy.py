import numpy as np
import time
import matplotlib.pyplot as plt

def generate_random_set(num_segments, x_range=(-10, 10), y_range=(-10, 10)):
    x1 = np.random.uniform(*x_range, num_segments)
    y1 = np.random.uniform(*y_range, num_segments)
    x2 = np.random.uniform(*x_range, num_segments)
    y2 = np.random.uniform(*y_range, num_segments)
    return np.stack((x1, y1, x2, y2), axis=1)

def filter_segments(segment, rectangle):
    x_min, y_min, x_max, y_max = rectangle
    x1, y1, x2, y2 = segment[:, 0], segment[:, 1], segment[:, 2], segment[:, 3]
    inside = (
        (x_min <= x1) & (x1 <= x_max) & (y_min <= y1) & (y1 <= y_max) &
        (x_min <= x2) & (x2 <= x_max) & (y_min <= y2) & (y2 <= y_max)
    )
    return segment[inside]

if __name__ == "__main__":
    num_segments = 100000 
    segments = generate_random_set(num_segments) 

    rectangle = [-1, -1, 3, 2]

    start_time = time.time()  
    filtered_segments = filter_segments(segments, rectangle) 
    end_time = time.time()  

    print(f"Filtering {num_segments} segments with NumPy took {end_time - start_time:.4f} seconds.")
    print(f"Number of segments inside the rectangle: {len(filtered_segments)}")

    plt.figure(figsize=(10, 6))

    for seg in segments[:1000]:
        plt.plot([seg[0], seg[2]], [seg[1], seg[3]], color='gray', alpha=0.5)

    for seg in filtered_segments[:1000]:
        plt.plot([seg[0], seg[2]], [seg[1], seg[3]], color='blue', alpha=0.8)

    rect_x = [rectangle[0], rectangle[2], rectangle[2], rectangle[0], rectangle[0]]
    rect_y = [rectangle[1], rectangle[1], rectangle[3], rectangle[3], rectangle[1]]
    plt.plot(rect_x, rect_y, color='red', linewidth=2)

    plt.title("Segments Inside Rectangle (NumPy)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()






