
# import ile csv dosyalarını okumak için kullanılan csv kütüphanesi
# ve kendi yazdığım işlem fonksiyonlarını kullanmak statistic_core_functions dosyasını ekliyorum
import csv
import statistic_core_functions

# hesaplamaları yapıp alt alta sonuçları yazan bir fonksiyon
# tekrar tekrar iki kez bu uzun satırı yazmamak için
def analysis_results():
    print("\n------------------ ANALYSIS RESULTS ------------------")
    print(f"Number of Data    : {statistic_core_functions.number_of_data(data_list)}")
    print(f"Total Sum         : {statistic_core_functions.total_sum(data_list)}")
    print(f"Arithmetic Mean   : {statistic_core_functions.aritmetic_mean(data_list)}")
    print(f"Median            : {statistic_core_functions.median(data_list)}")
    print(f"Data Range        : {statistic_core_functions.data_range(data_list)}")
    print(f"Sample Variance   : {statistic_core_functions.sample_variance(data_list)}")
    print(f"Sample Std Dev    : {statistic_core_functions.sample_standard_deviation(data_list)}")
    print(f"Q1 (First Quartile): {statistic_core_functions.Q1(data_list)}")
    print(f"Q3 (Third Quartile): {statistic_core_functions.Q3(data_list)}")
    print(f"IQR               : {statistic_core_functions.IQR(data_list)}", "\n")


print("------------------Statistic Calculator------------------")
print("'1' : Enter data manually")
print("'2' : Import a csv file")
print("'3' : Exit","\n")

# csv dosyası da olsa elle de girilse verilerin ekleneceği liste
data_list = []

# kullanıcı geçersiz input girerse tekrar sormak için bir döngü içine alınır
while True :

    s = input("Please choose a option: ")

    # match - case ile spesifik olarak istediğim değer olursa yapılacaklar ayrılır
    # ( _ ) else anlamında kullanılıyor
    match (s):

        case "1":
            print("Please enter your data separated by comma ( , ) ")
            manual_input_str = input("(example; 10, 4, 6, 23, ... ) : ")
            # split ile ( , ) lerden ayraç gibi ayrılır
            manual_input_str_split = manual_input_str.split(",")

            # for döngüsünü tek satırda yazdım bu şekilde yazıldığında [] içinde olması lazım
            # append fonksiyonuna gerek yok direk float(number) yazarak float a çevrilip manual_input listesine ekleniyor
            manual_input = [float(number) for number in manual_input_str_split]
            data_list = data_list + manual_input
            print(f"{len(manual_input)} data entries were made","\n")

            # eğer dosya boş değilse analysis_results fonksiyonu kullanılıp sonuçlar yazılır yoksa çıkılır
            if len(data_list) > 0:
                analysis_results()
            else:
                print("No data to analyze. Exiting program.")
                break

            while True:
                choice = input("\nType 'z' for Z-Score list, or '1' to exit : ").lower()

                if choice == "z":
                    print("\n--- Z-Scores ---")
                    print(statistic_core_functions.z_scores_list(data_list))

                    while True:
                        exit_choice = input("\nType '1' to exit : ")
                        if exit_choice == "1":
                            exit()
                        else:
                            print("Invalid input. Please type '1' to exit.")

                    break

                elif choice == "1":
                    exit()

                else:
                    print("Invalid choice. Please type 'z' or '1'.")

        case "2":
            # kullanıcıdan okunacak csv dosyasının dosya yolunu istiyoruz
            # with open ile o dosya açılır "r" okuma modunda as file ile bu dosyaya kod içinde bir isim atanır
            file_path = input("Please enter the path your file (example; C:/folder/data.csv) : ")
            with open(file_path, mode = "r") as file:

                # csv reader fonksiyonu tüm dosyayı okuyor
                whole_file_reader = csv.reader(file)

                # next fonksiyonu o satırı koparıyor ve alt satıra geçiriyor imleci
                # titles diye dosyanın başındaki başlıkları ayrı bir liste olarak elde ediyoruz
                # hem de ilk  satırı ayırdığı için kalan whole_file_reader sadece sayısal değerleri içeriyor
                titles = next(whole_file_reader)

                # enumerate iki değer çıkarır hem index i hem değeri o liste içindeki değeri çıkarır
                # o yüzden for içinde index ve name diye iki değişken atadım
                for index,name in enumerate(titles):
                    print(f"{index} : {name}")

                title_index = int(input("Choose a title to calculate : "))

                # bu for döngüsü ise satır satır dolanıp kullanıcının seçtiği başlığa denk gelen indexdeki değerleri listeye ekliyor
                for element in whole_file_reader:
                    data_list.append(float(element[title_index]))

                # eğer dosya boş değilse analysis_results fonksiyonu kullanılıp sonuçlar yazılır yoksa çıkılır
                if len(data_list) > 0:
                    analysis_results()

                else:
                    print("No data to analyze. Exiting program.")
                    break
            while True:
                choice = input("\nType 'z' for Z-Score list, or '1' to exit : ").lower()

                if choice == "z":
                    print("\n--- Z-Scores ---")
                    print(statistic_core_functions.z_scores_list(data_list))

                    while True:
                        exit_choice = input("\nType '1' to exit : ")
                        if exit_choice == "1":
                            exit()
                        else:
                            print("Invalid input. Please type '1' to exit.")

                elif choice == "1":
                    exit()

                else:
                    print("Invalid choice. Please type 'z' or '1'.")

        # 3 girilirse çıkılır
        case "3":
            print("Exiting...")
            break
        # döngü içinde olduğu için geçersiz bir girdi olunca tekrar sorar geçerli bir seçenek yazılana kadar
        case _:
            print("Please choose a valid option","\n")