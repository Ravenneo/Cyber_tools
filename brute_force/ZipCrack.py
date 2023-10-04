from zipfile import ZipFile
import argparse
import concurrent.futures

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return password.decode()
    except Exception as e:
        return None

def main():
    parser = argparse.ArgumentParser(description="\nUsage: python zipbrute.py -z <zipfile.zip> -p <passwordfile.txt>")
    parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
    parser.add_argument("-p", dest="passfile", help="Password file")
    parsed_args = parser.parse_args()

    try:
        ziparchive = ZipFile(parsed_args.ziparchive)
        passfile = parsed_args.passfile
    except Exception as e:
        print("Error opening files:", str(e))
        exit(1)

    found_password = None

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Read passwords from the password file and test them
        with open(passfile, "r") as f:
            for line in f:
                password = line.strip("\n").encode("utf-8")
                result = executor.submit(extract_zip, ziparchive, password)
                
                # Check if a password is found and exit the loop
                if result.result():
                    found_password = result.result()
                    break

    if found_password:
        print("\nFound password:", found_password)
    else:
        print("\nPassword not found. Try a bigger password list.")

if __name__ == "__main__":
    main()
