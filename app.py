import tkinter as tk
from tkinter import messagebox
import random

# danh sách từ vựng  
vocabulary = {
    "Hello": "Xin chào",
    "Goodbye": "Tạm biệt",
    "Thank you": "Cảm ơn",
    "Yes": "Có",
    "No": "Không",
    "Please": "Vui lòng",
    "Sorry": "Xin lỗi",
    "Love": "Yêu",
    "Friend": "Bạn",
    "Family": "Gia đình",
    "Food": "Thức ăn",
    "Water": "Nước",
    "Happy": "Hạnh phúc",
    "Sad": "Buồn",
    "Computer": "Máy tính",
    "Book": "Sách",
    "School": "Trường học",
    "Teacher": "Giáo viên",
    "Student": "Học sinh",
    "Home": "Nhà",
}

class VocabularyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Học Từ Vựng")
        self.root.geometry("450x600") # kích thước cửa sổ ứng dụng
        self.root.configure(bg="#f0f0f0") # màu nền của background

        # khung tiêu đề
        # xây dựng giao diện người dùng bằng Tkinter
        self.title_frame = tk.Frame(root, bg="#2196F3")
        self.title_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.title_frame, text="Học Từ Vựng", font=("Arial", 24), bg="#2196F3", fg="white")
        self.title_label.pack(pady=20)

        # khung nội dung
        self.content_frame = tk.Frame(root, bg="#f0f0f0")
        self.content_frame.pack(pady=20)

        self.word_label = tk.Label(self.content_frame, text="", font=("Arial", 20), bg="#f0f0f0")
        self.word_label.pack(pady=10)

        self.meaning_entry = tk.Entry(self.content_frame, font=("Arial", 14), width=20)
        self.meaning_entry.pack(pady=10)

        # nút kiểm tra
        self.check_button = tk.Button(self.content_frame, text="Kiểm Tra", command=self.check_meaning, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
        self.check_button.pack(pady=10)

        # nút tiếp theo
        self.next_button = tk.Button(self.content_frame, text="Từ Tiếp Theo", command=self.next_word, bg="#2196F3", fg="white", font=("Arial", 12), width=15)
        self.next_button.pack(pady=10)

        #  điểm
        self.score_label = tk.Label(self.content_frame, text="Điểm: 0", font=("Arial", 16), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # thêm từ vựng
        self.add_frame = tk.Frame(root, bg="#f0f0f0")
        self.add_frame.pack(pady=20)

        self.new_word_entry = tk.Entry(self.add_frame, font=("Arial", 14), width=15)
        self.new_word_entry.pack(side=tk.LEFT, padx=5)

        self.new_meaning_entry = tk.Entry(self.add_frame, font=("Arial", 14), width=15)
        self.new_meaning_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.add_frame, text="Thêm Từ Vựng", command=self.add_vocabulary, bg="#FF9800", fg="white", font=("Arial", 12))
        self.add_button.pack(side=tk.LEFT, padx=5)

        # nút sửa từ vựng
        self.edit_button = tk.Button(self.add_frame, text="Sửa Từ Vựng", command=self.edit_vocabulary, bg="#2196F3", fg="white", font=("Arial", 12))
        self.edit_button.pack(side=tk.LEFT, padx=5)

        # nút xóa từ vựng
        self.delete_button = tk.Button(self.add_frame, text="Xóa Từ Vựng", command=self.delete_vocabulary, bg="#F44336", fg="white", font=("Arial", 12))
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # khung tra cứu từ vựng
        self.lookup_frame = tk.Frame(root, bg="#f0f0f0")
        self.lookup_frame.pack(pady=20)

        self.lookup_entry = tk.Entry(self.lookup_frame, font=("Arial", 14), width=15)
        self.lookup_entry.pack(side=tk.LEFT, padx=5)

        self.lookup_button = tk.Button(self.lookup_frame, text="Tra Cứu", command=self.lookup_vocabulary, bg="#2196F3", fg="white", font=("Arial", 12))
        self.lookup_button.pack(side=tk.LEFT, padx=5)

        self.score = 0
        self.current_word = ""

        self.next_word()

    def next_word(self):
        self.current_word = random.choice(list(vocabulary.keys()))
        self.word_label.config(text=self.current_word)
        self.meaning_entry.delete(0, tk.END)

    def check_meaning(self):
        user_input = self.meaning_entry.get().strip()
        correct_answer = vocabulary[self.current_word]

        if user_input.lower() == correct_answer.lower():  # Kiểm tra không phân biệt chữ hoa thường
            self.score += 1
            messagebox.showinfo("Kết Quả", f"Đúng rồi! Điểm của bạn: {self.score}", icon='info')
        else:
            messagebox.showerror("Kết Quả", f"Sai rồi! Đáp án đúng là: {correct_answer}", icon='error')

        self.score_label.config(text="Điểm: " + str(self.score))
        self.next_word()

    def add_vocabulary(self):
        new_word = self.new_word_entry.get().strip()
        new_meaning = self.new_meaning_entry.get().strip()

        if new_word and new_meaning:
            vocabulary[new_word] = new_meaning  # Thêm từ vựng mới vào từ điển
            messagebox.showinfo("Thông báo", "Từ vựng đã được thêm thành công!", icon='info')
            self.new_word_entry.delete(0, tk.END)
            self.new_meaning_entry.delete(0, tk.END)
            self.next_word()  # Gọi lại để hiển thị từ mới đã thêm
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập cả từ và nghĩa!", icon='warning')

    def edit_vocabulary(self):
        new_meaning = self.new_meaning_entry.get().strip()

        if self.current_word in vocabulary and new_meaning:
            vocabulary[self.current_word] = new_meaning  # Cập nhật nghĩa từ vựng
            messagebox.showinfo("Thông báo", "Từ vựng đã được sửa thành công!", icon='info')
            self.new_meaning_entry.delete(0, tk.END)
            self.next_word()  # Cập nhật từ mới
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập nghĩa mới!", icon='warning')

    def delete_vocabulary(self):
        if self.current_word in vocabulary:
            del vocabulary[self.current_word]  # Xóa từ vựng
            messagebox.showinfo("Thông báo", "Từ vựng đã được xóa thành công!", icon='info')
            self.next_word()  # Chuyển đến từ mới
        else:
            messagebox.showwarning("Cảnh báo", "Không có từ nào để xóa!", icon='warning')

    def lookup_vocabulary(self):
        lookup_word = self.lookup_entry.get().strip()

        if lookup_word in vocabulary:
            meaning = vocabulary[lookup_word]
            messagebox.showinfo("Kết Quả Tra Cứu", f"{lookup_word}: {meaning}", icon='info')
        else:
            messagebox.showerror("Kết Quả Tra Cứu", "Không tìm thấy từ vựng này!", icon='error')

# Khởi tạo ứng dụng
root = tk.Tk()
app = VocabularyApp(root)
root.mainloop()
