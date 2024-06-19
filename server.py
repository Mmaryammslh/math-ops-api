from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import subprocess
#import time

app = FastAPI()

@app.exception_handler(404)
def custom_404_handler(request, exc):
    return JSONResponse(status_code = 404, content = {"message": "Not found. The requested resource does not exist."})

@app.exception_handler(RequestValidationError)
def custom_422_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
        content = {"message": "Invalid numbers. The values must be an integer."})

executable_path = "operations.exe"

"""Call to an arbitrary external executable"""
def call_to_executable(path, num1, opr, num2):
    #if (num1 == "100"): (to simulate a blocking call)
        #time.sleep(45) 
    output_result = subprocess.run([path, num1, opr, num2], capture_output = True)
    return output_result.stdout.decode('utf-8')

@app.get("/multiplication/{Num1}/{Num2}")
def get_multi_numbers(num1:int, num2:int):
    if ((num1 > 10**5) or (num2 > 10**5)):
        raise HTTPException(status_code= 400, detail= "Bad request. Numbers are too large.")
    result_of_multiplication = call_to_executable(executable_path, str(num1), '.', str(num2))
    response_content = {"value1": num1, "value2": num2, "operation": "multiplication", "result": result_of_multiplication}
    return JSONResponse(response_content)

@app.get("/division/{Num1}/{Num2}")
def get_div_numbers(num1:int, num2:int):
    if num2 == 0:
        return JSONResponse(status_code= 500, content= {"message": "Division by zero is not possible."})
    result_of_division = call_to_executable(executable_path, str(num1), '/', str(num2))
    response_content = {"value1": num1, "value2": num2, "operation": "division", "result": result_of_division}
    return JSONResponse(response_content)



