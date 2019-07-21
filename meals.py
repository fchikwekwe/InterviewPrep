def get_unique_meal_count(meals):
    unique_meals = set()

    for meal in meals:
        if not unique_meals:
            unique_meals.add(set(meal.ingredients))
        for ingredient in meal:
            for unique in unique_meals:
                if ingredient in unique:
                    pass
            else: 
                unique

        
    return len(unique_meals)

sample_meals = [
    {
        'name': 1,
        'ingredients': ["Lettuce", "Tomato", "Onion", "Cheese"]
    },
    {
        'name': 2,
        'ingredients': ["Lettuce", "Tomato", "Onion", "Cheese"]
    }
]
print(get_unique_meal_count(sample_meals))
