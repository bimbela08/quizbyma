import streamlit as st
import time

# ==== Pertanyaan ====
questions = [
    {"question": "Tahun berapa SMAN 1 Bangkalan didirikan?", "answer": "1962"},
    {"question": "Ada berapa seluruh jumlah kelas di Smansa?", "answer": "31"},
    {"question": "Apa nama ekskul di sana yang berhubungan dengan kesehatan? (huruf kecil)", "answer": "pmr"},
    {"question": "Apa nama/sebutan supporter Smansaba? (huruf kecil)", "answer": "settong mania"},
    {"question": "Siapa ketua umum Komunitas MPS SMAN 1 Bangkalan? (nama panggilan & huruf kecil)", "answer": "bima"}
]

# ==== Inisialisasi ====
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.show_result = False
    st.session_state.show_feedback = False
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

# ==== Fungsi ====
def reset_for_next_question():
    st.session_state.start_time = time.time()
    st.session_state.show_feedback = False
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

# ==== Judul ====
st.title("🎓 Kuis SMAN 1 Bangkalan")

if st.session_state.show_result:
    st.success("🎉 Kuis Selesai!")
    st.write(f"Kamu menjawab **{st.session_state.score} dari {len(questions)}** dengan benar.")
    st.write(f"**Nilai akhir: {(st.session_state.score / len(questions)) * 100:.2f}**")
else:
    q = questions[st.session_state.index]
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, 20 - elapsed)

    st.markdown(f"### Pertanyaan {st.session_state.index + 1}")
    st.write(q["question"])
    st.info(f"Sisa waktu: {remaining} detik")

    if not st.session_state.show_feedback:
        st.session_state.user_answer = st.text_input("Jawaban kamu:", value=st.session_state.user_answer)
        if st.button("Kirim Jawaban") or remaining == 0:
            correct = q["answer"]
            if st.session_state.user_answer.lower().strip() == correct:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Jawaban benar!"
            else:
                st.session_state.feedback = f"❌ Salah. Jawaban yang benar: **{correct}**"
            st.session_state.show_feedback = True
    else:
        st.markdown(st.session_state.feedback)
        if st.button("Lanjut ke pertanyaan berikutnya"):
            st.session_state.index += 1
            if st.session_state.index >= len(questions):
                st.session_state.show_result = True
            else:
                reset_for_next_question()


