import random
from fastapi import FastAPI

app = FastAPI()

lucky_messages = [
    "오늘은 뜻밖의 행운이 찾아올 거예요! 🍀",
    "잠시 휴식을 취하면 좋은 아이디어가 떠오를 겁니다. ☕",
    "가까운 사람에게 따뜻한 말을 건네보세요. 💬",
    "당신의 노력이 곧 결실을 맺을 것입니다. 🍎",
    "오늘 점심은 정말 맛있는 걸 드세요! 🍔",
    "지금 하고 있는 고민이 곧 해결될 거예요. ✨",
    "버그 없는 쾌적한 코딩이 기다리고 있습니다! 🐛🚫",
    "하늘을 한번 올려다보세요. 기분이 좋아질 거예요. ☁️",
    "자신을 믿으세요! 당신은 정말 잘하고 있습니다. 💪",
    "작은 성취들이 모여 큰 성공이 될 것입니다. 📈"
]

@app.get("/")
def read_root():
    return {"status": "Service is running", "service_name": "Lucky API"}

@app.get("/fortune")
def get_fortune():
    selected_message = random.choice(lucky_messages)
    return {
        "message": selected_message,
        "lucky_number": random.randint(1, 100)
    }

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"안녕하세요, {name}님! 오늘도 화이팅하세요."}