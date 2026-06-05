from datetime import datetime
from storage import save_records
import matplotlib.pyplot as plt

def sort_by_date(records):
    records.sort(key=lambda record: record["date"])

def input_date():
    date_text = input("日付:")
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        print("日付は YYYY-MM-DDの形式で入力してください")
        return None
    return date_text

def input_int(records):
    try:
        number = int(input("編集する番号を入力してください。"))
    except ValueError:
        print("Please input NUMBER")
        return None
    
    if number < 1 or number > len(records):
        print(f"0<number<{len(records)}")   
        return None
    
    return number

def input_record_type():
    record_type = input("収入or支出:")
    if record_type != "収入" and record_type != "支出":
        print("Please input:収入or支出")
        return  None
    return record_type

def input_amount():
    try:
        amount =int(input("金額:"))
    except ValueError:
        print("Please input NUMBER")
        return None
    
    if amount < 0:
        print("金額は0円以上で入力してください")
        return None
    return amount

def input_record_data():
    date = input_date()
    if date is None:
        return None

    record_type = input_record_type()
    if record_type is None:
        return None

    category = input("カテゴリ＝:")

    amount = input_amount()
    if amount is None:
        return None
    
    memo = input("メモ:")

    record = {
        "date":date,
        "record_type":record_type,
        "category":category,
        "amount":amount,
        "memo":memo
    }
    return record

def input_record_data_for_edit(old_record):
    print("新しい内容を入力してください。変更しない場合はEnterを押してください。")

    date = input(f"日付(現在:{old_record['date']}):")
    if date == "":
        date = old_record["date"]
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("日付は YYYY-MM-DDの形式で入力してください")
            return None
    
    record_type = input(f"種類(現在:{old_record['record_type']}):")
    if record_type == "":
        record_type = old_record["record_type"]

    category = input(f"カテゴリ(現在:{old_record['category']}):")
    if category == "":
        category = old_record["category"]

    amount_text = input(f"金額(現在:{old_record['amount']}):")
    if amount_text == "":
        amount_text = old_record["amount"]
    else:
        try:
            amount = int(amount_text)
        except ValueError:
            print("Please input NUMBER")
            return None

        if amount < 0:
            print("金額は0円以上で入力してください。")
            return None

    memo = input(f"メモ(現在:{old_record['memo']}):")
    if memo == "":
        memo = old_record["memo"]

    new_record = {
        "date": date,
        "record_type": record_type,
        "category": category,
        "amount": amount,
        "memo": memo,
    }
    return new_record

def add_record(records):
    record = input_record_data()

    if record is None:
        return

    records.append(record)
    save_records(records)
    print("記録しました。")

def show_records(records):
    if len(records) == 0:
        print("Error")

    else:
        for i, record in enumerate(records, start=1):
            print(f"{i}.|{record['date']} | {record['record_type']} | {record['amount']}円 | {record['memo']}")

#   関数外から別の関数を持ってくるとき、()の中に関数を入れる->record_type
def show_total(records,record_type):
    total = 0

    for record in records:
        if record["record_type"] == record_type:
            total += record["amount"]

    print(f"{record_type}の合計 {total} 円")

def show_category_total(records):
    category_totals = {}

    for record in records:
        if record["record_type"] == "支出":
            category = record["category"]
            amount = record["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if len(category_totals) == 0:
        print("記録がありません。")
        return
    
    print("カテゴリ別支出")
    for category, total in category_totals.items():
        print(f"{category}:{total}円")

def show_monthly_total(records):
    month = input("年月を入力(2026-06):")

    income_total = 0
    expense_total = 0

    for record in records:
        if record["date"].startswith(month):
            if record["record_type"] == "収入":
                income_total += record["amount"]
            elif record["record_type"] =="支出":
                expense_total += record["amount"]
        
    profit = income_total - expense_total

    print()
    print(f"==={month} 月次損益計算===")
    print()
    print(f"売上高:     {income_total:,}円")
    print(f"費用合計:   {expense_total:,}円")
    print("-----------------------")

    if profit >= 0:
        print(f"当月純利益:     {profit:,}円")
    elif profit < 0:
        print(f"当月純損益:     {abs(profit):,}円")

def show_monthly_category_total(records):
    month = input("年月を入力してください。:")

    category_totals = {}

    for record in records:
        if record["date"].startswith(month) and record["record_type"] == "支出":
            category = record["category"]
            amount =record["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if len(category_totals) == 0:
        print(f"{month} の支出記録がありません。")
        return
    
    print()
    print(f"==== {month} のカテゴリ別支出 ====")

    for category, total in category_totals.items():
        print(f"{category}:{total:,}円")

def show_monthly_category_graph(recoreds):
    month = input("年月を入力してください:")

    category_totals = {}

    for record in recoreds:
        if record["date"].startswith(month) and record["record_type"]== "支出":
            category = record["category"]
            amount = record["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    if len(category_totals) == 0:
        print(f"{month}の支出記録がありません")
        return
    
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts)
    plt.title(f"{month}のカテゴリ別支出")
    plt.xlabel("カテゴリ")
    plt.ylabel("金額(円)")
    plt.tight_layout()
    plt.show()

def delete_record(records):
    if len(records) == 0:
        print("I can't delete your records.")
        return
    
    show_records()
    
    number = input_int()

    if number is None:
        return
    
    delete_record = records.pop(number-1)
    print(f"{delete_record['date']} | {delete_record['category']} | {delete_record['amount']}円 の記録を削除しました。")

def edit_record(records):
    if len(records) == 0:
        print("I can't edit your record")
        return
    
    show_records()

    number = input_int()
    if number is None:
        return
    
    record = records[number-1]

    print("現在の内容")
    print(f"日付:{record['date']}")
    print(f"種類:{record['record_type']}")
    print(f"カテゴリ:{record['category']}")
    print(f"金額:{record['amount']}")
    print(f"メモ:{record['memo']}")

    new_record = input_record_data_for_edit(record)
    if new_record is None:
        return

    records[number-1] = new_record

    save_records(records)
    print("編集しました")
