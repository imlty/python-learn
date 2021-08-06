import requests

url_ip = "http://localhost:8080"

import_regions_path = "/import/regions"
import_virtual_machine_ec2_path = "/import/virtualMachines/ec2"
import_virtual_machine_rds_path = "/import/virtualMachines/rds"

res1 = requests.post(url_ip + import_regions_path)
res2 = requests.post(url_ip + import_virtual_machine_ec2_path)
res3 = requests.post(url_ip + import_virtual_machine_rds_path)
