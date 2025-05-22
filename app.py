import streamlit as st
import time
import random

# === WARNA TEMA ===
st.markdown("""
    <style>
    .stApp {
        background-color: #fffbe6;
    }
    .question {
        background-color: #fff176;
        padding: 15px;
        border-radius: 10px;
        color: black;
    }
    .timer {
        font-size: 24px;
        font-weight: bold;
        color: #e65100;
    }
    </style>
""", unsafe_allow_html=True)

# === PERTANYAAN ===
original_questions = [
    {"question": "Tahun berapa SMAN 1 Bangkalan didirikan?", "answer": "1962"},
    {"question": "Ada berapa seluruh jumlah kelas di Smansa?", "answer": "31"},
    {"question": "Apa nama ekskul di sana yang berhubungan dengan kesehatan? (huruf kecil)", "answer": "pmr"},
    {"question": "Apa nama/sebutan supporter Smansaba? (huruf kecil)", "answer": "settong mania"},
    {"question": "Siapa ketua umum Komunitas MPS SMAN 1 Bangkalan? (nama panggilan & huruf kecil)", "answer": "bima"}
]

# === INISIALISASI STATE ===
if "shuffled" not in st.session_state:
    st.session_state.shuffled = random.sample(original_questions, len(original_questions))
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.show_result = False
    st.session_state.show_feedback = False
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

# === FUNGSI ===
def reset_for_next():
    st.session_state.start_time = time.time()
    st.session_state.show_feedback = False
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

# === TAMPILAN UTAMA ===
st.title("🎓 Kuis SMAN 1 Bangkalan")
st.markdown("**Tema: Kuning - Putih | Soal Acak | Timer 20 Detik**")

if st.session_state.show_result:
    st.success("🎉 Kuis Selesai!")
    st.write(f"Kamu menjawab **{st.session_state.score} dari {len(st.session_state.shuffled)}** dengan benar.")
    st.write(f"**Nilai akhir: {(st.session_state.score / len(st.session_state.shuffled)) * 100:.2f}**")
else:
    q = st.session_state.shuffled[st.session_state.index]
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, 20 - elapsed)

    st.markdown(f"<div class='question'><b>Pertanyaan {st.session_state.index + 1}:</b><br>{q['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='timer'>Sisa waktu: {remaining} detik</div>", unsafe_allow_html=True)

    if not st.session_state.show_feedback and remaining > 0:
        st.session_state.user_answer = st.text_input("Jawaban kamu:", value=st.session_state.user_answer)
        if st.button("Kirim Jawaban"):
            correct = q["answer"]
            if st.session_state.user_answer.lower().strip() == correct:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Jawaban benar!"
            else:
                st.session_state.feedback = f"❌ Salah. Jawaban yang benar: **{correct}**"
            st.session_state.show_feedback = True
    elif not st.session_state.show_feedback and remaining == 0:
        st.warning("⏰ Waktu habis! Lanjut ke soal berikutnya.")
        st.session_state.feedback = f"❌ Waktu habis. Jawaban: **{q['answer']}**"
        st.session_state.show_feedback = True

    if st.session_state.show_feedback:
        st.markdown(st.session_state.feedback)
        if st.button("Lanjut ke pertanyaan berikutnya"):
            st.session_state.index += 1
            if st.session_state.index >= len(st.session_state.shuffled):
                st.session_state.show_result = True
            else:
                reset_for_next()


