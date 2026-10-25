
# Multi-Plan Telecommunications Cost Optimization

plans = [
    {"name": "Plan A", "price": 199, "data": 2, "validity": 28, "rate": 20},
    {"name": "Plan B", "price": 249, "data": 3, "validity": 28, "rate": 15},
    {"name": "Plan C", "price": 299, "data": 5, "validity": 56, "rate": 10},
    {"name": "Plan D", "price": 349, "data": 6, "validity": 84, "rate": 12}
]

# User requirements
usage = 4
required_validity = 28
budget = 300

eligible_plans = []

print("TELECOMMUNICATION PLAN COMPARISON")
print("-" * 70)

for plan in plans:
    excess_data = max(0, usage - plan["data"])
    excess_charge = excess_data * plan["rate"]
    total_cost = plan["price"] + excess_charge

    eligible = (
        plan["validity"] >= required_validity
        and total_cost <= budget
    )

    print(f"\n{plan['name']}")
    print(f"Base price: Rs.{plan['price']}")
    print(f"Excess data: {excess_data} GB")
    print(f"Excess charge: Rs.{excess_charge}")
    print(f"Total cost: Rs.{total_cost}")
    print(f"Validity: {plan['validity']} days")
    print(f"Eligible: {'Yes' if eligible else 'No'}")

    if eligible:
        eligible_plans.append({
            "name": plan["name"],
            "total_cost": total_cost,
            "validity": plan["validity"]
        })

print("\n" + "-" * 70)

if eligible_plans:
    best_plan = min(
        eligible_plans,
        key=lambda p: p["total_cost"]
    )

    print("MOST ECONOMICAL ELIGIBLE PLAN")
    print(f"Plan: {best_plan['name']}")
    print(f"Total cost: Rs.{best_plan['total_cost']}")
    print(f"Validity: {best_plan['validity']} days")
    print(f"Budget remaining: Rs.{budget - best_plan['total_cost']}")
else:
    print("No plan satisfies all the requirements.")
