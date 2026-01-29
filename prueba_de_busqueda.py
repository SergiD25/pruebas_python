import os

# 🏁 Set your main folder path (use r"" for Windows paths with spaces)
root_dir = r"\\172.16.2.252\contenedor\HOJAS DE VIDA GENERAL"

# ✅ Required and 🚫 Forbidden keywords to look for
required_keywords = ["cv", "id"]
forbidden_keywords = ["insurance"]

results = []

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if not os.path.isdir(folder_path):
        continue

    print(f"🔍 Checking folder: {folder_name}")

    try:
        files = os.listdir(folder_path)
    except PermissionError:
        print(f"⚠️ Cannot access {folder_path}")
        continue

    file_names_lower = [f.lower() for f in files]

    found_required = [req for req in required_keywords if any(req in f for f in file_names_lower)]
    missing_required = [req for req in required_keywords if req not in found_required]
    found_forbidden = [forb for forb in forbidden_keywords if any(forb in f for f in file_names_lower)]

    # Save results
    results.append({
        "folder": folder_name,
        "found_required": found_required,
        "missing_required": missing_required,
        "found_forbidden": found_forbidden
    })

# 🧾 Print clear summary
print("\n=== SUMMARY ===\n")
for r in results:
    print(f"📁 Folder: {r['folder']}")
    print(f"  ✅ Found required: {', '.join(r['found_required']) if r['found_required'] else 'None'}")
    print(f"  ⚠️ Missing required: {', '.join(r['missing_required']) if r['missing_required'] else 'None'}")
    print(f"  🚫 Forbidden found: {', '.join(r['found_forbidden']) if r['found_forbidden'] else 'None'}")
    print()