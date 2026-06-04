from storage import load_records, save_records
from records import (
    sort_by_date,
    add_record,
    show_records,
    show_total,
    show_category_total,
    show_monthly_total,
    show_monthly_category_total,
    delete_record,
    edit_record,
)
from datetime import datetime
records = []

def show_memu():
    print()
    print("===家計簿===")
    print("1:記録を追加")
    print("2:記録一覧")
    print("3:支出合計")
    print("4:収入合計")
    print("5:カテゴリー別で見る")
    print("6:月別集計")
    print("7:月別カテゴリ支出で見る")
    print("8:記録を削除")
    print("9:記録を編集")
    print("10:保存")
    print("11:終了")


def main():
    global records
    records = load_records()
    sort_by_date()
    
    while True:
        show_memu()
        choice = input("番号を入力:")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            show_total(records,"支出")
        elif choice == "4":
            show_total(records,"収入")
        elif choice == "5":
            show_category_total(records)
        elif choice == "6":
            show_monthly_total(records)
        elif choice == "7":
            show_monthly_category_total(records)
        elif choice == "8":
            delete_record(records)
        elif choice == "9":
            edit_record(records)
        elif choice == "10":
            save_records(records)
        elif choice == "11":
            break
        else:
            save_records(records)
            print("Error Number")
        

main()