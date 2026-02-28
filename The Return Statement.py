def calculate_area(width, height):
    area = width * height
    area = area * 1.05 # Adding 10% for waste
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft