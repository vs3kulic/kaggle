"""A module to calculate the actual cost of painting a room."""
import math

# Painting cost calculation using math.ceil
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    """Calculate the actual cost of painting a room."""
    gallons = math.ceil((sqft_walls + sqft_ceiling) / sqft_per_gallon)
    # gallons = (sqft_walls + sqft_ceiling + sqft_per_gallon + 1) // sqft_per_gallon
    cost = gallons * cost_per_gallon
    return cost

# Expected cost calculation based on house features
def get_expected_cost(beds, baths, has_basement):
    """Calculate the expected cost of a house based on its features."""
    value = 80_000 + 30_000*beds + 10_000*baths + 40_000*has_basement
    return value

# Engraving cost calculation based on material type
def cost_of_project(engraving: str, solid_gold: bool) -> float:
    """Calculate the cost of an engraving project based on material type."""
    if solid_gold:
        cost = 100 + len(engraving)*10
    else:
        cost = 50 + len(engraving)*7
    return cost

def main():
    """Main function to demonstrate the get_actual_cost function."""
    sqft_walls=400
    sqft_ceiling=200
    sqft_per_gallon=350
    cost_per_gallon=25.0
    total_cost = get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
    print(f"The total cost of painting the room is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
