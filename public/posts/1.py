import os

folder = "content/posts/training_plan"
for file in os.listdir(folder):
    if file.endswith(('.jpg', '.png', '.jpeg')):
        print(f"![{file}]({folder}/{file})")

