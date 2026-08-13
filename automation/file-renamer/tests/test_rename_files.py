from pathlib import Path

from src.rename_files import (
    validate_folder,
    get_files,
    plan_changes,
    apply_changes,
)


def test_validate_folder(tmp_path):
    folder = tmp_path / "files"
    folder.mkdir()

    # Should not raise an error
    validate_folder(folder)


def test_get_files_only_returns_supported_files(tmp_path):
    # Create test files
    image = tmp_path / "photo.jpg"
    png = tmp_path / "image.png"
    pdf = tmp_path / "document.pdf"
    video = tmp_path / "video.mp4"

    image.touch()
    png.touch()
    pdf.touch()
    video.touch()

    files = get_files(tmp_path)

    file_names = {file.name for file in files}

    assert file_names == {"photo.jpg", "image.png"}


def test_plan_changes_creates_new_names(tmp_path):
    file = tmp_path / "IMG_001.jpg"
    file.touch()

    changes, skipped_count = plan_changes(
        [file],
        tmp_path,
        "photo_",
    )

    assert len(changes) == 1
    assert skipped_count == 0

    old_file, new_file = changes[0]

    assert old_file.name == "IMG_001.jpg"
    assert new_file.name == "photo_IMG_001.jpg"


def test_plan_changes_skips_existing_destination(tmp_path):
    file = tmp_path / "IMG_001.jpg"
    existing_file = tmp_path / "photo_IMG_001.jpg"

    file.touch()
    existing_file.touch()

    changes, skipped_count = plan_changes(
        [file],
        tmp_path,
        "photo_",
    )

    assert len(changes) == 0
    assert skipped_count == 1


def test_apply_changes_renames_files(tmp_path):
    file = tmp_path / "IMG_001.jpg"
    new_file = tmp_path / "photo_IMG_001.jpg"

    file.touch()

    renamed_count, failed_count = apply_changes(
        [(file, new_file)]
    )

    assert renamed_count == 1
    assert failed_count == 0

    assert not file.exists()
    assert new_file.exists()


def test_apply_changes_handles_failure(tmp_path):
    file = tmp_path / "IMG_001.jpg"

    # The source file doesn't exist
    new_file = tmp_path / "photo_IMG_001.jpg"

    renamed_count, failed_count = apply_changes(
        [(file, new_file)]
    )

    assert renamed_count == 0
    assert failed_count == 1