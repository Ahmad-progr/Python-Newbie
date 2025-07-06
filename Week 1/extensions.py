def main():
    t_ext = v_ext()

    if t_ext is None:
        print("application/octet-stream")
    else:
        final_ext = file_extension(t_ext)
        print(final_ext)


def v_ext():
    f_name = input("Enter file name: ").lower().strip()
    f_ext = f_name.endswith(('.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip'))
    if f_ext:
        return f_name
    else:
        return None


def file_extension(t_ext1):
    extension = t_ext1[-3:]
    if t_ext1.endswith(('.gif','.png')):
        return f"image/{extension}"
    elif t_ext1.endswith(('.jpg','.jpeg')):
        return "image/jpeg"
    elif t_ext1.endswith(('.pdf','.zip')):
        return f"application/{extension}"
    elif t_ext1.endswith(('.txt')):
        return "text/plain"

main()