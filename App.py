from shiny import App, render, ui, reactive
import asyncio

# Portion sizes per person (grams or pcs)
# PORTION_SIZES = {
#     # Carbohydrates
#     "Rice": 75,
#     "Pasta": 75,
#     "Bread": 60,
#     "Couscous": 80,
#     "Quinoa": 70,
#     "Oats": 50,
#     "Potatoes": 150,  # Added missing potatoes

#     # Fruits
#     "Apple": 1,
#     "Oranges": 1,
#     "Banana": 1,
#     "Grapes": 100,
#     "Strawberries": 100,
#     "Blueberries": 80,
#     "Mango": 1,

#     # Protein
#     "Chicken": 130,
#     "Eggs": 2,
#     "Fish": 120,
#     "Tofu": 100,
#     "Lentils": 100,
#     "Beef": 150,
#     "Beans": 100,

#     # Fats
#     "Butter": 15,
#     "Palm oil": 13,
#     "Cheese": 30,
#     "Olive oil": 10,
#     "Peanut butter": 20,
#     "Avocado": 1,
#     "Nuts": 25,

#     # Vegetables
#     "Broccoli": 80,
#     "Lettuce": 50,
#     "Carrots": 70,
#     "Spinach": 60,
#     "Peas": 90,
#     "Tomatoes": 80,
#     "Cucumber": 60,

#     # Vitamins/Minerals
#     "Almonds": 25,
#     "Pistachios": 25,
#     "Dates": 3,
#     "Walnuts": 25,
#     "Chia seeds": 15,
#     "Raisins": 30,
#     "Cashews": 25,
#     "Sunflower seeds": 30,
# }

# def food_section(title, color, foods):
#     elements = []
#     for food in foods:
#         key = food.lower().replace(" ", "")
#         elements.append(ui.p(food, style="margin-bottom:4px; font-weight:600;"))
#         elements.append(
#             ui.input_action_button(
#                 f"add_{key}",
#                 "ADD",
#                 class_="btn btn-primary btn-sm",
#                 style="margin-bottom:10px;",
#             )
#         )
#     return ui.card(
#         ui.h4(
#             title,
#             style=f"background-color:{color}; color:white; padding:8px 12px; border-radius:8px;",
#         ),
#         *elements,
#         style="padding:15px; margin-bottom:15px;",
#     )

def app_ui(request):
    return ui.page_fluid(
        ui.navset_tab(
            ui.nav_panel(
                "Household Size",
                #ui.div(
                    # ui.layout_column_wrap(
                    #     ui.card(
                    #         ui.h2("Welcome to Your Grocery Planner!"),
                    #         ui.h3("How many people are there in your household?"),
                    #         ui.layout_columns(
                                ui.input_action_button("decrease", "-"),
                                ui.div(
                                    ui.output_text("household_count"),
                                    #style="font-weight:700; font-size:22px; margin:auto;",
                                ),
                                ui.input_action_button("increase", "+"),
                            ),
                            #style="text-align: center; padding: 30px;",
                        )
                        #width=1,
                        #style="max-width: 400px; margin: auto; margin-top: 50px;",
                    )
               # )
            #),
            # ui.nav_panel(
            #     "Food Category Selection",
            #     ui.div(
            #         ui.layout_columns(
            #             food_section("Carbohydrates", "#1b9e77", ["Rice", "Pasta", "Bread", "Potatoes", "Oats", "Quinoa"]),
            #             food_section("Fruits", "#d95f02", ["Apple", "Oranges", "Banana", "Grapes", "Strawberries", "Mango"]),
            #             food_section("Proteins", "#7570b3", ["Chicken", "Eggs", "Fish", "Tofu", "Lentils", "Beef"]),
            #             food_section("Fats", "#e7298a", ["Butter", "Palm oil", "Cheese", "Olive oil", "Avocado", "Nuts"]),
            #             food_section("Vegetables", "#66a61e", ["Broccoli", "Lettuce", "Carrots", "Spinach", "Peas", "Tomatoes"]),
            #             food_section("Vitamins/Minerals", "#e6ab02", ["Almonds", "Pistachios", "Dates", "Raisins", "Sunflower seeds"])
            #         ),
            #         # Confirmation message area
            #         ui.div(ui.output_text("add_confirmation"), style="color: green; font-weight: 600; margin-top: 10px;"),
            #         style="padding: 20px;",
            #     ),
            # ),
            # ui.nav_panel(
            #     "Food List",
            #     ui.div(
            #         ui.layout_column_wrap(
            #             ui.card(
            #                 ui.h4("Food List  and  Portion Sizes"),
            #                 ui.output_ui("food_list_display"),
            #             ),
            #             width=1,
            #             style="max-width: 500px; margin: auto; margin-top: 50px;",
            #         ),
            #     ),
            # ),
      #  )#,
    # style="background-color: #d2e6c7; min-height: 100vh; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;",
   # )




