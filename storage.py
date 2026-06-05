import json
import os
import csv

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

def export_csv(records):
    CSV_FILE_NAME = "money_records.csv"

    with open(CSV_FILE_NAME, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["date","record_type","category","amount","memo"])

        for record in records:
            writer.writerow([
                record["date"],
                record["record_type"],
                record["category"],
                record["amount"],
                record["memo"],
            ])
    print(f"{CSV_FILE_NAME}に出力しました。")