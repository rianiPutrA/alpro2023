# file I/O ada dua mode
# mode pertama -> baca (READ) r
# mode kedua -> tulis (WRITE) w


if __name__ == "__main__":
    nama_file = "test.txt"
    text = "santai tapi serius"

    # contoh write atau tulis
    with open(nama_file, "w") as f:
        f.write(text)

    # contoh read atau baca
    with open(nama_file, "r") as f:
        print(f.read())
