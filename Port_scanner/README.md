# Port Scanner Scripts

## V1 - Sequential Port Scanner

### Description
This is a simple Python script that performs sequential port scanning on a target IP address. It uses a basic loop to iterate through ports and checks the connectivity to each port one at a time.

### Usage
1. Run the script: `python port_scanner_v1.py`
2. Enter the target IP address when prompted.

---

## V2 - Multithreaded Port Scanner

### Description
This Python script enhances the port scanning process by utilizing multithreading. It uses the `concurrent.futures` module to create multiple threads, allowing parallel scanning of ports for improved efficiency.

### Usage
1. Run the script: `python port_scanner_v2.py`
2. Enter the target IP address when prompted.

---

## V2 Updated - Enhanced User Interface

### Description
Building upon the V2 script, this version provides an improved user interface by displaying additional information. It includes messages indicating the progress of the scan, and at the end, it reports the total time taken for the scan.

### Usage
1. Run the script: `python port_scanner_v2_updated.py`
2. Enter the target IP address when prompted.

## Port Scanner with Enhanced Reporting (Nmap Integration) PS_Nmap.py

This Python script enhances port scanning capabilities by utilizing multithreading for parallel port scans. Additionally, it integrates Nmap to provide detailed information about the target host, including its operating system. The results are saved in a report file for further analysis.

### Usage

1. Run the script: `python port_scanner.py 192.168.0.1 --timeout 2 --threads 4`
2. Replace `192.168.0.1` with the target IP address.
3. Adjust `timeout` and `threads` values as needed.

   

Feel free to customize and contribute to this project!

---

### Additional Notes
- Ensure you have the required Python libraries installed (`socket`, `concurrent.futures`, and `time`).
- Use responsibly and with proper authorization, as port scanning without permission may violate network security policies.
- Adjust script parameters such as timeout and thread count based on your specific requirements.

Feel free to customize these scripts or contribute to their improvement. Happy scanning!


![image](https://github.com/Ravenneo/Caesar/assets/41577767/a36784c1-22f1-48ce-b649-dc0f804ac202)
![image](https://github.com/Ravenneo/Caesar/assets/41577767/ea056198-a3f2-4028-a6a4-9981d8547b78)


