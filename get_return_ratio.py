import csv

def func_analysis(f_in, f_out):
    with open(f_in, encoding = "utf-8") as finput, open(f_out, "w", newline = "", encoding = "utf-8") as foutput:
        reader = csv.DictReader(finput)
        writer = csv.DictWriter(foutput, fieldnames = ["購入回数", "総購入金額", "的中回数", "総払戻金額", "回収率"])
        writer.writeheader()
        buycount = 0
        buymoney = 0
        hitcount = 0
        returnmoney = 0
        
        for row in reader:
            if not row ["購入金額"]:
                continue
            buycount += 1
            buy = int(row["購入金額"].replace("¥", ""))
            buymoney += buy
            
            if row["的中"] == "TRUE":
                hitcount += 1
                payback = int(row["払い戻し"].replace("¥", ""))
                returnmoney += payback

        returnratio = 100 * returnmoney / buymoney

        writer.writerow({
            "購入回数": buycount,
            "総購入金額": buymoney,
            "的中回数": hitcount,
            "総払戻金額": returnmoney,
            "回収率": returnratio
        })

func_analysis("sample/競馬-結果リスト.csv", "results/分析結果.csv")