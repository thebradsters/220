class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales_list = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sales):
        self.sales_list.append(sales)

    def total_sales(self):
        total = 0
        for num in self.sales_list:
            total += num
        return total

    def get_sales(self):
        return self.sales_list

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if self.total_sales() > SalesPerson.total_sales(other):
            return 1
        if self.total_sales() < SalesPerson.total_sales(other):
            return -1
        if self.total_sales() == SalesPerson.total_sales(other):
            return 0

    def __str__(self):
        return "{}-{}:{}".format(self.employee_id, self.name, self.total_sales())
