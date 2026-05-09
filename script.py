from turtle import *
import random
import time

screen = Screen()
screen.setup(width=1.0, height=1.0) 
screen.bgcolor("#121212")

screen.addshape("germ_pzkpfw_vi_ausf_b_tiger_iih.gif")
screen.addshape("ussr_t_44.gif")
screen.addshape("us_t34.gif")

screen.addshape("3f39d75886e7ab8a00bc4bf8422ccc313c83db26.gif")
screen.addshape("300px-MapLayout_Ground_Karelia.gif")
screen.addshape("300px-MapLayout_Domination_Sweden_ABRBSB.gif")

screen.addshape("ussr_is_2_1943.gif")
screen.addshape("germ_pzkpfw_v_ausf_a_panther.gif")
screen.addshape("us_m26_pershing.gif")
screen.addshape("it_l3_cc.gif")

game_cleared = False

tank_visual = Turtle()
tank_visual.penup()
tank_visual.goto(-250, -100)

minimap = Turtle()
minimap.penup()
minimap.goto(600, 350)
minimap.hideturtle()

enemy_visual = Turtle()
enemy_visual.penup()
enemy_visual.goto(250, 150)
enemy_visual.hideturtle()

pen = Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")


def write_text(message, y_offset=-400):
    pen.clear()
    pen.goto(0, y_offset)
    pen.write(message, align="center", font=("Arial", 20, "bold"))


def battle(player_tank, is_easter_egg=False):
    global game_cleared

    if is_easter_egg:
        enemy_name = "L3/33 CC (найсильніший)"
        enemy_img = "it_l3_cc.gif"
    else:
        balance_table = {
            "Tiger-2": ["IS-2", "M26 Pershing"],
            "T-44": ["Panther", "M26 Pershing"],
            "T34": ["IS-2", "Panther"]
        }
        enemies_images = {
            "IS-2": "ussr_is_2_1943.gif",
            "Panther": "germ_pzkpfw_v_ausf_a_panther.gif",
            "M26 Pershing": "us_m26_pershing.gif"
        }
        available_enemies = balance_table.get(player_tank, ["Panther"])
        enemy_name = random.choice(available_enemies)
        enemy_img = enemies_images[enemy_name]

    enemy_visual.shape(enemy_img)
    enemy_visual.showturtle()

    write_text(f"Ворог на точці: {enemy_name}!\nВаш танк: {player_tank}")
    time.sleep(2)

    enemy_criticals = 0
    is_stunned = False

    while True:
        action = screen.textinput("Бій", "1 - Постріл, 2 - Від'їхати")

        if action == "1":
            chance = random.randint(1, 100)

            if is_easter_egg:
                if chance == 100:
                    write_text("НЕМОЖЛИВО! Ви знищили L3! Ви — легенда!")
                    game_cleared = True
                    time.sleep(4)
                    break
                else:
                    write_text("РИКОШЕТ! Снаряд просто злякався броні L3!")
                    time.sleep(2)
            else:
                bonus = 15 if enemy_criticals > 0 else 0
                if chance <= (1 + bonus):
                    write_text(f"ВАНШОТ! {enemy_name} розірвало! Перемога!")
                    game_cleared = True
                    time.sleep(3)
                    break
                elif 2 <= chance <= 21:
                    enemy_criticals += 1
                    if enemy_criticals >= 2:
                        write_text("ДРУГИЙ КРИТ! Екіпаж ворога залишив машину!")
                        game_cleared = True
                        time.sleep(3)
                        break
                    crit_type = random.choice(["Guns", "Engine"])
                    if crit_type == "Guns":
                        write_text("КРИТ: Вибито казенник! Ворог не зможе стріляти!")
                        is_stunned = True
                    else:
                        write_text("КРИТ: Двигун пошкоджено! Ворог не зможе від'їхати!")
                    time.sleep(3)
                elif 22 <= chance <= (71 + bonus):
                    write_text("ВЛУЧЕННЯ!")
                    time.sleep(2)
                elif 72 <= chance <= 86:
                    write_text("НЕ ПРОБИВ!")
                    time.sleep(2)
                else:
                    if enemy_criticals > 0:
                        write_text("ВЛУЧЕННЯ (Ворог не зміг від'їхати)!")
                    else:
                        write_text("ПРОМАХ! Ворог зміг від'їхати!")
                    time.sleep(2)

            if is_stunned:
                write_text(f"{enemy_name} пошкоджений і не стріляє...")
                is_stunned = False
                time.sleep(2)
            else:
                write_text(f"{enemy_name} веде вогонь у відповідь...")
                time.sleep(1)

                hit_rate = 95 if is_easter_egg else (10 if enemy_criticals > 0 else 30)

                if random.random() * 100 <= hit_rate:
                    if is_easter_egg:
                        write_text("L3 споглянув на вас... ВАС РОЗІРВАЛО ВЩЕНТ!")
                    else:
                        write_text("ВАС ЗНИЩЕНО! Повернення в ангар...")
                    time.sleep(3)
                    break
                else:
                    write_text("ВОРОГ НЕ ПРОБИВ ВАС!")
                    time.sleep(2)

        elif action == "2" or action is None:
            write_text("Ви відступили. Бій завершено.")
            break

    enemy_visual.hideturtle()


def start_game():
    global game_cleared
    while True:
        my_tank_input = screen.textinput("Вибір танка", "Введіть: Tiger-2, T34, T-44")
        if not my_tank_input: break

        current_tank_name = ""

        if "Tiger" in my_tank_input:
            current_tank_name = "Tiger-2"
            tank_visual.shape("germ_pzkpfw_vi_ausf_b_tiger_iih.gif")
        elif "44" in my_tank_input:
            current_tank_name = "T-44"
            tank_visual.shape("ussr_t_44.gif")
        elif "34" in my_tank_input:
            current_tank_name = "T34"
            tank_visual.shape("us_t34.gif")
        else:
            current_tank_name = "T34"

        maps_data = {
            "Лінія Мажино": "3f39d75886e7ab8a00bc4bf8422ccc313c83db26.gif",
            "Карелія": "300px-MapLayout_Ground_Karelia.gif",
            "Швеція": "300px-MapLayout_Domination_Sweden_ABRBSB.gif"
        }

        current_map = random.choice(list(maps_data.keys()))
        map_gif = maps_data[current_map]

        minimap.shape(map_gif)
        minimap.showturtle()

        write_text(f"Матч знайдено!\nКарта: {current_map}")
        time.sleep(2)

        points = "A, B, C"
        if game_cleared:
            points += ", D"

        point = screen.textinput("Точка", f"На яку точку їхати? ({points}):")

        if point and point.strip().upper() == "D":
            battle(current_tank_name, is_easter_egg=True)
        else:
            battle(current_tank_name, is_easter_egg=False)

        again = screen.textinput("Гра", "Бажаєте ще раз? (1 = так/ 2 = ні)")
        if again != "1":
            break


start_game()
screen.mainloop()