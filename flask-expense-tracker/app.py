from flask import Flask, render_template, url_for, request, redirect


app=Flask(__name__)

expenses=[]


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        name = request.form.get("expense_name")
        amount = float(request.form.get("amount_name"))
        expenses.append({"name": name, "amount": amount})
        return redirect(url_for("home"))

    total_amount = sum(expense["amount"] for expense in expenses)
    return render_template("index.html", expenses=expenses, total_amount=total_amount)


@app.route("/delete/<int:index>",methods=["POST"])
def delete_expense(index):
    if 0<=index<len(expenses):
        expenses.pop(index)
    return redirect(url_for("home"))


if __name__ =="__main__":
    app.run(debug=True)
