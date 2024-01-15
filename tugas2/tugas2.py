poin = int(input("masukan nilai mahasiswa: "))
grade = "E"

if poin > 85:
    grade = "4.00 \ndengan predikat A"
elif poin >= 80:
    grade = "3.70 \ndengan predikat A-"
elif poin >= 75:
    grade = "3.30 \ndengan predikat B+"
elif poin >= 70:
    grade = "3.00 \ndengan predikat B"
elif poin >= 65:
    grade = "2.70 \ndengan predikat B-"
elif poin >= 60:
    grade = "2.30 \ndengan predikat C+"
elif poin >= 55:
    grade = "2.00 \ndengan predikat C"
elif poin >= 50:
    grade = "1.70 \ndengan predikat C-"
elif poin >= 40:
    grade = "1.00 \ndengan predikat D"
else:
    grade = "0 \ndengan predikat E"

print("IPK mahasiswa adalah {}".format(grade))
