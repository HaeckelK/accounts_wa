import os

import pytest

from accounts.database import AccountsDatabase


def test_uploads(tmpdir):
    filename = os.path.join(tmpdir, 'test.db')
    db = AccountsDatabase(filename)
    db.initial_setup()

    db.insert_upload('abc.txt', '123.txt', 'bank_statement', 'imports.upload_bank_statement',
                     'form_data', '20201015', 123, 0, 0, 0)
    assert db.get_all_upload() == [{'id': 1, 'original_name': 'abc.txt', 'name': '123.txt', 'document_type': 'bank_statement',
                                    'upload_function': 'imports.upload_bank_statement', 'form_data': 'form_data',
                                    'date_added': 20201015, 'time_added': 123, 'is_deleted': 0, 'is_archived': 0, 'is_processed': 0}]
