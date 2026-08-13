from pathlib import Path
import sys


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def validate_folder(folder: Path) -> None:
    """Validate that the provided folder exists and is a directory."""

    if not folder.exists():
        print(f"Error: folder '{folder}' does not exist.")
        sys.exit(1)

    if not folder.is_dir():
        print(f"Error: '{folder}' is not a directory.")
        sys.exit(1)


def get_files(folder: Path) -> list[Path]:
    """Return files that can be renamed."""

    files = []

    for file in folder.iterdir():

        # Ignore directories
        if not file.is_file():
            continue

        extension = file.suffix.lower()

        # Ignore unsupported file types
        if extension not in SUPPORTED_EXTENSIONS:
            continue

        files.append(file)

    return files


def plan_changes(
    files: list[Path],
    folder: Path,
    prefix: str,
) -> tuple[list[tuple[Path, Path]], int]:
    """Create the list of files that can safely be renamed."""

    changes = []
    skipped_count = 0

    for file in files:

        new_name = f"{prefix}{file.stem}{file.suffix}"
        new_path = folder / new_name

        # Don't rename a file to the same name
        if file == new_path:
            skipped_count += 1
            continue

        # Don't overwrite an existing file
        if new_path.exists():
            print(
                f"Skipping: {file.name} → {new_name} "
                f"(destination already exists)"
            )
            skipped_count += 1
            continue

        changes.append((file, new_path))

    return changes, skipped_count


def show_changes(changes: list[tuple[Path, Path]]) -> None:
    """Display the changes that will be made."""

    print("\nChanges to be applied:")
    print("-" * 40)

    for file, new_path in changes:
        print(f"{file.name} → {new_path.name}")

    print("-" * 40)


def confirm_changes() -> bool:
    """Ask the user whether the changes should be applied."""

    answer = input("Apply these changes? (y/n): ").strip().lower()

    return answer == "y"


def apply_changes(changes: list[tuple[Path, Path]]) -> tuple[int, int]:
    """Rename files and return renamed and failed counts."""

    renamed_count = 0
    failed_count = 0

    for file, new_path in changes:

        try:
            file.rename(new_path)
            renamed_count += 1

            print(f"Renamed: {file.name} → {new_path.name}")

        except OSError as error:
            failed_count += 1

            print(f"Failed: {file.name}")
            print(f"Reason: {error}")

    return renamed_count, failed_count


def print_summary(
    renamed_count: int,
    skipped_count: int,
    failed_count: int,
) -> None:
    """Display the final automation summary."""

    print("\nAutomation completed.")
    print("-" * 30)
    print(f"Renamed: {renamed_count}")
    print(f"Skipped: {skipped_count}")
    print(f"Failed:  {failed_count}")
    print("-" * 30)


def main() -> None:
    """Main application workflow."""

    # Validate command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python rename_files.py <folder_path> [prefix]")
        sys.exit(1)

    folder = Path(sys.argv[1])
    prefix = sys.argv[2] if len(sys.argv) > 2 else "renamed_"

    # Validate folder
    validate_folder(folder)

    # Find files
    files = get_files(folder)

    if not files:
        print("No supported files found.")
        sys.exit(0)

    # Plan the changes
    changes, skipped_count = plan_changes(
        files,
        folder,
        prefix,
    )

    if not changes:
        print("No files to rename.")
        sys.exit(0)

    # Preview
    show_changes(changes)

    # Confirmation
    if not confirm_changes():
        print("Aborting...")
        sys.exit(0)

    # Apply changes
    renamed_count, failed_count = apply_changes(changes)

    # Summary
    print_summary(
        renamed_count,
        skipped_count,
        failed_count,
    )


if __name__ == "__main__":
    main()