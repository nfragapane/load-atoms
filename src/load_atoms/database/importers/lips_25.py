from load_atoms.database.backend import BASE_GITHUB_URL, SingleFileImporter
from load_atoms.database.internet import FileDownload

class Importer(SingleFileImporter):
    @classmethod
    def file_to_download(cls) -> FileDownload:
        return FileDownload(
            url=f"{BASE_GITHUB_URL}/LiPS-25/lips-25.extxyz",
            expected_hash="c299a6bfd3ac38510488700a29fd8c910598a536fe77f4b9de4e6b08bf6ba62c",
        )
    