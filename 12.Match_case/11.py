print('''pdf
jpg
png
mp3
mp4''')
payment=input("enter extension: ").lower().strip()

match payment:
    case "pdf":
        print("Document file")
    case "jpg":
        print("Image file")
    case "png":
        print("Image file")
    case "mp3":
       print("Audio file")
    case "mp4":
           print("Video file")
    case _:
        print("Unknown File Type")

