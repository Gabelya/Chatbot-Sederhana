import datetime
import difflib
import random

responses = {
    "halo": "Halo juga! 😊",
    "apa kabar": "Saya baik, terima kasih 😊",
    "hari apa": None,
    "jam berapa": None,
    "tanggal berapa": None,
    "bulan apa": None,
    "tahun berapa": None,
    "siapa nama kamu": "Saya tidak mempunyai nama tertentu 😊",
    "apa yang bisa kamu lakukan": "Saya bisa menjawab pertanyaan sederhana seperti 'hari apa', 'jam berapa', tebak-tebakan, membuat lelucon, dan memberikan fakta 😊",
    "siapa pencipta kamu": "Saya diciptakan oleh mahasiswa UMSIDA bernama Galen Abel Wijaya 😊",
    "terima kasih": "Sama-sama 😊",
    "hai": "Hai juga 😊"
}


jokes = [
    "Kenapa programmer bingung di supermarket? Karena mereka tidak bisa menemukan 'array'! 😂",
    "Kenapa komputer selalu dingin? Karena mereka punya banyak 'fans'! 😂",
    "Kenapa programmer tidak pernah lapar? Karena mereka selalu makan 'bytes'! 😂",
    "Kenapa komputer tidak bisa menyimpan rahasia? Karena mereka selalu 'leaking'! 😂",
    "Kenapa programmer tidak pernah ke gym? Karena mereka sudah 'fit' dengan kode mereka! 😂",
    "Kenapa matahari tenggelam? Karena nggak bisa berenang! 😂",
    "Kenapa bulan selalu sedih? Karena dia selalu berada di sisi gelap! 😂",
    "Kenapa bintang selalu bersinar? Karena mereka punya banyak 'light'! 😂",
    "Burung, burung apa yang suka nolak? Burung gakgak mau! 😂",
    "Kenapa gajah tidak bisa menyembunyikan diri? Karena mereka terlalu besar! 😂",
    "Sayuran apa yang dingin? Sayur cold! 😂",
    "Nun mati bertemu ain? Ain nya terkejut 😂",
    "Gula, gula apa yang bukan gula? Gula aren’t! 😂",
    "Nama kota apa yang banyak bapak-bapaknya? Purwodaddy 😂",
    "Ikan, ikan apa yang bisa terbang? Lelelawar! 😂"
]

riddles = [
    "Apa yang selalu datang tapi tidak pernah tiba? Jawabannya: 'besok'! 😂",
    "Apa yang punya banyak kunci tapi tidak bisa membuka pintu? Jawabannya: 'piano'! 😂",
    "Apa yang punya banyak gigi tapi tidak bisa menggigit? Jawabannya: 'sisir'! 😂",
    "Apa yang punya banyak lubang tapi tidak bisa masuk? Jawabannya: 'saringan'! 😂",
    "Apa yang punya banyak kaki tapi tidak bisa berjalan? Jawabannya: 'kursi'! 😂",
    "Kenapa pohon mangga di depan rumah harus ditebang? Jawabannya: 'Kalau dicabut berat' 🌲😂",
    "Apa yang bisa dipegang di tangan kanan, tapi tidak bisa dipegang di tangan kirimu? Jawabannya: 'Siku tangan kiri kamu' 😂",
    "Mata apa yang nggak pake kacamata? Jawabannya: 'Matahari'! 😂",
    "Apa yang punya banyak huruf tapi tidak bisa membaca? Jawabannya: 'Alfabet'! 😂",
    "Punya jari, punya tangan, enggak punya leher, enggak punya kepala? Jawabannya: 'Baju'! 😂"
]

