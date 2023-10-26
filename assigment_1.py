def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == '끝':
            return None
        try:
            return float(user_input)
        except ValueError:
            print("숫자를 입력하세요.")

def adjust_recipe(recipe, factor):
    adjusted_recipe = {}
    for ingredient, quantity in recipe.items():
        adjusted_quantity = quantity * factor
        adjusted_recipe[ingredient] = adjusted_quantity
    return adjusted_recipe

def main():
    recipe = {}
    print("재료와 양을 입력하세요 (끝을 입력하면 종료):")
    while True:
        ingredient = input("재료: ")
        if not ingredient:
            continue
        quantity = get_user_input("재료의 양: ")
        if quantity is None:
            break
        recipe[ingredient] = quantity

    factor = get_user_input("레시피를 얼마나 조절하시겠습니까? (2 또는 0.5): ")

    if factor == 2:
        adjusted_recipe = adjust_recipe(recipe, 2)
        print(f"2배로 조절된 레시피:")
    elif factor == 0.5:
        adjusted_recipe = adjust_recipe(recipe, 0.5)
        print(f"반으로 조절된 레시피:")
    else:
        print("올바른 조절 계수를 입력하세요 (2 또는 0.5).")
        return

    for ingredient, quantity in adjusted_recipe.items():
        print(f"{ingredient}: {quantity}")

if __name__ == "__main__":
    main()
