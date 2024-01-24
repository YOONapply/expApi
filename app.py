from flask import Flask, render_template, request, redirect
import json
import funtionJson as fJ
import subprocess

app = Flask(__name__)

@app.route("/success", methods=['POST'])
def success():
    if request.method == "POST":
        name = request.form.get('name')
        stuId = request.form.get('stuId')
        schedule = request.form.get('schedule')
        email = request.form.get('email')
        stuM = request.form.get('stuM', default="입력 없음")
        snsId = request.form.get('snsId', default="입력 없음")

        print(f"{name} {stuId} {snsId} {email} {schedule} {stuM}")

        result = {
            "name": name,
            "stuId": stuId,
            "snsId": snsId,
            "email": email,
            "schedule": schedule,
            "stuM": stuM
        }

        fJ.userDataDump(result)

        script_path = "excel.py"
        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"오류 발생: {e}")

        # 외부 도메인으로의 리다이렉션
        return redirect("https://expschoolclub.netlify.app/success")

if __name__ == '__main__':
    app.run(debug=True)