household_size = reactive.Value(1)
def server(input, output, session):
    # selected_foods = reactive.Value({})
    # add_confirm = reactive.Value("")

   

    @reactive.event(input.increase)
    def increase_count():
        household_size.set(household_size.get() + 1)
        
        
    @reactive.event(input.decrease)
    def decrease_count():
        household_size.set(household_size.get() - 1)
            
        
    

    # def add_food_listener(food_key, display_name):
    #     @reactive.event(getattr(input, f"add_{food_key}"))
    #     def on_add():
    #         items = selected_foods.get().copy()
    #         items[display_name] = items.get(display_name, 0) + 1
    #         selected_foods.set(items)
    #         add_confirm.set(f"Added {display_name}!")

    #         async def clear_msg():
    #             await asyncio.sleep(2)
    #             add_confirm.set("")

    #         asyncio.create_task(clear_msg())

    # def remove_food_listener(food_key, display_name):
    #     @reactive.event(getattr(input, f"remove_{food_key}"))
    #     def on_remove():
    #         items = selected_foods.get().copy()
    #         if display_name in items:
    #             if items[display_name] > 1:
    #                 items[display_name] -= 1
    #             else:
    #                 del items[display_name]
    #             selected_foods.set(items)

    # for food in PORTION_SIZES:
    #     key = food.lower().replace(" ", "")
    #     add_food_listener(key, food)
    #     remove_food_listener(key, food)

    # @output
    # @render.text
    # def add_confirmation():
    #     return add_confirm.get()
    
    @output
    @render.text
    def household_count():
        return str(household_size.get())

    # @output
    # @render.ui
    # def food_list_display():
    #     people = household_size.get()
    #     foods = selected_foods.get()
        # if not foods:
        #     return ui.HTML("<p>No food selected yet.</p>")

        # html = "<ol style='padding-left: 20px;'>"
        # for food, times_added in sorted(foods.items()):
        #     key = food.lower().replace(" ", "")
        #     portion = PORTION_SIZES.get(food, 0)
        #     total = portion * people * times_added

        #     # Add remove button next to each item
        #     remove_btn_html = (
        #         f"<button id='remove_{key}' "
        #         f"class='btn btn-danger btn-sm' "
        #         f"style='float:right; margin-left: 8px;'>Remove</button>"
        #     )

        #     if food in ["Apple", "Banana", "Oranges", "Eggs", "Avocado", "Mango", "Dates"]:
        #         html += (
        #             f"<li style='margin-bottom: 8px;'>"
        #             f"{food} x{times_added} "
        #             f"<span style='float:right'>{total} pcs</span>"
        #             f"{remove_btn_html}"
        #             f"</li>"
        #         )
        #     else:
        #         weight_display = f"{total} g"
        #         if total >= 1000:
        #             weight_display = f"{total / 1000:.1f} kg"
        #         html += (
        #             f"<li style='margin-bottom: 8px;'>"
        #             f"{food} x{times_added} "
        #             f"<span style='float:right'>{weight_display}</span>"
        #             f"{remove_btn_html}"
        #             f"</li>"
        #         )
        # html += "</ol>"
        # return ui.HTML(html)


app = App(app_ui, server)
