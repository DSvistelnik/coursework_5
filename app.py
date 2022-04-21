app = Flask(__name__)

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

arena =  ... # TODO инициализируем класс арены


@app.route("/")
def menu_page():
    # TODO рендерим главное меню (шаблон index.html)
    pass
