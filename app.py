import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    name = '김땡땡'
    lotto =  [16, 18, 22, 43, 32, 11]

    def generate_lotto_numbers():
        numbers = random.sample(range(1,46),6)
        return sorted(numbers)
    random_lotto = generate_lotto_numbers()

    # 두 개의 리스트 생성
    list1 = [1, 2, 2, 3, 4, 5]
    list2 = [2, 2, 3, 4, 4, 5]

    # 두 리스트에서 공통으로 나타나는 요소를 저장할 리스트 생성
    common_elements = []

    # list1의 요소를 순회하면서 list2에도 있는지 확인
    for item in lotto:
        if item in random_lotto:
            common_elements.append(item)

    # 공통 요소 출력
    print("공통 요소:", common_elements)
    print("공통 요소 개수:", len(common_elements))

    context = {
        "name" : name,
        "lotto" : lotto,
        "random_lotto": random_lotto,
        "common_count" : len(common_elements),
    }

    return render_template('index.html', data = context)

@app.route('/mypage')
def mypage():
    return 'This is Mypage!'

if __name__ == '__main__':  
    app.run(debug=True)