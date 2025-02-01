import os
import json
import subprocess


def get_tModLoader_path():
    user_path = os.path.expanduser("~")
    tModLoader_paths = [
        os.path.join(
        user_path, "OneDrive", "Documents", "My Games",
        "Terraria", "tModLoader", "Mods"
        ),
        os.path.join(
            user_path, "Documents", "My Games",
            "Terraria", "tModLoader", "Mods"
        )
    ]

    if os.path.exists(tModLoader_paths[0]):
        return tModLoader_paths[0]
    elif os.path.exists(tModLoader_paths[1]):
        return tModLoader_paths[1]
    else:
        return None


def main():
    # Get the path for tModLoader and the enabled.json file in Mods folder.
    tModLoader_path = get_tModLoader_path()
    if not tModLoader_path:
        print("tModLoader is not installed!")
        return

    enabled_mods_json = os.path.join(tModLoader_path, "enabled.json")
    if not os.path.exists(enabled_mods_json):
        print("Current enabled.json folder does not exist!")
        return

    print("Welcome! This program checks to see if your currently enabled tModLoader mods are "
          "different from a given modpack.")

    # Get modpack folder path from input.
    modpack_path, modpack_name = "", ""
    while not os.path.exists(modpack_path):
        modpack_name = input("Enter modpack name: ")
        modpack_path = os.path.join(tModLoader_path, "ModPacks", modpack_name)
        if not os.path.exists(modpack_path) or not os.path.isdir(modpack_path):
            print("This modpack does not exist. Try again.")
    modpack_json = os.path.join(modpack_path, "Mods", "enabled.json")

    # Get list of mod names from these json files.
    with open(enabled_mods_json, 'r') as f:
        enabled_mods = json.load(f)

    with open(modpack_json, 'r') as f:
        modpack_mods = json.load(f)

    # Compare mods and see which extra mods are currently enabled and which are missing.
    missing_mods, extra_mods = [], []
    for mod in modpack_mods:
        if mod not in enabled_mods:
            missing_mods.append(mod)

    for mod in enabled_mods:
        if mod not in modpack_mods:
            extra_mods.append(mod)

    # Write results to results.txt
    with open("results.txt", 'w') as f:
        if not missing_mods and not extra_mods:
            f.write("There are no differences in mods being used.")
        else:
            f.write(f"The following mods are missing from {modpack_name}:\n")
            for mod in missing_mods:
                f.write("- " + mod + "\n")

            f.write(f"\nThe following mods are not from {modpack_name}:\n")
            for mod in extra_mods:
                f.write("- " + mod + "\n")

    print(os.path.dirname(__file__))
    subprocess.Popen(["notepad.exe", "results.txt"])


if __name__ == '__main__':
    main()
