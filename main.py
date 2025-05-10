import sys
import time
from colorama import Fore, Back, Style, init


init()

def jalanin_lirik():
    BACKGROUND = Back.BLUE
    JUDUL_COLOR = Fore.MAGENTA + Style.BRIGHT
    LIRIK_COLOR = [Fore.CYAN, Fore.WHITE, Fore.GREEN]  
    AKHIR_COLOR = Fore.YELLOW + Style.BRIGHT

    lirik = [
        ("Kapan terakhir kali kamu dapat tertidur tenang?", 0.09),
        ("(Renggang)", 0.4),
        ("Tak perlu memikirkan tentang apa yang akan datang", 0.09),
        ("Esok hari", 0.2),
        ("Tubuh yang berpatah hati", 0.1),
        ("Bergantung pada gaji", 0.09),
        ("Berlomba jadi asri", 0.09),
        ("Mengais validasi",0.09),
        ("Dan aku pun terhadir",0.09),
        ("Seakan paling mahir",0.09),
        ("Menenangkan dirimu yang merasa terpinggirkan dunia",0.09),
        ("Tak pernah adil",0.09),
        ("Kita semua gagal",0.06),
        ("Angkat minuman mu",0.06),
    ]

    delay_antar_baris = [0.9, 0.6, 0.7, 0.7, 0.8, 0.8, 0.8,0.9,0.9,0.9,0.9,0.9,0.9,0.9,]

    print(BACKGROUND + Fore.WHITE + "\n\n  ✦🎵✦ LYRICS VISUALIZER ✦🎵✦  " + Style.RESET_ALL)
    print(JUDUL_COLOR + "\n≪≪≪ Secukupnya - Hindia ≫≫≫\n" + Style.RESET_ALL)
    time.sleep(1)

    for idx, (baris, char_delay) in enumerate(lirik):
        color = LIRIK_COLOR[idx % len(LIRIK_COLOR)]
        print(color + "♫ ", end="")
        
        for kar in baris:
            print(kar, end='')
            sys.stdout.flush()
            time.sleep(char_delay * 0.8)  
        
        print(Style.BRIGHT + " ✧" + Style.NORMAL)
        time.sleep(delay_antar_baris[idx] * 1.2)  

    print(AKHIR_COLOR + "\n✧･ﾟ･✧･ﾟ･ THE END ✧･ﾟ･✧･ﾟ･")
    print(Style.RESET_ALL + "// Lyrics Visualizer by GanzMods\n")

if __name__ == "__main__":
    jalanin_lirik()
