class media:
    def __init__ (self, media_type, caption, media_file):
        self.media_type = media_type
        self.caption = caption
        self.media_file = media_file
        self.like_counter = 1

    def give_like(self):
        self.like_counter += 1
    
    def unlike(self):
        self.like_counter -= 1

    def share(self):
        print("Share via:")
        print("1. Instagram")
        print("2. Text Message")

        choice = int(input("> "))

        if choice == 1:
            print("Sending post to Instagram")
        elif choice == 2:
            print("Sending post via Text Message")
    
    def print_info(self):
        print(f"This is a {self.media_type} post, with the caption {self.caption}, with {self.like_counter} likes")
        
def main():
    posts = []

    while True:
        print("Choose an option:")
        print("1. Post a video")
        print("2. Post a picture")
        print("3. See posts")
        print("4. Give like")

        choice = int(input("> "))

        if choice == 1:
            caption = input("Enter a caption: ")
            media_file = input("Submit your file: ")

            media_obj = media("video", caption, media_file)
            posts.append(media_obj)
        elif choice == 2:
            caption = input("Enter a caption: ")
            media_file = input("Submit your file: ")

            media_obj = media("picture", caption, media_file)
            posts.append(media_obj)
        elif choice == 3:
            for post in posts:
                print(post.print_info())
        elif choice == 4:
            for i in range(len(posts)):
                print(i, end=" ")
                posts[i].print_info()

            index = int(input("Select an index: "))

            posts[index].give_like()

if __name__ == "__main__":
    main()