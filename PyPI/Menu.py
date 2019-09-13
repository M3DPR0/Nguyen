# Wajib dijalankan menggunakan bahasa Python2

# fungsi untuk menampilkan menu
def show_menu():
    print "\n"
    print "----------- MENU ----------"
    print "[1] Login"
    print "[2] About"
    print "[3] Exit"
    
    menu = input("PILIH MENU> ")
    print "\n"

    if menu == 1:
        login_data()
    elif menu == 2:
        about_data()
    elif menu == 3:
        exit_data()
    else:
        print "Salah pilih!"











if __name__ == "__main__":

    while(True):
        show_menu()
