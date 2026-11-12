def calculate_tip(bill, tip, people):
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    grand_total = round(total_bill, 2)
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    return grand_total, final_amount 