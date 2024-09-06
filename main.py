from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/get_date")
def get_today_date():
    today = datetime.date.today()
    return {"date": today.strftime('%d-%m-%Y')}


if __name__ == "__main__":
    today_date = get_today_date()
