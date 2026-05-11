from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/calc-bmi")
def calc_bmi():
    height = request.args.get("height")
    weight = request.args.get("weight")

    result = get_bmi(height, weight)

    return render_template("bmi.html", result=result, height=height, weight=weight)


@app.route("/bmi")
def bmi():
    return render_template("bmi.html", result=None)


@app.route("/")
def index():
    stocks = [
        {"分類": "日經指數", "指數": "22,920.30"},
        {"分類": "韓國綜合", "指數": "2,304.59"},
        {"分類": "香港恆生", "指數": "25,083.71"},
        {"分類": "上海綜合", "指數": "3,380.68"},
    ]

    for stock in stocks:
        print(stock["分類"], stock["指數"])

    print(datetime.now())

    return render_template(
        "index.html", name="jerry", stocks=stocks, time=datetime.now()
    )


def get_bmi(height, weight):
    try:
        # 參數都為字串
        bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)
        if bmi < 18.5:
            category = "過輕"
        elif bmi < 24:
            category = "正常"
        elif bmi < 27:
            category = "略重"
        else:
            category = "肥胖"

        return {"success": True, "bmi": bmi, "category": category}

    except Exception as e:
        return {"success": False, "bmi": None, "category": None}


# 傳遞參數方式
@app.route("/hello/<name>/<height>/<weight>")
def hello(name, height, weight):
    result = get_bmi(height, weight)

    if result["success"]:
        return f"Welcome {name} BMI:{result['bmi']:.2f} 評語:{result['category']}"
    else:
        return "輸入不正確"


if __name__ == "__main__":
    app.run(debug=True)
