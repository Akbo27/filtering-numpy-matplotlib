import matplotlib.pyplot as plt
import time
import random

def generate_random_set(num_segments, x_range=(-10, 10), y_range=(-10, 10)):
    segments = []
    for i in range(num_segments):
        x1, y1 = random.uniform(*x_range), random.uniform(*y_range)
        x2, y2 = random.uniform(*x_range), random.uniform(*y_range)
        segments.append([x1, y1, x2, y2])
    return segments

def check_inside(segment, rectangle):
    x1, y1, x2, y2 = segment
    x_min, y_min, x_max, y_max = rectangle
    return (
        x_min <= x1 <= x_max and y_min <= y1 <= y_max and
        x_min <= x2 <= x_max and y_min <= y2 <= y_max
    )

def filter_segments(segments, rectangle):
    return [seg for seg in segments if check_inside(seg, rectangle)]

if __name__ == "__main__":
    num_segments = 100000
    segments = generate_random_set(num_segments)

    rectangle = [-1, -1, 3, 2]  

    start_time = time.time()
    filtered_segments = filter_segments(segments, rectangle) 
    end_time = time.time()

    print(f"Filtering {num_segments} segments took {end_time - start_time:.4f} seconds.")
    print(f"Number of filtered segments: {len(filtered_segments)}")

    plt.figure(figsize=(10, 6))

    for seg in segments[:1000]: 
        x, y = [seg[0], seg[2]], [seg[1], seg[3]]
        plt.plot(x, y, color='gray', alpha=0.5)

    for seg in filtered_segments[:1000]:
        x, y = [seg[0], seg[2]], [seg[1], seg[3]]
        plt.plot(x, y, color='blue', alpha=0.8)

    rect_x = [rectangle[0], rectangle[2], rectangle[2], rectangle[0], rectangle[0]]
    rect_y = [rectangle[1], rectangle[1], rectangle[3], rectangle[3], rectangle[1]]
    plt.plot(rect_x, rect_y, color='red', linewidth=2)

    plt.title("Segments Inside Rectangle")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
