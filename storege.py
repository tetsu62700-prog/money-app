import json
import os

FILE_NAME = "money_records.json"

def load_records():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = json.load(file)

            print("保存データを読み込みました。")
            return records

    else:
        print("保存したデータがないため、新しく開始します。")
        return []

def save_records(records):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)

    print("保存しました。")

