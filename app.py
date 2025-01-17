import streamlit as st
from PIL import Image

# Konfigurasi Halaman
st.set_page_config(
    page_title="Portofolio Keren",
    page_icon="💼",
    layout="wide",
)

# CSS untuk Tampilan Kustom
st.markdown("""
    <style>
        body {
            background: #1a1a1d;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4, h5 {
            color: #FFD700;
        }
        .main-container {
            background: #282828;
            border-radius: 10px;
            padding: 20px;
            color: white;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
        }
        .stButton > button {
            background-color: #FFD700;
            color: black;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton > button:hover {
            background-color: #FFA500;
            color: white;
        }
        .footer {
            text-align: center;
            color: #BBB;
            font-size: 14px;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>💼 Portofolio Saya 💼</h1>", unsafe_allow_html=True)
st.write("---")

# Tentang Saya
st.header("📋 Tentang Saya")
col1, col2 = st.columns([1, 2])
with col1:
    profile_img = "https://i.pinimg.com/736x/48/49/ba/4849ba2ea6517f805785071120cccc08.jpg"  # Ganti dengan URL atau path gambar lokal
    st.image(profile_img, caption="Foto Profil", width=150)
with col2:
    st.markdown("""
    Hai, nama saya **Player**.  
    Saya seorang **Software Engineer** yang gemar membuat aplikasi modern,  
    memecahkan masalah dengan teknologi, dan mengeksplorasi dunia pemrograman.  
    """)
st.write("---")

# Keahlian
st.header("🛠️ Keahlian")
st.markdown("""
- **Bahasa Pemrograman**: Python, JavaScript, C++
- **Frameworks**: Django, React.js, Flask
- **Tools**: Docker, Kubernetes, Git
- **Database**: MySQL, PostgreSQL, MongoDB
""")
st.write("---")

# Proyek
st.header("📂 Proyek Saya")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://i.pinimg.com/736x/24/7d/13/247d1354f2ce6f77c524c67a162aa4c6.jpg", caption="Proyek 1", use_container_width=True)
    st.markdown("**Deskripsi:** Seorang programmer web bertanggung jawab untuk merancang, mengembangkan, dan memelihara aplikasi serta situs web. Mereka memiliki keterampilan dalam bahasa pemrograman web seperti HTML, CSS, JavaScript, dan framework seperti React, Django, atau Flask. Programmer web memastikan situs web berfungsi dengan baik, responsif, dan memiliki pengalaman pengguna yang menyenangkan.")
    st.button("Lihat Proyek", key="proyek1")
with col2:
    st.image("https://i.pinimg.com/736x/6e/fa/87/6efa87d55f80267b24c8e7d951e61d14.jpg", caption="Proyek 2", use_container_width=True)
    st.markdown("**Deskripsi:** Seorang programmer C++ mengembangkan perangkat lunak dengan menggunakan bahasa pemrograman C++, yang dikenal karena kemampuannya dalam menangani aplikasi yang membutuhkan performa tinggi, seperti permainan, sistem operasi, dan perangkat lunak yang mengelola sumber daya perangkat keras. Mereka menguasai konsep seperti manajemen memori, pengolahan data tingkat rendah, dan pengoptimalan kode.")
    st.button("Lihat Proyek", key="proyek2")
with col3:
    st.image("https://i.pinimg.com/736x/0f/89/39/0f8939fc7bda5c155dde08127e452b8d.jpg", caption="Proyek 3", use_container_width=True)
    st.markdown("**Deskripsi:** Seorang profesional multimedia menggabungkan berbagai bentuk media, seperti gambar, video, audio, dan animasi, untuk menciptakan pengalaman digital yang menarik. Mereka sering bekerja dengan perangkat lunak desain grafis dan animasi seperti Adobe Photoshop, Premiere Pro, dan After Effects untuk menghasilkan konten kreatif untuk website, video game, iklan, dan media sosial.")
    st.button("Lihat Proyek", key="proyek3")
st.write("---")

# Kontak
st.header("📞 Kontak")
st.markdown("""
- **Email**: johndoe@example.com
- **LinkedIn**: [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)
- **GitHub**: [github.com/johndoe](https://github.com/johndoe)
""")
st.write("---")

# Footer
st.markdown(
    """
    <div class="footer">
        Dibuat dengan 💖 oleh John Doe | © 2025
    </div>
    """, 
    unsafe_allow_html=True
)