facts = [
    "Kucing punya 32 otot di setiap telinga mereka! 😺",
    "Lumba-lumba tidur dengan satu mata terbuka! 🐬",
    "Gajah adalah satu-satunya hewan yang tidak bisa melompat! 🐘",
    "Lebah punya lima mata! 🐝",
    "Ular bisa merasakan getaran lewat lidah mereka! 🐍",
    "Sebelum Masehi bahasa Inggrisnya adalah B.C (Before Christ). Setelah Masehi adalah A.D (Anno Domini) 🗓️",
    "Ikan hiu kehilangan gigi lebih dari 6000 buah setiap tahun, dan gigi barunya tumbuh dalam waktu 24 jam 🦈",
    "Julius Caesar tewas dengan 23 tikaman pada saat pembunuhannya! 🗡️",
    "Nama mobil Nissan berasal dari bahasa Jepang: Ni = 2 dan San = 3. Nissan = 23 🚗",
    "Jerapah dan tikus bisa bertahan hidup lebih lama tanpa air dari pada unta🐪🐀",
    "Perut memproduksi lapisan lendir setiap dua minggu agar perut tidak mencerna organnya sendiri🧑‍⚕️",
    "98% dari perkosaan dan pembunuhan dilakukan oleh keluarga dekat atau teman korban🗡️🩸",
    " Semut dapat mengangkat beban 50 kali tubuhnya! 🐜",
    "Deklarasi Kemerdekaan Amerika ditulis diatas kertas marijuana🌎",
    "Lidah jerapah panjangnya sekitar 50 cm🦒",
    "Mulut menghasilkan 1 liter ludah setiap hari! 👄",
    "Kita bernafas kira-kira 23.000 kali setiap hari! 🌬️",
    "Kata ZIP (kode pos) adalah kepanjangan dari Zoning Improvement Plan 📬",
    " Coca-Cola mengandung Coca (yang merupakan zat aktif pada kokain) dari tahun 1885 sampai 1903🍺",
    "4 simbol raja pada kartu remi melambangkan 4 raja yang etrkenal di jaman masing-masing: Sekop = David/Raja Daud ; Keriting = Alexander the Great/Iskandar Agung ; Hati = Charlemagne/ Raja Prancis ; Wajik =Julius Caesar",
    "Seumur hidup kita meminum air sebanyak kurang lebih 75.000 liter! 💧",
    " Pria kehilangan 40 helai rambut tiap hari. wanita 70 helai.👩‍🦲👨‍🦲",
    "Unta punya 3 kelopak mata. 🐪",
    "Albert Einstein dan Charles Darwin,keduanya menikah dengan sepupu pertama mereka (Elsa Löwenthal dan Emma Wedgewood)👨‍🔬👩‍🔬",
    "Seseorang masih akan sadar selama 8 detik setelah dipenggal! 🗡️"
]

def chatbot():
    print("Selamat datang 😊")
    print("Apa yang bisa saya bantu? 😊")
    while True:
        user_input = input("Anda: ").lower().strip()

        if user_input in ["exit", "keluar"]:
            print("Chatbot: Sampai jumpa 😊")
            break


        match = difflib.get_close_matches(user_input, responses.keys(), n=1, cutoff=0.6)
        if match:
            key = match[0]
            if key == "hari apa":
                today = datetime.date.today()
                print(f"Chatbot: Hari ini {today.strftime('%A')}, {today.strftime('%d %B %Y')} 🗓️")
            elif key == "jam berapa":
                now = datetime.datetime.now()
                print(f"Chatbot: Sekarang jam {now.strftime('%H:%M:%S')} 🕰️")
            
            elif key == "tanggal berapa":
                today = datetime.date.today()
                print(f"Chatbot: Hari ini tanggal {today.strftime('%d')} 🗓️")
            elif key == "bulan apa":
                today = datetime.date.today()
                print(f"Chatbot: Sekarang bulan {today.strftime('%B')} 🗓️")
            elif key == "tahun berapa":
                today = datetime.date.today()
                print(f"Chatbot: Sekarang tahun {today.strftime('%Y')} 🗓️")

            else:
                print("Chatbot:", responses[key])
        else:

            if "lelucon" in user_input:
                print("Chatbot:", random.choice(jokes))
            elif "tebak" in user_input:
                print("Chatbot:", random.choice(riddles))
            elif "fakta" in user_input:
                print("Chatbot:", random.choice(facts))
            else:
                print("Chatbot: Maaf, saya tidak mengerti 😊")

chatbot()
