def isPolidrom(string):
    while len(string) > 1:
        if string[0] != string[-1]:
            return False
        else:
            string = string[1:-1]
    return True


print(isPolidrom("rtyfdytr"))


def countWords(string):
    counter = 1
    for i in range(len(string)):
        if string[i] == " ":
            counter += 1
    return counter


print(countWords("gsjkn jhim fnmo k"))


def acronyms(string):
    strNew = ""
    if string[0] != " ":
        strNew = string[0]
    for i in range(len(string)):
        if string[i] == " ":
            if len(string) > i + 1:
                strNew += string[i + 1]
    return strNew
print(acronyms("ahuvi storch .  yhudit"))
print("---lesson 5-----------------------------")
import os


def show_menu():
    print("\n--- מערכת לניהול קבצים ותיקיות ---")
    print("1. יצירת תיקייה חדשה")
    print("2. מחיקת תיקייה קיימת (אם היא ריקה)")
    print("3. יצירת קובץ חדש בתיקייה")
    print("4. כתיבה לקובץ או הוספת תוכן לקובץ קיים")
    print("5. מחיקת קובץ")
    print("6. רשימת כל הקבצים והתיקיות בתיקייה")
    print("7. הצגת נתיב מלא של תיקייה נוכחית")
    print("0. יציאה")


def main():
  while True:
    show_menu()
    choice = input("בחר אפשרות: ")

    if choice == "1":
      path = input("הכנס את נתיב התיקייה שברצונך ליצור: ")
      try:
        os.makedirs(path, exist_ok=True)
        print(
            "התיקייה נוצרה בהצלחה (או כבר קיימת בנתיב זה)."
            if os.path.exists(path)
            else "שגיאה ביצירת התיקייה."

        )
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "2":
      path = input("הכנס את נתיב התיקייה למחיקה: ")
      try:
        if os.path.exists(path) and os.path.isdir(path):
          # בדיקה האם התיקייה ריקה
          if not os.listdir(path):
            os.rmdir(path)
            print("התיקייה נמחקה בהצלחה.")
          else:
            print("שגיאה: התיקייה אינה ריקה ולכן לא ניתן למחוק אותה.")
        else:
          print("שגיאה: התיקייה אינה קיימת או שאינה תיקייה חוקית.")
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "3":
      path = input("הכנס את נתיב הקובץ ליצירה (כולל שם הקובץ): ")
      try:
        # פתיחת הקובץ במצב כתיבה יוצרת אותו אם אינו קיים
        with open(path, "w", encoding="utf-8") as f:
          pass
        print("הקובץ נוצר בהצלחה.")
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "4":
      path = input("הכנס את נתיב הקובץ: ")
      print("בחר מצב כתיבה:")
      print("1. דריסת תוכן קיים")
      print("2. הוספת תוכן בסוף הקובץ")
      mode_choice = input("בחירה (1 או 2): ")

      mode = "w" if mode_choice == "1" else "a"
      content = input("הכנס את הטקסט שברצונך לכתוב: ")

      try:
        with open(path, mode, encoding="utf-8") as f:
          f.write(content + "\n")
        print("התוכן נכתב בהצלחה.")
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "5":
      path = input("הכנס את נתיב הקובץ למחיקה: ")
      try:
        if os.path.exists(path) and os.path.isfile(path):
          os.remove(path)
          print("הקובץ נמחק בהצלחה.")
        else:
          print("שגיאה: הקובץ אינו קיים או שאינו קובץ תקין.")
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "6":
      path = input("הכנס את נתיב התיקייה להצגה (או השאר ריק לנוכחית): ")
      if not path:
        path = "."
      try:
        if os.path.exists(path) and os.path.isdir(path):
          items = os.listdir(path)
          print(f"תוכן התיקייה '{path}':")
          for item in items:
            print(f" - {item}")
        else:
          print("שגיאה: התיקייה לא נמצאה.")
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "7":
      path = input(
          "הכנס את שם או נתיב התיקייה שברצונך לדעת את נתיבה המלא (או השאר ריק"
          " לנוכחית): "
      )
      if not path:
        path = "."
      try:
        abs_path = os.path.abspath(path)
        print(f"הנתיב המלא הוא: {abs_path}")
      except Exception as e:
        print(f"אירעה שגיאה: {e}")

    elif choice == "0":
      print("להתראות!")
      break
    else:
      print("בחירה לא שגויה, נסה שנית.")


if __name__ == "__main__":
  main()