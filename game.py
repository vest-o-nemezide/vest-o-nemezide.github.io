from js import document  # type: ignore # Импортируем возможности JS для взаимодействия с HTML
from pyodide.ffi import create_proxy # type: ignore

# Переменная для отслеживания текущей сцены
game_state = {
    'stage': 'start'
}

def display_text(text):
    output = document.getElementById("game-output")
    output.innerHTML = text  # Прямо используем текст с HTML

def handle_choice(choice):
    if game_state['stage'] == 'start':
        if choice == 1:
            game_state['stage'] = 'forest'
            display_text(
                "Вы пошли по тропе с красивым лесом. На вас напали гоблины:<br>"
                "1) Сразиться с ними мечом<br>"
                "2) Убежать за помощью<br>"
                "Выберите 1 или 2."
            )
        elif choice == 2:
            game_state['stage'] = 'snake_pit'
            display_text(
                "Вы пошли по тропе 2 и упали в яму со змеями:<br>"
                "Ваши действия?<br>"
                "1) Оставаться неподвижным<br>"
                "2) Попробовать вылезти<br>"
                "Выберите 1 или 2."
            )
        elif choice == 3:
            display_text("Вы пошли по странной тропе... Вас скушали волки. Игра окончена!")
            game_state['stage'] = 'end'
        else:
            display_text("Пожалуйста, выберите 1, 2 или 3.")
    
    elif game_state['stage'] == 'forest':
        if choice == 1:
            display_text("Ваш меч не помог. Вы погибли. Игра окончена!")
            game_state['stage'] = 'end'
        elif choice == 2:
            display_text("Поздравляем! Это был единственный путь к спасению. Ждите 2 часть!")
            game_state['stage'] = 'end'
        else:
            display_text("Пожалуйста, выберите 1 или 2.")
    
    elif game_state['stage'] == 'snake_pit':
        if choice == 1:
            display_text("Это сработало! Вы выжили. Ждите 2 часть!")
            game_state['stage'] = 'end'
        elif choice == 2:
            display_text("Вы погибли. Игра окончена!")
            game_state['stage'] = 'end'
        else:
            display_text("Пожалуйста, выберите 1 или 2.")
    
    elif game_state['stage'] == 'end':
        display_text("Игра завершена. Спасибо за игру!")

# Начальное сообщение
display_text(
    "Привет, ты видишь перед собой 3 тропы...<br>"
    "в какую лучше зайти?<br><br>"
    "Выберите 1, 2 или 3."
)

# Прокси-обработчики для кнопок
button1_proxy = create_proxy(lambda e: handle_choice(1))
button2_proxy = create_proxy(lambda e: handle_choice(2))
button3_proxy = create_proxy(lambda e: handle_choice(3))

# Привязка кнопок к функциям
document.getElementById("button1").addEventListener("click", button1_proxy)
document.getElementById("button2").addEventListener("click", button2_proxy)
document.getElementById("button3").addEventListener("click", button3_proxy)