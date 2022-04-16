from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, 'r')
        for line in in_file.readlines():
            stripper = line.rstrip()
            splitter = stripper.split(",")
            sales_person = SalesPerson(splitter[0], splitter[1].lstrip())
            sales_split = splitter[2].lstrip().rstrip().split()
            for sales in sales_split:
                SalesPerson.enter_sale(sales_person, eval(sales))
            self.sales_people.append(sales_person)

    def quota_report(self, quota):
        sales_list = []
        for i in range(len(self.sales_people)):
            employee = self.sales_people[i]
            sales_person = []
            sales_id = SalesPerson.get_id(employee)
            sales_person.append(int(sales_id))
            sales_name = SalesPerson.get_name(employee)
            sales_person.append(sales_name)
            total_sales = float(SalesPerson.total_sales(employee))
            sales_person.append(total_sales)
            if SalesPerson.met_quota(employee, quota):
                sales_person.append(True)
            else:
                sales_person.append(False)
            sales_list.append(sales_person)
        return sales_list

    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        pass

    def get_sale_frequencies(self):
        pass
