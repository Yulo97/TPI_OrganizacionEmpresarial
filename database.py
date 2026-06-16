import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EMPLOYEES_FILE = BASE_DIR / "data" / "empleados.csv"


def load_employees():
    employees = []
    try:
        with EMPLOYEES_FILE.open(mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["saldo"] = int(row["saldo"])
                employees.append(row)
    except FileNotFoundError:
        print(f"No se encontró el archivo de empleados: {EMPLOYEES_FILE}")
    return employees


def save_employees(employees):
    fieldnames = ["id", "nombre", "saldo"]
    try:
        with EMPLOYEES_FILE.open(mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in employees:
                writer.writerow({
                    "id": emp["id"],
                    "nombre": emp["nombre"],
                    "saldo": emp["saldo"],
                })
    except IOError as error:
        print(f"Error al guardar empleados en CSV: {error}")


def get_employee(employees, employee_id):
    for emp in employees:
        if emp["id"] == employee_id:
            return emp
    return None


def update_balance(employees, employee_id, days_used):
    employee = get_employee(employees, employee_id)
    if employee:
        employee["saldo"] -= days_used
        save_employees(employees)
        print(f"Nuevo saldo para {employee['nombre']}: {employee['saldo']} días")
