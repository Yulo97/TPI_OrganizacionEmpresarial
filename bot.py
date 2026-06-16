from states import START, WAITING_DATES, VALIDATING_BALANCE, CONFIRMATION, FINISHED
from database import load_employees, get_employee, update_balance
from utils import parse_date, days_between, show_error, confirm_text


def run_bot():
    employees = load_employees()
    state = START

    while state != FINISHED:
        if state == START:
            print("\nPaso 1: Seleccione empleado")
            employee_id = input("Ingrese el ID del empleado: ").strip()
            employee = get_employee(employees, employee_id)
            if employee is None:
                show_error("Empleado no encontrado. Intente nuevamente.")
                continue
            print(f"Empleado: {employee['nombre']}, saldo actual: {employee['saldo']} días")
            state = WAITING_DATES

        elif state == WAITING_DATES:
            start_text = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
            end_text = input("Ingrese fecha de fin (YYYY-MM-DD): ")
            start_date = parse_date(start_text)
            end_date = parse_date(end_text)
            if not start_date or not end_date:
                show_error("Formato de fecha inválido. Use YYYY-MM-DD.")
                continue
            if end_date < start_date:
                show_error("La fecha de fin no puede ser anterior a la fecha de inicio.")
                continue
            days_requested = days_between(start_date, end_date)
            print(f"Días solicitados: {days_requested}")
            state = VALIDATING_BALANCE

        elif state == VALIDATING_BALANCE:
            if days_requested > employee["saldo"]:
                show_error("No hay saldo suficiente para esos días de vacaciones.")
                state = FINISHED
                continue
            print("Hay saldo suficiente.")
            state = CONFIRMATION

        elif state == CONFIRMATION:
            if confirm_text("Desea confirmar la solicitud de vacaciones?"):
                update_balance(employees, employee["id"], days_requested)
                print("Vacaciones aprobadas y saldo actualizado.")
            else:
                print("Solicitud de vacaciones cancelada.")
            state = FINISHED

    print("Proceso finalizado. Gracias.")
