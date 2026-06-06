import time
from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Employee,Log
from . import signals
import threading
# Create your views here.
def home(request):
    return render(request,"home.html")

def question1(request):
    result=[
        "Before save",
        *signals.signal_messages,
        " ",
        "Conclusion:","Django signals are synchronous by default."
    ] #
    Employee.objects.create(name="Question1")
    # time.sleep(2) Simulate long-running task
    return render(request, "result.html", {"title": "Question 1", "result": result})

def question2(request):
    view_thread = threading.get_ident()
    print(f"View Thread ID: {view_thread}")
    Employee.objects.create(name="Question2")
    result = [
        f"View Thread ID: {view_thread}",
        f"Signal Thread ID: {signals.signal_thread_id}",
        "",
        "Conclusion:",
        "Signals run in the same thread as the caller."
    ]
    return render(
        request,
        "result.html",
        {
            "title": "Question 2",
            "result": result
        }
    )

def question3(request):
    Employee.objects.all().delete()
    Log.objects.all().delete()
    try:
        with transaction.atomic():
            Employee.objects.create(
                name="Question3"
            )
            raise Exception(
                "Rollback"
            )
    except Exception:
        pass
    employee_count = Employee.objects.count()
    print(f"Employee Count: {employee_count}")
    log_count = Log.objects.count()
    print(f"Log Count: {log_count}")
    result = [
        f"Employees in DB: {employee_count}",
        f"Logs in DB: {log_count}",
        "",
        "Conclusion:",
        "Both counts are 0 because the transaction rolled back.",
        "Signals execute in the same database transaction."
    ]
    return render(
        request,
        "result.html",
        {
            "title": "Question 3",
            "result": result
        }
    )