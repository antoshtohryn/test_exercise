import os
import yaml
import json
import subprocess
import platform
from datetime import datetime


FILE_1_PATH = 'file_1'
FILE_2_PATH = 'file_2'


def test_file_1_exists():
    assert os.path.exists(FILE_1_PATH), f"{FILE_1_PATH} does not exist"
    print(f"{FILE_1_PATH} exist")


def test_file_1_age():
    assert os.path.exists(FILE_1_PATH), f"{FILE_1_PATH} does not exist"
    creation_time = os.path.getctime(FILE_1_PATH)
    age_seconds = datetime.now().timestamp() - creation_time
    age_hours = age_seconds / 3600
    print(f"File age: {age_hours} hours")


def test_file_1_hnmanager():
    assert os.path.exists(FILE_1_PATH), f"{FILE_1_PATH} does not exist"
    with open(FILE_1_PATH, 'r') as f:
        data = yaml.safe_load(f)
    hnmanager_value = data.get("global", {}).get("hnmanager", None)
    assert hnmanager_value is not None, "Parameter 'hnmanager' not found"
    assert hnmanager_value, "'hnmanager' value is empty"
    print(f"'hnmanager' value: {hnmanager_value}")


def test_file_2_exists():
    assert os.path.exists(FILE_2_PATH), f"{FILE_2_PATH} does not exist"
    print(f"{FILE_2_PATH} exist")


def test_file_2_size():
    assert os.path.exists(FILE_2_PATH), f"{FILE_2_PATH} does not exist"
    file_size = os.path.getsize(FILE_2_PATH)
    print(f"File size (in bytes): {file_size}")


def test_file_2_updated():
    assert os.path.exists(FILE_2_PATH), f"{FILE_2_PATH} does not exist"
    with open(FILE_2_PATH, 'r') as f:
        data = json.load(f)
    updated_value = data.get("data", [{}])[0].get("attributes", {}).get("updated", None)
    assert updated_value is not None, "Parameter 'updated' not found"
    assert updated_value, "'updated' value is empty"
    print(f"'updated' value: {updated_value}")


service_name = "Themes"


def test_service_status():
    result = subprocess.run(["sc", "query", service_name], capture_output=True, text=True)
    status = "RUNNING" in result.stdout
    assert status, f"Service {service_name} is not running."
    print(f"Service {service_name} running: {status}")


def test_stop_and_check_service():  #You may be required to run script in administartor mode
    subprocess.run(["sc", "stop", service_name])
    result = subprocess.run(["sc", "query", service_name], capture_output=True, text=True)
    status = "RUNNING" in result.stdout
    assert status == False, f"Service {service_name} is still running."
    print(f"Service {service_name} running: {status}")


def test_os_version():
    os_version = platform.platform()
    print(f"OS Version: {os_version}")
