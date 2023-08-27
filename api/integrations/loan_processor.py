from celery_tasks.tasks.tasks_loan_processor import task_loan_request


class LoanProcessor:
    def __init__(self):
        self.base_url = "https://loan-processor.digitalsys.com.br/api/v1"
        self.headers = {
            'Content-Type': 'application/json'
        }
        

    def loan_request(self, customer):
        url = self.base_url + '/loan'
        task_loan_request.delay(url, self.headers, customer.id)
        return
        
        