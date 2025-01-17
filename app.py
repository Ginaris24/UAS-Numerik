import streamlit as st
from PIL import Image
from datetime import date

# Konfigurasi Halaman
st.set_page_config(
    page_title="Aplikasi Streamlit Keren",
    page_icon="🌟",
    layout="wide",
)

# CSS Kustom untuk Tampilan yang Menarik
st.markdown("""
    <style>
        body {
            background-color: #0f2027;
            background-image: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #FFD700;
            font-size: 50px;
        }
        .stButton > button {
            background-color: #FFD700;
            color: black;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton > button:hover {
            background-color: #FFA500;
            color: white;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 50px;
            color: #BBB;
        }
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown("<h1>🌟 Aplikasi Streamlit Keren 🌟</h1>", unsafe_allow_html=True)
st.write("---")

# Sidebar Navigasi
st.sidebar.title("🔮 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:", 
    ["Beranda", "Profil Pengguna", "Kalkulator Umur", "Galeri"]
)

# Halaman Beranda
if menu == "Beranda":
    st.image("https://via.placeholder.com/1200x400?text=Aplikasi+Keren", use_column_width=True)
    st.markdown(
        """
        <div style="text-align: center; font-size: 24px; margin-top: 20px;">
            Selamat datang di aplikasi Streamlit yang penuh gaya! 🌟  
            Jelajahi fitur kami, temui desain modern, dan nikmati pengalaman interaktif.  
        </div>
        """, 
        unsafe_allow_html=True
    )

# Halaman Profil Pengguna
elif menu == "Profil Pengguna":
    st.subheader("📋 Tentang Anda")
    col1, col2 = st.columns([1, 3])
    with col1:
        image = Image.open("profile_placeholder.png")  # Ganti dengan file foto Anda
        st.image(image, caption="Foto Anda", width=200)
    with col2:
        st.markdown(
            """
            **Nama**: John Doe  
            **Profesi**: Software Engineer  
            **Hobi**: Membuat aplikasi keren, membaca, dan mendaki gunung  
            **Kutipan Favorit**:  
            > "Keep pushing your limits, because only then will you grow."  
            """
        )
    st.balloons()

# Halaman Kalkulator Umur
elif menu == "Kalkulator Umur":
    st.subheader("⏳ Hitung Umur Anda")
    nama = st.text_input("Masukkan Nama Anda:", placeholder="Nama Anda...")
    tanggal_lahir = st.date_input("Masukkan Tanggal Lahir Anda:")
    if st.button("Hitung Umur"):
        umur = date.today().year - tanggal_lahir.year
        st.success(f"🎉 Halo, {nama}! Anda berumur {umur} tahun.")
        st.snow()

# Halaman Galeri
elif menu == "Galeri":
    st.subheader("📸 Galeri Keren")
    st.write("Jelajahi koleksi gambar-gambar keren berikut:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/300x200?text=Gambar+1", caption="Gambar 1")
    with col2:
        st.image("https://via.placeholder.com/300x200?text=Gambar+2", caption="Gambar 2")
    with col3:
        st.image("https://via.placeholder.com/300x200?text=Gambar+3", caption="Gambar 3")

# Footer
st.markdown(
    """
    <div class="footer">
        Dibuat dengan 💖 oleh [Nama Anda] | © 2025 Aplikasi Keren
    </div>
    """, 
    unsafe_allow_html=True
)
