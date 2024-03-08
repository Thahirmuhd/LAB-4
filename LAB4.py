
#LAB4
#CODED BY : MUHD THAHIR BIN AINUDDIN
#DATA MANAGEMENT SYSTEM


def total_units_sold(units_sold):
    # Calculate the total units sold
    return sum(units_sold)

def highest_sales(flower_names, units_sold):
    # Find the flower with the highest sales
    max_index = units_sold.index(max(units_sold))
    return flower_names[max_index], units_sold[max_index]

def above_average_customer_reviews(flower_names, customer_reviews):
    # Identify flowers with above-average customer reviews
    return [flower for flower, review in zip(flower_names, customer_reviews) if review > 3]

def average_customer_review_score(customer_reviews):
    # Calculate the average customer review score
    return sum(customer_reviews) / len(customer_reviews)

def below_average_sales(flower_names, units_sold):
    # Identify flowers with below-average sales
    average_units_sold = sum(units_sold) / len(units_sold)
    return [(flower, units) for flower, units in zip(flower_names, units_sold) if units < average_units_sold]

def main():
    # New data for 20 flowers
    flower_names = [
        "Rose", "Lily", "Tulip", "Sunflower", "Daisy",
        "Orchid", "Carnation", "Daffodil", "Peony", "Hydrangea",
        "Crocus", "Dahlia", "Chrysanthemum", "Iris", "Magnolia",
        "Poppy", "Forget-Me-Not", "Lavender", "Bluebell", "Pansy"
    ]
    units_sold = [
        50, 30, 20, 45, 35,
        25, 15, 10, 40, 55,
        60, 70, 80, 65, 75,
        85, 90, 95, 100, 110
    ]
    customer_reviews = [
        4.2, 3.8, 4.5, 3.9, 4.1,
        4.0, 3.7, 4.3, 4.6, 3.6,
        4.4, 4.7, 3.5, 4.8, 3.4,
        4.9, 3.3, 3.2, 3.1, 4.0
    ]

    while True:
        print("Select an option:")
        print("1. Total Units Sold")
        print("2. Highest Sales Identification")
        print("3. Above-Average Customer Reviews Identification")
        print("4. Average Customer Review Score Calculation")
        print("5. Below-Average Sales Identification")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            total_units = total_units_sold(units_sold)
            print("1. Total Units Sold:".center(50))
            print("-" * 50)
            print(f"Total Units Sold: {total_units}".center(50))
            print()
        elif choice == '2':
            highest_flower, highest_units = highest_sales(flower_names, units_sold)
            print("2. Flower with Highest Sales:".center(50))
            print("-" * 50)
            print(f"{highest_flower}: Units Sold - {highest_units}".center(50))
            print()
        elif choice == '3':
            above_average_flowers = above_average_customer_reviews(flower_names, customer_reviews)
            print("3. Flowers with Above Average Customer Reviews:".center(50))
            print("-" * 50)
            for flower in above_average_flowers:
                print(flower.center(50))
            print()
        elif choice == '4':
            average_review_score = average_customer_review_score(customer_reviews)
            print("4. Average Customer Review Score:".center(50))
            print("-" * 50)
            print(f"Average Customer Review Score: {average_review_score:.1f}".center(50))
            print()
        elif choice == '5':
            below_average_flowers = below_average_sales(flower_names, units_sold)
            print("5. Flowers with Below Average Sales:".center(50))
            print("-" * 50)
            for flower, units in below_average_flowers:
                print(f"{flower}: Units Sold - {units}".center(50))
            print()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

