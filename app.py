import streamlit as st
import time

# ==== Pertanyaan dan Jawaban ====
questions = [
    {"question": "Tahun berapa SMAN 1 Bangkalan didirikan?", "answer": "1962"},
    {"question": "Ada berapa seluruh jumlah kelas di Smansa?", "answer": "31"},
    {"question": "Apa nama ekskul di sana yang berhubungan dengan kesehatan? (huruf kecil)", "answer": "pmr"},
    {"question": "Apa nama/sebutan supporter Smansaba? (huruf kecil)", "answer": "settong mania"},
    {"question": "Siapa ketua umum Komunitas MPS SMAN 1 Bangkalan? (nama panggilan & huruf kecil)", "answer": "bima"}
]

# ==== State (menyimpan data sesi) ====
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.answered = False

# ==== Fungsi ====
def reset_timer():
    st.session_state.start_time = time.time()
    st.session_state.answered = False

def show_question():
    q = questions[st.session_state.current_question]["question"]
    st.markdown(f"### Pertanyaan {st.session_state.current_question + 1}")
    st.markdown(q)

    remaining_time = max(0, 20 - int(time.time() - st.session_state.start_time))
    st.info(f"Sisa waktu: {remaining_time} detik")

    answer = st.text_input("Jawaban Anda:", key=f"answer_{st.session_state.current_question}")

    if remaining_time <= 0 and not st.session_state.answered:
        st.warning("⏰ Waktu habis! Pertanyaan akan lanjut otomatis.")
        next_question()
    elif st.button("Kirim Jawaban") and not st.session_state.answered:
        check_answer(answer.strip().lower())

def check_answer(user_answer):
    correct = questions[st.session_state.current_question]["answer"]
    if user_answer == correct:
        st.success("✅ Jawaban benar!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Jawaban salah. Yang benar: **{correct}**")
    st.session_state.answered = True
    if st.button("Lanjut"):
        next_question()

def next_question():
    st.session_state.current_question += 1
    if st.session_state.current_question >= len(questions):
        show_result()
    else:
        reset_timer()
        st.experimental_rerun()

def show_result():
    st.markdown("## 🎉 Kuis Selesai!")
    st.write(f"Kamu menjawab **{st.session_state.score} dari {len(questions)}** dengan benar.")
    st.write(f"**Nilai akhir: {(st.session_state.score / len(questions)) * 100:.2f}**")

# ==== Tampilan ====
st.title("🎓 Kuis SMAN 1 Bangkalan")
if st.session_state.current_question < len(questions):
    show_question()
else:
    show_result()
