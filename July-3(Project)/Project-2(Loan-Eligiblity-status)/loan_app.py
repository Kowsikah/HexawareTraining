class LoanEligibility:
    def __init__(self, customer_name, salary, credit_score, employed):
        self.customer_name = customer_name
        self.salary = salary
        self.credit_score = credit_score
        self.employed = employed

    def check_eligibility(self):
        if (
            self.salary >= 50000
            and self.credit_score >= 700
            and self.employed
        ):
            return "Eligible for Loan"
        else:
            return "Not Eligible for Loan"


def main():
    print("========== Loan Eligibility System ==========")

    customer_name = input("Enter Customer Name: ")
    salary = float(input("Enter Salary: "))
    credit_score = int(input("Enter Credit Score: "))
    employed_input = input("Are you employed? (Yes/No): ").strip().lower()

    employed = employed_input == "yes"

    customer = LoanEligibility(
        customer_name,
        salary,
        credit_score,
        employed
    )

    print("\n========= Loan Eligibility Result =========")
    print("Customer Name :", customer.customer_name)
    print("Salary        :", customer.salary)
    print("Credit Score  :", customer.credit_score)
    print("Employment    :", "Employed" if customer.employed else "Unemployed")
    print("Loan Status   :", customer.check_eligibility())


if __name__ == "__main__":
    main()