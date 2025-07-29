import os
import sys
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to the menu...")

def get_futurerestore_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if sys.platform == 'win32':
        return os.path.join(base_dir, 'Windows', 'futurerestore.exe')
    else:
        return os.path.join(base_dir, 'futurerestore')

def get_gaster_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if sys.platform == 'win32':
        return os.path.join(base_dir, 'Windows', 'gaster.exe')
    else:
        return os.path.join(base_dir, 'gaster')

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error while running the command!")

def palera1n_menu():
    clear()
    print("== Palera1n Menu ==")
    print("1) Install Rootless")
    print("2) Install Rootful")
    print("3) Uninstall")
    print("4) Go Back")

    choice = input("Choose an option: ").strip()
    if choice == '1':
        print("\nRunning Rootless installation...")
        run_command("curl -s https://palera.in/rootless | bash")
    elif choice == '2':
        print("\nRunning Rootful installation...")
        run_command("curl -s https://palera.in/rootful | bash")
    elif choice == '3':
        print("\nUninstalling Palera1n...")
        run_command("palera1n uninstall")
    elif choice == '4':
        return
    else:
        print("Invalid option.")
    pause()

def futurerestore_menu():
    clear()
    print("== FutureRestore ==")
    futurerestore = get_futurerestore_path()
    gaster = get_gaster_path()

    print("Enter the following parameters (leave blank if not applicable):")

    sep = input("SEP file (e.g., sep.im4p): ").strip()
    bb = input("Baseband file (e.g., bb.mbn): ").strip()
    shsh = input("SHSH file (e.g., blob.shsh2): ").strip()
    ipsw = input("IPSW file (e.g., iPhone13,2_16.6_20G506_Restore.ipsw): ").strip()

    if not shsh or not ipsw:
        print("SHSH and IPSW are required!")
        pause()
        return

    command = f'"{futurerestore}"'
    if sep:
        command += f' -s "{sep}"'
    if bb:
        command += f' -b "{bb}"'

    command += f' -t "{shsh}" --latest-sep "{ipsw}"'

    print("\nRunning command:\n", command)
    run_command(command)
    pause()

def trollstore_menu():
    clear()
    print("== TrollStore via SSHRD ==")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sshrd_path = os.path.join(base_dir, 'sshrd.sh')
    if not os.path.isfile(sshrd_path):
        print("Error: sshrd.sh not found!")
        pause()
        return

    print("1) Install TrollStore")
    print("2) Uninstall TrollStore")
    print("3) Go Back")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        print("\nInstalling TrollStore...")
        run_command(f'bash "{sshrd_path}" install')
    elif choice == '2':
        print("\nUninstalling TrollStore...")
        run_command(f'bash "{sshrd_path}" uninstall')
    elif choice == '3':
        return
    else:
        print("Invalid option.")
    pause()

def activation_menu():
    clear()
    print("== Activation ==")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    backup_path = os.path.join(base_dir, 'backup.sh')
    activate_path = os.path.join(base_dir, 'activate.sh')

    print("1) Backup Activation")
    print("2) Activate Device")
    print("3) Go Back")

    choice = input("Choose an option: ").strip()

    if choice == '1':
        if not os.path.isfile(backup_path):
            print("backup.sh not found!")
        else:
            print("\nRunning activation backup...")
            run_command(f'bash "{backup_path}"')
    elif choice == '2':
        if not os.path.isfile(activate_path):
            print("activate.sh not found!")
        else:
            print("\nRunning device activation...")
            run_command(f'bash "{activate_path}"')
    elif choice == '3':
        return
    else:
        print("Invalid option.")
    pause()

def main_menu():
    while True:
        clear()
        print("=== Firera1n Menu ===")
        print("1) Palera1n")
        print("2) FutureRestore")
        print("3) TrollStore")
        print("4) Activation")
        print("5) Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            palera1n_menu()
        elif choice == '2':
            futurerestore_menu()
        elif choice == '3':
            trollstore_menu()
        elif choice == '4':
            activation_menu()
        elif choice == '5':
            print("Bye! 👋")
            sys.exit(0)
        else:
            print("Invalid choice.")
            pause()

if __name__ == "__main__":
    main_menu()
