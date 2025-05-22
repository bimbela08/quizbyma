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

# ==== Inisialisasi State ====
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.answered = False
    st.session_state.answer_input = ""

def reset_timer():
    st.session_state.start_time = time.time()
    st.session_state.answered = False
    st.session_state.answer_input = ""

# ==== Fungsi ====
def show_question():
    question_data = questions[st.session_state.current_question]
    remaining_time = max(0, 20 - int(time.time() - st.session_state.start_time))

    st.markdown(f"### Pertanyaan {st.session_state.current_question + 1}")
    st.write(question_data["question"])
    st.info(f"Sisa waktu: {remaining_time} detik")

    if not st.session_state.answered and remaining_time > 0:
        st.session_state.answer_input = st.text_input("Jawaban Anda:", value=st.session_state.answer_input)
        if st.button("Kirim Jawaban"):
            check_answer(st.session_state.answer_input.strip().lower())
    elif not st.session_state.answered and remaining_time == 0:
        st.warning("⏰ Waktu habis! Pertanyaan akan lanjut otomatis.")
        next_question()
    elif st.session_state.answered:
        if st.button("Lanjut ke Pertanyaan Berikutnya"):
            next_question()

def check_answer(user_answer):
    correct = questions[st.session_state.current_question]["answer"]
    if user_answer == correct:
        st.success("✅ Jawaban benar!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Jawaban salah. Jawaban yang benar: **{correct}**")
    st.session_state.answered = True

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

# ==== Tampilan Utama ====
st.title("🎓 Kuis SMAN 1 Bangkalan")

if st.session_state.current_question < len(questions):
    show_question()
else:
    show_result()
