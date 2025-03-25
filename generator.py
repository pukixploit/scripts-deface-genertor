import os
import sys
from termcolor import colored

# Pastikan modul termcolor terinstal
def install_dependencies():
    try:
        import termcolor
    except ImportError:
        print("📦 Menginstal dependensi termcolor...")
        os.system(f"{sys.executable} -m pip install termcolor")
        print("✅ Instalasi selesai!")
        os.execv(sys.executable, [sys.executable] + sys.argv)  # Restart skrip

install_dependencies()

# Simpan HTML asli di dalam script
HTML_TEMPLATE = """



<html> <HEAD> <title>Hacked By mis.style</title> 
<meta content='Hacked By mis.style , Hacked By KEJE ARMY, KEJE ARMY' name='description'/> 
<meta content='Hacked By mis.style, KEJE ARMY' name='subject'/> 
<style> body { position: relative; } body:before { content: ''; display: block; position: absolute; z-index: 999999999999999 !important; top: 0; left: 0; right: 0; bottom: 0; pointer-events: none; background-image: url(''), url('https://www.dropbox.com/s/54le1eyh01vb253/divi-life-snowflakes-b.png?dl=1'), url('https://www.dropbox.com/s/gfm01rozxanf3ub/divi-life-snowflakes-d.png?dl=1'); -webkit-animation: snow 15s linear infinite; -moz-animation: snow 15s linear infinite; -ms-animation: snow 15s linear infinite; animation: snow 15s linear infinite; } @keyframes snow { 0% {background-position: 0px 0px, 0px 0px, 0px 0px;} 50% {background-position: 500px 500px, 100px 200px, -100px 150px;} 100% {background-position: 500px 1000px, 200px 400px, -100px 300px;} } @-moz-keyframes snow { 0% {background-position: 0px 0px, 0px 0px, 0px 0px;} 50% {background-position: 500px 500px, 100px 200px, -100px 150px;} 100% {background-position: 400px 1000px, 200px 400px, 100px 300px;} } @-webkit-keyframes snow { 0% {background-position: 0px 0px, 0px 0px, 0px 0px;} 50% {background-position: 500px 500px, 100px 200px, -100px 150px;} 100% {background-position: 500px 1000px, 200px 400px, -100px 300px;} } @-ms-keyframes snow { 0% {background-position: 0px 0px, 0px 0px, 0px 0px;} 50% {background-position: 500px 500px, 100px 200px, -100px 150px;} 100% {background-position: 500px 1000px, 200px 400px, -100px 300px;} } html { background-color: #000000; color: #000; } h2, h3 { font-family: Sedgwick Ave; font-size: 38px; text-shadow: 15px 15px 30px grey; } .x { background-color: #000000; color: #fff; font-family: Courier; font-size: 24px; left: 0; bottom: 0; position: fixed; width: 100% display: flex; text-shadow: 10px 10px 25px white; justify-content: center; align-items: center; } :selection { color: #fff; background: #000; } a { color: red; text-decoration: none; } </style>

</style> 
  </HEAD> 
  <link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'> 
  
  <body bgcolor="#000000" 
  
  
  <DIV align="right"><FONT style="FONT-SIZE: 13pt" face="Courier" color="green"><center><br /> 
 
<body> <br /><br /> 
       <p id='s0'> 
        
<body> 
<img src='
https://raw.githubusercontent.com/pukixploit/shell-backdoor/refs/heads/main/logo.png' height='400' title='KEJE ARMY' /><br /> 

  <p id="example2"><p align="center"><font face="Orbitron" size="7" color="red"><p><font color="red">KEJE </font><font face="Orbitron" size="7" color="red">ARMY
  </font></p> 
  <font face="Orbitron" size="3" color="white">Hacked By mis.style
  <pre> Dear Admin:</br
><br> Hello, I'm mis.style!</br
><br> Thanks To My Team:</br
><br> Fr13Nd | mis.style | Mr.XnX | kalomba | MrSanZz | DoWnfeal | ARJUN-X001</br
><br>My family:</br
><br> ALL TEAM DEFACER INDONESIA
<html>
  <style type="text/css">.lagu{background:transparent;border:1px solid red;font-family:Share\ Tech\ Mono;color:;font-size:10px;font-weight:normal;padding:2px 25px;text-decoration:none;text-shadow:0 0 0px #000000}</style>
  <script>
  function play(){var audio=document.getElementById('lagu');audio.play();}function liat(){document.getElementById('galiat').style.visibility='visible';}</script>
  <script src="" type="text/javascript">
  </script>
  <br>
  <button class="lagu" onclick="play();liat();"><font face="courier new" size="4" color="white">PLAY MUSIC</font></button><audio id="lagu" src="  https://k.top4top.io/m_2823x88jj0.mp3  "></audio>
  <br><br>
    </p>
      </html>
        </div> 
</body></html>
"""

def print_banner():
    banner = """
                                                          ====================================
                                                             DEFACE SCRIPTS GENETOR KEJE ARMY
                                                          ====================================
    """
    print(colored(banner, 'red'))

def buat_file_html(nama_file):
    """Membuat file HTML jika belum ada."""
    if not os.path.exists(nama_file):
        with open(nama_file, 'w', encoding='utf-8') as file:
            file.write(HTML_TEMPLATE)
        print(colored(f"✅ File '{nama_file}' berhasil dibuat!", 'green'))

def ganti_teks_html(nama_file, perubahan):
    """Mengganti teks dalam file HTML berdasarkan perubahan yang diberikan."""
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            data = file.read()
        
        for teks_lama, teks_baru in perubahan.items():
            data = data.replace(teks_lama, teks_baru)
        
        with open(nama_file, 'w', encoding='utf-8') as file:
            file.write(data)
        
        print(colored(f"✅ Perubahan berhasil disimpan di '{nama_file}'!", 'yellow'))
    except Exception as e:
        print(colored(f"❌ Terjadi kesalahan: {e}", 'red'))

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    
    nama_file = input(colored("Masukkan nama file HTML (contoh: index.html): ", 'blue')).strip()
    if not nama_file:
        print(colored("❌ Nama file tidak boleh kosong! Menggunakan default 'index.html'.", 'red'))
        nama_file = "index.html"
    
    buat_file_html(nama_file)
    
    nama_baru = input(colored("Masukkan nama kamu: ", 'magenta')).strip()
    pesan_baru = input(colored("Masukkan pesanmu: ", 'magenta')).strip()
    tim_baru = input(colored("Masukkan nama temanmu gunakan tanda | : ", 'magenta')).strip()
    keluarga_baru = input(colored("Masukkan nama komunitas hacker mu: ", 'magenta')).strip()
    
    perubahan = {
        "Hacked By mis.style": f"Hacked By {nama_baru}",
        "Hello, I'm mis.style!": pesan_baru,
        "Fr13Nd | mis.style | Mr.XnX": tim_baru,
        "ALL TEAM DEFACER INDONESIA": keluarga_baru
    }
    
    ganti_teks_html(nama_file, perubahan)
    print(colored(f"\n🎉 Perubahan selesai! Silakan cek file '{nama_file}' di browser.", 'green'))
